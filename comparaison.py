import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
l=['amds','gmds','pi2']
cost=[]
r=[]
for i in l:
    cost.append(np.genfromtxt(f'mds_out/{i}/cost.csv', delimiter=','))
    r.append(np.genfromtxt(f'mds_out/{i}/rollout.csv', delimiter=','))


plt.plot(r[0],cost[0],label=l[0])
plt.plot(r[1],cost[1],label=l[1])
plt.plot(r[2],cost[2],label=l[2])
plt.legend()
plt.show()