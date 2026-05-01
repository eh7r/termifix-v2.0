from colorama import Fore, init
import json
import subprocess
import webbrowser
import re

init(autoreset=True, convert=True)

with open("commands.json", "r", encoding="utf-8") as f:
    commands = json.load(f)


def show_banner(system):
    logo = r"""
████████╗███████╗██████╗ ███╗   ███╗██╗███████╗██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║██╔════╝██║╚██╗██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║█████╗  ██║ ╚███╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██╔══╝  ██║ ██╔██╗ 
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║     ██║██╔╝ ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
"""
    print(Fore.MAGENTA + logo)
    print(Fore.MAGENTA + "TERMIFIX v2\n")
    print(Fore.MAGENTA + "Created By Yzeed Al Harthi\n")

    print(Fore.MAGENTA + f"[ {system.upper()} COMMANDS ]\n")

    for i, (cmd, data) in enumerate(commands[system].items(), start=1):
        print(Fore.CYAN + f"{i} - {cmd}")
        print(Fore.YELLOW + f"   EN: {data['en']}")
        print(Fore.YELLOW + f"   AR: {data['ar']}")

    print(Fore.MAGENTA + "=" * 40)


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


while True:
    print("\nChoose action:")
    print("1 - Search error on Google")
    print("2 - Run command tool")
    print("3 - Password strength checker")
    print("4 - Linux basics guide")
    print("0 - Exit")

    action = input("Enter choice: ")

    if action == "1":
        error = input("Paste error: ")
        webbrowser.open(f"https://www.google.com/search?q={error}")

    elif action == "2":
        print("\n1 - Arch Linux")
        print("2 - Debian/Ubuntu")

        system_choice = input("System: ")

        if system_choice == "1":
            system = "arch"
        elif system_choice == "2":
            system = "debian"
        else:
            print("Invalid system")
            continue

        show_banner(system)

        system_commands = commands[system]

        try:
            choice = int(input("\nEnter command number: "))
            cmd_key = list(system_commands.keys())[choice - 1]
            data = system_commands[cmd_key]
            command_to_run = data["command"]

            if "<package_name>" in command_to_run:
                pkg = input("Package name: ")
                command_to_run = command_to_run.replace("<package_name>", pkg)

            print(f"\nRunning: {command_to_run}\n")
            subprocess.run(command_to_run, shell=True)

        except (ValueError, IndexError):
            print("Invalid selection")

    elif action == "3":
        pwd = input("Enter password: ")
        print("Strength:", check_password_strength(pwd))

    elif action == "4":
        print(Fore.MAGENTA + "\n[ Linux Basics Guide ]\n")

        print(Fore.CYAN + "📁 Navigation:")
        print("cd folder_name → دخول مجلد")
        print("cd .. → الرجوع للخلف")
        print("ls → عرض الملفات")

        print(Fore.CYAN + "\n📂 Files:")
        print("touch file.txt → إنشاء ملف")
        print("rm file.txt → حذف ملف")
        print("rm -r folder → حذف مجلد")

        print(Fore.CYAN + "\n📦 Compression:")
        print("tar -xvf file.tar → فك ضغط tar")
        print("unzip file.zip → فك ضغط zip")

        print(Fore.CYAN + "\n🔧 System:")
        print("clear → تنظيف الشاشة")
        print("whoami → اسم المستخدم")
        print("pwd → عرض المسار الحالي")

        print(Fore.CYAN + "\n📡 Network:")
        print("ip a → معلومات الشبكة")
        print("ping google.com → اختبار الاتصال")

    elif action == "0":
        print("Goodbye")
        break

    else:
        print("Invalid option")