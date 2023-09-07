from sense_hat import SenseHat
from time import sleep
import matplotlib.pyplot as plt

sense=SenseHat()
sense.clear()
temperature=sense.get_temperature()
temperature=round(temperature,1)  ## round temperature to 1 decimal place
old = []
new = []


for i in range(10):
    curr = []
    for j in range(1000):
        temp = sense.get_temperature()
        curr.append(temp)
    old = old + curr
    new.append(sum(curr)/len(curr))
    
fig, axes = plt.subplots(1,2)
axes[0].plot([i for i in range(len(old))], old)
axes[0].set_title("Old readings")
axes[1].plot([i for i in range(len(new))], new)
axes[1].set_title("New Averaged readings")
plt.show()