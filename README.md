# fhash
Simple tool to generate files hashes (MD5, SHA1, SHA256, SHA512).   Good for incident response, research or just a tool to verify downloads.

Warning - this really is a simple tool.  There are no fail-safes programmed in.  The tool just takes a single file for a command-line argument and gives you the MD5, SHA1, SHA256, and SHA512 sums.  This is useful when using an application white-listing tool, during incident response, or just for a quick command line tool to verify downloads.

The zip file contains a version compiled for Windows.  If you want to use this my suggestion is to unzip to somewhere consistent, such as C:\Program File (x86)\.  Then make sure to add the location to your PATH environment variable.  Otherwise, Windows will not know where to find it and it won't be globally available to you.

For the Python version you only need fhash.py.  If you want to compile for Windows yourself using py2exe, grab the setup.py and compile using Python 2.7 with:

`python.exe setup.py install py2exe`



##Usage



###Python
*Note: Programmed with Python 2.7*

`python fhash.py <filename>`




###Windows Compiled version
*Assumes you have set PATH correctly*

`fhash <filename>`

**Sample Output:**

```
C:\Users\me\Downloads>fhash shodan.pdf

fhash - version 1.0
By James Wright



File inspected: shodan.pdf

MD5:     102206a269bceedb00c4d287c6b66689
SHA1:    07036728ce58cda163682e3c78f7aa12cae80c79
SHA256:  0aafcf347479f6c20b856b13df39c941a0f67fd52a0dc2a1bb5e087dc4c466b5
SHA512:  0b1d3bab80e2b3d3870f3af70a73fd9772dba54f2ae93c995a32ade3939bed9cfb1914bcb4c078fa962d6e482758b0213d0ce93e90cb43b50917aa14cbed213a

C:\Users\me\Downloads>
```

