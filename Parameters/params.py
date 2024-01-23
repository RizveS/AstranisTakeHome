#Namespace for including system & controller parameters
k = 1
b = 2
m = 3

kp = 2
kd = 0.01
ki = 0.02
posFinal = 100

t_sim = 1000
deltaT = 0.005
pos0 = 0
vel0 = 2

SystemParams = dict([("k",k),("b",b),("m",m)])
ControllerParams = dict([("kp",kp),("kd",kd),("ki",ki),("posFinal",posFinal),('deltaT',deltaT)])
SimulationParams = dict([("t_sim",t_sim),("deltaT",deltaT),("pos0",pos0),("vel0",vel0)])

