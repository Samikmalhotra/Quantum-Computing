# %%
from qiskit import *
from matplotlib import *
from qiskit.tools.visualization import plot_histogram

# %%
# Classicial Search
randomList = [5, 4, 7, 9, 1, 3, 2, 6, 8]

# %%


def oracle(number):
    winningNumber = 7
    if number == winningNumber:
        return True
    else:
        return False


# %%
for index, number in enumerate(randomList):
    if oracle(number):
        print("The winning number is: ", number)
        print("The index of the winning number is: ", index)
        break
# %%
# Grover's Search Algo
# Oracle Circuit - (WinningState 11)

oracleCircuit = QuantumCircuit(2, name="OracleCircuit")
oracleCircuit.cz(0, 1)
oracleCircuit.to_gate()
oracleCircuit.draw(output='mpl')

# %%
mainCircuit = QuantumCircuit(2, 2, name="MainCircuit")
mainCircuit.h([0, 1])
mainCircuit.append(oracleCircuit, [0, 1])
mainCircuit.draw(output='mpl')
