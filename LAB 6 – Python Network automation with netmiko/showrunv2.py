from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '172.16.7.1',
    'username': 'admin',
    'password': 'cisco123',
    'port' : 22,          # optioneel, standaardpoort is 22
}

net_connect = ConnectHandler(**cisco_881)

# Verkrijg de prompt
prompt = net_connect.find_prompt()
print(prompt)

# Voer het commando uit
output = net_connect.send_command('show running-config', expect_string=prompt)
print(output)

# Sluit de verbinding
net_connect.disconnect()

