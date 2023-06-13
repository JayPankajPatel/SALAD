"""

Relay Module.

This module will control:
Lights, Atomizer Fans, and Tec Fans and will
be passed into the scheduler. To be executed,
by some configuration.
"""

import lib8relind


class Relay:
    def __init__(self, stack_number: int, relay_number: int) -> None:
        if 1 <= relay_number <= 8:
            self.relay_number = relay_number
        if 0 <= relay_number <= 7:
            self.stack_number = stack_number
        else:
            raise ValueError(
                "Invalid relay reference or Invalid stack reference, they are numbered from 0 to 7 inclusive and Relays are numbered 1 to 8 inclusive."
            )

    def set_state(self, state: int) -> None:
        lib8relind.set(self.stack_number, self.relay_number, state)

    def get_state(self) -> int:
        return lib8relind.get(self.stack_number, self.relay_number)

    def toggle(self) -> None:
        value = self.get_state()
        flipped_value = 1 - value
        self.set_state(flipped_value)


class BoardStack:
    """

    Stackable Relay Board class

    This represents a stackable relay board made by Sequent Microsystems which has 8 relay modules onboard
    There is a max of 8 boards that can be used at one time.
    `Click here to go to the product site` <https://sequentmicrosystems.com/collections/industrial-automation/products/8-relays-stackable-card-for-raspberry-pi>

    """

    def __init__(self, stack_number: int, relays: list[Relay]) -> None:
        if 0 <= stack_number <= 7:
            self.stack_number = stack_number
            self.relays = relays
        else:
            raise ValueError(
                "Invalid stack reference, they are numbered from 0 to 7 inclusive."
            )

    def set_all_on(self) -> None:
        lib8relind.set_all(self.stack_number, 0b1111_1111)

    def set_all_off(self) -> None:
        lib8relind.set_all(self.stack_number, 0b0000_0000)

    def set_all(self, bitfield: int) -> None:
        lib8relind.set_all(self.stack_number, bitfield)
