#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request

from pygithub3.requests.base import ValidationError
from pygithub3.resources.repos import Status


class List(Request):

    uri = 'repos/{user}/{repo}/statuses/{sha}'
    resource = Status


class Create(Request):

    uri = '/repos/{user}/{repo}/statuses/{sha}'
    resource = Status
    body_schema = {
        'schema': ('state', 'target_url', 'description'),
        'required': ('state',)}

    def clean_body(self):
        state = self.body.get('state', '')
        if not Status.is_valid_state(state):
            raise ValidationError('The state must be one of "%s", not "%s"' % (
                    '", "'.join(Status.VALID_STATES),
                    state))
        else:
            return self.body
