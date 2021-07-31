from dataclasses import dataclass


@dataclass
class EndpointConfig:
    endpoint_health_check_server: str = "/health_server"
    endpoint_children: str = "/children"
    endpoint_father: str = "/father"
    endpoint_database_create: str = "/databaseCreate"
    endpoint_database_delete: str = "/databaseDelete"
