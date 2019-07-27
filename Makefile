PACKAGE_NAME := dzo

.PHONY: test
test:
	@python3 $(CURDIR)/setup.py test

.PHONY: check/lint
check/lint:
	@pylint $(CURDIR)/$(PACKAGE_NAME)

.PHONY: check/type
check/type:
	@MYPYPATH=$(CURDIR)/stubs mypy @.mypy_check_files --config-file=$(CURDIR)/mypy.ini

.PHONY: build/ext
build/ext:
	@python3 $(CURDIR)/setup.py build_ext --inplace

# Build distribution source.
.PHONY: build/dist
build/dist:
	@python3 setup.py sdist

# Build package of this library.
.PHONY: build/wheel
build/wheel:
	@python3 setup.py bdist_wheel

# Build this package.
.PHONY: build/pkg
build/pkg: build/dist build/wheel

.PHONY: upload/pkg/test
upload/pkg/test:
	twine upload --repository testpypi dist/*

.PHONY: upload/pkg
upload/pkg:
	twine upload --repository pypi dist/*

.PHONY: clean/ext
clean/ext:
	rm $(CURDIR)/$(PACKAGE_NAME)/ext/*.so
	rm $(CURDIR)/$(PACKAGE_NAME)/ext/*.c

.PHONY: clean/pyc
clean/pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean/pkg
clean/pkg:
	rm -rf $(CURDIR)/$(PACKAGE_NAME).egg-info/* dist/*

.PHONY: fetch/numpy-stubs
fetch/numpy-stubs:
	@mkdir -p $(CURDIR)/stubs/tmp
	@git clone --depth=1 https://github.com/machinalis/mypy-data.git $(CURDIR)/stubs/tmp
	@mv $(CURDIR)/stubs/tmp/numpy-mypy/numpy $(CURDIR)/stubs/numpy
	@rm -rf $(CURDIR)/stubs/tmp
