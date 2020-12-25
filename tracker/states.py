states = ["Buried", "Paused", "In progress", "Shipping soon", "Shipped"]


class State:
    def __init__(self, state_id):
        if state_id < 0 or state_id > 4:
            raise ValueError("invalid state id")

        self.id = state_id

    def __str__(self):
        return states[self.id]
