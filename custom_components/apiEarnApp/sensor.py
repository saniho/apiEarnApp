"""Sensor for my first"""
import logging
from collections import defaultdict
from datetime import timedelta, datetime

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_TOKEN,
    CONF_NAME,
    ATTR_ATTRIBUTION,
    CONF_SCAN_INTERVAL,
)

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.util import slugify
from homeassistant.util.dt import now, parse_date


from .const import (
    DOMAIN,
    __VERSION__,
    __name__,
    SCAN_INTERVAL_http,
)

_LOGGER = logging.getLogger(__name__)
DOMAIN = "saniho"
ICON = "mdi:package-variant-closed"
SCAN_INTERVAL = timedelta(seconds=1800)
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_TOKEN): cv.string,
    }
)

from . import apiEarnApp, sensorApiEarnApp

class myEarnApp:
    def __init__(self, token, _update_interval):
        self._lastSynchro = None
        self._update_interval = _update_interval
        self._token = token
        self._myEarnApp = apiEarnApp.apiEarnApp()
        pass


    def update(self,):
        import datetime

        courant = datetime.datetime.now()
        if ( self._lastSynchro == None ) or \
            ( (self._lastSynchro + self._update_interval) < courant ):
            _LOGGER.warning("-update possible- on lance")
            self._myEarnApp.setToken( self._token )
            self._myEarnApp.getInfo()
            self._lastSynchro = datetime.datetime.now()

    # revoir recupearation valeur
    def getmyEarnApp(self):
        return self._myEarnApp

    def getMoney(self):
        return self._myEarnApp.getMoney()

    def getData(self):
        return self._myEarnApp.getData()


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the platform."""
    name = config.get(CONF_NAME)
    update_interval = config.get(CONF_SCAN_INTERVAL, SCAN_INTERVAL)
    update_interval_http = SCAN_INTERVAL_http
    try:
        token = config.get(CONF_TOKEN)
        session = []
    except :
        _LOGGER.exception("Could not run my apiMaree Extension miss argument ?")
        return False
    myEarn = myEarnApp( token, update_interval )
    myEarn.update()
    add_entities([infoEanAppSensorMoney(session, name, update_interval, myEarn )], True)
    add_entities([infoEanAppSensorData(session, name, update_interval, myEarn )], True)

class infoEanAppSensorMoney(Entity):
    """."""

    def __init__(self, session, name, interval, myEarn):
        """Initialize the sensor."""
        self._session = session
        self._name = name
        self._myEarn = myEarn
        self._attributes = None
        self._state = None
        self.update = Throttle(interval)(self._update)
        self._sAM = sensorApiEarnApp.manageSensorState()
        self._sAM.init( self._myEarn )

    @property
    def name(self):
        """Return the name of the sensor."""
        return "myEarnApp"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return "$"

    def _update(self):
        """Update device state."""
        self._myEarn.update()
        self._state, self._attributes = self._sAM.getstatus()

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return ICON


class infoEanAppSensorData(Entity):
    """."""

    def __init__(self, session, name, interval, myEarn):
        """Initialize the sensor."""
        self._session = session
        self._name = name
        self._myEarn = myEarn
        self._attributes = None
        self._state = None
        self.update = Throttle(interval)(self._update)
        self._sAM = sensorApiEarnApp.manageSensorState()
        self._sAM.init( self._myEarn )

    @property
    def name(self):
        """Return the name of the sensor."""
        return "myEarnApp.data"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return ""

    def _update(self):
        """Update device state."""
        self._myEarn.update()
        self._state, self._attributes = self._sAM.getstatusData()

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return ICON