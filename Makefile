all:
	git push origin master
	python setup.py sdist upload
