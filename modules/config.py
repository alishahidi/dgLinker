from modules import loading

def configServer():
    redirectUrl = loading.inputPlus("Enter the redirect address (Ex: https://google.com, None => defaullt Url)")
    if (redirectUrl):
        redirectName = loading.inputPlus("Enter the redirect name (Ex: Google, None => defaullt name)")

    if(redirectUrl and redirectName):
        loading.server.serverConfig(redirectName, redirectUrl)

    if (redirectUrl == ""):
        loading.server.serverConfig()

    if(redirectUrl and redirectName == ""):
        redirectName = "any Site"
        loading.server.serverConfig(redirectName,redirectUrl)
    port = loading.inputPlus("Enter port number: None => default 4050");
    if port == "":
        port = 4050
    with open('appData/port', "w") as portFile:
        portFile.write(port)

def configTokenBot():
    botToken = loading.inputPlus("Enter the Telegram Bot Token")
    if (botToken and botToken != "None"):
        with open("appData/botToken", "w") as bot:
            bot.write(botToken)
    chatId = loading.inputPlus("Enter the Telegram cahtId")
    if (chatId and chatId != "None"):
        with open("appData/chatId", "w") as bot:
            bot.write(chatId)
    return True

