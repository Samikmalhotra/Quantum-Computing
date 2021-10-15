# %%
from qiskit import *
from qiskit import circuit
from qiskit.visualization import plot_histogram
from matplotlib import *

# %%
circuit = QuantumCircuit(3, 3)

circuit.x(0)

circuit.barrier()

circuit.h(1)
circuit.cx(1, 2)

circuit.barrier()

circuit.draw(output='mpl')

# %%
