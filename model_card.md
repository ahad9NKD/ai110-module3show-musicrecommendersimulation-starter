# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This model suggests songs from a small CSV catalog.
It tries to match a user profile based on genre, mood, energy, and acoustic preference.
It is built for classroom learning and demos.
It is intended for simple recommendation experiments.
It is not intended for real user-facing product decisions.
It is not intended to model mental health, identity, or culture-level taste.

---

## 3. How the Model Works  

The model gives each song a score.
It adds points for matching genre and mood.
It adds similarity points when song energy is close to target energy.
It adds a bonus when acousticness matches user preference.
Then it sorts songs by score and returns the top results.
In sensitivity testing, I reduced genre weight and increased energy weight to see how rankings shift.

---

## 4. Data  

The dataset has 18 songs in `data/songs.csv`.
Each song has `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`.
I expanded the starter data by adding 8 songs.
The catalog covers multiple genres and moods, but it is still tiny.
Many real-world signals are missing, like skip history, lyrics, and session context.

---

## 5. Strengths  

The model is easy to understand.
It gives clear reason strings for each recommendation.
It works well when the user has clear genre and energy preferences.
It also works well as a CLI-first simulation for quick testing.

---

## 6. Limitations and Bias 

One clear weakness is an energy-based filter bubble.
When energy weight is high, many recommendations have similar intensity and less style diversity.
If a user mood or genre is missing from the dataset, the system falls back to energy and acousticness.
That can ignore users with more complex or mixed tastes.
The small dataset can also over-represent whichever genres have more examples.

---

## 7. Evaluation  

I tested normal and adversarial user profiles.
I checked whether the top-5 songs matched the strongest user preferences.
I compared outputs across profile pairs in `reflection.md`.
I also ran a sensitivity experiment by changing weights.
The biggest surprise was how quickly rankings changed when energy weight increased.

---

## 8. Future Work  

I would add diversity rules so top results are not all the same vibe.
I would add more user signals, like skips, repeats, and recency.
I would tune weights per user instead of using one global setting.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can rewrite the whole top-5 list.
AI tools helped me move faster when drafting code structure and documentation.
I still needed to double-check outputs, math, and imports by running the CLI and tests.
I was surprised that a simple weighted score can still feel like a real recommendation feed.
If I extend this project, I want to add collaborative signals and better diversity controls.
