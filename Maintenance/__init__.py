from . import wmic
from . import clean
from dataclasses import dataclass



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
        result.append(DiskInfoStruct(name, drive.Caption, "Status\n" + drive.Status))
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
