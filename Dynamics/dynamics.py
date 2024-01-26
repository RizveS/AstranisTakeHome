import numpy as np

def StateDerivative(t,currentState,Param,F):
    pos = currentState[0]
    vel = currentState[1]
    disturbance = lambda t: 10 if t < 50 else 0
    acc = (1/Param["m"])*(F-Param["k"]*pos-Param["b"]*vel)
    return np.asarray([vel,acc],dtype=float)

def Propagate(deltaT,t,currentState,Param,F):
    k1 = StateDerivative(t,currentState,Param,F)
    k2 = StateDerivative(t+0.5*deltaT,currentState+0.5*k1,Param,F)
    k3 = StateDerivative(t+0.5*deltaT,currentState+0.5*k2,Param,F)
    k4 = StateDerivative(t+deltaT,currentState+k3,Param,F)
    nextState = currentState + (deltaT)*((k1 +2*k2 + 2*k3 +k4)/6)
    return nextState
