"""
Daily Contribution Script
Appends a meaningful daily entry (with a random motivational quote)
to contributions/daily_log.md — keeping the GitHub streak alive!
"""

import random
from datetime import datetime, timezone, timedelta

# ── Quotes bank ──────────────────────────────────────────────────────────────
QUOTES = [
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    ("In order to be irreplaceable, one must always be different.", "Coco Chanel"),
    ("Java is to JavaScript what car is to carpet.", "Chris Heilmann"),
    ("Knowledge is power.", "Francis Bacon"),
    ("Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.", "Dan Salomon"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Before software can be reusable it first has to be usable.", "Ralph Johnson"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
    ("Debugging is twice as hard as writing the code in the first place.", "Brian W. Kernighan"),
    ("It's not a bug – it's an undocumented feature.", "Anonymous"),
    ("The best error message is the one that never shows up.", "Thomas Fuchs"),
    ("Real programmers count from 0.", "Anonymous"),
    ("Every great developer you know got there by solving problems they were unqualified to solve until they did it.", "Patrick McKenzie"),
    ("Clean code always looks like it was written by someone who cares.", "Robert C. Martin"),
]

# ── IST timezone ─────────────────────────────────────────────────────────────
IST = timezone(timedelta(hours=5, minutes=30))
now = datetime.now(IST)
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S IST")
day_str  = now.strftime("%A")          # e.g. Monday

quote_text, quote_author = random.choice(QUOTES)

# ── Build new log entry ───────────────────────────────────────────────────────
entry = f"""
---

### 📅 {date_str} — {day_str}

**🕐 Time:** {time_str}

**💬 Quote of the day:**
> "{quote_text}"
> — *{quote_author}*

**✅ Status:** Daily contribution logged successfully.
"""

# ── Append to the log file ────────────────────────────────────────────────────
LOG_PATH = "contributions/daily_log.md"

with open(LOG_PATH, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"[✓] Entry added for {date_str} — "{quote_text[:40]}..."")
