# %%
from qiskit import *
IBMQ.save_account(open("ibmapi.txt", "r").read())
IBMQ.load_account()

# %%
Aer.backends()

# %%
