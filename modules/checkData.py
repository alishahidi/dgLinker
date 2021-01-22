from modules import loading

stat_file = 0
def monitorLog(bot):
    def printLog(log):
        client = log["client"]
        ipInfo = log["ip_info"]
        print (f"\n {loading.colored('[!]', 'green')} IP: {ipInfo['ip']}  Opened link : {loading.time.ctime()} \n")
        if(bot):
            loading.telegram.sendMessage(f"[!] IP: {ipInfo['ip']}  Opened link : {loading.time.ctime()}")
        print(loading.coloredBold("\nClient Info", 'yellow'))
        print(loading.coloredBold("--------------------++++++++++--------------------\n", "red"))
        client = printDic(client)
        if(bot):
            loading.telegram.sendMessage(client) 
        print(loading.coloredBold("\nIp Info", 'yellow'))
        print(loading.coloredBold("--------------------++++++++++--------------------\n", "red"))
        ip = printDic(ipInfo)
        if(bot):
            loading.telegram.sendMessage(ip)  
        print(f"\n\n  [!~] {loading.colored('Wating For Another', 'red')} [~!]")
    def readLog():
        global stat_file
        if not str(loading.os.stat(loading.os.path.realpath('server/infoLogs/info.log')).st_size) == stat_file:
            stat_file = str(loading.os.stat(loading.os.path.realpath('server/infoLogs/info.log')).st_size)
            with open(loading.os.path.realpath('server/infoLogs/info.log'), "r") as log:
                log = log.read()
            try:
                clearLog()
                printLog(loading.json.loads(log))
            except:
                ""
    while True:
        readLog()
        loading.time.sleep(1)

def clearLog():
    with open(loading.os.path.realpath('server/infoLogs/info.log'), "w") as log:
        log.write("")

def printDic(dic):
    content = ""
    numOfDic = 0
    numOfPrint = 0
    indexOfDic = dic.keys()
    valueOfDic = dic.values()
    for a in dic:
        temp = f"[!] {list(indexOfDic)[numOfDic]} : {list(valueOfDic)[numOfDic]}\n"
        print(f"{loading.colored('[!]', 'blue')} {list(indexOfDic)[numOfDic]} : {list(valueOfDic)[numOfDic]}")
        content = content + temp
        numOfPrint = numOfPrint + 1
        if numOfPrint < len(dic) :
            print("-----------------")
        numOfDic = numOfDic + 1
        loading.time.sleep(.1)
    return content