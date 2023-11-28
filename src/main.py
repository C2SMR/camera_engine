import sys
import time

from camera import Camera
from api import Api


class Main:
    def __init__(self):
        self.city: str = sys.argv[1]
        self.api_key: str = sys.argv[2]
        self.time_to_sleep: int = int(sys.argv[3])
        self.camera: Camera = Camera(self.city)
        self.api: Api = Api(self.api_key, self.city)
        self.run()

    def run(self):
        while True:
            self.camera.take_picture()
            self.api.send_picture()
            time.sleep(self.time_to_sleep)


if __name__ == '__main__':
    Main()
