

import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


class TestExerciseNotebooks:

    @pytest.mark.parametrize(
        "notebook_path",
        [
            Path("exercise1.ipynb"),
            Path("exercise1_sol.ipynb"),
        ],
    )
    def test_notebook_runs_without_errors(self, notebook_path):
        """Check that each Exercise 1 notebook runs without errors."""

        assert notebook_path.exists(), (
            f"Notebook was not found: {notebook_path}"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            output_name = notebook_path.stem

            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "script",
                    "--output",
                    output_name,
                    "--output-dir",
                    temp_dir,
                    str(notebook_path),
                ],
                check=True,
            )

            script_path = Path(temp_dir) / f"{output_name}.py"

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "IPython",
                    str(script_path),
                ],
                check=True,
                env={
                    **os.environ,
                    "MPLBACKEND": "Agg",
                    "PYTHONIOENCODING": "utf-8",
                },
            )