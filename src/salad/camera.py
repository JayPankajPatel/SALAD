"""

Camera Functions.

This class will allow you to interface with
the Raspberry pi library and opencv
"""
from typing import Union

import cv2
import numpy as np


def from_cv2_take_picture(
    index: int,
    cv_picture_flags: int,
) -> Union[None, np.ndarray]:
    """
    Take a picture using cv2 and save it to a file.

    :param index: index of camera connected to USB or built-in
    :type index: int
    :param cv_picture_flags: Flags to specify how the image should be read.
    :type cv_picture_flags: int
    :return: The captured image as a NumPy array, or None if capture failed.
    :rtype: Union[None, np.ndarray]
    """
    # Capture image using cv2
    capture = cv2.VideoCapture(index)
    ret, frame = capture.read()
    capture.release()

    if ret:
        # if frame was captured without error
        return frame

    return None


# def from_pi_cam_take_picture() -> Union[None, np.ndarray]:
# TODO Implement picture taking from pi
#    return


def write_picture_file(
    dir_name: str,
    file_name: str,
    picture_in: np.ndarray,
) -> None:
    """
    Write a picture to a directory.

    :param dir_name: This is where you save your picture in.
    :type dir_name: str
    :param file_name: Save with name and file extenstion ex. *.png
    :type file_name: str
    :param picture_in: Picture that was taken.
    :type picture_in: np.ndarray
    :return None
    :rtype None
    """
    fmt = dir_name + file_name
    cv2.imwrite(fmt, picture_in)


if __name__ == "__main__":
    image = from_cv2_take_picture(0, 1)
    write_picture_file("../pictures", "ran_from_camera_py.png", image)
