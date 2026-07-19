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
ACTIVE_PROFILE = "lofi_studier"


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = PROFILES[ACTIVE_PROFILE]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nProfile: {ACTIVE_PROFILE} -> {user_prefs}")
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
