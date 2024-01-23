import numpy as np


class Sensor:
        
        def __init__(self):
            #Sensor parameters
            self.delay = 0.01
            self.offset = 0
            self.noise = 2
            self.updateRate = 0.1
            self.t = []
            self.StateHistory = []

        def updateStateMemory(self,time,state):
               self.t.append(time)
               self.StateHistory.append(state)

               if len(self.t) > 1000:
                      self.t = self.t[50:]
                      self.StateHistory= self.StateHistory[50:]


        def measure(self,currentTime):
                #Routine to generate the sensor measurements

                timeHistory = self.t
                StateHistory = self.StateHistory
                #Generate the delayed position estimate
                delayedTime = currentTime - self.delay - self.updateRate
                if delayedTime < 0:
                       delayedTime = 0

                posHistory = [state[0] for state in StateHistory]
                delayedMeasure = np.interp(delayedTime,timeHistory,posHistory)

                #Add noise and offset
                delayedMeasure = delayedMeasure + self.offset
                delayedMeasure = delayedMeasure + np.random.normal(0,0.1)

                return np.array([delayedMeasure,None])

