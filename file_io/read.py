f = open("file_io/albums.txt")
f.read()
f.seek(1)
f.read()
f
f.seek(0)
f.read()
f.seek(23)
f.read()

f.readline()
f.readlines()
f.close()