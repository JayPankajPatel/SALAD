"""
Schedule jobs at specified times or intervals.

TODO Create a configuration file for this module.
"""
import time
from datetime import datetime

import schedule
from camera import USBCamera


def timelaspe() -> None:
    """
    Take pictures with intent of making a timelaspe.

    :return None
    :rtype None
    """
    camera_obj = USBCamera(0)
    file_name = f"{datetime.now}.jpg"
    print(f"Taking picture called: {file_name}")
    camera_obj.take_and_save("../pictures", file_name)


if __name__ == "__main__":
    PICTURE_INTERVAL = 20
    schedule.every(PICTURE_INTERVAL).seconds.do(timelaspe)

    while True:
        schedule.run_pending()
        time.sleep(1)
