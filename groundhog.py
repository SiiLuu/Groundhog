#!/usr/bin/env python3

##
## EPITECH PROJECT, 2019
## groundhog
## File description:
## groundhog python<
##

import sys
import numbers
from math import *

nbSwitches = 0
outlierses = []

def didSwitchOccured(r, previousr):
	if (previousr < 0 and r > 0) :
		switch = True
	elif (previousr > 0 and r < 0) :
		switch = True
	else :
		switch = False
	return (switch)

def temperatureAverage(tab, period):
    if len(tab) <= period:
        return
    else:
        valueG = 0
        tempA = len(tab) - period
        while (tempA < len(tab)):
            d = tab[tempA] - tab[tempA - 1]
            valueG += (d if d > 0 else 0)
            tempA += 1
        valueG /= period
        return valueG

def temperatureEvolution(tab, period):
    if len(tab) <= period:
        return
    else:
        minim = tab[len(tab) - 1 - period]
        maxim = tab[len(tab) - 1]
        pourc = (maxim - minim) * 100 / minim
        if (pourc - floor(pourc) >= 0.5):
            return ceil(pourc)
        return floor(pourc)

def standardDeviation(tab, period):
    if len(tab) < period:
        return
    else:
        standD = []
        valueD = 0
        tempA = len(tab) - period
        while (tempA < len(tab)):
            valueD += tab[tempA]
            tempA += 1
        valueD /= period
        tempA = len(tab) - period
        while (tempA < len(tab)):
            standD.append((tab[tempA] - valueD) * (tab[tempA] - valueD))
            tempA += 1
        standDTotal = 0
        for i in standD:
            standDTotal += i
        standDTotal /= period
        return sqrt(standDTotal)

def printResults(tempA, tempB, tempC, switch):
    (print("g=%.2f" % tempA, end="    ") if tempA != None else print("g=nan", end="    "))
    (print("r=%i%%" % tempB, end="    ") if tempB != None else print("r=nan%", end="    "))
    if (switch == True):
        (print("s=%.2f" % tempC, end="    ") if tempC != None else print("s=nan", end="    "))
        print("a switch occurs")
    else:
        (print("s=%.2f" % tempC) if tempC != None else print("s=nan"))

def outliers(tab, period, tempC):
    global outlierses
    i = 0
    averageTemp = 0
    list = []

    list.append(tab[len(tab) -1])
    while (i < period):
        averageTemp += tab[i - period]
        i += 1
    high = (averageTemp / period) + 2 * tempC
    low = (averageTemp / period) - 2 * tempC
    gap = (tab[len(tab) -1] - low) / (high - low)
    if (gap > 0.5):
        gap = 1 - gap
    list.append(gap)
    outlierses.append(list)

def relTempEvol(tab, prev, period):
    global nbSwitches
    switch = False
    tempA = temperatureAverage(tab, period)
    tempB = temperatureEvolution(tab, period)
    tempBP = temperatureEvolution(prev, period)
    tempC = standardDeviation(tab, period)
    if (len(tab) >= period):
        outliers(tab, period, tempC)
    if (tempBP != None):
        if ((abs(tempB + tempBP)) != (abs(tempB) + abs(tempBP))):
            nbSwitches += 1;
            switch = True;
        else:
            switch = False;
    printResults(tempA, tempB, tempC, switch)

def previson(tab, txt, period):
    tab.append(float(txt))
    prev = tab
    prev = prev[:-1]
    relTempEvol(tab, prev, period)

def end(tab, period):
    global outlierses
    fiveOutliers = []
    i = 0

    if (len(tab) < period):
        sys.stderr.write("Not enough values.\n")
        sys.exit(84)
    outlierses.sort(key=lambda x: x[1], reverse = False)
    if (len(outlierses) > 5):
        while (i < 5):
            fiveOutliers.append(outlierses[i][0])
            i += 1
    print("Global tendency switched %i times" % nbSwitches)
    print("5 weirdest values are ", fiveOutliers)

def loop(period):
    tab = []
    while (1):
        try:
            txt = input()
        except (EOFError, KeyboardInterrupt):
            sys.stderr.write("No stop.\n")
            sys.exit(84)
        if (txt == "STOP"):
            end(tab, period)
            break
        elif (isFloat(txt)):
            previson(tab, txt, period)
        else:
            print("Bad input !!!")

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        sys.stderr.write("Bad input !!!\n")
        sys.exit(84)

def checkArgs(a):
    if (not a.isdigit()):
        sys.stderr.write("Error: period need to be integers.\n")
        sys.exit(84)

def help():
    print("SYNOPSIS")
    print("    ./groundhog period")
    print("\nDESCRIPTION")
    print("    period\t   the number of days defining a period")
    sys.exit(0)

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        help()
    if (len(sys.argv) == 2):
        checkArgs(sys.argv[1])
        loop(int(sys.argv[1]))
        sys.exit(0)
    sys.exit(84)

if __name__  == "__main__":
    main()
