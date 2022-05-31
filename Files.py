
f = open('data.txt', 'w') # Skapa fil i output mode, sparar i current dir ('w' = write, 'r' = read)
f.write('Hello\n')
f.write('world\n')
f.close() # Close to flush output buffers to disk

f = open('data.txt') # Öppna filen
text = f.read() # Lagra texten som läses av i variabel text
print(text) # Print variabel text som innehåller den avlästa texten

# Kan splitta texten i filen
text.split()

# Skriva text i en fil utan 
for line in open('data.txt'): print (line)

dir(f) # See all methods on file
help(f.seek) # See information about a method

# Binary Byte Files

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('data.bin', 'wb')
file.write(packed)
file.close()

# Reading binary data
data = open('data.bin', 'rb').read()
print(data)

# Går att slica
data[4:8]

list(data) # 115, 112, 97, 109 blir t.ex. spam i Ascii.

# Unpack till objekt igen
struct.unpack('>i4sh', data)

# UNICODE TEXT FILES
