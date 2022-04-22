from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Improved method for reading the first/last/specific line from csv into a DataFrame'
LONG_DESCRIPTION = 'Improved method for reading the first/last/specific line from csv into a DataFrame'

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
        
        keywords=['python', 'pandas', 'readcsv', 'readfirstlinecsv', 'readlastlinecsv', 'readspecificlinecsv'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
        ]
)