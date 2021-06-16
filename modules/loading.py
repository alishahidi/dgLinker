import os
from termcolor import colored
import os
import platform
from getpass import getuser
from pyngrok import ngrok, conf
from subprocess import Popen
import requests
import time
import json
from modules import server, checkData, config, telegram
import signal
import sys

colors = ("yellow", "blue", "red", "magenta", "cyan", "green")

def coloredBold(text, color):
    if color in colors:
       return colored(text, color = color, attrs = ["bold"])
    else:
        raise ValueError("color is not in exists color list")


def banner():
    with open('appData/banner', 'w', encoding="utf8") as file:
        file.write(""" * * * * * * * * * * * * * * * * * *
 *  ┌-┐ ┌─┐ ╦   ┬ ┌┐┌ ┬┌─ ┌─┐ ┬─┐  *
 *    │ │ ┬ ║   │ │││ ├┴┐ ├┤  ├┬┘  *
 *  ─-┘ └─┘ ╩═╝ ┴ ┘└┘ ┴ ┴ └─┘ ┴└─  *
 * * * * * * * * * * * * * * * * * *""")
    with open(os.path.realpath("appData/banner"), "r", encoding="utf8") as banner:
        bannerText = banner.read()
    print(colored(f"\n{bannerText}\n", "red", attrs=["bold", "blink"]))

def signal_exit_handler(sig, frame):
    checkData.stopMonitor()


def clear():
    if os.name == "nt":
            os.system("cls")
    elif os.name == "posix":
            os.system("clear")

def loading():
    clear()
    banner()

def menu_creator(menuItems):
    menuContent = []
    count = 0
    for item in menuItems:
        content = f"{colored('[', 'red')}{count}{colored(']', 'red')} {colored(item, 'green', attrs = ['bold'])}"
        menuContent.append(content)
        count+=1
    return menuContent

def main_menu():
    print("\n")
    menus = menu_creator(["exit", "config (set telegram bot)", "config (set server)", "start dglinker"])
    for item in menus:
        print (item)
        time.sleep(.2)
    print("\n")

def inputPlus(inputText):
    print("\n")
    inputValue = input(f"{colored('[', 'red')}{inputText}{colored(']', 'red')}$ ")
    print("\n")
    return inputValue;

def check_dir():
    if os.path.exists("temp") is not True:
        os.makedirs("temp")
    if os.path.exists("appData") is not True:
        os.makedirs("appData")

def check_file():
    if not os.path.exists('appData/botToken'):
        with open('appData/botToken', 'w') as file:
            file.write("Type your token here.")
    if not os.path.exists('appData/chatId'):
        with open('appData/chatId', 'w') as file:
            file.write("Type your chatId here.")
    if not os.path.exists('appData/port'):
        with open('appData/port', "w") as portFile:
            portFile.write("4050")

def run():
    checkData.clearLog()
    check_dir()
    check_file()
    main_menu()
    state = inputPlus("Select option")
    if state == "0":
        return False
    elif state == "1":
        config.configTokenBot()
    elif state == "2":
        config.configServer()
    elif state == "3":
        ngrokTunnel = server.getConnection()
        server.printConnection(ngrokTunnel)
        print(colored('\nUse CTRL + C for exit monitor mode\n', 'green'))
        checkData.monitorLog()