import subprocess
import os
import tempfile
from dataclasses import dataclass
from typing import Generator, Any
import ctypes
from ctypes import windll


@dataclass
class CleanStruct:
    filepath: str
    filename: str
    message: str
    size: int
    isfile: bool


def clean_temp() -> Generator[CleanStruct, Any, Any]:
    temp_dir = tempfile.gettempdir()
    return __clean_dir(temp_dir)


def clean_prefetch() -> Generator[CleanStruct, Any, Any]:
    prefetch_dir = r"C:\Windows\Prefetch"
    return __clean_dir(prefetch_dir)


def clean_recent() -> Generator[CleanStruct, Any, Any]:
    code = windll.Shell32.SHAddToRecentDocs(1, None)
    if code == 0:
        yield CleanStruct("Recent", "Recent", "", 0, True)
    elif code < 0:
        yield CleanStruct("Recent", "Recent", "Recent Folder is Empty", 0, False)
    elif code > 0:
        yield CleanStruct("Recent", "Recent", "Unknow Error, clear failed", 0, False)


def __total_size(folder: str) -> int:
    total = 0
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            total += os.path.getsize(f)
        else:
            total += __total_size(f)
    return total


def __clean_dir(folder: str) -> Generator[CleanStruct, Any, Any]:
    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            file_size = os.stat(path).st_size
            p = subprocess.Popen(f'del "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode().rstrip("\r\n"), file_size, True)
        elif os.path.isdir(path):
            file_size = __total_size(path)
            p = subprocess.Popen(f'rmdir /s /q "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            yield CleanStruct(path, file, p.communicate()[-1].decode().rstrip("\r\n"), file_size, False)
        else:
            yield CleanStruct(path, file, "Unknow error", 0, False)


def clean_backup_database(folder: str) -> Generator[CleanStruct, Any, Any]:
    if not os.path.isdir(folder):
        yield CleanStruct(folder, folder, "Invalid BackupDatabase Folder", 0, False)
        return
    files = os.listdir(folder)
    current = files[0]
    current_path = os.path.join(folder, current)
    current_time = os.path.getctime(current_path)
    for file in files[1:]:
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            ctime = os.path.getctime(path)
            if ctime < current_time:
                file_size = os.stat(path).st_size
                p = subprocess.Popen(f'del "{path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                yield CleanStruct(path, file, p.communicate()[-1].decode().rstrip("\r\n"), file_size, True)
            else:
                file_size = os.stat(current_path).st_size
                p = subprocess.Popen(f'del "{current_path}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                yield CleanStruct(current_path, current, p.communicate()[-1].decode().rstrip("\r\n"), file_size, True)
                current = file
                current_path = path
                current_time = ctime
