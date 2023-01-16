#initialization
import random as r
import time as t
start = ""

#time
def startime(x):
    print(x, end="")
    t.sleep(r.randint(1, 3))
    print("Done")
    t.sleep(0.5)


#start program
def mistart():
    startime("Starting BIOS...  ")
    startime("Booting EFI partition...  ")
    startime("Booting system...  ")
    startime("Starting system...  ")
    print('''======================================================================
                         MicroComputer 6.0
======================================================================''')
    print('''Instructions:  (1)This PC   (2)Information   (3)Internet   (4)Shutdown''')


def bluescreen():
    import turtle as tu
    tu.speed(0)
    tu.bgcolor("blue")
    tu.pencolor("white")
    tu.hideturtle()
    tu.penup()
    tu.goto(-200,200)
    tu.write(":(",font=("align",100))
    tu.goto(-200,90)
    tu.write("Your PC ran into a problem and needs to restart. We're just",font=("align",15))
    tu.goto(-200,45)
    tu.write("collecting some error info, and then we'll restart for you.",font=("align",15))
    tu.done()


#main program
def mininit():
    try:
        print()
        minin = int(input("Select a number and enter to complete the command  "))
        if minin == 1:
            print('''---------------
    This PC
---------------''')
            print("No disk.")
            mininit()
        elif minin == 2:
            print('''---------------
  Information
---------------''')
            print('''MicroComputer 6.0  23H1  Build 23001.900
Copyright (c) [2022-2023] WF Corporation.All rights reserved.''')
            mininit()
        elif minin == 3:
            print('''---------------
   Internet
---------------''')
            print("No Internet connection.")
            mininit()
        elif minin == 4:
            startime("Shutting down...  ")
        else:
            bluescreen()
    except:
        bluescreen()


#program framework
while start != "start":
    start = input("Please enter 'start' to start  ")
    if start == "start":
        mistart()
        mininit()
    else:
        print("Invalid statement!")