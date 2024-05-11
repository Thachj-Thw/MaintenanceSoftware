import subprocess
import os
import tempfile
from dataclasses import dataclass



@dataclass
class CleanStruct:
    filepath: str
    filename: str
    message: str
    size: int


def clean_temp():
    temp_dir = tempfile.gettempdir()
    return __clean_dir(temp_dir)


def clean_prefetch():
    prefetch_dir = r"C:\Windows\Prefetch"
    return __clean_dir(prefetch_dir)


def clean_recent():
    recent_dir = os.path.join(r"C:\Users", os.getlogin(), "Recent")
    print(recent_dir)
    return __clean_dir(recent_dir)


def __total_size(folder: str):
    total = 0
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            total += os.path.getsize(f)
        else:
            total += __total_size(f)
    return total


def __clean_dir(folder: str):
    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            file_size = os.stat(path).st_size
            p = subprocess.Popen(f'del "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode(), file_size)
        elif os.path.isdir(path):
            file_size = __total_size(path)
            p = subprocess.Popen(f'rmdir "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode(), file_size)