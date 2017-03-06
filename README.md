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


