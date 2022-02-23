def testMoney():
  from custom_components.apiEarnApp import apiEarnApp, sensorApiEarnApp

  _myEarn = apiEarnApp.apiEarnApp()

  import configparser
  mon_conteneur = configparser.ConfigParser()
  mon_conteneur.read("../myCredential/security.txt")
  print( mon_conteneur.keys)
  token = mon_conteneur["EARNAPP"]['TOKEN']
  _myEarn.setToken( token )
  _myEarn.getInfo()
  print(_myEarn.getMoney())
  sAM = sensorApiEarnApp.manageSensorState()
  sAM.init(_myEarn )
  state, attributes = sAM.getstatusMoney()
  sensorApiEarnApp.logSensorState( attributes )
  state, attributes = sAM.getstatusTotalMoney()
  sensorApiEarnApp.logSensorState( attributes )
  state, attributes = sAM.getstatusData()
  sensorApiEarnApp.logSensorState( attributes )


testMoney()