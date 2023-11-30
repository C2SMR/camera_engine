import requests


class Api:

    def __init__(self, key: str, city: str):
        self.url_api: str = ''
        self.api_key: str = key
        self.city: str = city
        self.name_extension: str = '-not-trained'
        self.name_extension_2_count: int = 0
        self.extension: str = 'png'

    def send_picture(self):
        try:
            requests.post(self.url_api + "/add_picture_alert_or_moment", json={
                "key": self.api_key,
            }, files={
                'file': open(f'{self.city}{self.name_extension}.'
                             f'{self.extension}', 'rb')
            })
            requests.post(self.url_api + "/add_picture_alert_or_moment", json={
                "key": self.api_key,
            }, files={
                'file': open(f'{self.city}{self.name_extension_2_count}.'
                             f'{self.extension}', 'rb')
            })
            self.name_extension_2_count += 1
        except Exception:
            pass
