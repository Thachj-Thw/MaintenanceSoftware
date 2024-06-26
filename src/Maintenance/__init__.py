from . import wmic
from . import clean
from dataclasses import dataclass
import win32com.client
import os



@dataclass
class DiskInfoStruct():
    name: str
    caption: str
    status: str


def get_all_disk() -> list[DiskInfoStruct]:

    def get_device_id(text: str) -> str:
        return text.split('"')[-2]
    
    result = []
    logicals = []
    logical_partition = wmic.logical_disk_to_partition()
    drive_partition = wmic.disk_drive_to_partition()
    for logical in logical_partition:
        for drive in drive_partition:
            if get_device_id(logical.Antecedent) == get_device_id(drive.Dependent):
                logicals.append({
                    "logical": get_device_id(logical.Dependent),
                    "drive": get_device_id(drive.Antecedent)
                })
                break
    disk_drive = wmic.disk_drive()
    for drive in disk_drive:
        name = "Disk " + str(drive.Index) + " ("
        first = True
        for logical in logicals:
            if drive.DeviceID == logical["drive"]:
                if first:
                    name += logical["logical"]
                    first = False
                else:
                    name += " " + logical["logical"]
        name += ")"
        result.append(DiskInfoStruct(name, drive.Caption, drive.Status))
    return result


def to_TB(B: int) -> float:
    return round(B / 1024**4, 2)

def to_GB(B: int) -> float:
    return round(B / 1024**3, 2)

def to_MB(B: int) -> float:
    return round(B / 1024**2, 2)

def to_KB(B: int) -> float:
    return round(B / 1024, 2)

def auto_format(B: int) -> str:
    if B >= 1024**4:
        return str(to_TB(B)) + " TB"
    if B >= 1024**3:
        return str(to_GB(B)) + " GB"
    if B >= 1024**2:
        return str(to_MB(B)) + " MB"
    if B >=1024:
        return str(to_KB(B)) + " KB"
    return str(B) + " Bytes"

def detect_car_parking_folder() -> str:
    all_name = (
        "PMS.lnk",
        "HTParking.lnk",
        "PMS.exe - Shortcut.lnk",
        "HTParking.exe - Shortcut.lnk"
    )
    shell = win32com.client.Dispatch("WScript.Shell")
    for name in all_name:
        shortcut1 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', name)
        shortcut2 = os.path.join('C:', os.sep, 'Users', 'Public', 'Desktop', name)
        if os.path.exists(shortcut1):
            return os.path.dirname(shell.CreateShortCut(shortcut1).Targetpath)
        if os.path.exists(shortcut2):
            return os.path.dirname(shell.CreateShortCut(shortcut2).Targetpath)
    return ""
