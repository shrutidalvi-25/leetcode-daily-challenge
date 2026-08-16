"""
Marks a day complete, logs it to PROGRESS.md with today's real date, and reschedules
every future date in SCHEDULE.csv to flow from that real date. This is what makes missed
days self-correcting: whatever the actual completion date is, everything after it shifts
to match, so SCHEDULE.csv always reflects the real, current plan instead of a fixed
calendar that drifts out of sync with reality.

Usage:
  python tools/complete_day.py <day_number> "<approach_note>" "<time_complexity>" "<space_complexity>"

Example:
  python tools/complete_day.py 1 "Used a hash map to store seen values and their indices, one pass." "O(n)" "O(n)"

Expects the solution file to already exist at:
  solutions/day-<NNN>-<problem-slug>.java
"""
import csv
import datetime
import re
import sys
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCHEDULE_PATH = os.path.join(ROOT, "SCHEDULE.csv")
PROGRESS_PATH = os.path.join(ROOT, "PROGRESS.md")
README_PATH = os.path.join(ROOT, "README.md")
SOLUTIONS_DIR = os.path.join(ROOT, "solutions")

ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|")

FIELDNAMES = [
    "day_number", "date", "phase", "topic", "problem_name",
    "difficulty", "leetcode_url", "notes",
]


def next_day(d):
    return d + datetime.timedelta(days=1)


def slugify(name):
    s = name.lower()
    s = re.sub(r"[()',!?]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def compute_streaks(progress_content):
    """Read completed (day, date) rows from PROGRESS.md and return (current, longest) streaks,
    where a streak is unbroken consecutive calendar days with a logged entry."""
    entries = []
    for line in progress_content.splitlines():
        m = ROW_RE.match(line)
        if m:
            entries.append((int(m.group(1)), datetime.date.fromisoformat(m.group(2))))
    entries.sort(key=lambda e: e[0])

    if not entries:
        return 0, 0

    current = longest = 1
    for (_, prev_date), (_, date) in zip(entries, entries[1:]):
        if date == prev_date + datetime.timedelta(days=1):
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return current, longest


def update_streak_in_readme(current, longest):
    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    new_block = (
        f"<!-- STREAK_START -->\n"
        f"\U0001f525 **Current streak:** {current} day{'s' if current != 1 else ''} · "
        f"**Longest streak:** {longest} day{'s' if longest != 1 else ''}\n"
        f"<!-- STREAK_END -->"
    )
    content = re.sub(
        r"<!-- STREAK_START -->.*?<!-- STREAK_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def update_progress_bar_in_readme(completed, total, bar_width=20):
    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    filled = round(bar_width * completed / total) if total else 0
    bar = "█" * filled + "░" * (bar_width - filled)
    pct = (completed / total * 100) if total else 0
    new_block = (
        f"<!-- PROGRESS_BAR_START -->\n"
        f"`{bar}` **{completed} / {total} days ({pct:.1f}%)**\n"
        f"<!-- PROGRESS_BAR_END -->"
    )
    content = re.sub(
        r"<!-- PROGRESS_BAR_START -->.*?<!-- PROGRESS_BAR_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def update_status_in_readme(day_num, last_date, next_row):
    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    if next_row:
        status_line = (
            f"**Status: Day {day_num} complete** (last solved: {last_date}). "
            f"Next up: Day {next_row['day_number']} — {next_row['problem_name']} "
            f"({next_row['date']})."
        )
    else:
        status_line = (
            f"**Status: Day {day_num} complete** (last solved: {last_date}). "
            f"All 625 days done — challenge complete."
        )

    new_block = f"<!-- STATUS_START -->\n{status_line}\n<!-- STATUS_END -->"
    content = re.sub(
        r"<!-- STATUS_START -->.*?<!-- STATUS_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)

    day_num = int(sys.argv[1])
    approach = sys.argv[2]
    time_complexity = sys.argv[3]
    space_complexity = sys.argv[4]
    today = datetime.date.today()

    with open(SCHEDULE_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    idx = next((i for i, r in enumerate(rows) if int(r["day_number"]) == day_num), None)
    if idx is None:
        print(f"Day {day_num} not found in SCHEDULE.csv")
        sys.exit(1)

    completed_row = rows[idx]
    problem_name = completed_row["problem_name"]
    difficulty = completed_row["difficulty"]

    # Reschedule: this day = actual completion date, every day after = the next consecutive day
    rows[idx]["date"] = today.isoformat()
    cur = today
    for r in rows[idx + 1:]:
        cur = next_day(cur)
        r["date"] = cur.isoformat()

    with open(SCHEDULE_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    # Append to PROGRESS.md, right before the row-template comment block
    with open(PROGRESS_PATH, encoding="utf-8") as f:
        content = f.read()

    slug = slugify(problem_name)
    solution_rel_path = f"solutions/day-{day_num:03d}-{slug}.java"
    solution_full_path = os.path.join(ROOT, solution_rel_path)
    if not os.path.exists(solution_full_path):
        print(f"WARNING: expected solution file not found at {solution_rel_path} "
              f"(logging anyway, but add the file).")

    time_space = f"{time_complexity} / {space_complexity}"
    link_md = f"[{os.path.basename(solution_rel_path)}]({solution_rel_path})"
    new_row = (
        f"| {day_num} | {today.isoformat()} | {problem_name} | {difficulty} | "
        f"{approach} | {time_space} | {link_md} |"
    )

    marker = "<!-- COMPLETE_DAY_INSERT_MARKER -->"
    if marker not in content:
        print("ERROR: PROGRESS.md is missing the COMPLETE_DAY_INSERT_MARKER line. Not modifying it.")
        sys.exit(1)
    content = content.replace(marker, new_row + "\n" + marker, 1)

    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    current_streak, longest_streak = compute_streaks(content)
    update_streak_in_readme(current_streak, longest_streak)
    update_progress_bar_in_readme(day_num, len(rows))

    # Report tomorrow's task
    next_row = rows[idx + 1] if idx + 1 < len(rows) else None
    update_status_in_readme(day_num, today.isoformat(), next_row)
    print(f"Day {day_num} logged for {today.isoformat()}: {problem_name} ({difficulty})")
    print(f"Streak -> current: {current_streak} day(s), longest: {longest_streak} day(s)")
    if next_row:
        print(f"Next up -> Day {next_row['day_number']} ({next_row['date']}): {next_row['problem_name']}")
    else:
        print("That was the final scheduled day. Challenge complete.")


if __name__ == "__main__":
    main()
