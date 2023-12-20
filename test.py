import os
import time
from datetime import datetime

# Specify the folder
folder = "files"

# Create the folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

for i in range(5000):
    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Create a new file with the current timestamp
    with open(f"{folder}/{timestamp}.txt", "w") as file:
        file.write(f"File created at {now}")

    # Add the new file to the repository
    os.system(f"git add {timestamp}.txt")

    # Commit the changes
    os.system(f'git commit -m "Added file at {now}"')

    # # Push the changes to the repository
    # os.system("git push origin main")

    print(f"Added file at {now}")
