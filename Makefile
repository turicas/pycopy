test:
	./runtests.sh

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf reg-settings.py
	rm -rf MANIFEST dist build *.egg-info

install: clean uninstall
	python setup.py install

uninstall:
	pip uninstall -y rows

lint:
	pylint *.py

lint-tests:
	pylint test*.py

dev:
	pip install -r requirements-development.txt

.PHONY:	test clean lint lint-tests install uninstall dev
