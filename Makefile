install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

format:
	black *.py

test:
	python -m pytest -v test_main.py
