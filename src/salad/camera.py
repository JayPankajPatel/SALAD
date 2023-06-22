"""
Camera Classes.

Different camera implementations exist in our system
However, we want to treat them the same.
This class implements an abstract Camera class
where Camera implementations inherit them and then
wrap them inside a easy to use interface for the user.
"""
import time
from abc import ABC, abstractmethod

import cv2
import numpy as np


class AbstractCamera(ABC):
    """

    Abstract Camera class.

    For USB cameras and CSI cameras
    """

    @abstractmethod
    def take_picture(self) -> np.ndarray:
        """
        Abstract Method for taking a picture.

        raises: NotImplementedError: Must be implemented.

        return: A numpy array

        rtype np.ndarray
        """
        raise NotImplementedError("take_picture method must be implemented.")

    def show_image(self, window_name: str, image: np.ndarray) -> None:
        """
        Open a window with `window_name` and show image.

        Destroy window by pressing any key.

        :param arg1: Name of opened window.

        :type arg1: str

        :param arg2: Image to show.

        :type arg2: np.ndarray

        :return None

        :rtype None
        """
        cv2.imshow(window_name, image)
        cv2.waitKey(1)  # This means any key press.
        cv2.destoryAllWindows()

    def save_to_file(
        self,
        image: np.ndarray,
        destination: str,
        image_name: str,
    ) -> None:
        """
        Write picture to a file destination.

        :param arg1: Image data as a numpy array.

        :type arg1: np.ndarray

        :param arg2: File save destination.

        :type arg2: str

        :param arg3: Image name with extension i.e. `*.png`, `*.jpg`

        :type arg3: str

        :return: None

        :rtype None
        """
        cv2.imwrite(f"{destination}/{image_name}", image)

    def take_and_save(self, destination: str, image_name: str) -> None:
        """
        Take a picture and write picture to a file destination.

        :param arg1: File save destination.

        :type arg1: str

        :param arg2: Image name with extension i.e. `*.png`, `*.jpg`

        :type arg2: str

        :return: None

        :rtype: None
        """
        image = self.take_picture()
        self.save_to_file(image, destination, image_name)


class USBCamera(AbstractCamera):
    """

    USB Camera camera class.

    Allows interfacing with cameras on the USB bus.
    """

    def __init__(self, index: int) -> None:
        """
        Get the USB camera's index from the user.

        :param arg1: Camera index.

        :type arg1: int

        :return None

        :rtype None

        :raises RuntimeError: If an error occurs while capturing the image.
        """
        self._index = index

    def take_picture(self) -> np.ndarray:
        """
        Define take_picture to USB camera implementation.

        :return A numpy array

        :rtype np.ndarray
        """
        camera = cv2.VideoCapture(self._index)
        time.sleep(1)
        ret, image = camera.read()
        if not ret:
            raise RuntimeError("Failed to capture image.")

        return image


if __name__ == "__main__":
    webcam = USBCamera(0)
    webcam.take_and_save("../pictures/", "test.jpg")
