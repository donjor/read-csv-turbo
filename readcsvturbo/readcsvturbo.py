from tokenize import String
import pandas as pd
import subprocess
from io import StringIO

def csv_head(path, header):
    if header:
        csv_head = subprocess.check_output(f"sed -n '2p' {path}", shell=True).decode("utf-8").strip()
        return csv_head
    else:
        csv_head = subprocess.check_output(f"head -1 {path}", shell=True).decode("utf-8").strip()
        return csv_head

def csv_tail(path):
    csv_tail = subprocess.check_output(f"tail -1 {path}", shell=True).decode("utf-8").strip()
    return csv_tail

def csv_line(path, n):
    csv_line = subprocess.check_output(f"sed -n '{n}p' {path}", shell=True).decode("utf-8").strip()
    return csv_line

def read_csv_header(path):
    csv_header_str = subprocess.check_output(f"head -1 {path}", shell=True).decode("utf-8").strip()
    return csv_header_str

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
