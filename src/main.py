"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def print_profile_recommendations(profile_name: str, user_prefs: dict, songs: list[dict], k: int = 5) -> None:
    """Print a readable top-k recommendation block for one user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 80)
    print(f"Top Recommendations (Profile: {profile_name})")
    print("=" * 72)

    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"\n{rank}. {song['title']} — {song['artist']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")
        print(f"   Tags: {song['genre']} | {song['mood']} | energy {song['energy']:.2f}")

    print("\n" + "-" * 80)


def main() -> None:
    songs = load_songs("data/songs.csv")

    adversarial_profiles = {
        "Conflict: Pop + Sad + Very High Energy + Acoustic": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",  # mood intentionally absent from the catalog
            "target_energy": 0.95,
            "likes_acoustic": True,
        },
        "Conflict: Classical + Intense + Very Low Energy + Non-Acoustic": {
            "favorite_genre": "classical",
            "favorite_mood": "intense",
            "target_energy": 0.10,
            "likes_acoustic": False,
        },
        "Cold-Start-Like: Unseen Genre + Focused + Max Energy": {
            "favorite_genre": "drill",  # genre intentionally absent from the catalog
            "favorite_mood": "focused",
            "target_energy": 1.00,
            "likes_acoustic": False,
        },
    }

    print("\nAdversarial / Edge-Case Profile Run")
    for profile_name, user_prefs in adversarial_profiles.items():
        print_profile_recommendations(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
