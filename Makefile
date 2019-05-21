gendeps: 
	pipreqs . --force

test: 
	pytest tests

gendocs: 
	pdoc tfchain --html --html-dir docs/api --overwrite

sdist:
	python3 setup.py sdist

upload:
	python3 setup.py sdist upload