from os import path
pkg_dir_path = path.dirname(path.realpath(__file__))
pkg_dir = path.basename(pkg_dir_path)

def read(fname):
    fname = path.join(path.dirname(__file__), fname)
    return open(fname).read()

from distutils.core import setup

setup(
    name = pkg_dir,
    version = "1.0",
    author = "CASH Productions",
    author_email = "support@cash-productions.com",
    description = ("Generic __index__.py generator"),
    long_description = read("README.rst"),
    license = "GPL v2",
    keywords = "package module loader init",
    url = "https://github.com/camilin87/pkgtools",
    package_data={'forecastio': ['LICENSE.txt', 'README.rst']},
    packages = [pkg_dir + ".modules"]
)
