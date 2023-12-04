import subprocess


class Camera:
    def __init__(self, city: str):
        self.city: str = city
        self.name_extension: str = '-not-trained'
        self.extension: str = 'png'

    def take_picture(self):
        subprocess.call(['sudo', 'libcamera-jpeg', '-o',
                         f'{self.city}{self.name_extension}.{self.extension}'])
