
mypy:
	mypy *.py

flake8:
	flake8

test:
	./elfin.py tests/hello

bigtest:
	find /usr/bin -type f |xargs -n 1 ./elfin.py >xxx 2>yyy
