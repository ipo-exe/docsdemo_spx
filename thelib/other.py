"""
Other - Python library for cooks and food lovers.

ah shit!

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    import lumache

    # Call its only function
    get_random_ingredients(kind=["cheeses"])
"""
import numpy as np

__version__ = "0.1.0"


def get_random_numper(nsize=10):
    """
    Returns a ``numpy`` array of integer random numbers.

    :param nsize: size of array.
    :type nsize: int or None
    :return: the random array.
    :rtype: ndarray
    """
    return np.random.randint(0, 10, nsize)
