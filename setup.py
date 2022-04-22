from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'Improved method for reading the first/last/specific line from csv into a DataFrame'
LONG_DESCRIPTION = """Improved method for reading the first/last/specific line from csv into a DataFrame

Ever deal with multiple huge csv files and and the panads `read_csv/skiprows` method is slowing you down? You are not alone.

read-csv-turbo is an improved method of reading the first and last lines using unix `head` and `tail` commands to get the data you want in a dataframe as fast as possible. I may include Windows support in the future if requested.

Reading a large csv once is "fine" but often I find myself looping through many files and this process is painfully slow which is why StackOverflow suggestions didn't cut it. There may be a newer/smarter way of approaching this but this method should be as fast as you could get. 

At the moment the use case of this is quite limited as it just provides a fast way to read the `first`, `last` or `n` row of a csv into a dataframe

github: https://github.com/donjor/read-csv-turbo
"""

# Setting up
setup(
        name="readcsvturbo", 
        version=VERSION,
        author="Donjor",
        author_email="donjordev@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas"],
        url="https://github.com/donjor/read-csv-turbo",

        keywords=['python', 'pandas', 'readcsv', 'readfirstlinecsv', 'readlastlinecsv', 'readspecificlinecsv'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
        ]
)