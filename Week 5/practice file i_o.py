# Python File I/O

'''Writing to a new file that doesn't exist.'''

myfile = open("file.txt", "w")
myfile.write("This is my first File I/O practice session.\nI am so delighted about it.")

myfile.close()

'''Appending newlines to the "text.txt" file i just created.'''

myfile = open("file.txt", "a")
myfile.writelines(["\nIn this session, i'm appending newline to the text file i created initially.\n", "I'm also writing newlines in a list to my text file.\n"])

myfile.close()

'''Reading the content of "myfile" on read mode "r"'''
myfile = open("file.txt", "r")
text = myfile.read()
print(text)

myfile.close()

'''Using the "with" statement on write mode "w" to write to "myfile"'''

with open("file.txt", "w") as paul:
    paul.write("This is another session of learning.\n")
    paul.write("In conuation with the lessons on file I/O\ni'm learning how to write to my file using the 'with' keyword.\n")

'''Using the "with" statement on read mode "r" to read my file'''

with open("file.txt", "r") as paul:
    text = paul.read()
    print(text)

'''
The best way to close a file is by using the with statement. 
This ensures that the file is closed when the block inside the with statement is exited.

We don't need to explicitly call the close() method. It is done internally.
'''
# Try and Finally Statement
'''Using the "try" and "finally" statement to perform operations on a file'''
try:
    f = open("file.txt")
    rd = f.read()
    print(rd)
finally:
    f.close()

# File Methods and Description.
'''
   Method	-                   Description

1. close() - Closes an opened file. It has no effect if the file is already closed.

2. detach() - Separates the underlying binary buffer from the TextIOBase and returns it.

3. fileno()	- Returns an integer number (file descriptor) of the file.

4. flush() - Flushes the write buffer of the file stream.

5. isatty() - Returns True if the file stream is interactive.

6. read(n) - Reads at most n characters from the file. Reads till end of file if it is negative or None.

7. readable() - Returns True if the file stream can be read from.

8. readline(n=-1) - Reads and returns one line from the file. Reads in at most n bytes if specified.

9. readlines(n=-1) - Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.

10. seek(offset,from=SEEK_SET) - Changes the file position to offset bytes, in reference to from (start, current, end).

11. seekable() - Returns True if the file stream supports random access.

12. tell() - Returns the current file location.

13. truncate(size=None) - Resizes the file stream to size bytes. If size is not specified, resizes to current location.

14. writable() - Returns True if the file stream can be written to.

15. write(s) - Writes the string s to the file and returns the number of characters written.

16. writelines(lines) - Writes a list of lines to the file.
'''