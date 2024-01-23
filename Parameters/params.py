#Namespace for including system & controller parameters
k = 3
b = 2
m = 1

kp = 5
kd = 0
ki = 2
posFinal = 5

t_sim = 100
deltaT = 0.005
pos0 = 0
vel0 = 2

enableSensorModel = False
enableSaturatedActuator = False
enableReferenceTracking = True

SystemParams = dict([("k",k),("b",b),("m",m)])
ControllerParams = dict([("kp",kp),("kd",kd),("ki",ki),("posFinal",posFinal),('deltaT',deltaT)])
SimulationParams = dict([("t_sim",t_sim),("deltaT",deltaT),("pos0",pos0),("vel0",vel0),('sensor',enableSensorModel),('actuator',enableSaturatedActuator)])

