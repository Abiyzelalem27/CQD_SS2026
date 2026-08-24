




# Computational Quantum Dynamics

[![CI](https://github.com/Abiyzelalem27/CQD_SS2026/actions/workflows/python_CI.yml/badge.svg)](https://github.com/Abiyzelalem27/CQD_SS2026/actions/workflows/python_CI.yml)

## Exercise 1: Single Particle in a One-Dimensional Potential

This repository contains the code selected for my Computational Quantum
Dynamics oral examination.

The code numerically solves the time-independent Schrödinger equation

\[
\hat{H}\psi_n(x)=E_n\psi_n(x),
\]

where

\[
\hat{H}
=
-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x).
\]

The continuous spatial coordinate is represented by a finite numerical
grid. The second derivative is approximated using a finite-difference
method, converting the Schrödinger equation into a matrix eigenvalue
problem.

The harmonic oscillator is considered as an example potential.

## Main Topics

- Time-independent Schrödinger equation
- One-dimensional harmonic oscillator
- Spatial discretization
- Finite-difference approximation
- Hamiltonian matrix construction
- Numerical matrix diagonalization
- Energy eigenvalues and eigenstates
- Comparison with analytical results

## Selected Examination Code

I will present the relevant implementation contained in:

`exercise1_sol.ipynb`

During the presentation, I will explain:

- the physical problem;
- the mathematical discretization;
- the Python implementation;
- the numerical results;
- numerical accuracy and limitations.

## Repository Structure

```text
CQD_SS2026/
├── src/
│   └── cqd/
├── tests/
│   
├── exercise1.ipynb
├── exercise1_sol.ipynb
├── pyproject.toml
├── LICENSE
└── README.md
```
## References

### CQD_SS26 Main Repository — Primary Course Source

Course code repository for **Computational Quantum Dynamics (SS26)** taught by **Prof. Gärttner**.

https://github.com/NiklasEuler/CQD_SS26

### Quantum Information and Quantum Simulation Group

The **Quantum Information and Quantum Simulation (QIQS) Group** at Friedrich Schiller University Jena, Germany, provides the research group and academic environment associated with the course.

https://qiqs-jena.de/ 
