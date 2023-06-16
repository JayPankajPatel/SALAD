"""
Schedule jobs at specified times or intervals.

TODO Create a configuration file for this module.
"""
import time
from datetime import datetime

from relay import BoardStack, Relay
from rocketry import Rocketry
from rocketry.conds import every

relays = {
    "light": Relay(0, 1),
    "atomizer": Relay(0, 2),
    "atomizer-fans": Relay(0, 3),
    "tec-fans": Relay(0, 4),
}

stack_one = BoardStack(0, relays)

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

relays = {
    "light": Relay(0, 1),
    "atomizer": Relay(0, 2),
    "atomizer-fans": Relay(0, 3),
    "tec-fans": Relay(0, 4),
}

stack_one = BoardStack(0, relays)


# The seconds in this case alone is how often the system is going
# to try to poll this task to turn it on or off
@app.task(every("1 seconds"), execution="thread")
def toggle_atomizer_sys() -> None:
    stack_one.relays["atomizer"].set_state(1)
    stack_one.relays["atomizer-fans"].set_state(1)
    print("atomizer ON", datetime.now())

    # TODO not hard code these values
    time.sleep(30)
    stack_one.relays["atomizer"].set_state(0)
    stack_one.relays["atomizer-fans"].set_state(0)
    print("atomizer OFF", datetime.now())
    time.sleep(180)


@app.task("time of day between 06:00 and 21:59", execution="thread")
def light_on() -> None:
    print("Light ON", datetime.now())
    stack_one.relays["light"].set_state(1)


@app.task("time of day between 22:00 and 05:59", execution="thread")
def light_off() -> None:
    print("Light OFF", datetime.now())
    stack_one.relays["light"].set_state(0)


if __name__ == "__main__":
    print("Test")
    app.run()
