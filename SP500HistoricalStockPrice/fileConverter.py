import os

for f in os.listdir('.'):
    if f.endswith('.txt'):
        print(f, f[:-4]+'.csv')
        os.rename(f, f[:-4]+'.csv')