# States for many qubits

We've already seen how to write down the state of a single qubit. Now we can look at how to do it when we have more than just one.

Quite simply, we just put a $$|$$ and  $$\rangle$$around bit strings. So to describe two qubits, both of which are in state $$|0\rangle$$, we write $$|00\rangle$$. The four possible bit strings for two bits are then converted into four orthogonal states, which together completely specify the state of two qubits, 

$$
|a\rangle = a_{00}|00\rangle+ a_{01}|01\rangle+a_{10}|10\rangle+ a_{11}|11\rangle = \begin{pmatrix} a_{00} \\ a_{01} \\ a_{10} \\ a_{11} \end{pmatrix}.
$$

As in the single qubit case, the elements of this vector are complex numbers. We require the state to be normalized so that $$\langle a|a\rangle = 1$$, and probabilites are given by the Born rule \( $$p_{00}^{zz} = |\langle00|a\rangle |^2$$, etc\).

Suppose we have two qubits, with one in state $$|a\rangle = a_0 |0\rangle + a_1 |1\rangle$$ and the other in state $$|b\rangle = b_0 |0\rangle + b_1 |1\rangle$$, and we want to create the two qubit state that describes them both. This can be constructed using the [tensor product](https://en.wikipedia.org/wiki/Tensor_product#Intuitive_motivation_and_the_concrete_tensor_product),

$$
|a\rangle \otimes |b\rangle = a_{0}b_0|00\rangle+ a_{0}b_1|01\rangle+a_{1}b_0|10\rangle+ a_{1}b_1|11\rangle.
$$

We also make use of the tensor product to represent sing single qubit matrices on a multiqubit space. For example, here's an$$X$$ that acts only on the first qubit,

$$
X \otimes I= \begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix} \otimes \begin{pmatrix} 1&0 \\ 0&1 \end{pmatrix} = \begin{pmatrix} 0&1&0&0 \\ 1&0&0&0\\0&0&0&1\\0&0&1&0 \end{pmatrix}, ~~~ I= \begin{pmatrix} 1&0 \\ 0&1 \end{pmatrix}.
$$

This was made by combining the $$X$$ matrix for the first qubit with the single qubit identity operator for the second. The result allows us to calculate expectation values for x measurements of the first qubit, in exactly the same way as before. To do the same for the second qubit, we make the matrix $$I \otimes X$$.

For more than two qubits, we can similarly use a basis consisting of all bit strings. We can also use multiple applications of the tensor product to construct states and operators.

### Entangled states

Using the tensor product we can construct matrices such as $$X \otimes X$$, $$Z \otimes Z$$, $$Z \otimes X$$ and so on. The expectation values of these also represent probabilities. For example, for a general two qubit state $$|a\rangle$$,

$$
\langle a|Z\otimes Z|a\rangle = P^{zz}_{0} - P^{zz}_{1}.
$$

Here $$P^{zz}_{0}$$ is the probability that the results from z measurements of the two qubits are the same, and $$P^{zz}_{1}$$  is the probability they are different. Quantities such as $$\langle a|Z\otimes X|a\rangle$$ reflect similar probabilities governing the results for different choices of measurements on the qubits.

These multiqubit Pauli operators can be used to analyze a new kind of state, that cannot be described as a simple tensor product. For example,

$$
|\Phi^+\rangle =\frac{1}{\sqrt{2}}\left(|00\rangle+|11\rangle\right).
$$

This cannot be written as a simple combination of two independent qubit states. It represents a quantum form of correlated state, known as an entangled state. For example, it is clear that a z measurement of the two qubits will result in either `00` or `11`. So in all cases, the z outputs of the two qubits always agree. This is reflected by the fact that

$$
\langle \Phi^+|Z\otimes Z|\Phi^+\rangle = 1
$$

for this state.It's also true that $$a = b$$ and $$\langle \Phi^+|Y\otimes Y|\Phi^+\rangle = -1$$. There are a lot of correlations in this little state!

For more qubits, we can get ever larger multiqubit Pauli operators. In this case, the more general definition of probabilities such as  $$P^{zz\ldots zz}_{0}$$ and $$P^{zz\ldots zz}_{1}$$ are that they reflect the cases where the total output bit string is of even or odd parity, respectively \(i.e., they consist of an even or odd number of `1`s\).



