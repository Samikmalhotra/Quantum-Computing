from qiskit import *
from matplotlib import *
circuit = QuantumCircuit(2, 2)

circuit.draw(output='mpl')

circuit.h(0)
print(circuit.draw())
