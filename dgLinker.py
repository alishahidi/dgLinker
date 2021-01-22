from modules import loading

loading.loading()
loading.checkData.clearLog()
loading.config.configServer()
bot = loading.config.configTokenBot()
loading.loading()
ngrokTunnel = loading.server.getConnection(4050)
loading.server.printConnection(ngrokTunnel)
loading.checkData.monitorLog(bot)
