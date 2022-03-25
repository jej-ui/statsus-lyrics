import requests
import json
from time import sleep

# lyrics
with open('lyrics.txt', 'r') as f:
    all_lines = f.readlines()

token = "your token here"

while True:
    for i in range(len(all_lines)):
        #loop through lyrics.txt
        content = {
            "custom_status": {"emoji": ":bigassforehead:", "text": all_lines[i]}
        }

        requests.patch("https://ptb.discordapp.com/api/v8/users/@me/settings", headers={"authorization": token}, json=content)
        #good rule of thumb is to delay for 4-5 seconds or more, to avoid insta ban
        sleep(5)
