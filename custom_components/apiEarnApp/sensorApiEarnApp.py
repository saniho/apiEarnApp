import datetime
import logging
from collections import defaultdict

try:
    from .const import (
        __VERSION__,
        __name__,
    )

except ImportError:
    from const import (
        __VERSION__,
        __name__,
    )


class manageSensorState:
    def __init__(self):
        self._myEarnApp = None
        self._LOGGER = None
        self.version = None
        pass

    def init(self, _myEarnApp, _LOGGER=None, version=None):
        self._myEarnApp = _myEarnApp
        if (_LOGGER == None):
            _LOGGER = logging.getLogger(__name__)
        self._LOGGER = _LOGGER
        self.version = version

    def getstatus(self):
        state = "unavailable"
        status_counts = defaultdict(int)
        status_counts["version"] = self.version

        status_counts["version"] = __VERSION__
        status_counts["amount"] = self._myEarnApp.getMoney()
        self._attributes = status_counts
        self._state = self._myEarnApp.getMoney()
        return self._state, self._attributes

def logSensorState(status_counts):
    for x in status_counts.keys():
        print(" %s : %s" % (x, status_counts[x]))
