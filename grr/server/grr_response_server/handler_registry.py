#!/usr/bin/env python
"""A registry of all new style well known flows."""

from grr.server.grr_response_server.flows.general import administrative
from grr.server.grr_response_server.flows.general import ca_enroller

message_handlers = [
    ca_enroller.EnrolmentHandler,
    administrative.ClientStatsHandler,
]

handler_name_map = {
    handler.handler_name: handler for handler in message_handlers
}
