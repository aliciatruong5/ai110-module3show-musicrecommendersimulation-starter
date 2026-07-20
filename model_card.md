# 🎧 Model Card: Music Recommender Simulation

## 1. VibeCheck 1.0  

---

## 2. Intended Use  

My recommender tries to predict which songs a listener will like. It takes a
user's taste (favorite genre, mood, energy level, and whether they like acoustic
music) and suggests the songs that best match it.

It assumes the user can describe their taste in those few features. It also
assumes taste stays the same, since it does not learn over time.

It runs on a tiny catalog and
is meant to show how a simple recommender works.

---

## 3. How the Model Works  

The model gives each song a score based on how well it fits the user. Then it
sorts the songs from highest to lowest score and shows the top few.

It uses four things about each song: genre, mood, energy, and how acoustic it is.
It compares these to what the user wants.

Here is how points are given:

- If the genre matches, the song gets points. Genre is worth the most.
- If the mood matches, the song gets some points too.
- For energy, the song gets more points the closer it is to the user's target.
  Too high or too low both lose points.
- If the user likes acoustic music, acoustic songs get a bonus.

The starter code just returned the first few songs. I added the real scoring
rules, the sorting, a short reason for each pick, and the closeness math for
energy so it rewards a good match instead of just loud or quiet songs.

---

## 4. Data  

The dataset is a small CSV file of songs. It started with 10 songs. I added 8
more, so it now has 18.

Each song has these features: title, artist, genre, mood, energy, tempo, valence,
danceability, and how acoustic it is. My scoring uses genre, mood, energy, and
acousticness.

The songs cover many genres, like pop, lofi, rock, jazz, EDM, metal, classical,
and folk. Moods include happy, chill, intense, melancholy, and more.

---

## 5. Strengths  

The system works well when the user has a clear, common taste. Each of my four
test profiles got a top pick that made sense. It matches genre and mood the way I expected. The energy score rewards songs that are close to what the user wants, not just loud or quiet ones.

---

## 6. Limitations and Bias 

Limits: the catalog is tiny, so some genres only have one song. It has no lyrics
or language, no artist popularity, and no real listening history. It is just a
sample, so it does not cover all kinds of music or taste.

Filter bubble: My recommender is pure exploitation — it heavily weights exact genre matches and has no exploration or genre-similarity, so it can only recommend more of what the user already likes and structurally cannot broaden their taste.

Bias / fairness: It favors acoustic-preferring users (extra scoring term) and users whose genres are well-represented in the catalog (the sparse-genre cliff), meaning the quality of someone's experience depends on both their stated preferences and who happens to be in the dataset — a small-scale echo of representation bias in real systems.

---

## 7. Evaluation  

### Profiles I tested

- **pop_fan** – pop, happy, high energy
- **lofi_studier** – lofi, chill, low energy, likes acoustic
- **edm_fan** – EDM, euphoric, very high energy
- **classical_fan** – classical, melancholy, low energy, likes acoustic

Top pick for each: 
- pop_fan got Sunrise City
- lofi_studier got Library Rain
- edm_fan got Pulse Reactor
- classical_fan got Winter Elegy.

### What surprised me
- Typing "Pop" instead of "pop" broke the match. The system ignored genre and mood and gave no warning.
- Adding raw tempo took over the whole score. A pop fan got metal songs just because they were fast.
- The system never says "no good match." It always fills the list, even with weak picks.

### Comparing pairs of profiles

- **pop_fan vs lofi_studier:** No shared songs. They are opposites in genre, mood, and energy, so the picks go in different directions. Makes sense.
- **pop_fan vs edm_fan:** Both want high energy. Gym Hero shows up for both, but scores high for pop_fan (genre match) and low for edm_fan (energy only). Makes sense.
- **pop_fan vs classical_fan:** No shared songs. classical_fan scores higher because it likes acoustic, which adds points. That points to a bias.
- **lofi_studier vs edm_fan:** Total opposites. One is calm and acoustic, one is loud and not. Nothing overlaps. Makes sense.
- **lofi_studier vs classical_fan:** Both are calm and like acoustic, but still share no songs. Genre is an exact match, so lofi and classical stay separate even though they feel similar.
- **edm_fan vs classical_fan:** Opposites, and both genres only have one song. After the top pick, both drop off fast. classical_fan's backups score higher because its acoustic bonus keeps helping.

---

## 8. Future Work  

In a future model, I would add more features so the recommendations fit each user better. For example, I would let users pick more than one favorite genre or mood. I would also treat similar genres as somewhat the same, so users can discover new songs instead of hearing the same style every time. Finally, I would add a "surprise me" feature so the list changes and doesn't always show the same songs.

---

## 9. Personal Reflection  

This project opened my eyes to how recommender systems really work. Before, I thought an app just guessed what I might like. But I discovered it is more math than guessing. Once I saw that, it surprised me how simple the idea behind it actually is.
The most interesting thing I discovered was that the system can still be biased based on the genre or mood you enter. Because I decide how much each feature is worth, the results lean toward whatever I weight the most. 

In the end, there is no magic 8 ball randomly picking the next song I should hear. It is just data and rules working together. 



