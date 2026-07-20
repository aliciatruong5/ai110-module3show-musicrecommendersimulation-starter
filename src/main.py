"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


# A few example listeners to demo how the recommender adapts to taste.
# Switch the active profile below to try a different one.
PROFILES = {
    "pop_fan": {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False},
    "lofi_studier": {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True},
    "edm_fan": {"genre": "EDM", "mood": "euphoric", "energy": 0.95, "likes_acoustic": False},
    "classical_fan": {"genre": "classical", "mood": "melancholy", "energy": 0.3, "likes_acoustic": True},
}

# Change this key to switch listeners.
ACTIVE_PROFILE = "classical_fan"


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = PROFILES[ACTIVE_PROFILE]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # --- Header: who these recommendations are for ---
    print()
    print("=" * 60)
    print(f"  Recommendations for: {ACTIVE_PROFILE}")
    print(f"  Taste: genre={user_prefs.get('genre')}, "
          f"mood={user_prefs.get('mood')}, "
          f"energy={user_prefs.get('energy')}, "
          f"likes_acoustic={user_prefs.get('likes_acoustic')}")
    print("=" * 60)

    # --- Ranked list: number, title, artist, score, then reasons ---
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}  —  {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why:   {explanation}")

    print()


if __name__ == "__main__":
    main()
