"""define the loggger and do some example output"""

from demo_patrikspiess.log_helper import auditlog, log


class Loggie:
    """The logging demo class

    Here we just do some logging for demo purposes. The loggers are defined in log_helper.py
    """

    def __init__(self) -> None:
        """initialize the class and do the demo logs"""
        self.do_logs()
        self.do_audit_logs()

    @staticmethod
    def do_logs(message: str = "demo log message") -> None:
        """do demo logging with all levels"""
        log.debug(message)
        log.info(message)
        log.warning(message)
        log.error(message)
        log.critical(message)

    @staticmethod
    def do_audit_logs(message: str = "demo audit message") -> None:
        """do demo audit logging with all levels"""
        auditlog.debug(message)
        auditlog.info(message)
        auditlog.warning(message)
        auditlog.error(message)
        auditlog.critical(message)

        # Under normal circumstances one would simply log without any message
        # The audit logger takes care itself of all the fields to be logged
        auditlog.info("")
