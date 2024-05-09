import subprocess
import re
from dataclasses import dataclass


@dataclass
class DiskPartition:
    Access: str
    AdditionalAvailability: str
    Availability: str
    BlockSize: str
    Bootable: str
    BootPartition: str
    Caption: str
    ConfigManagerErrorCode: str
    ConfigManagerUserConfig: str
    CreationClassName: str
    Description: str
    DeviceID: str
    DiskIndex: str
    ErrorCleared: str
    ErrorDescription: str
    ErrorMethodology: str
    HiddenSectors: str
    IdentifyingDescriptions: str
    Index: int
    InstallDate: str
    LastErrorCode: str
    MaxQuiesceTime: str
    Name: str
    NumberOfBlocks: str
    OtherIdentifyingInfo: str
    PNPDeviceID: str
    PowerManagementCapabilities: str
    PowerManagementSupported: str
    PowerOnHours: str
    PrimaryPartition: str
    Purpose: str
    RewritePartition: str
    Size: int
    StartingOffset: str
    Status: str
    StatusInfo: str
    SystemCreationClassName: str
    SystemName: str
    TotalPowerOnHours: str
    Type: str

    @staticmethod
    def to_GB(B: int) -> float:
        return round(B / 1024**3, 2)


def Win32_DiskPartition():
    result = []
    p = subprocess.Popen("wmic path win32_diskpartition", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sources = p.communicate()[0].split(b"\r\r\n")[:-2]
    keys = (
        'Access', 'AdditionalAvailability', 'Availability', 'BlockSize', 'Bootable', 'BootPartition', 'Caption', 'ConfigManagerErrorCode', 
        'ConfigManagerUserConfig', 'CreationClassName', 'Description', 'DeviceID', 'DiskIndex', 'ErrorCleared', 'ErrorDescription', 'ErrorMethodology',
        'HiddenSectors', 'IdentifyingDescriptions', 'Index', 'InstallDate', 'LastErrorCode', 'MaxQuiesceTime', 'Name', 'NumberOfBlocks', 'OtherIdentifyingInfo',
        'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'PowerOnHours', 'PrimaryPartition', 'Purpose', 'RewritePartition', 'Size',
        'StartingOffset', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TotalPowerOnHours', 'Type'
    )
    head = sources[0].decode()
    index_value = []
    index = 0
    for key in keys:
        index = head.find(key)
        index_value.append(index)
        if index == -1:
            print(key)
    print(head)
    print(index_value)
    return result
    # for source in sources:
    #     result.append(DiskDrive(source.decode()))
    # return result


class LogicalDisk:
    def __init__(self, source):
        pass