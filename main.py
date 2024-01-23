from Parameters.params import SystemParams
from Dynamics.dynamics import StateDerivative
from Parameters.params import ControllerParams
from Parameters.params import SimulationParams
from Dynamics.dynamics import Propagate
from Sensor.sensor import Sensor
from Controller.controlller import Controller
import matplotlib.pyplot as plt
import numpy as np

#Pre-allocate
t = np.linspace(0,SimulationParams['t_sim'], int(SimulationParams['t_sim']/SimulationParams['deltaT']))
StateHistory = [np.asarray([SimulationParams['pos0'],SimulationParams['vel0']],dtype=float)]
errorHistory = [np.asarray([StateHistory[0][0]-ControllerParams['posFinal'],0,0],dtype=float)]
timestep = 0

#Initialize Controller
control = Controller(ControllerParams,idealControllerBool=False)
sensor = Sensor()

#Controllers
for elem in t:
    currentState = StateHistory[timestep]
    sensor.updateStateMemory(elem,currentState)
    control.updateStateMemory(elem,sensor.measure(elem))
    F = control.ControlSignal()
    nextState = Propagate(SimulationParams['deltaT'],elem,currentState,SystemParams,F)
    StateHistory.append(nextState)
    timestep = timestep + 1


#Plot results
posTrue = [state[0] for state in StateHistory]
velTrue = [state[1] for state in StateHistory]

posMeas = [state[0] for state in control.StateHistory]

plt.plot(t,posTrue[1:],label="Position")
plt.plot(t,velTrue[1:],label="Speed")
plt.plot(t,posMeas,label="Measured Position")
plt.xlabel("Time (in seconds)")
plt.ylabel("Magnitude")
plt.grid()
plt.legend()
plt.show()

