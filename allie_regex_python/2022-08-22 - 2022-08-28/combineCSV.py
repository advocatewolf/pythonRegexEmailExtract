import os
import glob
import pandas as pd

# path = os.getcwdb()
# os.chdir(path)

all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')