import pandas as pd
import time
from pathlib import Path
import readcsvturbo as rct

################### Reading the first and last line from big_csv and getting a df ###################
csv_file_path = Path("./big_csv.csv")

print("""
############## RAW PANDAS ###############
# Read the whole file in using read_csv #
#########################################
""")

start_time = time.perf_counter()

df = pd.read_csv(csv_file_path)

df_first_line = df.iloc[[0]]
df_last_line = df.iloc[[-1]]

frames = [df_first_line, df_last_line]
df = pd.concat(frames)

print(df)

end_time = time.perf_counter()

print(f'RAW PANDAS TIME: {round(end_time-start_time,2)}s\n')


print("""
################### SKIPROWS ##################
# Get the length of the file from readlines() #
# Read big_csv using skiprows                 #
###############################################
""")


start_time = time.perf_counter()

count=len(open(csv_file_path).readlines())
df = pd.read_csv(csv_file_path, skiprows=range(2,count-1), header=0)

print(df)

end_time = time.perf_counter()

print(f'SKIPROWS TIME: {round(end_time-start_time,2)}s\n')

print("""
##################### TURBO #####################
# Read first and last line using read-csv-turbo #
#################################################
""")


start_time = time.perf_counter()

df = rct.read_csv_headtail(csv_file_path)
print(df)

end_time = time.perf_counter()

print(f'RAW TIME: {round(end_time-start_time,2)}s\n')