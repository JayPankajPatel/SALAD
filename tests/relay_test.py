from salad.relay import BoardStack, Relay


def test_relay_get_and_set_state() -> None:
    relay = Relay(0, 1)

    relay.set_state(1)

    assert relay.get_state() == 1


def test_board_stack_set_all_on() -> None:
    relays = {"mock1": Relay(0, 1), "mock2": Relay(0, 2), "mock3": Relay(0, 3)}
    stack = BoardStack(0, relays)
    stack.set_all_on()
    assert stack.get_all() == 255


def test_board_stack_set_all_off() -> None:
    relays = {"mock1": Relay(0, 1), "mock2": Relay(0, 2), "mock3": Relay(0, 3)}
    stack = BoardStack(0, relays)
    stack.set_all_off()
    assert stack.get_all() == 0


def test_board_relay_indiviual_on() -> None:
    relays = {"mock1": Relay(0, 1), "mock2": Relay(0, 2), "mock3": Relay(0, 3)}
    stack = BoardStack(0, relays)
    stack.relays["mock1"].set_state(1)
    assert stack.relays["mock1"].get_state() == 1


def test_board_relay_indiviual_off() -> None:
    relays = {"mock1": Relay(0, 1), "mock2": Relay(0, 2), "mock3": Relay(0, 3)}
    stack = BoardStack(0, relays)
    stack.relays["mock1"].set_state(0)
    assert stack.relays["mock1"].get_state() == 0
