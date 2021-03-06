# noqa: D100
#%% 
import numpy as np
import functools
from functools import reduce
#%%

def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    i : int
        The row index of the maximum.

    j : int
        The column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy error or
        if the shape is not 2D.
    """
    i = 0
    j = 0

    # TODO
    if type(X) is not np.ndarray:
        raise ValueError('The input is not a numpy array') 
    if len(X.shape) != 2 : 
        raise ValueError('The shape is not 2D')
    (i,j) = np.unravel_index(np.argmax(X, axis=None), X.shape)

    return i, j
#%%

def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    XXX : write Parameters and Returns sections as above.

    """
    if n_terms == 0 :
        pi=2
    else :
        pi = 2 * reduce(lambda x, y: x*y, [(4.0*(i**2))/(4.0*(i**2)-1) for i in range (1, n_terms+1)])
    return pi
# %%
