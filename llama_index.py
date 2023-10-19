"""Numpy tool spec."""

from llama_index.tools.tool_spec.base import BaseToolSpec
from typing import Optional, List, Tuple, Union
import numpy as np


class NumpyToolSpec(BaseToolSpec):
    """Numpy Tool Spec"""

    spec_functions = [
        "compute_eigenvalues_and_eigenvectors",
        "transpose_matrix",
        "solve_linear_equation",
    ]

    def compute_eigenvalues_and_eigenvectors(
        self, a: List[List[float]]
    ) -> Tuple[List[complex], List[List[complex]]]:
        """
        Compute the eigenvalues and right eigenvectors of a square array.

        Parameters:
            a (List[List[float]]): Matrices for which the eigenvalues and right eigenvectors will be computed

        Returns:
            Tuple[List[complex], List[List[complex]]]: A tuple containing the eigenvalues and eigenvectors.
                The eigenvalues are a list of complex numbers, each repeated according to its multiplicity.
                The eigenvectors are a list of lists, where each inner list represents a normalized eigenvector.
                The column eigenvectors[i] is the eigenvector corresponding to the eigenvalue eigenvalues[i].
        """
        return np.linalg.eig(a)

    def transpose_matrix(self, a: List[List[float]]) -> List[List[float]]:
        """
        Transpose each matrix in a stack of matrices.

        Parameters:
            a (List[List[float]]): The matrix to transpose

        Returns:
            List[List[float]]: The transposed matrix
        """
        return np.transpose(a)

    def solve_linear_equation(
        self, a: List[List[float]], b: Union[List[float], List[List[float]]]
    ) -> Union[List[float], List[List[float]]]:
        """
        Solve a linear matrix equation, or system of linear scalar equations.

        Parameters:
            a (List[List[float]]): Coefficient matrix.
            b (Union[List[float], List[List[float]]]): Ordinate or "dependent variable" values.

        Returns:
            Union[List[float], List[List[float]]]: Solution to the system a x = b.
                The returned shape is identical to b.
        """
        return np.linalg.solve(a, b)
