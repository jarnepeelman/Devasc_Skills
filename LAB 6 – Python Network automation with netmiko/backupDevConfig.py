from netmiko import ConnectHandler

# Define device parameters
device = {
    "device_type": "cisco_ios",
    "ip": "172.16.7.1",
    "username": "admin",
    "password": "cisco123",
}

# Establish SSH connection to device
ssh = ConnectHandler(**device)

# Send command to capture configuration
output = ssh.send_command("show running-config")

# Save output to file
with open("backup.cfg", "w") as file:
    file.write(output)

# Close SSH connection
ssh.disconnect()

