server = {
    "name": "web-server-01",
    "ip": "192.168.1.10",
    "os": "Ubuntu 24.04",
    "status": "running"
}

print(server)
print(server["name"])
print(server.get("ip"))

server["cpu"] = "4 vCPU"
server["status"] = "stopped"

print(server)

for key, value in server.items():
    print(key, "→", value)
