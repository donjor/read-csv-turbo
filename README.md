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
RAW PANDAS TIME: 1.15s
SKIPROWS TIME:   0.44s (2.6x faster)
TURBO TIME:      0.06s (19x faster)
```

## Speed Test
Test completed with a csv file 128mb. The `tests.py` script was run to produce this.
The test is reading the first and last lines of a csv file including the header.

```
############## RAW PANDAS ###############
# Read the whole file in using read_csv #
#########################################

       ticker   tradeDate  ... snapShotEstTime          snapShotDate
0        AMZN  2020-08-07  ...             931  2020-08-07T13:31:02Z
344104   AMZN  2020-08-07  ...            1600  2020-08-07T20:00:01Z

[2 rows x 45 columns]
RAW PANDAS TIME: 1.15s


################### SKIPROWS ##################
# Get the length of the file from readlines() #
# Read big_csv using skiprows                 #
###############################################

  ticker   tradeDate  ... snapShotEstTime          snapShotDate
0   AMZN  2020-08-07  ...             931  2020-08-07T13:31:02Z
1   AMZN  2020-08-07  ...            1600  2020-08-07T20:00:01Z

[2 rows x 45 columns]
SKIPROWS TIME: 0.44s


##################### TURBO #####################
# Read first and last line using read-csv-turbo #
#################################################

  ticker   tradeDate  ... snapShotEstTime          snapShotDate
0   AMZN  2020-08-07  ...            0931  2020-08-07T13:31:02Z
1   AMZN  2020-08-07  ...            1600  2020-08-07T20:00:01Z

[2 rows x 45 columns]
TURBO TIME: 0.06s

```
