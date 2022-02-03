import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
date = yesterday.strftime("%d-%m-%Y")
month = yesterday.strftime("%m-%Y")

dl_rates_str = []
ul_rates_str = []
times = []
temp = []

working_dir = os.getcwd()
file = open(f"{working_dir}/{month}/{date}.txt", "r")
file_read = file.readlines()

for i in range(1, len(file_read)):
    temp = file_read[i].split("\t")
    dl_rates_str.append(temp[1])
    ul_rates_str.append(temp[2])
    times.append(temp[3])

# convert strings to floats   
dl_rates = [float(i) for i in dl_rates_str]
ul_rates = [float(i) for i in ul_rates_str]

plt.grid()
plt.ylim(0, 1000)
plt.suptitle('Download/Uploadraten in der WG "Die WG"')
plt.title("Schauinslandstr. 35, 76199 Karlsruhe")
plt.ylabel("Mbit/s")
plt.plot(times, dl_rates, label="Download")
plt.plot(times, ul_rates, label="Upload")
plt.legend()

plt.xticks(fontsize=8)
plt.show()

