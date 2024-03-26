import requests
import threading
import time

success = 0
failed = 0

headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def start(name):
    status = requests.get(f"https://solo.to/{name}", headers=headers)
    if not status.status_code == 404:
        try:
            def send_request():
                global success, failed
                r = requests.get(f"https://solo.to/{name}", headers=headers)
                if r.status_code == 200:
                    success += 1
                else:
                    failed += 1
                print(f"\rsuccess: {success} failed: {failed}", end="")

            while True:
                threading.Thread(target=send_request).start()
                time.sleep(0.05)
        except KeyboardInterrupt as e:
            pass
    else:
        input("ユーザーが見つかりませんでした。")