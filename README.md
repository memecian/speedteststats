# speedteststats
### a python script to automate data collection from Ookla's Speedtest CLI
Does what it says on the tin: runs ookla-speedtest, grabs data collected by it (namely latency, download and upload speeds) and puts into a tab-delimited text file. From there, you are free to do whatever you want - create a graph, make a scene in your ISP's local shop - the options are endless.

I wholeheartedly recommend putting this into Task Scheduler as a reccurring job (or make it a cron job if you're on Linux)
### Sample Data
```
LATENCY	DOWNLOAD	UPLOAD	TIME
13.08	200.84	23.65	20:00
12.83	606.22	42.98	20:15
14.16	701.04	35.82	20:30
15.34	35.86	49.22	20:45
14.30	500.89	35.47	21:00
```
Yes, the above data is very real and captured in the wilderness of Baden-Württemberg.

## Requirements:
- Python 3.8 or newer
- a working internet connection

## Planned Features
 - add daily average of all collected values
 - plot results into nice jpeg/png/tiff files 