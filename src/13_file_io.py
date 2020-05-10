"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open(r"C:\Users\chris\OneDrive\Documents\GitHub\Projects\Intro-Python-I\src\foo.txt", "r") as foo:
    all_lines = foo.readlines()
    print(all_lines)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
arbirtray_tuple = ("tick tock", "the clock goes", "bing boing!")

with open(r"C:\Users\chris\OneDrive\Documents\GitHub\Projects\Intro-Python-I\src\bar.txt", "w") as bar:
    for i in arbirtray_tuple:
        bar.write(i + ', ')

with open(r"C:\Users\chris\OneDrive\Documents\GitHub\Projects\Intro-Python-I\src\bar.txt", "r") as bar:
    all_lines = bar.readlines()
    print(all_lines)
