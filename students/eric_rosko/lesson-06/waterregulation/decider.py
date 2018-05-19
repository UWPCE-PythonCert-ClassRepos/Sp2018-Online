#!/usr/bin/env python3
"""
Encapsulates decision making in the water-regulation module
"""


class Decider(object):
    """
    Encapsulates decision making in the water-regulation module
    """

    def __init__(self, target_height, margin):
        """
        Create a new decider instance for this tank.

        :param target_height: the target height for liquid in this tank
        :param margin: the margin of liquid above and below
        the target height for
       which the pump should not turn on.
        Ex: .05 represents a
       5% margin above and below the target_height.
        """
        self.target_height = target_height
        self.margin = margin

    def decide(self, current_height, current_action, actions):
        """
        change the state of the pump
        """
        next_action = current_action

        if actions['PUMP_OFF'] == current_action and \
                current_height < (self.target_height - self.margin):
                next_action = actions['PUMP_IN']
        elif actions['PUMP_OFF'] == current_action and \
                current_height > (self.target_height + self.margin):
                next_action = actions['PUMP_OUT']
        elif actions['PUMP_OFF'] == current_action and \
                current_height <= (self.target_height + self.margin) and \
                current_height >= (self.target_height - self.margin):
                next_action = actions['PUMP_OFF']
        elif actions['PUMP_IN'] == current_action and \
                current_height > self.target_height:
                next_action = actions['PUMP_OFF']
        elif actions['PUMP_OUT'] == current_action and \
                current_height < self.target_height:
                next_action = actions['PUMP_OFF']

        return next_action
