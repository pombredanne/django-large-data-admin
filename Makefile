all: git pypi

git:
	git push origin master
	git push origin --tags

pypi:
	python setup.py sdist upload

