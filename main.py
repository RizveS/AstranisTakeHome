from Parameters.params import SystemParams
from Dynamics.dynamics import StateDerivative
from Parameters.params import ControllerParams
from Parameters.params import SimulationParams
from Dynamics.dynamics import Propagate
from Sensor.sensor import measure
from Controller.controlller import Controller
import matplotlib.pyplot as plt
import numpy as np

#Pre-allocate
t = np.linspace(0,SimulationParams['t_sim'], int(SimulationParams['t_sim']/SimulationParams['deltaT']))
StateHistory = [np.asarray([SimulationParams['pos0'],SimulationParams['vel0']],dtype=float)]
errorHistory = [np.asarray([StateHistory[0][0]-ControllerParams['posFinal'],0,0],dtype=float)]
timestep = 0

#Initialize Controller
control = Controller(ControllerParams,idealControllerBool=True)

#Controllers
for elem in t:
    currentState = StateHistory[timestep]
    control.updateStateMemory(elem,currentState)
    F = control.ControlSignal()
    nextState = Propagate(SimulationParams['deltaT'],elem,currentState,SystemParams,F)
    StateHistory.append(nextState)
    timestep = timestep + 1


#Plot results
pos = [state[0] for state in StateHistory]
vel = [state[1] for state in StateHistory]

plt.plot(t,pos[1:],label="Position")
plt.plot(t,vel[1:],label="Speed")
plt.grid()
plt.legend()
plt.show()

