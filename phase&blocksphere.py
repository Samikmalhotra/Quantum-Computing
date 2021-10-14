# %%
from matplotlib.pyplot import plot
from qiskit import *
from qiskit import circuit
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram
import math

# %%
Aer.backends()

# %%
qasm_simulator = Aer.get_backend('qasm_simulator')

# %%
statevector_simulator = Aer.get_backend('statevector_simulator')

# %%


def run_on_simulators(circuit):
    statevec_job = execute(circuit, backend=statevector_simulator)
    result = statevec_job.result()
    statevec = result.get_statevector()

    num_qubits = circuit.num_qubits
    circuit.measure([i for i in range(num_qubits)],
                    [i for i in range(num_qubits)])

    qasm_job = execute(circuit, backend=qasm_simulator, shots=1024).result()
    counts = qasm_job.get_counts()

    return statevec, counts


# %%
circuit = QuantumCircuit(2, 2)
x = run_on_simulators(circuit)

# %%
plot_bloch_multivector(x[0])
plot_histogram(x[1])
# %%
circuit.h(0)
x = run_on_simulators(circuit)
plot_histogram(x[1])

# %%
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
x = run_on_simulators(circuit)
plot_bloch_multivector(x[0])
# plot_histogram(x[1])

# %%
plot_histogram(x[1])
# %%
