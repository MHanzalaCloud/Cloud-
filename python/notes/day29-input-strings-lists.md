**Day 28 confirmed.** Perfect start with Python.

You have:
- Python 3.12.3 installed
- First script working
- Variables and data types understood

---

### Week 6 – Day 29 (Today) – Python Input, Strings & Lists

**Goal**  
Learn how to take user input, work with strings, and use lists.

#### Exact tasks for today

1. Go to the labs folder:

```bash
cd ~/projects/devops/python/labs
```

2. **User Input practice:**

```bash
nano input.py
```

Write:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("You are", age, "years old")
print(type(age))          # age is string by default

age = int(age)            # convert to integer
print("Next year you will be", age + 1)
```

Run it:

```bash
python3 input.py
```

3. **Strings practice:**

```bash
nano strings.py
```

Write:

```python
text = "  AWS Solutions Architect  "

print(text)
print(text.strip())           # remove spaces
print(text.lower())
print(text.upper())
print(text.replace("AWS", "Amazon Web Services"))
print(len(text))
print(text[0:5])              # slicing
```

Run it:

```bash
python3 strings.py
```

4. **Lists practice:**

```bash
nano lists.py
```

Write:

```python
fruits = ["apple", "banana", "mango", "orange"]

print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("grape")
print(fruits)

fruits.remove("banana")
print(fruits)

print(len(fruits))

for fruit in fruits:
    print("I like", fruit)
```

Run it:

```bash
python3 lists.py
```

5. Write notes:

```bash
cd ~/projects/devops/python/notes
nano day29-input-strings-lists.md
```

#### End-of-Day Checkpoint
When finished, reply with:

**“Day 29 done”**

and paste the output of:

```bash
python3 lists.py
```

Continue.
