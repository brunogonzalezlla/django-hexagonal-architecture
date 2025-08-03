.PHONY: build install clean

build:
	poetry build

publish:
	poetry publish --build

install:
	pip install --force-reinstall dist/django_hexagonal_cli-*.whl

clean:
	rm -rf dist build *.egg-info
