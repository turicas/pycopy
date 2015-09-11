#!/bin/bash

for python_version in $(ls -d .tox/py*); do
	source $python_version/bin/activate
	$python_version/bin/python --version
	$python_version/bin/nosetests -dsv --with-yanc \
		--with-coverage --cover-package=pycopy tests_pycopy.py
	echo
done
