ReTextPortable
==============
This repository contains configuration files for creating a PortableApps
version of ReText for Windows.

Following the steps in this document you can get ReText up and running
on your machine and optionally create an installer that you can easily
take with you.


Creating a PortableApps version of ReText
-----------------------------------------

1. Get the [ReTextPortable files][1] from github.com and put them in a
   directory called `ReTextPortable`
2. Install the [portableapps.com launcher][2] from portableapps.com
3. Install [NSIS Portable (unicode version)][3] in a sibling directory of 
   the PortableApps.com Launcher as NSISPortable
4. Extract the [64-bit Windows embeddable package][4] from python.org into
   `ReTextPortable\App\python`
5. Edit the file named similarly to `python312._pth` and uncomment the line `import site` 
6. Download [get-pip.py][5] into
   `ReTextPortable\App\python`
7. From a command prompt go to the python directory and run get-pip:

        cd ReTextPortable\App\python
        python get-pip.py
        
8. In the same command window install retext and all its dependencies using pip:

        python -m pip install retext
        python -m pip install PyQt6-WebEngine

12. Run the portable apps launcher generator on the `ReTextPortable` directory
    to create `ReTextPortable.exe`
13. Run `ReTextPortable.exe` to start ReText


[1]: https://github.com/Griffon26/ReTextPortable
[2]: http://portableapps.com/apps/development/portableapps.com_launcher
[3]: http://portableapps.com/apps/development/nsis_portable
[4]: https://www.python.org/downloads/windows/
[5]: https://bootstrap.pypa.io/get-pip.py


Using the latest versions from github
-------------------------------------

TBD



Creating an installer for ReTextPortable
----------------------------------------

If you want you can also package the application created in the previous
section in a single executable.

1. Install the [portableapps.com installer][6] from portableapps.com
2. Run the portable apps installer generator on the `ReTextPortable` directory
   to create `ReTextPortable_8.0.1.paf.exe`, which will be stored next to the
   `ReTextPortable` directory.

[6]: http://portableapps.com/apps/development/portableapps.com_installer

