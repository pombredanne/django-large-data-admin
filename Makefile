all: git pypi

git:
	git push origin master

pypi:
	python setup.py sdist upload

