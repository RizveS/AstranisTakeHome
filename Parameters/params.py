#Namespace for including system & controller parameters
k = 1
b = 2
m = 3

kp = 2
kd = 1
ki = 0.2
posFinal = 5

t_sim = 10
deltaT = 0.005
pos0 = 0
vel0 = 2

enableSensorModel = True
enableSaturatedActuator = True
enableReferenceTracking = True

SystemParams = dict([("k",k),("b",b),("m",m)])
ControllerParams = dict([("kp",kp),("kd",kd),("ki",ki),("posFinal",posFinal),('deltaT',deltaT)])
SimulationParams = dict([("t_sim",t_sim),("deltaT",deltaT),("pos0",pos0),("vel0",vel0),('sensor',enableSensorModel)])

