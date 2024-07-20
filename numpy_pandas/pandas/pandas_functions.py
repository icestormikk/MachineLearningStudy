from typing import Any

import numpy as np


def pandas_test(txt_filepath: str) -> Any:
    return np.genfromtxt(txt_filepath, dtype=float, skip_header=1, delimiter=",")
