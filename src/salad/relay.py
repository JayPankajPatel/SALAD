"""
BoardStack and Relay Classes.

This module focuses on creating easy to use wrappers.
The BoardStack and their Relays can be easily mapped,
and validated.
"""

import lib8relind


class Relay:
    """

    Relay Module.

    This module will control lights, atomizer fans, and tec fans and will
    be passed into the scheduler to be executed based on some configuration.
    """

    def __init__(self, stack_number: int, relay_number: int) -> None:
        """
        Constructor for assigning relays and which board they belong to.

        :param stack_number: Board number reference range is (0-7)
        :param relay_number: Relay number reference range is (1-8)
        :raises ValueError: If values are out of valid range
        """
        if 0 <= stack_number <= 7:
            self.stack_number = stack_number
        if 1 <= relay_number <= 8:
            self.relay_number = relay_number
        else:
            raise ValueError(
                "Invalid relay or stack reference. "
                "Relay numbers range from 1 to 8, "
                "and stack numbers range from 0 to 7."
            )

    def set_state(self, state: int) -> None:
        """
        Set state of the relay.

        This can be 1 (ON) or 0 (OFF).

        :param state: Set `self.relay_number` on `self.stack_number` to `state`
        """
        lib8relind.set(self.stack_number, self.relay_number, state)

    def get_state(self) -> int:
        """
        Get state of the relay.

        This can be 1 (ON) or 0 (OFF).

        :return: Current state of the relay
        """
        return lib8relind.get(self.stack_number, self.relay_number)

    def toggle(self) -> None:
        """
        Flip the state of a relay.

        This will first get the state of a relay and then flip the value.
        Ex. 1 -> 0 or 0 -> 1
        """
        value = self.get_state()
        flipped_value = 1 - value
        self.set_state(flipped_value)


class BoardStack:
    """

    Stackable Relay Board class.

    This represents a stackable relay board made by Sequent Microsystems,
    which has 8 relay modules onboard.
    There is a maximum of 8 boards that can be used at one time.
    Click here to go to the product site: https://sequentmicrosystems.com/collections/industrial-automation/products/8-relays-stackable-card-for-raspberry-pi
    """

    def __init__(self, stack_number: int, relays: dict[str, Relay]) -> None:
        """
        Constructor for assigning stack number and relays to the board.

        :param stack_number: Board number reference range is (0-7)
        :param relays: Dictionary mapping relay names to their numbers
        :raises ValueError: If stack number is out of valid range
        """
        if 0 <= stack_number <= 7:
            self.stack_number = stack_number
            self.relays = relays
        else:
            raise ValueError(
                "Invalid stack reference. Stack numbers range from 0 to 7."
            )

    def set_all_on(self) -> None:
        """Set all relays on."""
        lib8relind.set_all(self.stack_number, 0b1111_1111)

    def set_all_off(self) -> None:
        """Set all relays off."""
        lib8relind.set_all(self.stack_number, 0b0000_0000)

    def set_all(self, bitfield: int) -> None:
        """
        Set the state of all relays using a bitfield.

        :param bitfield: Bitfield representing the state of each relay
        """
        lib8relind.set_all(self.stack_number, bitfield)

    def get_all(self) -> int:
        """Get the state of all relays of `stack_number`."""
        return lib8relind.get_all(lib8relind.get_all(self.stack_number))
