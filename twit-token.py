import os
import time
import subprocess
from datetime import datetime

def git_push():
    os.chdir("./screenshots/") #this should be the directory that the screenshots are saved to, and the repo itself. name accordingly or change to suit.
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "--all"])
    subprocess.run(["git", "commit", "-m", "twitter-post"]) #change to whatever commit name you want

    # Git push with username and password input
    git_process = subprocess.Popen(["git", "push"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = git_process.communicate(input=b"<GITHUB_USER_NAME>\<GITHUB_PERSONAL_KEY>\n") #make sure you add your github credentials here
    print(stdout.decode(), stderr.decode())

    os.chdir("..")

def main(screenshotPath):  # Accept screenshotPath as an argument, again make sure its correct and suits youruse case
    folder_path = "./screenshots/"

    while True:
           git_push()

        # Get the next file to be used as screenshot.png and overwrite the existing
        os.system('node "grab.js"')
        git_push()

        # Wait for 4 hours
        time.sleep(14400)

if __name__ == "__main__":
    screenshotPath = "./screenshots/screenshot.png"  # Define screenshotPath
    main(screenshotPath)  # Pass screenshotPath to main function
