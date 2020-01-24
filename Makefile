
mypy:
	mypy *.py

flake8:
	flake8

test:
	./elfin.py tests/hello
