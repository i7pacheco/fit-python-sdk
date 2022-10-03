'''accumulator.py: Contains the Accumulator class and sub-component class AccumulatedField'''

###########################################################################################
# Copyright 2022 Garmin International, Inc.
# Licensed under the Flexible and Interoperable Data Transfer (FIT) Protocol License; you
# may not use this file except in compliance with the Flexible and Interoperable Data
# Transfer (FIT) Protocol License.
###########################################################################################
# ****WARNING****  This file is auto-generated!  Do NOT edit this file.
# Profile Version = 21.94Release
# Tag = production/akw/21.94.00-0-g0f668193
############################################################################################


class AccumulatedField:
    '''A class that accumulates a value for a particular field.
        Attributes:
            _accumulated_value: Resulting accumulated value
            _last_value: The previous accumulated value thus far.
    '''
    def __init__(self, value = 0):
        self._accumulated_value = value
        self._last_value = value

    def accumulate(self, value, bits):
        ''''Accumulates to the previous value and gives the updated accumulated value.'''
        mask = (1 << bits) - 1

        self._accumulated_value += (value - self._last_value) & mask
        self._last_value = value

        return self._accumulated_value

class Accumulator:
    '''A class that represents the accumulated values for particular fields.
        Attributes:
            _messages: A list of messages with a field or fields to accumulate.
    '''
    def __init__(self):
        self._messages = {}

    def add(self, mesg_num, field_num, value):
        '''Adds a message and field which will be accumulated.'''
        if mesg_num not in self._messages:
            self._messages[mesg_num] = {}

        self._messages[mesg_num][field_num] = AccumulatedField(value)

    def accumulate(self, mesg_num, field_num, value, bits):
        '''Accumulates the given field value if present in the accumulator.'''
        if mesg_num in self._messages and field_num in self._messages[mesg_num]:
            return self._messages[mesg_num][field_num].accumulate(value, bits)
        else:
            return value

