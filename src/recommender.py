import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by profile match score."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored_songs = []
        for song in self.songs:
            score, _ = score_song(
                user_prefs=user_prefs,
                song={
                    "id": song.id,
                    "title": song.title,
                    "artist": song.artist,
                    "genre": song.genre,
                    "mood": song.mood,
                    "energy": song.energy,
                    "tempo_bpm": song.tempo_bpm,
                    "valence": song.valence,
                    "danceability": song.danceability,
                    "acousticness": song.acousticness,
                },
            )
            scored_songs.append((song, score))

        ranked = sorted(scored_songs, key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short reason string describing why a song fits a user."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(
            user_prefs=user_prefs,
            song={
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "tempo_bpm": song.tempo_bpm,
                "valence": song.valence,
                "danceability": song.danceability,
                "acousticness": song.acousticness,
            },
        )
        return "; ".join(reasons) if reasons else "general profile fit"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV path and coerce numeric fields to numbers."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted match score and explanation reasons for one song."""
    def _pref(*keys: str, default=None):
        for key in keys:
            if key in user_prefs:
                return user_prefs[key]
        return default

    score = 0.0
    reasons: List[str] = []

    favorite_genre = _pref("favorite_genre", "genre")
    favorite_mood = _pref("favorite_mood", "mood")
    target_energy = float(_pref("target_energy", "energy", default=0.5))
    likes_acoustic = bool(_pref("likes_acoustic", default=False))

    if favorite_genre and song.get("genre") == favorite_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if favorite_mood and song.get("mood") == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = max(0.0, 1.0 - abs(float(song["energy"]) - target_energy))
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    acousticness = float(song.get("acousticness", 0.0))
    if likes_acoustic and acousticness >= 0.6:
        score += 1.0
        reasons.append("acoustic preference match (+1.0)")
    elif not likes_acoustic and acousticness <= 0.4:
        score += 1.0
        reasons.append("low-acoustic preference match (+1.0)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, rank, and return the top-k song recommendations."""
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "general profile fit"
        scored.append((song, score, explanation))

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
