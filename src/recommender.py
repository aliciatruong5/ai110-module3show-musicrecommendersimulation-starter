import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# Feature weights: how much each signal matters in the final score.
# Tune these in your Experiments section and watch how the ranking changes.
WEIGHT_GENRE = 2.0
WEIGHT_MOOD = 1.5
WEIGHT_ENERGY = 1.0
WEIGHT_ACOUSTIC = 1.0

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

    def score(self, user: UserProfile, song: Song) -> float:
        """Weighted sum of how well one song matches the user's taste."""
        total = 0.0
        # Categorical features: exact match earns the full weight.
        if song.genre == user.favorite_genre:
            total += WEIGHT_GENRE
        if song.mood == user.favorite_mood:
            total += WEIGHT_MOOD
        # Numeric feature: reward closeness to the target, not raw magnitude.
        energy_closeness = 1 - abs(song.energy - user.target_energy)
        total += WEIGHT_ENERGY * energy_closeness
        # Acousticness only counts if the user actually wants acoustic songs.
        if user.likes_acoustic:
            total += WEIGHT_ACOUSTIC * song.acousticness
        return total

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Score every song, then sort highest-first and take the top k.
        ranked = sorted(self.songs, key=lambda s: self.score(user, s), reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # Turn the matched features into a human-readable "because" string.
        reasons: List[str] = []
        if song.genre == user.favorite_genre:
            reasons.append(f"it's your favorite genre ({song.genre})")
        if song.mood == user.favorite_mood:
            reasons.append(f"it matches your {song.mood} mood")
        if abs(song.energy - user.target_energy) <= 0.15:
            reasons.append(f"its energy ({song.energy}) is close to what you want")
        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append(f"it's acoustic ({song.acousticness})")

        if not reasons:
            return f"'{song.title}' is a loose match for your taste."
        return f"'{song.title}' was recommended because " + ", and ".join(reasons) + "."

NUMERIC_FIELDS = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dicts.
    Numeric columns are converted from strings to floats.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in NUMERIC_FIELDS:
                if field in row:
                    row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns (score, reasons) where reasons explains what matched.
    """
    score = 0.0
    reasons: List[str] = []

    # Genre: exact categorical match.
    if user_prefs.get("genre") and song.get("genre") == user_prefs["genre"]:
        score += WEIGHT_GENRE
        reasons.append(f"genre matches ({song['genre']})")

    # Mood: exact categorical match.
    if user_prefs.get("mood") and song.get("mood") == user_prefs["mood"]:
        score += WEIGHT_MOOD
        reasons.append(f"mood matches ({song['mood']})")

    # Energy: reward closeness to the user's target, not high/low values.
    if "energy" in user_prefs and "energy" in song:
        closeness = 1 - abs(song["energy"] - user_prefs["energy"])
        score += WEIGHT_ENERGY * closeness
        if closeness >= 0.85:
            reasons.append(f"energy is close ({song['energy']})")

    # Acousticness: only rewarded if the user asked for acoustic songs.
    if user_prefs.get("likes_acoustic") and "acousticness" in song:
        score += WEIGHT_ACOUSTIC * song["acousticness"]
        if song["acousticness"] >= 0.6:
            reasons.append(f"acoustic ({song['acousticness']})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, ranks highest-first, and returns the top k as
    (song_dict, score, explanation) tuples.
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "weak match"
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
