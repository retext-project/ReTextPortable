ReTextPortable
==============
This repository contains configuration files for creating a PortableApps
version of ReText for Windows.

Following the steps in this document you can get ReText up and running
on your machine and optionally create an installer that you can easily
take with you.

Creating a PortableApps version of ReText
-----------------------------------------

1. Install the [portableapps.com launcher][1] from portableapps.com
2. Install [NSIS Portable (unicode version)][2] in a sibling directory
3. Install [`python-3.4.4.amd64.msi`][3] from python.org into `ReTextPortable\App\python`  
   (you can exclude tcl/tk, Documentation and the Test suite)
4. Install [`PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x64.exe`][4] from riverbankcomputing.com
   into `ReTextPortable\App\python`  
   (the "Minimal" install will suffice)
5. Get the [ReText source code][5], either using git or downloading a zip file from github.com
6. Store the source code in `ReTextPortable\App\retext`  
   (if you download a zip file you can extract it to the `App` dir and rename `retext-<branch>` to `retext`)
7. Get the [pymarkups source code][6], either using git or downloading a zip file from github.com
8. Store the source code in `ReTextPortable\App\retext`  
   (if you download a zip file you can extract it to the `App` dir and rename `retext-<branch>` to `retext`)
9. Install ReText's remaining python dependencies:

        cd ReTextPortable\App\python
        python -m pip install docutils
        python -m pip install markdown
        python -m pip install pyenchant
        python -m pip install pygments

10. Run the portable apps launcher generator on the `ReTextPortable` directory to create `ReTextPortable.exe`
11. Run `ReTextPortable.exe` to start ReText


[1]: http://portableapps.com/apps/development/portableapps.com_launcher
[2]: http://portableapps.com/apps/development/nsis_portable
[3]: https://www.python.org/downloads/windows/
[4]: https://www.riverbankcomputing.com/software/pyqt/download5
[5]: https://github.com/retext-project/retext
[6]: https://github.com/retext-project/pymarkups


Creating an installer for ReTextPortable
----------------------------------------

If you want you can also package the application created in the previous section in a single executable.

1. Install the [portableapps.com installer][7] from portableapps.com
2. Run the portable apps installer generator on the `ReTextPortable` directory
   to create `ReTextPortable_5.2.1.paf.exe`, which will be stored next to the
   `ReTextPortable` directory.

[7]: http://portableapps.com/apps/development/portableapps.com_installer
