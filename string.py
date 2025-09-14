a ="20"
b = "25"

print(a+b)

# translate()
# Replace the String
table = str.maketrans("abc", "123")
text = "abcxyz"
print(text.translate(table))   # ➝ "123xyz"

# Remove the String
table = str.maketrans("", "", "aeiou")  # Remove vowels
text = "beautiful"
print(text.translate(table))   # ➝ "btfl"

# isalpha() function

print("hello".isalpha())      # ✅ True
print("HelloWorld".isalpha()) # ✅ True
print("hello123".isalpha())   # ❌ False (contains digits)
print("hello world".isalpha())# ❌ False (contains space)
print("".isalpha())           # ❌ False (empty string)

# count()
text = "banana"

print(text.count("a"))       # ➝ 3
print(text.count("an"))      # ➝ 2
print(text.count("na"))      # ➝ 2
print(text.count("n", 2))    # ➝ 1 (starts from index 2)

# find()
text = "Hello, world!"

print(text.find("world"))    # ➝ 7
print(text.find("Python"))   # ➝ -1 (not found)
print(text.find("o"))        # ➝ 4 (first 'o')
print(text.find("o", 5))     # ➝ 8 (second 'o', starts at index 5)


# title() method
text = "python is fun"
print(text.title())  # Output: "Python Is Fun"

# startswith() function
text = "Python is powerful"

print(text.startswith("Python"))     # ✅ True
print(text.startswith("python"))     # ❌ False (case-sensitive)
print(text.startswith("is", 7))      # ✅ True (starts from index 7)
print(text.startswith(("Py", "Java")))  # ✅ True (matches "Py")


# repr() function
text = 'hello\nworld'

print(str(text))   # Output: hello
                   #         world
print(repr(text))  # Output: 'hello\nworld'

