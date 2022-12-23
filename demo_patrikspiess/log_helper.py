"""Define the loggers from the configuration

First let's define the requirements we want to cover with this module:

*   The logging configuration for the user has to be simplified. The typical user is not a python
    developer so she/he has not to be aware of all the possibilities of the python logging module.
    To respect that the configuration module should only allow simple and easy to understand
    settings.

*   By default the tool does not log anything. Only after configuring any loggers in the config
    module logging should tak place. Therefore the logging module should read the logging
    configuration from the configuration file and if none is present it should set an appropriate
    default.

*   The tool must be able to do normal logging (log) and audit logging (auditlog). These both types
    of logs may have different formats and destinations.

*   It must be able to specify different loggers for log and also for auditlog. The loggers may have
    different destinations and/or different lof levels.

*   At least audit logs must be abel to send to a SYSLOG destination. This is for external revision
    control. Only this way a user may be restricted to delete it's own audit logs.

*   Logs sent by SYSLOG should contain a message with key value paris. e.g.:
        01.01.2011 11:11 hostname=machine, user=luke, command=demops 3, ...


Two loggers are added. One for normal logs and another for audit logs. As stated I want no logging
by default. Therefore I add the logging.NullHandler() after the logging.getLogger() command. This
adds the loggers but they do not log anything yet. Also the default log level of DEBUG is set there.
The effective log level will be set by the handlers added later.

For each logging type (log and audit) three will be three possible destinations.

logging_types
+-- log
|   +-- console
|   +-- file
|   +-- syslog
+-- audit
    +-- console
    +-- file
    +-- syslog

Each of these destinations may have a different logging configuration. Additional loggers may be
added on demand.


Writing normal logs
-------------------

Just use the log command as you would normally do it. e.g.:
+---
|   from demo_patrikspiess.log_helper import log
|   log.info("any information")
+---


Writing audit logs
------------------

The ContextFilter() class is use to enrich the logging message with contextual information. E.g.
the host- or username. see:
https://docs.python.org/3/howto/logging-cookbook.html#adding-contextual-information-to-your-logging-output

As the ContextFilter() class already enriches the log message with all relevant information it is
not needed to add a message to the log command. Because of that the command without a message is
enough to add an audit log entry. It is not meant to have lots of audit logs anyway. Only one audit
log is needed for each execution of the tool. The only log level which should be used is INFO, even
though all other levels are supported.
+---
|   from demo_patrikspiess.log_helper import auditlog
|   auditlog.info("")
+---

"""

import getpass
import logging
import socket
import sys
from logging import LogRecord
from typing import Any

from rich.logging import RichHandler

from demo_patrikspiess.config_helper import config


class ContextFilter(logging.Filter):  # pylint: disable=too-few-public-methods
    """
    This is a filter which injects contextual information into the log.

    This context is used to enrich the audit log. There I want to add the username of the currently
    logged in user, the hostname where the module is running and the exact command which has been
    issued.

    The hostname is needed because it is intended to send the audit log to a network destination by
    SYSLOG. In this case it is important to also record the hostname.
    """

    hostname = socket.gethostname()
    username = getpass.getuser()
    command = " ".join(sys.argv)

    def filter(self, record: LogRecord) -> bool:
        """Define the ContextFilter filter method"""
        record.hostname = ContextFilter.hostname
        record.username = ContextFilter.username
        record.command = ContextFilter.command
        return True


log = logging.getLogger("demolog")
log.setLevel(logging.DEBUG)
log.addHandler(logging.NullHandler())
auditlog = logging.getLogger("demoaudit")
auditlog.setLevel(logging.DEBUG)
auditlog.addHandler(logging.NullHandler())

for logger in config.logging:
    log_destination = logger.get("destination", "")
    log_handler: Any = logging.NullHandler()  # just used to set the Any type for mypy

    if logger.get("type") == "log":

        if log_destination.lower().startswith("console"):
            log_handler = RichHandler()
            log_formatter = logging.Formatter("%(name)s - %(message)s", datefmt="%H:%M:%S")
            log_handler.setFormatter(log_formatter)
            log_handler.setLevel(logger.get("level", "INFO").upper())
            log.addHandler(log_handler)

        if log_destination.lower().startswith("file:"):
            log_filename = log_destination.split(":")[1]
            log_handler = logging.FileHandler(log_filename)
            log_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(message)s", datefmt="%d.%m.%Y %H:%M:%S"
            )
            log_handler.setFormatter(log_formatter)
            log_handler.setLevel(logger.get("level", "INFO").upper())
            log.addHandler(log_handler)

        if log_destination.lower().startswith("syslog:"):
            # here I would add the syslog logger for normal logs (if needed at all
            pass

    if logger.get("type") == "audit":

        if log_destination.lower().startswith("console"):
            log_handler = RichHandler(show_level=False)
            log_formatter = logging.Formatter(
                "AUDIT - %(hostname)s - %(username)s - %(command)s - %(message)s",
                datefmt="%H:%M:%S",
            )
            log_handler.setFormatter(log_formatter)
            log_handler.setLevel(logger.get("level", "INFO").upper())
            log_filter = ContextFilter()
            auditlog.addFilter(log_filter)
            auditlog.addHandler(log_handler)

        if log_destination.lower().startswith("file:"):
            # here I would add the file logger for audit logs
            pass

        if log_destination.lower().startswith("syslog:"):
            # here I would add the syslog logger for audit logs
            # format would be something like:
            # "%(asctime)s, hostname=%(hostname)s, username=%(username)s, command=%(command)s \
            # , message=%(message)s", datefmt="%d.%m.%Y %H:%M:%S"
            pass
