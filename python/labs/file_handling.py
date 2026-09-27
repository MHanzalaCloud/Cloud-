# Writing to a file
with open("servers.txt", "w") as f:
    f.write("web-01\n")
    f.write("web-02\n")
    f.write("db-01\n")
    f.write("cache-01\n")

print("File written successfully!")

# Reading the file
print("\n=== Reading file ===")
with open("servers.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
print("=== Reading line by line ===")
with open("servers.txt", "r") as f:
    for line in f:
        print("Server:", line.strip())
