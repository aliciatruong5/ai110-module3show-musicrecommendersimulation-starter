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
python3 -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output for Each Profile
```
============================================================
  Recommendations for: pop_fan
  Taste: genre=pop, mood=happy, energy=0.8, likes_acoustic=False
============================================================

1. Sunrise City  —  Neon Echo
   Score: 3.98
   Why:   genre matches (pop); mood matches (happy); energy is close (0.82)

2. Gym Hero  —  Max Pulse
   Score: 2.87
   Why:   genre matches (pop); energy is close (0.93)

3. Rooftop Lights  —  Indigo Parade
   Score: 1.96
   Why:   mood matches (happy); energy is close (0.76)

4. Night Drive Loop  —  Neon Echo
   Score: 0.95
   Why:   energy is close (0.75)

5. Concrete Kings  —  Verse Machine
   Score: 0.90
   Why:   energy is close (0.7)
```
```
============================================================
  Recommendations for: lofi_studier
  Taste: genre=lofi, mood=chill, energy=0.4, likes_acoustic=True
============================================================

1. Library Rain  —  Paper Lanterns
   Score: 4.81
   Why:   genre matches (lofi); mood matches (chill); energy is close (0.35); acoustic (0.86)

2. Midnight Coding  —  LoRoom
   Score: 4.69
   Why:   genre matches (lofi); mood matches (chill); energy is close (0.42); acoustic (0.71)

3. Focus Flow  —  LoRoom
   Score: 3.78
   Why:   genre matches (lofi); energy is close (0.4); acoustic (0.78)

4. Spacewalk Thoughts  —  Orbit Bloom
   Score: 2.80
   Why:   mood matches (chill); energy is close (0.28); acoustic (0.92)

5. Coffee Shop Stories  —  Slow Stereo
   Score: 1.86
   Why:   energy is close (0.37); acoustic (0.89)
```
```
============================================================
  Recommendations for: edm_fan
  Taste: genre=EDM, mood=euphoric, energy=0.95, likes_acoustic=False
============================================================

1. Pulse Reactor  —  Kilovolt
   Score: 4.00
   Why:   genre matches (EDM); mood matches (euphoric); energy is close (0.95)

2. Gym Hero  —  Max Pulse
   Score: 0.98
   Why:   energy is close (0.93)

3. Iron Verdict  —  Blackspire
   Score: 0.97
   Why:   energy is close (0.98)

4. Storm Runner  —  Voltline
   Score: 0.96
   Why:   energy is close (0.91)

5. Sunrise City  —  Neon Echo
   Score: 0.87
   Why:   energy is close (0.82)
```
```
============================================================
  Recommendations for: classical_fan
  Taste: genre=classical, mood=melancholy, energy=0.3, likes_acoustic=True
============================================================

1. Winter Elegy  —  The Aurelian Quartet
   Score: 4.95
   Why:   genre matches (classical); mood matches (melancholy); energy is close (0.3); acoustic (0.95)

2. Spacewalk Thoughts  —  Orbit Bloom
   Score: 1.90
   Why:   energy is close (0.28); acoustic (0.92)

3. Coffee Shop Stories  —  Slow Stereo
   Score: 1.82
   Why:   energy is close (0.37); acoustic (0.89)

4. Library Rain  —  Paper Lanterns
   Score: 1.81
   Why:   energy is close (0.35); acoustic (0.86)

5. Focus Flow  —  LoRoom
   Score: 1.68
   Why:   energy is close (0.4); acoustic (0.78)
```

As you can see in this sample, this system shows genre outweighing mood. 

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



