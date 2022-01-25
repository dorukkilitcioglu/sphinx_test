import numpy as np


def relu(x: np.ndarray) -> np.ndarray:
    """Rectified Linear Unit

    Parameters
    ----------
    x: np.ndarray
        The input array

    Returns
    -------
    np.ndarray
        Input array with ReLU applied
    """
    return np.maximum(x, 0.)
