# Progress Log

Starting this challenge from zero — no LeetCode problems solved before Day 1.
The goal is 1 problem/day, in Java, from true beginner fundamentals up through
advanced interview-level topics. Every row below is a real problem solved
myself.

Rows are appended automatically by `tools/complete_day.py` — don't hand-edit the
table below unless you're fixing a mistake.

| Day | Date | Problem | Difficulty | Approach/Rationale | Time/Space Complexity | Solution Link |
|---|---|---|---|---|---|---|
| 1 | 2026-08-16 | Two Sum | Easy | Brute-force nested loop checking every pair for target sum. | O(n^2) / O(1) | [day-001-two-sum.java](solutions/day-001-two-sum.java) |
| 2 | 2026-08-16 | Valid Anagram | Easy | Sorted both char arrays and compared for equality after an early length check. | O(n log n) / O(n) | [day-002-valid-anagram.java](solutions/day-002-valid-anagram.java) |
| 3 | 2026-08-17 | Contains Duplicate | Easy | Used a HashSet, adding each number and checking membership before insert; return true on first repeat, false if loop completes. | O(n) / O(n) | [day-003-contains-duplicate.java](solutions/day-003-contains-duplicate.java) |
| 4 | 2026-08-17 | Valid Palindrome | Easy | Lowercased and stripped non-alphanumeric characters via regex, then compared the string to its reversed StringBuilder form. | O(n) / O(n) | [day-004-valid-palindrome.java](solutions/day-004-valid-palindrome.java) |
| 5 | 2026-08-18 | Reverse String | Easy | Two-pointer in-place swap from both ends toward the middle. | O(n) / O(1) | [day-005-reverse-string.java](solutions/day-005-reverse-string.java) |
| 6 | 2026-08-20 | Best Time to Buy and Sell Stock | Easy | one-pass min-price tracking, update max profit as we scan | O(n) / O(1) | [day-006-best-time-to-buy-and-sell-stock.java](solutions/day-006-best-time-to-buy-and-sell-stock.java) |
<!-- COMPLETE_DAY_INSERT_MARKER -->

## Redo log

Every ~6 months, redo one early problem (Day 1-20 range) from scratch and log it
here side-by-side with the original. This is the single most convincing "growth"
proof for interviews — visible before/after on your own timeline.

| Redo Date | Original Day | Problem | Original Solution | Redo Solution | What changed / why |
|---|---|---|---|---|---|
| | | | | | |

## Feedback log

Roughly every 2-3 weeks, review recurring mistakes or patterns you keep missing
and note what you changed as a result. Self-practice alone plateaus — this is
what prevents that.

| Date | Topic / Pattern | What went wrong | What I changed |
|---|---|---|---|
