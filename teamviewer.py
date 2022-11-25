


from os import system
from time import sleep
import datetime

dt = datetime.datetime.now()
kill = lambda name : system(f'taskkill /im {name}.exe')

while True:
    if int(dt.strftime('%H')) == 8:
        for process in ['TeamViewer']:
            for _ in range(10):
                kill(process)
                sleep(.25)
            sleep(.25)
            

    if int(dt.strftime('%H')) == 23:
        system("run.bat")

    sleep(3660)