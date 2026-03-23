# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it appeared to be a working number guessing game with a text input, a Submit Guess button, and a hint display. However, several bugs became clear after playing twice.

**Bug 1: Hints were backwards**
- **Expected:** When I guessed 50 and the secret number was 14, the hint should have said "Go LOWER" since 50 is greater than 14.
- **Actual:** The game said "Go HIGHER," pointing me in completely the wrong direction.

**Bug 2: Hints kept saying "Go Higher" even past the secret number**
- **Expected:** Once my guess exceeded the secret number (e.g., guessing 60 when the secret was 40), the hint should have switched to "Go LOWER."
- **Actual:** The game kept telling me to go higher all the way up to 100, only flipping direction at the very top — making the game nearly unwinnable.

**Bug 3: Score went negative**
- **Expected:** Running out of attempts should end the game with a score of 0, or at least not penalize the player below zero.
- **Actual:** The score dropped to -5 after one lost game and -10 after another, suggesting the scoring formula has a bug that subtracts points incorrectly.

**Bug 4: Game state did not reset cleanly between rounds**
- **Expected:** Starting a new game should reset the score, guess history, and secret number completely.
- **Actual:** When I opened the Developer Debug Info at the start of a new game, it still showed the guess history and score from the previous round, meaning session state was not being properly cleared.

---

## 2. How did you use AI as a teammate?

On this project I used Claude (by Anthropic) as my AI assistant since GitHub Copilot had reached its usage quota. I pasted my full `app.py` and `logic_utils.py` code directly into the chat and described the bugs I observed while playing.

**Correct AI suggestion:** Claude correctly identified that the hint bug was caused by a type mismatch in `app.py` — on even-numbered attempts, the secret number was being converted to a string using `str(st.session_state.secret)`, which caused Python's string comparison to produce wrong results instead of a numeric comparison. I verified this by reading the specific lines in `app.py` where `if st.session_state.attempts % 2 == 0` was switching the secret to a string, and confirmed it matched exactly what Claude described.

**Incorrect/misleading suggestion:** Claude's first draft of `logic_utils.py` still contained the old buggy hint messages — `check_guess` returned `"Go HIGHER!"` when the guess was too high, when it should say `"Go LOWER!"`. I caught this by comparing the function's return values against what the game should logically do: if your guess is too high, you need to go lower. I pointed this out and Claude corrected the messages in the next version.

---

## 3. Debugging and testing your fixes

I verified each fix in two ways: by manually playing the game in the browser and by running pytest. For manual testing, I opened the Developer Debug Info panel to see the secret number, then made a guess I knew should trigger a specific hint — for example, guessing 80 when the secret was 31 to confirm it now correctly said "Go LOWER." For automated testing, I ran the existing tests in `tests/test_game_logic.py` using `pytest` in the terminal. The three starter tests (`test_winning_guess`, `test_guess_too_high`, `test_guess_too_low`) all passed after my fixes to `logic_utils.py`, confirming the core logic was correct. Claude helped me understand what each test was asserting and why the return value needed to be a tuple like `("Too High", "📈 Go LOWER!")` rather than just a string.

---
## 4. What did you learn about Streamlit and state?

Streamlit works differently from most programs because every time you interact with it — clicking a button, typing in a box — the entire Python script reruns from the top. I would explain it to a friend like this: imagine every button click reloads the whole page from scratch, so any variables you set earlier are gone unless you specifically save them. That is what `st.session_state` is for — it is like a small notebook Streamlit keeps between reruns, so your score, your guess history, and the secret number do not disappear every time the script re-executes. This is exactly why the game had a bug where starting a new game did not fully reset things — the session state was only partially cleared, so old scores and history bled into the new round.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is adding `# FIXME` comments the moment I spot something suspicious, before I even try to fix it — it kept me organized and gave the AI a clear anchor point when describing the bug. Next time I work with AI on a coding task, I would paste the actual code and describe the specific behavior I observed rather than just describing the bug in general terms, because the more concrete context I gave Claude, the more accurate its explanation was. This project changed how I think about AI-generated code: I used to assume that if code runs without crashing it is probably correct, but now I understand that code can run perfectly fine and still have deeply wrong logic that only shows up when you actually play with it.
