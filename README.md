# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Create and activate a virtual environment:
   ```bash
   python3.13 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python -m streamlit run app.py
   ```

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask an AI: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.**
   - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:**
This is a number guessing game where the player tries to guess a secret number between 1 and 100. The game gives hints after each guess ("Go Higher" or "Go Lower") and tracks your score across attempts. You have a limited number of attempts depending on the difficulty level selected.

**Bugs Found:**
1. **Hints were backwards** — the `check_guess` function returned "Go HIGHER!" when the guess was too high and "Go LOWER!" when the guess was too low, the exact opposite of what they should say.
2. **Type mismatch causing broken hints** — on even-numbered attempts, `app.py` was converting the secret number to a string using `str()`, which caused Python's string comparison to produce wrong and unpredictable results instead of a numeric comparison.
3. **Score went negative** — the `update_score` function randomly added +5 points on even attempts for a wrong guess, causing the score to behave erratically and go negative.
4. **Game state did not reset between rounds** — clicking "New Game" only reset the secret number and attempts, but not the score, history, or game status, so old data carried over into the new round.

**Fixes Applied:**
1. Corrected the hint messages in `check_guess` in `logic_utils.py` so "Too High" maps to "Go LOWER!" and "Too Low" maps to "Go HIGHER!"
2. Removed the `str()` type conversion in `app.py` so the secret is always compared as an integer.
3. Simplified `update_score` to always subtract 5 points for a wrong guess, removing the broken even/odd attempt logic.
4. Updated the "New Game" handler in `app.py` to fully reset `score`, `status`, and `history` in addition to `secret` and `attempts`.
5. Refactored all game logic functions out of `app.py` and into `logic_utils.py`, then imported them cleanly at the top of `app.py`.

## 📸 Demo

> **Screenshot of fixed game — hints now correctly say "Go LOWER" when guess is too high:**

[Insert screenshot of your winning game here — take one with Cmd+Shift+4 on Mac, drag to select the game window, then drag the saved image file into this README in VS Code]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
