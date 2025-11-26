"""
Do the main configuration.

This Module loads and defines the main Configuration for the tool. It is meant to load the
configuration from a YAML file into a python dict.

Possible configurations are:

logging (list)
    The logging setting contains a list of logging configurations. As many loggers as needed may be
    configured.

logging.item (dict)
    A logging item is a dict with all the settings needed for the respective logger

logging.item.type (str)
    Define the type of log (log or audit)

    "log"
        defines that the logger is a normal logger
    "auditlog"
        defines that the logger is an audit logger

    Any other string set in type wil lbe ignored

logging.item.level (str)
    Define the og level from one of the following:
    "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    In you omit the level the default level of INFO is used

logging.item.destination (str)
    Define the logging destination

    "console"
        Log to the console to stdout

    "file:FILENAME"
        Log to a file. You must specify a FILENAME.

    "syslog:HOSTNAME:PORT
        Log to a SYSLOG server.
        You must define a HOSTNAME
        If you omit PORT the default port 514 will be used
"""

from dataclasses import dataclass

import yaml

# Here I just define an example YAML. In the future I'll load that from a configuration file
YAML_CONFIG: str = """
logging:
    -   type: log
        destination: hallo
        level: debug
    -   type: log
        destination: console
        level: info
    -   dummy1: Hello   # just used to simulate a wrong configuration
        dummy2: World   # just used to simulate a wrong configuration
    -   type: audit
        destination: console
        level: debug
    -   type: log
        destination: file:log.txt
        level: debug
"""
# YAML_CONFIG = ""  # If you uncomment this line it simulates an empty configuration file


@dataclass
class Config:
    """
    The global configuration class.
    """

    # set default values
    loaded_config = yaml.safe_load(YAML_CONFIG) or {}
    logging = loaded_config.get("logging", [{"type": "log", "destination": "console"}])


config = Config()
