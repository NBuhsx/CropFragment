import cv2
import enum


class Cropped(enum.Enum):
    NOTHING = 0
    CUT = 10
    CUTOUT = 100


class Rectangle:
    def __init__(self):
        self.x_start, self.y_start = 0, 0
        self.x_end, self.y_end = 0, 0

    def start(self, x: int, y: int):
        self.x_start, self.y_start = x, y

    def end(self, x: int, y: int):
        self.x_end, self.y_end = x, y

    def check_x(self):
        if self.x_start > self.x_end:
            return (self.x_end, self.x_start)
        else:
            return self.x_start, self.x_end

    def check_y(self):
        if self.y_start > self.y_end:
            return (self.y_end, self.y_start)
        else:
            return self.y_start, self.y_end

    def draw(self, img):
        cv2.rectangle(img, (self.x_start, self.y_start),
                      (self.x_end, self.y_end), (255, 0, 0), 2)

    def build(self, img):
        index_x = self.check_x()
        index_y = self.check_y()
        cv2.imshow("CroppFragment", img[
            index_y[0]:index_y[1],
            index_x[0]:index_x[1]
        ])


class App:
    def __init__(self):
        self.selection = Rectangle()
        self.__flag = Cropped
        self.__croping = self.__flag.NOTHING

        self.image = cv2.imread('test.jpeg')
        self.oriImage = self.image.copy()

    def cut(self, event):
        return event == cv2.EVENT_MOUSEMOVE and \
            self.__croping.value == 10

    def build_img(self, x: int, y: int):
        self.selection.end(x, y)
        self.__croping = self.__flag.NOTHING
        self.selection.build(self.oriImage)

    def mouse_crop(self, event: int, x: int, y: int, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.selection.start(x, y)
            self.selection.end(x, y)
            self.__croping = self.__flag.CUT
        elif self.cut(event):
            self.selection.end(x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.build_img(x, y)
            self.__croping = self.__flag.NOTHING
            self.cycle()

    def cycle(self):
        while True:
            if self.__croping.value == 10:
                img = self.image.copy()
                self.selection.draw(img)
                cv2.imshow("image", img)
            cv2.waitKey(1)

    def run(self):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.mouse_crop)
        cv2.imshow("image", self.image)
        self.cycle()
        cv2.destroyAllWindows()
