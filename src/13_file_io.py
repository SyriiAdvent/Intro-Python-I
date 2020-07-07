"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt', mode="r") as f:
  print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'a') as f:
  f.write("I am line 1 \n")
  f.write("I am line 2 \n")
  f.write("I am line 3 \n")


# Using python to create python script files!

with open('bar.py', 'a') as f:
  f.write("for ltr in 'Tuna ate the goldfish!':")
  f.write(f"\n \t print(ltr)")