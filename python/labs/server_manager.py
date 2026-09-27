servers = []

def add_server(name, ip):
    servers.append({"name": name, "ip": ip})
    print(f"Server {name} added.")

def list_servers():
    if not servers:
        print("No servers found.")
    else:
        print("\n=== Server List ===")
        for s in servers:
            print(f"Name: {s['name']} | IP: {s['ip']}")

# Testing
add_server("web-01", "192.168.1.10")
add_server("db-01", "192.168.1.20")
add_server("cache-01", "192.168.1.30")
list_servers()
