

from datetime import datetime
import os

def create_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    folder = "journal"
    os.makedirs(folder, exist_ok=True)
    
    filename = os.path.join(folder, f"{today}.md")
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f"# Journal Entry - {today}\n\n")
            f.write("What I learned today:\n- \n")
        print(f"Created new journal entry: {filename}")
    else:
        print(f"Journal entry already exists: {filename}")

if __name__ == "__main__":
    create_journal()

name: Daily Journal

on:
  schedule:
    - cron: '0 7 * * *'   # Runs every day at 07:00 UTC (09:00 Germany time)
  workflow_dispatch:       # Allows manual trigger

jobs:
  update-journal:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Run journal script
        run: python journal.py

      

    
