from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in eventcheckin/__init__.py
from eventcheckin import __version__ as version

setup(
	name="eventcheckin",
	version=version,
	description="This app allows to do checkin on Events",
	author="Aadhil",
	author_email="aadhilpm.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
