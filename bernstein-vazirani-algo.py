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
circuit.cx(0, 7)
circuit.cx(2, 7)
circuit.cx(6, 7)
circuit.barrier()
circuit.draw(output='mpl')

# %%
circuit.h([i for i in range(7)])
circuit.measure([i for i in range(7)], [i for i in range(7)])
circuit.draw(output='mpl')

# %%
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1).result()
counts = result.get_counts()
print(counts)

# %%
