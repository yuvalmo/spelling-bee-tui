.PHONY: test app clean

default: test

install:
	pip install -r requirements.txt

test:
	pytest test $(ARGS)

app:
	textual run app.py $(ARGS)

clean:
	git clean -xfd
