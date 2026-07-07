@dataclass
class Host:
    ip: str
    hostname: str
    os: str
    ports: list[int]
    services: list[str]

# we can add other data structs like MAC addresses, vendor ID, ipv6, etc. later on.

@dataclass
class Scan:
    timestamp: datetime
    command: str
    hosts: list[Host]
