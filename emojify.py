import requests
import sys

if len(sys.argv) < 2:
    print("[X] - Missing argument\n[+] - Usage: python emojify.py emoji_name")
    quit()

api_key = ""

keyword = f":{sys.argv[1]}:"


try:
    with open("emojify.conf", "r") as f:
        api_key = f.readline().replace("\n", "")

except:
    print("[X] - Can't open config file")
    quit()


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


emoji = {
    "alias": keyword
}


req = requests.post("https://api.m3o.com/v1/emoji/Find", headers=headers, json=emoji)


if req.status_code == 401:
    print("[X] - It seems that your API key is invalid")
    quit()


try:
    print(req.json()['emoji'])

except:
    print("[X] - Error invalid emoji name")
