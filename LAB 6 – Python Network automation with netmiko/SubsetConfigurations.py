from netmiko import ConnectHandler

# Device parameters
device = {
    "device_type": "cisco_ios",
    "ip": "172.16.7.7",
    "username": "admin",
    "password": "administrator",
}

# Establish an SSH connection to the device
ssh = ConnectHandler(**device)

# Enable privileged EXEC mode
ssh.enable()

# Enter global configuration mode
ssh.config_mode()

# Subset of interface configuration commands
config_commands = [
    'interface FastEthernet0/4',
    'description Pc Clients',
    'no shutdown',
    'interface FastEthernet0/5',
    'description PC Clients',
    'no shutdown'
]

# Send the configuration commands to the device
output = ssh.send_config_set(config_commands)
print(output)

# Disconnect from the device
print('Closing Connection')
ssh.disconnect()

