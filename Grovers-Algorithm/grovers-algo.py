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
