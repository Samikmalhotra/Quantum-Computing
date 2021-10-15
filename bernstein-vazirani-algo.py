# %%
from qiskit import *
from qiskit import circuit
from qiskit.visualization import plot_histogram
from matplotlib import *

# %%
secret_number = '1000101'

# %%
circuit = QuantumCircuit(8, 7)

# %%
circuit.h([i for i in range(7)])
circuit.x(7)
circuit.h(7)

circuit.barrier()
circuit.draw(output='mpl')

# %%
