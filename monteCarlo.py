from mainSimulation import mainSimulation
import numpy as np
import matplotlib.pyplot as plt


def MonteCarlo():
    def CreateParameterConfig(k,b,m,kp,kd,ki,posFinal,deltaT,t_sim,pos0,vel0):
        enableSensorModel = False
        enableSaturatedActuator = False
        enableReferenceTracking = True

        SystemParams = dict([("k",k),("b",b),("m",m)])
        ControllerParams = dict([("kp",kp),("kd",kd),("ki",ki),("posFinal",posFinal),('deltaT',deltaT)])
        SimulationParams = dict([("t_sim",t_sim),("deltaT",deltaT),("pos0",pos0),("vel0",vel0),('sensor',enableSensorModel),('actuator',enableSaturatedActuator)])

        return [SystemParams,ControllerParams,SimulationParams]

    #Loop through the main simulation using the parameter variation
    numSamples = 10
    k_nom = 3
    b_nom = 2
    m_nom = 1

    kp = 5
    kd = 0
    ki = 2
    posFinal = 5

    t_sim = 20
    deltaT = 0.005
    pos0 = 0
    vel0 = 2

    fig, axs = plt.subplots(1,2)

    for iteration in range(0,numSamples):
        k = np.random.uniform(k_nom-0.2*k_nom,k_nom+0.2*k_nom)
        b = np.random.uniform(b_nom-0.2*b_nom,b_nom+0.2*b_nom)
        m = np.random.uniform(m_nom-0.2*m_nom,m_nom+0.2*m_nom)
        [SystemParams,ControllerParams,SimulationParams] = CreateParameterConfig(k,b,m,kp,kd,ki,posFinal,deltaT,t_sim,pos0,vel0)
        [posTrue,velTrue,TotalEnergy,ForceHistory] = mainSimulation(False,SystemParams,ControllerParams,SimulationParams)
        axs[0].plot(posTrue,label = "(k,b,m) ="+"("+str(round(k,3))+","+str(round(b,3))+","+str(round(m,3))+")")
        axs[1].plot(TotalEnergy,label = "(k,b,m) ="+"("+str(round(k,3))+","+str(round(b,3))+","+str(round(m,3))+")")

    fig.suptitle("Monte-Carlo with Input Parameter Variation (Samples =" +str(numSamples)+" )")
    axs[0].set(title = "Position")
    axs[1].set(title = "Energy Consumed by Controller")
    axs[0].set(xlabel="Timesteps",ylabel="Magnitude")
    axs[1].set(xlabel="Timesteps",ylabel="Magnitude")
    axs[0].legend()
    axs[1].legend()
    axs[0].grid()
    axs[1].grid()
    plt.show()
        
