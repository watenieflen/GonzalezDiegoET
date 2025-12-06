import json
import requests
requests.packages.urllib3.disable_warnings()

router_ip = "192.168.56.4"
api_url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback55"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback55",
        "description": "Diego Gonzalez - Creada con Python", 
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.55.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

print("--- Enviando solicitud PUT para crear Loopback55 ---")

try:
    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
    )

    if resp.status_code >= 200 and resp.status_code <= 299:
        print(f"¡ÉXITO! Código de estado: {resp.status_code}")
        print("La interfaz Loopback55 ha sido creada correctamente.")
    else:
        print(f"FALLO. Código de estado: {resp.status_code}")
        print(f"Mensaje de error: {resp.text}")

except Exception as e:
    print(f"Ocurrió un error de conexión: {e}")