from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in epcqrcode/__init__.py
from epcqrcode import __version__ as version

setup(
	name="epcqrcode",
	version=version,
	description="An EPC-QRCode generator for creating QRCodes, e.g., on sales invoices.",
	author="4metrics",
	author_email="office@4metrics.at",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
