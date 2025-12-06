from netmiko import ConnectHandler

cisco1 = {
    "ip": "192.168.56.4", 
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

cmd_interfaces = "show ip interface brief"

cmd_config = "show running-config"

cmd_version = "show version"

commands_to_run = [cmd_interfaces, cmd_version, cmd_config]

print(f"--- Conectando a {cisco1['ip']} vía SSH ---")

try:
    with ConnectHandler(**cisco1) as net_connect:
        
        for command in commands_to_run:
            print(f"\n{'#'*20} EJECUTANDO: {command} {'#'*20}")
            
            output = net_connect.send_command(command)
            
            print(output)
            print("-" * 60)

    print("\n--- Tarea Completada Exitosamente ---")

except Exception as e:
    print(f"\n[!] Error de conexión: {e}")