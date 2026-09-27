def greet(name):
    print("Hello", name, "- Welcome to Python for DevOps")

def add(a, b):
    return a + b

def server_status(name, status="running"):
    print(f"Server {name} is currently {status}")

# Calling functions
greet("Hanzala")
greet("Ali")

result = add(10, 25)
print("Sum is:", result)

server_status("web-01")
server_status("db-01", "stopped")
