#!/bin/bash

# Define a function
greet() {
    echo "Hello, $1! Welcome to DevOps."
}

# Call the function
greet "Hanzala"
greet "Ali"

# Function with return/exit code
check_file() {
    if [ -f "$1" ]; then
        echo "File $1 exists."
        return 0
    else
        echo "File $1 does not exist."
        return 1
    fi
}

check_file "hello.sh"
check_file "missing.txt"

echo "Last exit code: $?"
