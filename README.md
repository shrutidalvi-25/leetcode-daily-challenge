# LeetCode Daily Challenge — 2 Years to Graduation

A structured, ~2-year (Aug 2026 -> May 2028) daily LeetCode practice log in Java: 625
real, verified problems, one per day, organized into 20 progressive phases — from
absolute first-timer fundamentals (arrays, strings, hashing) up through advanced
interview-level topics (advanced graphs, tries, DP on grids, mock-interview-hard
review). Every entry committed here is a real solved problem, so the commit history
itself is proof of consistent practice, not a certificate claiming it happened.

This schedule is shared with a friend doing the same challenge in parallel
(same 625 problems, same order) — we solve the same problem each day and
compare notes, but track progress in our own separate repos.

<!-- STREAK_START -->
🔥 **Current streak:** 2 days · **Longest streak:** 8 days
<!-- STREAK_END -->

<!-- PROGRESS_BAR_START -->
`█░░░░░░░░░░░░░░░░░░░` **16 / 625 days (2.6%)**
<!-- PROGRESS_BAR_END -->

<!-- STATUS_START -->
**Status: Day 16 complete** (last solved: 2026-08-30). Next up: Day 17 — Roman to Integer (2026-08-31).
<!-- STATUS_END -->

## Ground rule

**I solve every problem myself.** AI tools may explain concepts, review my code
after the fact, and unblock me when I'm stuck, but never write my solutions for
me. The entire value of this repo as interview-prep proof depends on every
solution being my own work, written under my own understanding — a recruiter
who opens `solutions/` should be looking at code that proves *I* can do this.

## Structure

The full day-by-day plan is in `SCHEDULE.csv`. Columns:
`day_number, date, phase, topic, problem_name, difficulty, leetcode_url, notes`.

| Phase | Focus |
|---|---|
| 1. Basics / Arrays & Strings | True fundamentals — arrays, strings, easy warmups |
| 2. Two Pointers & Sliding Window | Classic two-pointer and window patterns |
| 3. Hashing | Hash maps/sets as a problem-solving tool |
| 4. Stacks & Queues | Monotonic stacks, calculators, parsing |
| 5. Linked Lists | Pointer manipulation, cycle detection |
| 6. Recursion & Backtracking Basics | Base recursion, subsets/permutations |
| 7. Binary Search | Search space reduction, "search on the answer" |
| 8. Trees & BST | Traversals, BST properties, tree DP intro |
| 9. Heaps / Priority Queues | Top-K, scheduling, streaming median |
| 10. Graphs (BFS/DFS) | Grid/graph traversal, islands, topological basics |
| 11. Dynamic Programming 1D | Classic 1D DP (robber, coin change, LIS...) |
| 12. Dynamic Programming 2D | Grid DP, string DP (LCS, edit distance...) |
| 13. Greedy | Interval/greedy proofs and patterns |
| 14. Advanced Backtracking | N-Queens, Sudoku, harder search spaces |
| 15. Advanced Graphs | Dijkstra, Union-Find, topological sort, MST |
| 16. Tries | Prefix trees for word search/autocomplete-style problems |
| 17. Bit Manipulation | XOR tricks, bit counting |
| 18. Intervals | Merge/insert/scheduling interval problems |
| 19. Math & Geometry | Matrix manipulation, math-heavy problems |
| 20. Mixed Hard / Mock-Interview Review | Hard-tier review spanning all topics |

**Cadence:** 1 problem/day, not literal-every-single-day — sustainable through
exams and internship crunch. Every entry is real; the schedule is what flexes.

**On problem sourcing:** every problem name and URL in `SCHEDULE.csv` was checked
against real, published LeetCode problems (Blind 75, NeetCode 150/250, Grind 75/169,
LeetCode's official "Top Interview 150," "Dynamic Programming," "Graph Theory," and
"Binary Search" study plans, and similar well-documented, well-known lists). None
were guessed or invented — the schedule spans the full 625-day runway from
2026-08-16 through 2028-05-01, with the deepest phases (Trees & BST, Dynamic
Programming, Arrays & Strings) carrying the most extra depth since they show up
most in real interviews.

## How to log a day's work

The schedule is **living, not fixed** — `SCHEDULE.csv` dates always reflect the
real, current plan, not a calendar set in stone at the start. Miss a day (or
several) and every date after it automatically shifts forward — you never fall
"behind a fixed calendar," you just continue from wherever you actually are.
Your schedule will naturally drift independently from your friend's as you each
progress at your own real pace — that's expected, the day *number* (not the
date) is what keeps you on the same problem list.

1. Solve today's problem (whatever the next unfinished row in `SCHEDULE.csv` is
   — ignore its listed date if you're catching up, the day number is what
   matters).
2. Save your Java solution to `solutions/day-<NNN>-<problem-slug>.java`, e.g.
   `solutions/day-001-two-sum.java`.
3. Run:
   ```
   python tools/complete_day.py <day_number> "<approach/rationale>" "<time complexity>" "<space complexity>"
   ```
   Example:
   ```
   python tools/complete_day.py 1 "Hash map storing value -> index, single pass." "O(n)" "O(n)"
   ```
   This appends the entry to `PROGRESS.md` with **today's real date**, and
   reschedules every remaining day in `SCHEDULE.csv` to flow forward from today
   — so a missed day never needs manual date-fixing.
4. Commit, same day:
   ```
   git add .
   git commit -m "Day 001: Two Sum"
   git push
   ```
5. The script prints the next scheduled problem — that's tomorrow's task.

## Tech stack

- **Language:** Java
- **Tooling:** plain `.java` files per problem (no build system required to start;
  a Maven/Gradle wrapper can be added later if problems need external test
  scaffolding)
- **Automation:** `tools/complete_day.py` (Python) for daily logging — repo
  tooling only, not part of the solutions themselves

## Reading the log

- **`SCHEDULE.csv`** — the full plan: every problem, in order, with its current
  scheduled date. This is what "today's problem" means at any point in time.
- **`PROGRESS.md`** — the actual history: one row per problem *solved*, with the
  real date it was solved, the approach taken, time/space complexity, and a link
  to the solution file. This is the proof.
- **`solutions/`** — the Java source for every solved problem, named
  `day-<NNN>-<problem-slug>.java`.

## Redo ritual (every ~6 months)

Pick one problem from the first 20 days and re-solve it from scratch with
everything learned since. Log it side-by-side in the **Redo log** section of
`PROGRESS.md`. A visible before/after on your own timeline is strong, honest
proof of growth — stronger than volume alone.
