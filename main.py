from Parameters.params import SystemParams
from Dynamics.dynamics import StateDerivative
from Parameters.params import ControllerParams
from Parameters.params import SimulationParams
from Dynamics.dynamics import Propagate
import matplotlib.pyplot as plt
import numpy as np

#Pre-allocate
t = np.linspace(0,SimulationParams['t_sim'], int(SimulationParams['t_sim']/SimulationParams['deltaT']))
StateHistory = [np.asarray([SimulationParams['pos0'],SimulationParams['vel0']],dtype=float)]
errorHistory = [np.asarray([StateHistory[0][0]-ControllerParams['posFinal'],0,0],dtype=float)]
timestep = 0

#Controllers
def F_PID(error):
    kp = ControllerParams['kp']
    kd = ControllerParams['kd']
    ki = ControllerParams['ki']
    return -kp*error[0]-kd*error[1]-ki*error[2]

def F_P(error):
    kp = ControllerParams['kp']
    ki = ControllerParams['ki']
    return -kp*error[0] - ki*error[2]


for elem in t:
    currentState = StateHistory[timestep]
    nextState = Propagate(SimulationParams['deltaT'],elem,currentState,SystemParams,F_P(errorHistory[timestep]))
    errorState = np.asarray([nextState[0]-ControllerParams['posFinal'],nextState[1],errorHistory[timestep][2]+errorHistory[timestep][0]*SimulationParams['deltaT']],dtype=float)
    StateHistory.append(nextState)
    errorHistory.append(errorState)
    timestep = timestep + 1


#Plot results
pos = [state[0] for state in StateHistory]
vel = [state[1] for state in StateHistory]

plt.plot(t,pos[1:],label="Position")
plt.plot(t,vel[1:],label="Speed")
plt.grid()
plt.legend()
plt.show()

