import os
import time
from datetime import datetime

# Get the current date and time
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")

# Create a new file with the current timestamp
with open(f"{timestamp}.txt", "w") as file:
    file.write(f"File created at {now}")

# Add the new file to the repository
os.system(f"git add {timestamp}.txt")

# Commit the changes
os.system(f'git commit -m "Added file at {now}"')

# Push the changes to the repository
os.system("git push origin main")