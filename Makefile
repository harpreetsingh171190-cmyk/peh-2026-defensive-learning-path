PYTHON ?= python3

.PHONY: check compile test project index labs release clean

check: compile test project

compile:
	$(PYTHON) -m compileall -q labs tools 07-intro-to-python 13-exploit-development

test:
	cd labs && $(PYTHON) -m unittest discover -s . -p 'test_*.py' -v
	cd tools && $(PYTHON) -m unittest discover -s . -p 'test_*.py' -v

project:
	$(PYTHON) tools/check_project.py
	$(PYTHON) tools/check_markdown.py
	$(PYTHON) tools/module_index.py --check
	$(PYTHON) tools/scan_secrets.py
	$(PYTHON) labs/check_course_links.py

index:
	$(PYTHON) tools/module_index.py --write

labs:
	$(PYTHON) labs/detect_auth_anomalies.py
	$(PYTHON) labs/risk_register.py
	$(PYTHON) labs/cvss_calculator.py

release:
	$(PYTHON) tools/build_release.py dist

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	rm -rf dist
