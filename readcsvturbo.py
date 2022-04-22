import pandas as pd
import subprocess

def csv_head(path, header):
    if header:
        csv_head = subprocess.check_output(f"sed -n '2p' {path}", shell=True).decode("utf-8").replace("\n","")
        csv_head_list = csv_head.split(",")
        return csv_head_list
    else:
        csv_head = subprocess.check_output(f"head -1 {path}", shell=True).decode("utf-8").replace("\n","")
        csv_head_list = csv_head.split(",")
        return csv_head_list

def csv_tail(path):
    csv_tail = subprocess.check_output(f"tail -1 {path}", shell=True).decode("utf-8").replace("\n","")
    csv_tail_list = csv_tail.split(",")
    return csv_tail_list

def csv_line(path, n):
    csv_line = subprocess.check_output(f"sed -n '{n}p' {path}", shell=True).decode("utf-8").replace("\n","")
    csv_line_list = csv_line.split(",")
    return csv_line_list

def read_csv_header(path):
    csv_header_str = subprocess.check_output(f"head -1 {path}", shell=True).decode("utf-8").replace("\n","")
    csv_header = csv_header_str.split(",")
    return csv_header

def read_csv_head(path, header=True):
    head = csv_head(path,header)

    if header:
        csv_header = read_csv_header(path)
        df = pd.DataFrame([head], columns=csv_header)
        return df
    else:
        df = pd.DataFrame([head])
        return df

def read_csv_tail(path, header=True):
    tail = csv_tail(path)

    if header:
        csv_header = read_csv_header(path)
        df = pd.DataFrame([tail], columns=csv_header)
        return df
    else:
        df = pd.DataFrame([tail])
        return df

def read_csv_headtail(path, header=True):
    #tail
    head = csv_head(path,header)
    tail = csv_tail(path)

    if header:
        csv_header = read_csv_header(path)
        df = pd.DataFrame([head,tail], columns=csv_header)
        return df
    else:
        df = pd.DataFrame([head,tail])
        return df

def read_csv_line(path, n, header=True):
    line = csv_line(path, n)
    if header:
        csv_header = read_csv_header(path)
        df = pd.DataFrame([line], columns=csv_header)
        return df
    else:
        df = pd.DataFrame([line])
        return df 
