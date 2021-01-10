import threading; import socket; import requests
import time; import os; import re
import colorama; from termcolor import colored

colorama.init()

currentVersionNumber = "v1.0.0"
VERSION_CHECK_URL = "https://raw.githubusercontent.com/SHUR1K-N/PortNinja-Open-Ports-Finder/master/versionfile.txt"
BANNER1 = colored('''
   ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
  ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
  ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
  ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
  ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
  ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
  ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
  ░░       ░ ░ ░ ▒    ░░   ░   ░         ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
               ░ ░     ░                       ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                    -------------------------------------''', 'blue')
BANNER3 = colored('''                    || PortNinja: The Open Ports Finder ||''', 'red')
BANNER4 = colored('''                    -------------------------------------''', 'blue')

totalOpen = 0


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def versionCheck():
    global currentVersionNumber

    print("\nChecking for MeetNinja updates...", end="")

    crawlVersionFile = requests.get(VERSION_CHECK_URL)
    crawlVersionFile = str(crawlVersionFile.content)
    crawlVersionFile = re.findall(r"([0-9]+)", crawlVersionFile)
    latestVersionNumber = int(''.join(crawlVersionFile))

    currentVersionNumber = re.findall(r"([0-9]+)", currentVersionNumber)
    currentVersionNumber = int(''.join(currentVersionNumber))

    if currentVersionNumber >= latestVersionNumber:
        print(colored(" You are using the latest version!\n", "green"))
    elif currentVersionNumber < latestVersionNumber:
        print(colored(" You are using an older version of PortNinja.", "red"))
        print(colored("\nGet the latest version at https://github.com/SHUR1K-N/PortNinja-Open-Ports-Finder", "yellow"))
        print(colored("Every new version comes with fixes, improvements, new features, etc..", "yellow"))
        print(colored("Please do not open an Issue if you see this message and have not yet tried the latest version.", "yellow"))


def portCheck(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target, port))
    if (result == 0):
        print(colored(f"Port {port} is open", "green"))
        global totalOpen
        totalOpen += 1
    sock.close()


def checkThreads(target):
    threadingPool = []
    clrscr()
    print(f"\nScanning {target} for open ports within range 0 – 65535...\n")
    for thread in range(0, 65535):
        threadingPool.append(threading.Thread(target=portCheck, args=[target, thread]))
        threadingPool[thread].start()
    for thread in threadingPool:
        thread.join()


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == "__main__":

    printBanner()
    versionCheck()

    target = input("\nInput target URL to scan: ")
    if target.lower().startswith("http://"):
        target = target[7:]
    elif target.lower().startswith("https://"):
        target = target[8:]
    if (target[-1] == "/"):
        target = target[:-1]
    checkThreads(target)

    print("\nScan completed successfully!")
    print(f"Total open ports: {totalOpen}")

    print("\nPress Enter to exit.")
    input()
