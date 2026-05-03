# 🚀 Daily GitHub Contribution — Setup Instructions

These files will make a **meaningful commit every day at 9:00 AM IST** to keep
your GitHub contribution graph green automatically.

---

## 📁 Files to Copy Into Your Repository

```
your-repo/
├── .github/
│   └── workflows/
│       └── daily_contribution.yml   ← GitHub Actions workflow
├── scripts/
│   └── update_log.py               ← Python script that writes the daily entry
└── contributions/
    └── daily_log.md                ← The log file that gets a new entry each day
```

---

## ✅ Step-by-Step Setup

### Step 1 — Copy all three files/folders into your repo
Copy the `.github/`, `scripts/`, and `contributions/` folders into your
existing GitHub repository (keeping the same folder structure).

### Step 2 — Push to GitHub
```bash
git add .
git commit -m "Add daily contribution automation"
git push
```

### Step 3 — Verify the workflow is enabled
1. Go to your repo on GitHub.
2. Click the **Actions** tab.
3. You should see **"Daily Contribution"** listed.
4. If it shows a banner saying "Workflows aren't running", click **"I understand my workflows, go ahead and enable them"**.

### Step 4 — Test it manually (optional but recommended)
1. In the **Actions** tab, click **"Daily Contribution"**.
2. Click **"Run workflow"** → **"Run workflow"** (green button).
3. Wait ~30 seconds, then check your repo — a new commit should appear!

---

## ⏰ Schedule

The workflow runs every day at **3:30 AM UTC = 9:00 AM IST**.

To change the time, edit the `cron` line in `.github/workflows/daily_contribution.yml`:

```yaml
- cron: '30 3 * * *'   # 3:30 AM UTC = 9:00 AM IST
```

Use [crontab.guru](https://crontab.guru) to find the right cron expression for your timezone.

---

## 🔑 No Extra Secrets Needed

The workflow uses `secrets.GITHUB_TOKEN` which GitHub provides **automatically**
for every repository — no manual configuration required.

---

## 💬 What Each Commit Does

Every day the `update_log.py` script:
1. Picks a **random motivational quote** from a curated list of 20 developer quotes.
2. Appends a new dated entry to `contributions/daily_log.md`.
3. The workflow commits and pushes this change with the message:
   `🌱 Daily contribution - YYYY-MM-DD`

This counts as a **real commit** and shows up on your GitHub contribution graph!
