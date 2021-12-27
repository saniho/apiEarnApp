import logging
from datetime import datetime
_LOGGER = logging.getLogger(__name__)
import earnApp

class apiEarnApp:
    def __init__(self):
        self._money = {}
        self._userData= {}
        self._token = None
        pass

    def getEarnInfo(self,):
        user = earnApp.User()
        if user.login(self._token):
            self._money = user.money()
            self._userData = user.userData()
        else:
            print("il y a un soucis")
        pass

    def setToken(self, token):
        self._token = token

    def getInfo(self):
        self.getEarnInfo()

    def getMoney(self):
        return self._money.get("balance",0)

    def getUserData(self):
        return self._userData
