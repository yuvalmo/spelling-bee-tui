.PHONY: test clean

default: test

install:
	pip install -r requirements.txt

test:
	pytest test $(ARGS)

clean:
	git clean -xfd
