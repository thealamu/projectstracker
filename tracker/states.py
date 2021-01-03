states = ["Buried", "Paused", "In progress", "Shipping soon", "Shipped"]


def id_for_string(state_str):
    try:
        return states.index(state_str.capitalize())
    except ValueError:
        return 0


class State:
    def __init__(self, state_id):
        if state_id < 0 or state_id > 4:
            raise ValueError("invalid state id")

        self.id = state_id

    def __str__(self):
        return states[self.id]
