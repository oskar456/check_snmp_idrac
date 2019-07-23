check_snmp_idrac
================

This is a fork of [health_monitoring_plugins](https://github.com/rsmuc/health_monitoring_plugins), supporting only monitoring of Dell iDrac health over SNMP. The motivation was to enable Python 3 support and easy deployment as a python [zipapp](https://docs.python.org/3/library/zipapp.html).


Usage
-----

  1. Make sure you have `netsnmp` binding for Python version you want to use.
     For Python 3, you may try to install
     [python3-netsnmp](https://pypi.org/project/python3-netsnmp/) using Pip.

  2. Download `check-snmp-idrac` from lastest release or build it yourself.

  3. Run it! See embedded help for usage instructions.


Compilation
-----------

  1. Make sure you have at least Python3.6 and `pip` tool installed.
  2. Clone the repository and run `make`
