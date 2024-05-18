import subprocess
from dataclasses import dataclass



@dataclass
class Win32_DiskPartition:
    AdditionalAvailability: int
    Availability: int
    PowerManagementCapabilities: list[int]
    IdentifyingDescriptions: str
    MaxQuiesceTime: int
    OtherIdentifyingInfo: int
    StatusInfo: int
    PowerOnHours: int
    TotalPowerOnHours: int
    Access: int
    BlockSize: int
    Bootable: bool
    BootPartition: bool
    Caption: str
    ConfigManagerErrorCode: int
    ConfigManagerUserConfig: bool
    CreationClassName: str
    Description: str
    DeviceID: str
    DiskIndex: int
    ErrorCleared: bool
    ErrorDescription: str
    ErrorMethodology: str
    HiddenSectors: int
    Index: int
    InstallDate: str
    LastErrorCode: int
    Name: str
    NumberOfBlocks: int
    PNPDeviceID: str
    PowerManagementSupported: bool
    PrimaryPartition: bool
    Purpose: str
    RewritePartition: bool
    Size: int
    StartingOffset: int
    Status: str
    SystemCreationClassName: str
    SystemName: str
    Type: str


@dataclass
class Win32_LogicalDisk:
    Access: int
    Availability: int
    BlockSize: int
    Caption: str
    Compressed: bool
    ConfigManagerErrorCode: int
    ConfigManagerUserConfig: bool
    CreationClassName: str
    Description: str
    DeviceID: str
    DriveType: int
    ErrorCleared: bool
    ErrorDescription: str
    ErrorMethodology: str
    FileSystem: str
    FreeSpace: int
    InstallDate: str
    LastErrorCode: int
    MaximumComponentLength: int
    MediaTyp: int
    Name: str
    NumberOfBlocks: int
    PNPDeviceID: str
    PowerManagementCapabilities: list[int]
    PowerManagementSupported: bool
    ProviderName: str
    Purpose: str
    QuotasDisabled: bool
    QuotasIncomplete: bool
    QuotasRebuilding: bool
    Size: int
    Status: str
    StatusInfo: int
    SupportsDiskQuotas: bool
    SupportsFileBasedCompression: bool
    SystemCreationClassName: str
    SystemName: str
    VolumeDirty: bool
    VolumeName: str
    VolumeSerialNumber: str



@dataclass
class Win32_DiskDrive:
    Availability: int
    BytesPerSector: int
    Capabilities: list[int]
    CapabilityDescriptions: list[str]
    Caption: str
    CompressionMethod: str
    ConfigManagerErrorCode: int
    ConfigManagerUserConfig: bool
    CreationClassName: str
    DefaultBlockSize: int
    Description: str
    DeviceID: str
    ErrorCleared: bool
    ErrorDescription: str
    ErrorMethodology: str
    FirmwareRevision: str
    Index: int
    InstallDate: str
    InterfaceType: str
    LastErrorCode: int
    Manufacturer: str
    MaxBlockSize: int
    MaxMediaSize: int
    MediaLoaded: bool
    MediaType: str
    MinBlockSize: int
    Model: str
    Name: str
    NeedsCleaning: bool
    NumberOfMediaSupported: int
    Partitions: int
    PNPDeviceID: str
    PowerManagementCapabilities: list[int]
    PowerManagementSupported: bool
    SCSIBus: int
    SCSILogicalUnit: int
    SCSIPort: int
    SCSITargetId: int
    SectorsPerTrack: int
    SerialNumber: str
    Signature: int
    Size: int
    Status: str
    StatusInfo: int
    SystemCreationClassName: str
    SystemName: str
    TotalCylinders: int
    TotalHeads: int
    TotalSectors: int
    TotalTracks: int
    TracksPerCylinder: int


@dataclass
class Win32_LogicalDiskToPartition():
    EndingAddress: int
    StartingAddress: int
    Antecedent: str
    Dependent: str


@dataclass
class Win32_DiskDriveToDiskPartition():
    Antecedent: str
    Dependent: str


def disk_partition() -> list[Win32_DiskPartition]:
    return __create_object_from_wmic(Win32_DiskPartition, "wmic path win32_diskpartition")


def logical_disk() -> list[Win32_LogicalDisk]:
    return __create_object_from_wmic(Win32_LogicalDisk, "wmic logicaldisk")


def disk_drive() -> list[Win32_DiskDrive]:
    return __create_object_from_wmic(Win32_DiskDrive, "wmic diskdrive")


def logical_disk_to_partition() -> list[Win32_LogicalDiskToPartition]:
    return __create_object_from_wmic(Win32_LogicalDiskToPartition, "wmic path Win32_LogicalDiskToPartition")


def disk_drive_to_partition() -> list[Win32_DiskDriveToDiskPartition]:
    return __create_object_from_wmic(Win32_DiskDriveToDiskPartition, "wmic path Win32_DiskDriveToDiskPartition")


def __to_bool(value: str) -> (bool | None):
    if value == "TRUE":
        return True
    if value == "FALSE":
        return False
    return None


def __to_int(value: str) -> (int | None):
    if value.isnumeric():
        return int(value)
    return None


def __to_list_int(value: str) -> list[int]:
    if value:
        return [int(x) for x in value[1:-1].split(", ")]
    return []


def __to_list_str(value: str) -> list[str]:
    if value:
        return [x[1:-1] for x in value[1:-1].split(", ")]
    return []


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
        values = source.decode().replace("?", "??")
        value = ["" for _ in range(number_args)]
        for i, idx in enumerate(index_value):
            if idx >= 0:
                v = values[idx: values.find("  ", idx)]
                value_type = obj_key[keys[i][1:-1]]
                if  value_type is int:
                    v = __to_int(v)
                elif value_type is bool:
                    v = __to_bool(v)
                elif value_type == list[int]:
                    v = __to_list_int(v)
                elif value_type == list[str]:
                    v = __to_list_str(v)
                value[i] = v
        result.append(obj(*value))
    return result
