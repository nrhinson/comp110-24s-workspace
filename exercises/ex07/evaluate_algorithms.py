__author__ = ""

import matplotlib.pyplot as plt
from runtime_analysis_functions import *

START_SIZE: int = 0
END_SIZE: int = 1000

usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - 730664337")
plt.show()