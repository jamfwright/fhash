import hashlib
import sys

def md5(fname):
    file_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            file_md5.update(chunk)
    return file_md5.hexdigest()

def sha1(fname):
    file_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            file_sha1.update(chunk)
    return file_sha1.hexdigest()

def sha256(fname):
    file_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            file_sha256.update(chunk)
    return file_sha256.hexdigest()

def sha512(fname):
    file_sha512 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            file_sha512.update(chunk)
    return file_sha512.hexdigest()


print("\nfhash - version 1.0\nBy James Wright\n")

if sys.argv < 2:
    print("\nMissing filename!\n\nUsage:  fhash <filename>")


inspect_file = sys.argv[1]
print("\n\nFile inspected: " + inspect_file + "\n")

file_md5 = md5(inspect_file)
print("MD5:     " + file_md5)

file_sha1 = sha1(inspect_file)
print("SHA1:    " + file_sha1)

file_sha256 = sha256(inspect_file)
print("SHA256:  " + file_sha256)

file_sha512 = sha512(inspect_file)
print("SHA512:  " + file_sha512)

