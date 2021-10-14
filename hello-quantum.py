from qiskit import *
from matplotlib import *
circuit = QuantumCircuit(2, 2)
print("----------------------------------------\n")
print(circuit.draw())
print("----------------------------------------\n")

circuit.h(0)
print("----------------------------------------\n")
print(circuit.draw())
print("----------------------------------------\n")

circuit.cx(0, 1)  # 0->control-qubit  1->target qubit
circuit.measure([0, 1], [0, 1])
print("----------------------------------------\n")
print(circuit.draw())
print("----------------------------------------\n")
