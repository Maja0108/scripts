import os
import glob
import pandas as pd

# Collect files with csv extensions from the python directory
os.chdir("/python")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

filename = []

for file in all_filenames:
    name, ext = os.path.splitext(file)
    filename.append(name)

 
#combine all files in the list to a DataFrame
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#add filename as a new column to the DataFrame
combined_csv["filename"] = filename

#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')