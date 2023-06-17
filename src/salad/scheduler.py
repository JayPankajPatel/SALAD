"""
Schedule jobs at specified times or intervals.

TODO Create a configuration file for this module.
"""
import time
from datetime import datetime

from rocketry import Rocketry
from rocketry.conds import every

from salad import camera
from salad import relay

relays = {
    "light": relay.Relay(0, 1),
    "atomizer": relay.Relay(0, 2),
    "atomizer-fans": relay.Relay(0, 3),
    "tec-fans": relay.Relay(0, 4),
}

stack_one = relay.BoardStack(0, relays)
webcam = camera.USBCamera(0)

app = Rocketry()

relays = {
    "light": relay.Relay(0, 1),
    "atomizer": relay.Relay(0, 2),
    "atomizer-fans": relay.Relay(0, 3),
    "tec-fans": relay.Relay(0, 4),
}

stack_one = relay.BoardStack(0, relays)


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
def light_on_take_picture() -> None:
    print("Light ON", datetime.now())
    stack_one.relays["light"].set_state(1)
    image_name = f"{datetime.now()}.jpg"
    webcam.take_and_save("../pictures/", image_name)
    time.sleep(3)


@app.task("time of day between 22:00 and 5:59", execution="thread")
def light_off() -> None:
    print("Light OFF", datetime.now())
    stack_one.relays["light"].set_state(0)


if __name__ == "__main__":
    print("Test")
    stack_one.relays["light"].set_state(1)
    app.run()
