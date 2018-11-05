import pandas as pd
import matplotlib.pyplot as plt

import os
import shutil

readingDir = 'CSVs/'
savingDir = 'PNGs/'

files = os.listdir(readingDir)

for file in files:
    if ".csv" in file:
        step = 0
        with open(str(readingDir + file), mode='r') as f:
            l = f.read().split("\n")
            step = int(l[len(l)-1].split(",")[0])
        step = round(step, -2)
        name = file.replace(".csv",".png")
        plt.figure()

        df = pd.read_csv(readingDir + file, names=['num1', 'num2'])

        plt.scatter(df['num1'],df['num2'],marker=".", color="black", s=1)
        plt.xlabel('Step')
        plt.ylabel('Accuracy')
        plt.ylim(0.0, 1.0)
        plt.savefig(savingDir + name)
        shutil.move(readingDir + file, readingDir + 'done/')

