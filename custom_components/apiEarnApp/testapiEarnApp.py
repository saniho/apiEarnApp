def testMoney():
  import apiEarnApp, sensorApiEarnApp

  _myEarn = apiEarnApp.apiEarnApp()
  token = "1//0dMJijGNxvkEwCgYIARAAGA0SNwF-L9Irs6EZpoRZIeY7ibtyGypTtnTchAAc4_kv3JStbYM1UVE1VREr0sfE8C8dXHQ6fEhGC2M"
  _myEarn.setToken( token )
  _myEarn.getInfo()
  print(_myEarn.getMoney())
  sAM = sensorApiEarnApp.manageSensorState()
  sAM.init(_myEarn )
  state, attributes = sAM.getstatus()
  sensorApiEarnApp.logSensorState( attributes )


testMoney()