import threading; import socket; import requests
import time; import os; import re; import random
import colorama; from termcolor import colored

colorama.init()

currentVersionNumber = "v2.1.0"
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

print_lock = threading.Lock()
totalOpen = 0


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def versionCheck():
    global currentVersionNumber

    print("\nChecking for PortNinja updates...", end="")

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


def portScan(checkedURL, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((checkedURL, port))
    if (result == 0):
        with print_lock:
            print(colored(f"Port {port} is open", "green"))
            global totalOpen
            totalOpen += 1
    sock.close()


def createThreads(checkedURL):
    threadingPool = []
    clrscr()
    if (method in ["1", "2"]):
        print(f"\nScanning \"{URL}\" for open ports within range {portMin} – {portMax}...\n")
        for thread, port in enumerate(range(portMin, portMax + 1)):
            threadingPool.append(threading.Thread(target=portScan, args=[checkedURL, port]))
            threadingPool[thread].daemon = True
            threadingPool[thread].start()
        for thread in threadingPool:
            thread.join()
    if (method == "3"):
        print(f"\nScanning \"{URL}\" for open ports within {portSelective}...\n")
        for thread, port in enumerate(portSelective):
            threadingPool.append(threading.Thread(target=portScan, args=[checkedURL, port]))
            threadingPool[thread].daemon = True
            threadingPool[thread].start()
        for thread in threadingPool:
            thread.join()


def processURL(URL):
    if URL.lower().startswith("http://"):
        URL = URL[7:]
    if URL.lower().startswith("http://www."):
        URL = URL[11:]
    elif URL.lower().startswith("https://"):
        URL = URL[8:]
    if URL.lower().startswith("www."):
        URL = URL[4:]
    if (URL[-1] == "/"):
        URL = URL[:-1]
    return(URL)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == "__main__":

    printBanner()
    versionCheck()

    while(True):
        try:
            URL = input("\nInput target URL to scan: ")
            checkedURL = processURL(URL)
            break
        except:
            print(colored(" Failed!", "red"))
            print("\nInvalid URL. Try again.")
            continue

    while (True):
        print("\n\nMethods:-")
        print("1. Scan all ports (0 – 65535)\n2. Scan ports in a custom range\n3. Scan individually specified ports")
        method = input("\nSelect method number: ")
        if (method == "1"):
                portMin = 1
                portMax = 65535
                break
        elif (method == "2"):
            unsorted = []
            while (True):
                portMin = int(input("\nEnter starting port here: "))
                portMax = int(input("\nEnter ending port here: "))
                if ((portMax - portMin) > 0):
                    break
                else:
                    clrscr()
                    print("\nEither invalid port numbers specified, or starting port number is greater than ending port number. Try again.\n")
                    continue
            break
        elif (method == "3"):
            try:
                portSelective = list(map(int, input("\nEnter port numbers separated by spaces here: ").split()))
                break
            except:
                clrscr()
                print("\nOne or more invalid port numbers specified. Try again.\n")
                continue
        else:
            clrscr()
            print("\nInvalid entry. Choose either option 1, 2 or 3. Try again.")
            continue

    start = time.time()
    createThreads(checkedURL)
    completionTime = time.time() - start

    print(f"\n\nThe scan completed successfully in {completionTime} seconds.")
    print(f"Total open ports: {totalOpen}")

    print("\nPress Enter to exit.")
    input()
