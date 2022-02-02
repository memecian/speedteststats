import matplotlib.pyplot as plt
import os
from datetime import datetime

date = datetime.now().strftime("%d-%m-%Y")
month = datetime.now().strftime("%m-%Y")

dl_rates = []
ul_rates = []
times = []
temp = []

working_dir = os.getcwd()
print(working_dir)
file = open(f"{working_dir}/{month}/{date}.txt", "r")
file_read = file.readlines()

for i in range(1, len(file_read)):
    temp = file_read[i].split("\t")
    dl_rates.append(temp[1])
    ul_rates.append(temp[2])
    times.append(temp[3])
    

plt.grid()
plt.plot(times, dl_rates)
plt.plot(times, ul_rates)
plt.show()