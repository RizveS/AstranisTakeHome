import numpy as np

#Sensor parameters
delay = 0.01
offset = 0
noise = 0.1
updateRate = 0.1

def measure(currentTime,timeHistory,StateHistory):
        delayedTime = currentTime - delay - updateRate
        posHistory = [state[0] for state in StateHistory]
        delayedMeasure = 

