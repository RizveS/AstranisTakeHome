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
PowerConsumption = []
TotalEnergy = [0]
errorHistory = [np.asarray([StateHistory[0][0]-ControllerParams['posFinal'],0,0],dtype=float)]
timestep = 0

#Initialize Controller & Sensor objects
control = Controller(ControllerParams,DerivativeControl=True)
sensor = Sensor()

#Controllers
for elem in t:
    currentState = StateHistory[timestep]
    sensor.updateStateMemory(elem,currentState)

    #Update controller state based on whether the sensor flag is toggled (See params.py)
    if SimulationParams['sensor'] == True:
        control.updateStateMemory(elem,sensor.measure(elem))
    else:
        control.updateStateMemory(elem,currentState)
    
    #Calculate the actuator force
    F = control.ControlSignal()

    #Propagate state quantities
    PowerConsumption.append(F*currentState[1])
    TotalEnergy.append(TotalEnergy[timestep]+abs(PowerConsumption[-1]*SimulationParams['deltaT']))
    nextState = Propagate(SimulationParams['deltaT'],elem,currentState,SystemParams,F)
    StateHistory.append(nextState)
    timestep = timestep + 1


#Plot results
posTrue = [state[0] for state in StateHistory]
velTrue = [state[1] for state in StateHistory]


posMeas = [state[0] for state in control.StateHistory]

fig, axs = plt.subplots(1,2)
axs[0].plot(t,posTrue[1:],label="True Position")
axs[0].plot(t,velTrue[1:],label="True Speed")
axs[0].plot(t,posMeas,label="Measured Position")
axs[0].grid()
axs[0].legend()
axs[0].set(xlabel="Time (in seconds)",ylabel="Magnitude")
#axs[1].plot(t,PowerConsumption,label="Power Consumption (in W)")
axs[1].plot(t,TotalEnergy[1:],label="Total Energy Used (in Ws)")
axs[1].set(xlabel="Time (in seconds)",ylabel="Magnitude")
axs[1].grid()
axs[1].legend()

plt.show()


