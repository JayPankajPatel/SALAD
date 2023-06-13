"""
Schedule jobs at specified times or intervals.

TODO Create a configuration file for this module.
"""
import time
from datetime import datetime

from rocketry import Rocketry
from rocketry.conds import every

# PICTURE_DIR_NAME = "pictures"


# def timelaspe() -> None:
#     """
#     Take pictures with intent of making a timelaspe.
#
#     :return None
#     :rtype None
#     """
#     camera_obj = USBCamera(0)
#
#     create_directory_in_script_location(PICTURE_DIR_NAME)
#     current_datetime = datetime.now().strftime("%d-%m-%y-%H:%M:%S")
#     image_file_name = f"{current_datetime}.jpg"
#     print(f"Taking picture called: {image_file_name}")
#     camera_obj.take_and_save("../pictures", image_file_name)
#
app = Rocketry()


@app.task(every("1 seconds"), execution="thread")
def toggle_job1() -> None:
    print("Hello from job 1", datetime.now())
    time.sleep(4)
    print("Toggle from job 1", datetime.now())
    time.sleep(6)


@app.task(every("3 seconds"), execution="thread")
def job2() -> None:
    print("Hello from job 2", datetime.now())
    time.sleep(5)


if __name__ == "__main__":
    print("Test")
    app.run()
