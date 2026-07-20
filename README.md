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

### EXPERIMENT 1: WEIGHT_GENRE 2.0 -> 0.5 (profile: pop_fan)

```
WEIGHT_GENRE = 2.0:
   Sunrise City         3.98
   Gym Hero             2.87
   Rooftop Lights       1.96
   Night Drive Loop     0.95
   Concrete Kings       0.90

WEIGHT_GENRE = 0.5:
   Sunrise City         2.48
   Rooftop Lights       1.96
   Gym Hero             1.37
   Night Drive Loop     0.95
   Concrete Kings       0.90
```
In this experiment, I lowered the genre's weight. The genre weight acts as a tie-breaker between "right genre" and "right mood" songs — turning it down lets other features decide the order.

### EXPERIMENT 2: adding valence vs raw tempo
```
Baseline (pop_fan):
   Sunrise City         3.98
   Gym Hero             2.87
   Rooftop Lights       1.96
   Night Drive Loop     0.95
   Concrete Kings       0.90

+ valence term (normalized, well-behaved):
   Sunrise City         4.94
   Gym Hero             3.84
   Rooftop Lights       2.95
   Island Time          1.80
   Pulse Reactor        1.80

+ RAW tempo term (unnormalized, dominates):
   Iron Verdict         160.82
   Storm Runner         152.89
   Gym Hero             134.87
   Pulse Reactor        128.85
   Rooftop Lights       125.96
```
This is the normalization trap in action — an unnormalized feature silently hijacks the entire score. It's the strongest argument for why tempo_bpm must be scaled to 0–1 before use (or left out).

### "Adversarial" User Profiles/Edge Cases

```
================================================================
conflicting_energy_mood: {'genre': 'classical', 'mood': 'melancholy', 'energy': 0.95, 'likes_acoustic': False}
  1. Winter Elegy         [classical/melancholy] score=3.35  (genre matches (classical); mood matches (melancholy))
  2. Pulse Reactor        [EDM/euphoric] score=1.00  (energy is close (0.95))
  3. Gym Hero             [pop/intense] score=0.98  (energy is close (0.93))

================================================================
nonexistent_genre: {'genre': 'reggaeton', 'mood': 'happy', 'energy': 0.7, 'likes_acoustic': False}
  1. Rooftop Lights       [indie pop/happy] score=1.94  (mood matches (happy); energy is close (0.76))
  2. Sunrise City         [pop/happy] score=1.88  (mood matches (happy); energy is close (0.82))
  3. Concrete Kings       [hip-hop/confident] score=1.00  (energy is close (0.7))

================================================================
wrong_case: {'genre': 'Pop', 'mood': 'Happy', 'energy': 0.8, 'likes_acoustic': False}
  1. Sunrise City         [pop/happy] score=0.98  (energy is close (0.82))
  2. Rooftop Lights       [indie pop/happy] score=0.96  (energy is close (0.76))
  3. Night Drive Loop     [synthwave/moody] score=0.95  (energy is close (0.75))

================================================================
empty: {}
  1. Sunrise City         [pop/happy] score=0.00  (weak match)
  2. Midnight Coding      [lofi/chill] score=0.00  (weak match)
  3. Storm Runner         [rock/intense] score=0.00  (weak match)

================================================================
acoustic_only: {'likes_acoustic': True}
  1. Winter Elegy         [classical/melancholy] score=0.95  (acoustic (0.95))
  2. Spacewalk Thoughts   [ambient/chill] score=0.92  (acoustic (0.92))
  3. Coffee Shop Stories  [jazz/relaxed] score=0.89  (acoustic (0.89))

================================================================
genre_mood_impossible: {'genre': 'metal', 'mood': 'chill', 'energy': 0.9, 'likes_acoustic': False}
  1. Iron Verdict         [metal/aggressive] score=2.92  (genre matches (metal); energy is close (0.98))
  2. Midnight Coding      [lofi/chill] score=1.52  (mood matches (chill))
  3. Library Rain         [lofi/chill] score=1.45  (mood matches (chill))

================================================================
energy_out_of_range: {'genre': 'pop', 'mood': 'happy', 'energy': 2.0, 'likes_acoustic': False}
  1. Sunrise City         [pop/happy] score=2.82  (genre matches (pop); mood matches (happy))
  2. Gym Hero             [pop/intense] score=1.93  (genre matches (pop))
  3. Rooftop Lights       [indie pop/happy] score=0.76  (mood matches (happy))
```

---

## Limitations and Risks

Some limitations are
 - Genre lock-in, where the genre carries the highest weight and is scored by the exact match only.
 - No genre similarity, which enforces narrowness
 - Pure exploitation, zero exploration, where the same profile always returns the same songs in the same order
 - Acoustic-preference bias, where the likes_acoustic=True unlocks a fifth scoring term (up to +1.0) that False users never get
 - Catalog representation bias — the sparse-genre cliff, where genres with more songs serve their fans far better.

This will go deeper in the model card.

---

## Reflection

With this project, I learned that recommenders turn data into predictions by scoring. I always thought it would guess what I would like to hear by seeing what I just heard. The system would compare each song with what the user's preference then give each song a number for how well it would match with the user. It made me realize that the prediction is not really a prediction. It is just math on what the user liked to hear more than the rest. This made me see how bias can show up. It would favor the songs that user would listen to more and add that to the points that it had. So the user's music tastes more depends on what their dataset looks like not their "tastes"

[**Model Card**](model_card.md)




