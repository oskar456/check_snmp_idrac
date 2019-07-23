

check-snmp-idrac: check_snmp_idrac/*.py setup.py
	mkdir -p app
	python3 -m pip install --upgrade https://github.com/pynag/pynag/archive/pynag-v1.0.1.zip --target app
	python3 -m pip install . --no-dependencies --target app
	rm -rf app/*.dist-info app/*.egg-info
	find app/ -print0 | xargs -0 touch -t 201901010000
	python3 -m zipapp -p '/usr/bin/env python' -m 'check_snmp_idrac:main' -o check-snmp-idrac app
	rm -rf app

