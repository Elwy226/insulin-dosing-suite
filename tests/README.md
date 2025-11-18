# Tests

This folder contains unit tests for the project.  
The tests are written with [pytest](https://docs.pytest.org/) and cover the core functionality of functions and modules.

## Running the tests

To run all the tests, from the project root, run:

```bash
pytest
```

To run tests with more detailed output, run:

```bash
pytest -v
```

To run a single test file:

```bash
pytest tests/test_example.py
```

To run a single test function:

```bash
pytest tests/test_example.py::test_specific_function
```