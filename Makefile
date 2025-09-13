init:
	pip install -r requirements.txt

test:
	pytest -s

test-fast:
	pytest -s -m "not slow"

test-slow:
	pytest -s -m "slow"

fmt:
	black ./.