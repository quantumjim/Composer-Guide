# Pauli matrices and the Bloch sphere

### 

### Pauli matrices

Wherever there are vectors, matrices are not far behind. The three important matrices for qubits are known as the Pauli matrices.

$$
X= \begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix}\\
Y= \begin{pmatrix} 0&-i \\ i&0 \end{pmatrix}\\
Z= \begin{pmatrix} 1&0 \\ 0&-1 \end{pmatrix}
$$

These have many useful properties, as well as a deep connection to the x, y and z measurements. Specifically, we can use them to calculate the quantities

$$
\langle a | X | a\rangle = p^x_0 (|a\rangle)-p^x_1(|a\rangle),\\
\langle a | Y | a\rangle = p^y_0 (|a\rangle)-p^y_1(|a\rangle),\\
\langle a | Z | a\rangle = p^z_0 (|a\rangle)-p^z_1(|a\rangle).
$$

In calculating these, we make use of standard [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication#Definition).

Typically, we prefer to use a more compact notation for the quantities above. Since we usually know what state we are talking about in any given situation, we don't explicitly write it in. This allows us to write $$\langle X \rangle = \langle a|X|a \rangle$$, etc. Our statement from the last section, regarding the conservation of certainty for an isolated qubit, can then be written

$$
\langle X \rangle^2 + \langle Y \rangle^2 + \langle Z \rangle^2 = 1.
$$



