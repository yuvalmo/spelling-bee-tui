default: test

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: test
test:
	pytest test $(ARGS)
 
.PHONY: app
app:
	textual run app.py $(ARGS)

.PHONY: clean
clean:
	git clean -xfd
