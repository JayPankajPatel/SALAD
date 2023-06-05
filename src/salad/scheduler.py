"""
Schedule jobs at specified times or intervals.

TODO Create a configuration file for this module.
"""
import time
from datetime import datetime

import schedule
from camera import USBCamera
from file_io import create_directory_in_script_location

PICTURE_DIR_NAME = "pictures"


def timelaspe() -> None:
    """
    Take pictures with intent of making a timelaspe.

    :return None
    :rtype None
    """
    camera_obj = USBCamera(0)

    create_directory_in_script_location(PICTURE_DIR_NAME)
    current_datetime = datetime.now().strftime("%d-%m-%y-%H:%M:%S")
    image_file_name = f"{current_datetime}.jpg"
    print(f"Taking picture called: {image_file_name}")
    camera_obj.take_and_save("../pictures", image_file_name)


if __name__ == "__main__":
    PICTURE_INTERVAL = 20
    schedule.every(PICTURE_INTERVAL).seconds.do(timelaspe)

    while True:
        schedule.run_pending()
        time.sleep(1)
