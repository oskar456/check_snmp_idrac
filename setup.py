from setuptools import setup
import sys
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='check_snmp_idrac',
      version='0.0.1',
      description='Health monitoring of Dell iDrac',
      url='',
      author='Ondřej Caletka',
      author_email='ondrej@caletka.cz',
      license='GPLv2',
      classifiers=[
        "Topic :: System :: Monitoring",
        "Development Status :: 4 - Beta"],
      packages=["check_snmp_idrac"],
      long_description=read('README.md'),
      install_requires=['pynag'],
)
