# Tests

Pytest runs the unit tests in this folder.

## Setup
- Install dev dependencies (pytest) if not already available:
  - `pip install pytest`

## How to run
- From the project root:
  - All tests: `python -m pytest tests`
  - Single file: `python -m pytest tests/test_utils.py`

## What the example covers
- `tests/test_utils.py` demonstrates Arrange/Act/Assert with `save_as_npz`.
- It uses pytest’s `tmp_path` fixture to keep file writes in a temporary folder, so runs stay isolated and leave no artifacts.
- `np.testing.assert_array_equal` checks that saved data matches exactly when reloaded.
