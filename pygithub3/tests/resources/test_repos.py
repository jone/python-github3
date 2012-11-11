#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase

from pygithub3.resources.repos import Status


class TestStatus(TestCase):

    def test_is_valid_state(self):
        valid_states = ['pending', 'success', 'error', 'failure']
        for state in valid_states:
            self.assertTrue(Status.is_valid_state(state),
                            'The state "%s" should be valid' % state)

        invalid_states = ['foo', 1, None, 'Success']
        for state in invalid_states:
            self.assertFalse(Status.is_valid_state(state),
                             'The state "%s" should not be valid' % state)
