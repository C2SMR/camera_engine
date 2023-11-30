import picamera
import time


class Camera:
    def __init__(self, city: str):
        self.__camera = picamera.PiCamera()
        time.sleep(2)
        self.city: str = city
        self.name_extension: str = '-not-trained'
        self.extension: str = 'png'

    def take_picture(self):
        self.__camera.capture(f'{self.city}{self.name_extension}.'
                              f'{self.extension}')
