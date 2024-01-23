import numpy as np

#Sensor parameters
delay = 0.01
offset = 0
noise = 0.1
updateRate = 0.1

def measure(currentTime,timeHistory,StateHistory):
        #Routine to generate the sensor measurements

        #Generate the delayed position estimate
        delayedTime = currentTime - delay - updateRate
        posHistory = [state[0] for state in StateHistory]
        delayedMeasure = np.interp(delayedTime,timeHistory,posHistory)

        #Add noise and offset
        delayedMeasure = delayedMeasure + offset
        delayedMeasure = delayedMeasure + np.random.normal(0,0.1)

        return delayedMeasure

