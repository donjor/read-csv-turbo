# read-csv-turbo
Ever deal with multiple huge csv files and and the panads `read_csv/skiprows` method is slowing you down? You are not alone.

read-csv-turbo is an improved method of reading the first and last lines using unix `head` and `tail` commands to get the data you want in a dataframe as fast as possible. I may include Windows support in the future if requested.

Reading a large csv once is "fine" but often I find myself looping through many files and this process is painfully slow which is why StackOverflow suggestions didn't cut it. There may be a newer/smarter way of approaching this but this method should be as fast as you could get. 

At the moment the use case of this is quite limited as it just provides a fast way to read the `first`, `last` or `n` row of a csv into a dataframe

## Installation
`pip install readcsvturbo`

## Usage
```
import pandas as pd
import readcsvturbo as rct

csv_file_path = Path("./big_csv.csv")

df_head = rct.read_csv_head(csv_file_path)
df_tail = rct.read_csv_tail(csv_file_path)
df_headtail = rct.read_csv_headtail(csv_file_path)
df_specific_line = rct.read_csv_line(csv_file_path)

# Can also specify if there are no headers in the csv file

df_head = rct.read_csv_head(csv_file_path, headers=False)
```

## Speed Test Results
```
RAW PANDAS TIME: 5.47s
SKIPROWS TIME:   3.04s (1.7x faster)
TURBO TIME:      0.25s (21.8x faster)
```

## Speed Test
Test completed with a csv file 609MB with 5,000,000 lines. Downloaded from https://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/ 

The `tests.py` script was run to produce this.
The test is reading the first and last lines of a csv file including the header.

```
############## RAW PANDAS ###############
# Read the whole file in using read_csv #
#########################################

                        Region Country  ...  Total Cost Total Profit
0        Australia and Oceania   Palau  ...  1260428.96    303126.25
4999999                 Europe  Greece  ...  2272551.84    546536.25

[2 rows x 14 columns]
RAW PANDAS TIME: 5.47s


################### SKIPROWS ##################
# Get the length of the file from readlines() #
# Read big_csv using skiprows                 #
###############################################

                  Region Country  ...  Total Cost Total Profit
0  Australia and Oceania   Palau  ...  1260428.96    303126.25
1                 Europe  Greece  ...  2272551.84    546536.25

[2 rows x 14 columns]
SKIPROWS TIME: 3.04s


##################### TURBO #####################
# Read first and last line using read-csv-turbo #
#################################################

                  Region Country  ...  Total Cost Total Profit
0  Australia and Oceania   Palau  ...  1260428.96    303126.25
1                 Europe  Greece  ...  2272551.84    546536.25

[2 rows x 14 columns]
TURBO TIME: 0.25s

```
