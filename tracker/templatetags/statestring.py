from django import template
from tracker.states import State

register = template.Library()


def statestring(state_id):
    return str(State(state_id))


register.filter("statestring", statestring)
