# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version is a small content-based music recommender. It reads a catalog of songs from a CSV file, where each song has attributes like genre, mood, energy, and acousticness. It also takes a user's taste profile — their favorite genre, favorite mood, preferred energy level, and whether they like acoustic music. For every song, it calculates a score based on how well the song's attributes match that profile, giving more weight to genre and mood, rewarding songs whose energy is close to what the user wants, and adding points for acoustic songs when the user prefers them. It then sorts all the songs by score and returns the top few, along with a short explanation of why each one was recommended.

---

## How The System Works

### How real-world recommendations work

  Real-world recommenders like Spotify and YouTube rely on two main kinds of data. The first is content features — attributes of the item itself, such as a song's genre, mood, tempo, energy, or a video's topic and length. These describe what the item is, so the system can find others that are similar. The second is user history — what you've played, skipped, saved, liked, or watched to the end, plus context like time of day. This describes what you actually enjoy, and it also lets the system spot patterns across users ("people who liked this also liked that"). The platforms combine both: content features help recommend brand-new items that no one has interacted with yet, while user history captures personal taste and surprising connections that the attributes alone would miss. A ranking model weighs all these signals together to decide what to show next, and it keeps updating as you give it more feedback.

  ### My Version 

  My version focuses on just the content-based piece, since it works without any other users' data. It prioritizes matching a song's attributes to a user's stated taste — weighting genre and mood most heavily, rewarding songs whose energy is close to what the user wants rather than simply louder or quieter, and favoring acoustic tracks when the user prefers them. It's a deliberately simplified, transparent version of one part of how the real systems work

### Song features

**Identifiers (not scored):**
- `id`, `title`, `artist`

**Used in scoring:**
- `genre` — categorical (pop, lofi, rock, etc.)
- `mood` — categorical (happy, chill, intense, etc.)
- `energy` — numeric 0–1
- `acousticness` — numeric 0–1

**Reserved for experiments:**
- `valence`, `danceability` — numeric 0–1
- `tempo_bpm` — numeric (~60–152, not normalized)

### UserProfile fields
- `favorite_genre` — matched against the song's genre
- `favorite_mood` — matched against the song's mood
- `target_energy` — desired energy level (scored by closeness, not "higher is better")
- `likes_acoustic` — when true, rewards acoustic songs

### Features that connect them in the score
- `genre` ↔ `favorite_genre`
- `mood` ↔ `favorite_mood`
- `energy` ↔ `target_energy`
- `acousticness` ↔ `likes_acoustic`

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



