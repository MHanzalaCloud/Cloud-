print("=== For Loop ===")
for i in range(1, 6):
    print("Number:", i)

print("\n=== While Loop ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n=== Loop through list ===")
servers = ["web1", "web2", "db1", "cache1"]
for server in servers:
    print("Checking server:", server)
