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

colors = ("yellow", "blue", "red", "magenta", "cyan", "green")

def coloredBold(text, color):
    if color in colors:
       return colored(text, color = color, attrs = ["bold"])
    else:
        raise ValueError("color is not in exists color list")

def banner():
    with open(os.path.realpath("modules/banner"), "r") as banner:
        bannerText = banner.read()
    print(coloredBold("\n" + bannerText + "\n", "red"))

def loading():
    if os.name == "nt":
            print("Loading......")
            time.sleep(1)
            os.system("cls")
    elif os.name == "posix":
            print("Loading......")
            time.sleep(1)
            os.system("clear")
    banner()

def inputPlus(inputText):
    inputValue = input(f"\n{colored('┌─[', 'red')}{getuser()}{coloredBold('@', 'yellow')}{colored(platform.node(), 'cyan')}]─[{colored(inputText, 'green')}]\n{colored('└──╼', 'red')} {coloredBold('$', 'yellow')} ")
    print("\n")
    return inputValue


