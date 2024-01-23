import numpy as np

class Controller:
    def __init__(self, ControllerParams,idealControllerBool):
        self.Params = ControllerParams
        self.ideal = idealControllerBool
        self.t = []
        self.StateHistory = []
        self.desiredState = np.array([ControllerParams['posFinal'],0],dtype=float)
        self.errorState = np.array([0,0,0],dtype=float)

    def updateStateMemory(self,time,state):
        self.t.append(time)
        self.StateHistory.append(state)
        self.errorState = np.array([state[0]-self.desiredState[0],0,self.errorState[2]+self.errorState[0]*self.Params['deltaT']])


    def ControlSignal(self):
        error = self.errorState
        if self.ideal == True:
            kp = self.Params['kp']
            kd = self.Params['kd']
            ki = self.Params['ki']
            return -kp*error[0]-kd*error[1]-ki*error[2]
        else:
            kp = self.Params['kp']
            ki = self.Params['ki']
            return -kp*error[0] - ki*error[2]
