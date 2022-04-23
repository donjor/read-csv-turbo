import pandas as pd
import subprocess
import platform
from io import StringIO

def csv_head(path, header):
    s = ""
    if header:
        if platform.system() == "Windows":
            s = f'powershell "gc {path} | Select -Index 1"'
        else:
            s = f"sed -n '2p' {path}"
    else:
        if platform.system() == "Windows":
            s = f"powershell gc {path} -head 1"
        else:
            s = f"head -1 {path}"
    
    return subprocess.check_output(s, shell=True).decode("utf-8").strip()    

def csv_tail(path):
    s = ""
    if platform.system() == "Windows":
        s = f"powershell gc {path} -tail 1"
    else:
        s = f"tail -1 {path}"

    return subprocess.check_output(s, shell=True).decode("utf-8").strip()  

def csv_line(path, n):
    s = ""
    if platform.system() == "Windows":
        s = f'powershell "gc {path} | Select -Index {n}"'
    else:
        s = f"sed -n '{n}p' {path}"

    return subprocess.check_output(s, shell=True).decode("utf-8").strip()

def read_csv_header(path):
    s = ""
    if platform.system() == "Windows":
        s = f"powershell gc {path} -head 1"
    else:
        s = f"head -1 {path}"
    return subprocess.check_output(s, shell=True).decode("utf-8").strip()

def read_csv_head(path, header=True):
    head = csv_head(path,header)

    if header:
        csv_header = read_csv_header(path)
        string_data = StringIO(f'{csv_header}\n{head}')
        df = pd.read_csv(string_data, sep=",")
        return df
    else:
        string_data = StringIO(f'{head}')
        df = pd.read_csv(string_data, sep=",", header=None)
        return df


def read_csv_tail(path, header=True):
    tail = csv_tail(path)

    if header:
        csv_header = read_csv_header(path)
        string_data = StringIO(f'{csv_header}\n{tail}')
        df = pd.read_csv(string_data, sep=",")
        return df
    else:
        string_data = StringIO(f'{tail}')
        df = pd.read_csv(string_data, sep=",", header=None)
        return df

def read_csv_headtail(path, header=True):
    head = csv_head(path,header)
    tail = csv_tail(path)

    if header:
        csv_header = read_csv_header(path)
        string_data = StringIO(f'{csv_header}\n{head}\n{tail}')
        df = pd.read_csv(string_data, sep=",")
        return df
    else:
        string_data = StringIO(f'{head}\n{tail}')
        df = pd.read_csv(string_data, sep=",", header=None)
        return df

def read_csv_line(path, n, header=True):
    line = csv_line(path, n)
    if header:
        csv_header = read_csv_header(path)
        string_data = StringIO(f'{csv_header}\n{line}')
        df = pd.read_csv(string_data, sep=",")
        return df
    else:
        string_data = StringIO(f'{line}')
        df = pd.read_csv(string_data, sep=",", header=None)
        return df
