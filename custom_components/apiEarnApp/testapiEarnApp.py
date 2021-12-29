def testMoney():
  import apiEarnApp, sensorApiEarnApp

  _myEarn = apiEarnApp.apiEarnApp()
  token = "...."
  _myEarn.setToken( token )
  _myEarn.getInfo()
  print(_myEarn.getMoney())
  sAM = sensorApiEarnApp.manageSensorState()
  sAM.init(_myEarn )
  state, attributes = sAM.getstatus()
  sensorApiEarnApp.logSensorState( attributes )
  state, attributes = sAM.getstatusData()
  sensorApiEarnApp.logSensorState( attributes )


testMoney()