import logging
import os
import tarfile
import urllib.request
from io import BytesIO
from os.path import basename, join
from pathlib import Path


def bundle_icons():
	icons_tgz = 'https://github.com/retext-project/retext/archive/icons.tar.gz'
	response = urllib.request.urlopen(icons_tgz)
	tario = BytesIO(response.read())
	tar = tarfile.open(fileobj=tario, mode='r')
	for member in tar:
		if member.isfile():
			member.path = basename(member.path)
			logging.info('bundling ReText/icons/%s', member.path)
			tar.extract(member, join('ReText', 'icons'))
	tar.close()


if __name__ == '__main__':
    os.chdir(Path(__file__).parent/'Lib/site-packages')
    bundle_icons()
