import logging
from datetime import datetime
_LOGGER = logging.getLogger(__name__)
try:
    from . import earnApp
except:
    import earnApp

class apiEarnApp:
    def __init__(self):
        self._money = {}
        self._userData= {}
        self._devices= []
        self._token = None
        pass

    def getEarnInfo(self,):
        user = earnApp.User()
        if user.login(self._token):
            self._money = user.money()
            self._userData = user.userData()
            self._devices = user.devices()
        else:
            print("il y a un soucis")
        pass

    def setToken(self, token):
        self._token = token

    def getInfo(self):
        self.getEarnInfo()

    def getMoney(self):
        return self._money.get("balance",0)

    def getTotalMoney(self):
        return self._money.get("earnings_total",0)

    def getData(self):
        vol = 0
        for device in self._devices:
            vol += device.get("total_bw",0)
        return vol

    def getUserData(self):
        return self._userData
