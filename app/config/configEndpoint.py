from dataclasses import dataclass


@dataclass
class ConfigurationEndpoint:
    endpoint_health_check_server: str = "/health_server"
    endpoint_children: str = "/children"
    endpoint_father: str = "/father"
    endpoint_database: str = "/database"
