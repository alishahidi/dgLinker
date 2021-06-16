from modules import loading

def serverConfig(redirectName = "Google", redirectUrl = "https://google.com"):
    with open(loading.os.path.realpath('server/info/redirectName'), "w") as name:
        name.write(redirectName)
    with open(loading.os.path.realpath('server/info/redirectUrl'), "w") as url:
        url.write(redirectUrl)

def serverRun(server, port = 4040):
    with open(loading.os.path.realpath("logs/serverRun.log"),"w") as log:
        loading.Popen(("php","-S",f"localhost:{port}","-t",loading.os.path.realpath(server)),stderr = log, stdout = log)
        loading.conf.get_default().monitor_thread = False
        link = loading.ngrok.connect(port,"http")
        return link

def closePhpServer():
    with open(loading.os.path.realpath("logs/serverClose.log") , "w") as log:
        if loading.os.name == "nt":
            loading.Popen(("taskkill", "/F", "/IM", "php*"),stderr = log, stdout = log)
        elif loading.os.name == "posix":
            loading.Popen(("killall", "php"),stderr = log, stdout = log)

def serverClose(ngrokAddress):
    closePhpServer()
    loading.ngrok.disconnect(ngrokAddress)

def getConnection(close = [False, None]):
    with open('appData/port', "r") as portFile:
        port = int(portFile.read())
    if close[0]:
        serverClose(close[1])
    ngrokConnection = serverRun("server", port)
    connectionExtract = {"address": ngrokConnection.public_url.replace('http', 'https'), "addr": ngrokConnection.config['addr']}
    return connectionExtract

def printConnection(connection):
    print(f"{loading.colored('[!]', 'red', attrs = ['bold'])} {loading.colored(connection['address'], 'green')} {loading.coloredBold('=>', 'yellow')} {loading.colored(connection['addr'], 'blue')}")