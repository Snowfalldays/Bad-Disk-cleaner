import os
import time
from pathlib import Path
from humanize import naturalsize

try:
    USERNAME = os.getenv('Username')
    APPDATA = os.getenv("AppData")
    LOCALAPPDATA = os.getenv("LocalAppData")
    TEMP = os.getenv("TEMP")
    SYSDIR = os.getenv("systemdrive")

    USERTEMP = TEMP
    WINTEMP = f"{SYSDIR}\Windows\Temp"

    def reboot():
        os.system('shutdown /r /c "Clean disk opreation finished successfully rebooting!"')
        time.sleep(2)
        exit()

    def get_size(path = '.'):
        size = 0

        for file_ in Path(path).rglob('*'):

            size += file_.stat().st_size
        
        return naturalsize(size)
    def main():
        print(f"The size of the {USERTEMP} folder is: " + get_size(USERTEMP))
        print(f"The size of the {WINTEMP} folde is: " + get_size(WINTEMP))
        print("loading cleaner... You can exit when ever you want!")
        time.sleep(3)
        try: 
            os.system(f"rd {USERTEMP} /s /q")
            os.system(f'del /q "{SYSDIR}\Windows\Temp" && for /d %x in ({SYSDIR}windows\Temp) do @rd /s /q "%x"')
            time.sleep(1)
            myreboot = input("Do you want to reboot your system now y/n? ")
            if myreboot == "y":
                print("alright")
                reboot()
            elif myreboot == "yes":
                print("aighjt")
                reboot()
            else: 
                print("Alright thats fine but rememember to reboot so all the changes can be finished up!")
                exit()
        except:
            print("The file is either in use or needs admin perms to delete!")  
    main()
        
except KeyboardInterrupt:
    print("KeyboardInterrupted... Exiting!")
