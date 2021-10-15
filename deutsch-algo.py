# %%
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from matplotlib import *

# %%
circuit = QuantumCircuit(2, 1)

# %%
circuit.h(0)
circuit.x(1)
