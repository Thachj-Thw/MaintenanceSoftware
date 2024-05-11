import subprocess
import os
import tempfile
from dataclasses import dataclass



@dataclass
class CleanStruct:
    filepath: str
    filename: str
    message: str


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


def __clean_dir(folder: str):
    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            p = subprocess.Popen(f'del "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode())
        elif os.path.isdir(path):
            p = subprocess.Popen(f'rmdir "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode())