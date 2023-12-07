import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
# ignore this part --------x------------x-----------x-----#

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    dice_result.append(dice1 + dice2)

mean = sum(dice_result)/len(dice_result)
print("Mean of this data", mean)

std_deviation = statistics.stdev(dice_result)
print("Standard Deviation of this data", std_deviation)


median = statistics.median(dice_result)
print("Median of this data is: ", median)

mode = statistics.mode(dice_result)
print("Mode of this data is: ", mode)

# ignore this part --------x------------x-----------x-----#

fig = ff.create_distplot([dice_result], ["Result"], show_hist = False)

fig.show()