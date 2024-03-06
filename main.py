from bs4 import BeautifulSoup
import requests, json, random, threading, time

devices = ["desktop", "mobile", "tablet", "other"]
referrals = ["youtube.com", "discord.com", "twitter.com", "instagram.com", "facebook.com", "github.com", "note.com", "gmail.com", "telegram.org", "とっきーﾅﾏｽﾃ", "kap210"]
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ja,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "referrer": "https://lit.link/",
}

name = input('名前を入力してください: https://lit.link/')

document = requests.get(f"https://lit.link/{name}", headers={"content-type": "application/json"})
soup = BeautifulSoup(document.text, 'lxml')
userJson = json.loads(soup.find(id="__NEXT_DATA__").text)

def alive():
    if userJson["props"]["pageProps"]["metadata"]["description"] == "undefined":
        return False
    else:
        return True

if alive():
    try:
        linkList = []
        for link in userJson['props']['pageProps']['profile']['profileLinks']:
            linkList.append({
                "link_id": link['id'],
                "profile_image_id": None,
                "link_type": link['profileLinkType'],
                "link_title": link['buttonLink']['title'],
                "link_url": link['buttonLink']['url'],
            })

        success = 0
        failed = 0

        def send_request():
            global success, failed
            body = {
                "user_id": userJson['props']['pageProps']['profile']['userId'],
                "creator_id": userJson['props']['pageProps']['profile']['creatorId'],
                "device": random.choice(devices),
                "referral": random.choice(referrals),
                "links": linkList,
                "url_path": name
            }

            r = requests.post("https://prd.api.lit.link/v1/access_logs/view_type_access_logs", json=body, headers=headers)
            if r.status_code == 200:
                success += 1
            else:
                failed += 1
            print(f"\rsuccess: {success} failed: {failed}", end="")

        while True:
            thread = threading.Thread(target=send_request)
            thread.start()
            time.sleep(0.05)
    except KeyboardInterrupt as e:
            pass
else: input("ユーザーが見つかりませんでした。")
