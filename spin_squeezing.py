#Inspired by this paper: https://arxiv.org/pdf/1908.08343.pdf
from qiskit import *
from qiskit.circuit import Parameter
import numpy as np
from math import pi
from scipy import optimize

n = 2
qr = QuantumRegister(n)
cr = ClassicalRegister(n)
qc = QuantumCircuit(qr, cr)
qc.h(qr)
rhoX = Parameter('rhoX')
qc.rxx(rhoX, qr[0], qr[1])
thetaX = Parameter('thetaX')
qc.rx(thetaX, [0,1])
rhoZ = Parameter('rhoZ')
qc.rzz(rhoZ, qr[0], qr[1])
thetaZ = Parameter('thetaZ')
qc.rz(thetaZ, [0,1])
qc.h(qr)
qc.measure(qr, cr)
print(qc)


from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run(params, show=False):
    results = execute(qc, backend=BasicAer.get_backend('qasm_simulator'), parameter_binds=[{thetaX: params[0], rhoX: params[1], rhoZ: params[2], thetaZ: 0}],  shots=1024).result()
    answer = results.get_counts()
    Jx = answer.get("11", 0) - answer.get("00", 0)
    if show:
        plot_histogram(answer)
        plt.show()
        
    results = execute(qc, backend=BasicAer.get_backend('qasm_simulator'), parameter_binds=[{thetaX: params[0], rhoX: params[1], rhoZ: params[2], thetaZ: pi/2}],  shots=1024).result()
    answer = results.get_counts()
    Jy2 = (n*1024 + answer.get("11", 0) + answer.get("00", 0) - answer.get("01", 0) - answer.get("10", 0))/4
    xi = n*Jy2/(Jx**2 + 1e-09)
    if show:
        plot_histogram(answer)
        plt.show()
    return xi

x0 = [pi/2, pi/2, pi/2]
print(run(x0, show=False))
res = optimize.minimize(run,x0,method='Nelder-Mead')
print(res.x)
print(run(res.x, show=True))


