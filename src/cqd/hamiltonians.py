import numpy as np   # standard numerics library
import math
from scipy.special import hermite 


def create_xvals(L, npoints, endpoint=True):
    """
    Creates a grid of 'npoints' evenly spaced values between -L/2 and L/2.
    The 'endpoint' parameter determines whether the endpoint L/2 is included in the grid.
    Returns the grid of x values and the grid spacing dx.
    """
    xvals = np.linspace(-L / 2, L / 2, npoints, endpoint=endpoint)
    dx = xvals[1] - xvals[0]
    return xvals, dx

    
def HO_eigenstates_exact(n, x):
    """
   Return the normalized n-th eigenstate of the one-dimensional
    quantum harmonic oscillator at position(s) x.

    The analytical eigenfunction is

        phi_n(x) = normalization constant * Hn(x) * exp(-x^2 / 2),

    where

        normalization constant = 1 / sqrt(2^n * n! * sqrt(pi)) 
        
    the normalization constant, and Hn(x) is the n-th
    Hermite polynomial.

    Parameters
    ----------
    n : Quantum number, satisfying n >= 0.
    x : Position or array of positions at which the eigenfunction
        is evaluated.

    Notes
    -----
    The eigenfunction satisfies the normalization condition

        integral from -infinity to +infinity of
        |phi_n(x)|^2 dx = 1.
    """

    normalization = 1 / np.sqrt(2 ** n * math.factorial(n) * np.sqrt(np.pi)) 
    return normalization * hermite(n)(x) * np.exp(-x ** 2 / 2)


def HO_eigenenergies_exact(n):
    """
    Return the n-th eigenenergy of the one-dimensional
    quantum harmonic oscillator in numerical units.

    The analytical eigenenergy is

    En = n + 0.5

    where : n = 0, 1, 2 ... , quantum number.

    Returns
    -------
    En: The n-th harmonic-oscillator eigenenergy.
    """
    return n + 0.5

def H_kinetic(x):
    """
    Returns the kinetic energy operator of the quantum harmonic oscillator in the position basis for a grid 'x'.
    The kinetic energy operator is represented as a finite difference matrix approximating the second derivative, which is given by the formula:
    T = - (ħ^2 / 2m) * d^2/dx^2, or in numerical units, T = -0.5 * d^2/dx^2. The second derivative can be approximated using the central difference formula:
    d^2ψ/dx^2 ≈ (ψ(x + dx) - 2ψ(x) + ψ(x - dx)) / (dx^2).
    """

    n_points = len(x) # number of grid points
    dx = x[1] - x[0] # grid spacing

    main_diag = np.diag(np.ones(n_points))
    off_diag = -0.5 * np.diag(np.ones(n_points - 1), k=1)
    return (main_diag + off_diag + off_diag.T) / (dx * dx)

def HO_potential(x):
    """
    Return the harmonic-oscillator potential-energy operator on the spatial grid x.
    The harmonic-oscillator potential is

    math::

        V(x) = x^2/2.

    In the discrete position basis(allowing the particle’s position x to take infinitely many continuous values), the potential operator is
    represented by the diagonal matrix

    Parameters
    ----------
    x : One-dimensional array containing the spatial-grid points.

    Returns
    -------
    V : Diagonal matrix representing the potential-energy operator.
        Its shape is (N, N), where N = len(x).
    """
    return 0.5 * np.diag(x**2)