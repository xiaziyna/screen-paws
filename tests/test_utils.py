"""Pytest example for `save_as_npz`.

This keeps everything inside a temporary folder so running the test
does not leave files behind.
"""

import numpy as np

from screen_pause.utils import save_as_npz


def test_save_as_npz_writes_npz_and_preserves_data(tmp_path) -> None:
    """Exercise `save_as_npz` end-to-end using pytest's tmp_path fixture."""
    # Arrange: sample array and an isolated temp directory supplied by pytest.
    sample = np.array([1, 2, 3])
    data_dir = tmp_path / "artifacts"

    # Act: call the helper and capture the returned filepath.
    filepath = save_as_npz(sample, filename="sample", data_dir=str(data_dir))

    # Assert: file is created where we expect and contains the same data.
    expected_path = data_dir / "sample.npz"
    assert expected_path.exists(), "save_as_npz should create the .npz file"

    loaded = np.load(filepath, allow_pickle=True)["data"]
    np.testing.assert_array_equal(loaded, sample)
