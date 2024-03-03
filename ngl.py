import uuid
import cloudscraper


class NGLWrapper:
    def __init__(self):
        self.s = cloudscraper.create_scraper()
        self.submit_url = "https://ngl.link/api/submit"
        self.username = None
        self.counter = 0

    def set_username(self, username):
        self.username = username
    def send_question(self, question):
        device_id = str(uuid.uuid4())
        data = {
            "username": self.username,
            "question": question,
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        r = self.s.post(self.submit_url, data=data)
        if r.status_code == 200:
            self.counter += 1
            return True
        else:
            return False
