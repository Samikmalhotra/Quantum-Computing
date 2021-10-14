# %%
from matplotlib import *
from qiskit import *
from matplotlib import *
from qiskit.visualization import plot_histogram

# %%
circuit = QuantumCircuit(2, 2)
circuit.draw(output='mpl')

# %%
circuit.h(0)
circuit.draw(output='mpl')

# %%
circuit.cx(0, 1)  # 0->control-qubit  1->target qubit
circuit.measure([0, 1], [0, 1])
circuit.draw(output='mpl')

# %%
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator).result()
plot_histogram(result.get_counts(circuit))

# %%
