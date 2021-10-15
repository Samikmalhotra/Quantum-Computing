# %%
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from matplotlib import *

# %%
circuit = QuantumCircuit(2, 1)

# %%
circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.draw(output='mpl')

# %%
circuit.cx(0, 1)
circuit.barrier()
circuit.h(0)
circuit.barrier()
circuit.draw(output='mpl')

# %%
circuit.measure(0, 0)
circuit.draw(output='mpl')

# %%
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=backend, shots=1024).result()
counts = result.get_counts(circuit)

plot_histogram([counts])

# %%
