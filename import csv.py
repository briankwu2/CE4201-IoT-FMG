import csv
import random
#pip install pandas
import pandas as pd

#file location
data = pd.read_csv(r'C:\Users\plana\Desktop\42011\bpm_data.csv' )
df = pd.DataFrame(data)
#print("Dataframe is\n",df)
bpmAVG = (df.iloc[-30:,1].sum()/30)
#if it is below 70 randomize
if bpmAVG < 70 :
    bpmAVG=random.randint(60,80)

print("\n","Average bpm is: ", bpmAVG)


