import subprocess
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
    Index: str
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
    Size: str
    StartingOffset: str
    Status: str
    StatusInfo: str
    SystemCreationClassName: str
    SystemName: str
    TotalPowerOnHours: str
    Type: str

    def get_size_GB(self) -> float:
        return to_GB(int(self.Size))


@dataclass
class LogicalDisk:
    Access: str
    Availability: str
    BlockSize: str
    Caption: str
    Compressed: str
    ConfigManagerErrorCode: str
    ConfigManagerUserConfig: str
    CreationClassName: str
    Description: str
    DeviceID: str
    DriveType: str
    ErrorCleared: str
    ErrorDescription: str
    ErrorMethodology: str
    FileSystem: str
    FreeSpace: str
    InstallDate: str
    LastErrorCode: str
    MaximumComponentLength: str
    MediaType: str
    Name: str
    NumberOfBlocks: str
    PNPDeviceID: str
    PowerManagementCapabilities: str
    PowerManagementSupported: str
    ProviderName: str
    Purpose: str
    QuotasDisabled: str
    QuotasIncomplete: str
    QuotasRebuilding: str
    Size: str
    Status: str
    StatusInfo: str
    SupportsDiskQuotas: str
    SupportsFileBasedCompression: str
    SystemCreationClassName: str
    SystemName: str
    VolumeDirty: str
    VolumeName: str
    VolumeSerialNumber: str

    def get_size_GB(self) -> float:
            return to_GB(int(self.Size))


@dataclass
class DiskDrive:
    Availability: str
    BytesPerSector: str
    Capabilities: str
    CapabilityDescriptions: str
    Caption: str
    CompressionMethod: str
    ConfigManagerErrorCode: str
    ConfigManagerUserConfig: str
    CreationClassName: str
    DefaultBlockSize: str
    Description: str
    DeviceID: str
    ErrorCleared: str
    ErrorDescription: str
    ErrorMethodology: str
    FirmwareRevision: str
    Index: str
    InstallDate: str
    InterfaceType: str
    LastErrorCode: str
    Manufacturer: str
    MaxBlockSize: str
    MaxMediaSize: str
    MediaLoaded: str
    MediaType: str
    MinBlockSize: str
    Model: str
    Name: str
    NeedsCleaning: str
    NumberOfMediaSupported: str
    Partitions: str
    PNPDeviceID: str
    PowerManagementCapabilities: str
    PowerManagementSupported: str
    SCSIBus: str
    SCSILogicalUnit: str
    SCSIPort: str
    SCSITargetId: str
    SectorsPerTrack: str
    SerialNumber: str
    Signature: str
    Size: str
    Status: str
    StatusInfo: str
    SystemCreationClassName: str
    SystemName: str
    TotalCylinders: str
    TotalHeads: str
    TotalSectors: str
    TotalTracks: str
    TracksPerCylinder: str

    def get_size_GB(self) -> float:
            return to_GB(int(self.Size))


def Win32_DiskPartition():
    return __create_object_from_wmic(DiskPartition, "wmic path win32_diskpartition")


def Win32_LogicalDisk():
    return __create_object_from_wmic(LogicalDisk, "wmic logicaldisk")


def Win32_DiskDrive():
    return __create_object_from_wmic(DiskDrive, "wmic diskdrive")



def to_GB(B: int) -> float:
    return round(B / 1024**3, 2)


def __create_object_from_wmic(obj: object, cmd: str):
    obj_key = obj.__annotations__
    keys = []
    for key in obj_key:
        keys.append(" " + key + " ")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sources = p.communicate()[0].split(b"\r\r\n")[:-2]
    head = " " + sources[0].decode()
    index_value = []
    for key in keys:
        index = head.find(key)
        if index == 1:
            index -= 1
        index_value.append(index)
    number_args = len(index_value)
    result = []
    for source in sources[1:]:
        values = source.decode()
        value = ["" for _ in range(number_args)]
        for i, idx in enumerate(index_value):
            if idx >= 0:
                v = values[idx: values.find("  ", idx)]
                value[i] = v
        result.append(obj(*value))
    return result
