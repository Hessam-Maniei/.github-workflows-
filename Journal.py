from datetime import datetime
import os

def create_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    folder = "journal.py"
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
