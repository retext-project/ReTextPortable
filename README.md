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
3. Install [NSIS Portable (unicode version)][3] in a sibling directory
4. Install [`python-3.4.4.msi`][4] from python.org into
   `ReTextPortable\App\python`  
   (you can exclude tcl/tk, Documentation and the Test suite)
5. Install [`PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x32.exe`][5] from
   riverbankcomputing.com into `ReTextPortable\App\python`  
   (the "Minimal" install will suffice)
6. Get the [ReText source code][6], either using git or downloading a zip file
   from github.com
7. Store the source code in `ReTextPortable\App\retext`  
   (if you download a zip file you can extract it to the `App` dir and rename
   `retext-<branch>` to `retext`)
8. Get the [pymarkups source code][7], either using git or downloading a zip
   file from github.com
9. Store the source code in `ReTextPortable\App\pymarkups`  
   (if you download a zip file you can extract it to the `App` dir and rename
   `pymarkups-<branch>` to `pymarkups`)
10. Install ReText's remaining python dependencies as well as a backport of
    socketpair:

        cd ReTextPortable\App\python
        python -m pip install docutils
        python -m pip install markdown
        python -m pip install pyenchant
        python -m pip install pygments
        python -m pip install backports.socketpair

11. Copy the icons from `App\ReTextIcons` into `App\retext\icons`
12. Run the portable apps launcher generator on the `ReTextPortable` directory
    to create `ReTextPortable.exe`
13. Run `ReTextPortable.exe` to start ReText

[1]: https://github.com/Griffon26/ReTextPortable
[2]: http://portableapps.com/apps/development/portableapps.com_launcher
[3]: http://portableapps.com/apps/development/nsis_portable
[4]: https://www.python.org/downloads/windows/
[5]: https://www.riverbankcomputing.com/software/pyqt/download5
[6]: https://github.com/retext-project/retext
[7]: https://github.com/retext-project/pymarkups

### A note on creating a 64-bit version

Instead of installing 32-bit versions of Python and PyQt5 you can also use the
64-bit versions. Unfortunately this will disable the spell checker in ReText,
because pyenchant only provides the necessary plugin DLLs on 32-bit
installations of Python.

Creating an installer for ReTextPortable
----------------------------------------

If you want you can also package the application created in the previous
section in a single executable.

1. Install the [portableapps.com installer][8] from portableapps.com
2. Run the portable apps installer generator on the `ReTextPortable` directory
   to create `ReTextPortable_5.2.1.paf.exe`, which will be stored next to the
   `ReTextPortable` directory.

[8]: http://portableapps.com/apps/development/portableapps.com_installer

