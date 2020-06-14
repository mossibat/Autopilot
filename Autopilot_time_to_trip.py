import os
from datetime import datetime, timedelta
import time
import numpy as np

#Load the directory
path = ''

file_time = []
file_name = os.listdir(path)
for x in file_name:
    x = x[:19] #first 19 characters of the filename are the timestamp
    y = datetime.strptime(x, "%Y-%m-%d_%H-%M-%S")
    file_time.append(y)
    #print(x)
    #print(file_time)
    
total_travel_time = np.max(file_time) - np.min(file_time)

#Autopilot labelled
Autopilot = []
Autopilot_time = []
for x in file_name:
    if "AP" in x:
        x = x[:19]
        Autopilot.append(x)
        y = datetime.strptime(x, "%Y-%m-%d_%H-%M-%S")
        Autopilot_time.append(y)
        #print(x)
    
total_autopilot_time = np.sum(np.subtract(Autopilot_time[1:],Autopilot_time[:-1]))

print(f'Files: {len(file_name)}')
print(f'{len(Autopilot)} files labelled with Autopilot')

print(f'Total Travel Time: {total_travel_time} minutes')
print(f'Total Autopilot Time: {total_autopilot_time} minutes')

AP_percentage = total_autopilot_time.seconds / total_travel_time.seconds
print(f'Ratio of AP to total: {round(AP_percentage,2)}%')


# In[ ]:




