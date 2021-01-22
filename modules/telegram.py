from modules import loading

def sendMessage(message):
    with open("userInfo/botToken", "r") as token:
        token = token.read()
    with open("userInfo/chatId", "r") as chatId:
        chatId = chatId.read()
    
    api = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={message}"
    respons = loading.json.loads(loading.requests.get(api).text)
    if(respons["ok"]):
        return True
    else:
        return False