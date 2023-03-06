from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamic(self):
        pass

class HPLaptop(Laptop):
    def screen(self):
        print("HP laptop showing picture")
    def keyboard(self):
        print("HP laptop typing text")
    def touchpad(self):
        print("HP laptop moving cursor")
    def webcam(self):
        print("HP laptop recording video")
    def ports(self):
        print("HP laptop using ports")
    def dynamic(self):
        print("HP laptop playing music")

hp = HPLaptop()
hp.screen()
hp.keyboard()
hp.touchpad()
hp.webcam()
hp.ports()
hp.dynamic()