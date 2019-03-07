# Fun with matrices

Manipulating matrices is the heart of how we analyse quantum programs. In this section we'll look at some of the most common tools that can use for this.

### Unitary and Hermitian matrices

Studying universality is inherently an endeavour that needs math. As such, we'll need to get ourselves some mathematical tools.

Firstly, we need the concept of the [Hermitian conjugate](https://en.wikipedia.org/wiki/Conjugate_transpose#Example). For this we take a matrix $$M$$ , then we replace every element with its complex conjugate, and finally we transpose them \(replace the top left element with the bottom right, and so on\). This gives us a new matrix that we call $$M^\dagger$$.

There are two families of matrices that are defined by their relationship with the Hermitian conjugate, and which are very important to quantum computing. One is the family of unitary matrices, for which

$$
U U^\dagger = U^\dagger U = 1.
$$

This means that the Hermitian conjugate of a unitary is its inverse. It gives us another unitary $$U^\dagger$$ with the power to undo the effects of $$U$$. All gates in quantum computing, with the exception of measurement, can be represented by unitary matrices.

The other important family of matrices are the Hermitian matrices. These are the matrices that are unaffected by the Hermitian conjugate

$$
H = H^\dagger.
$$

The matrices $$X$$, $$Y$$, $$Z$$ and $$H$$ are examples of Hermitian matrices that you've already seen \(coincidentally, they are also all unitary since they are their own inverses\).

### Matrices as outer products

In a previous section, we calculated many _inner products_, such as  $$\langle0|0\rangle =1$$. These combine a bra and a ket to give us a single number. We can also combine them in a way that gives us a matrix, simply by putting them in the opposite order. This is called an outer product, and works by standard matrix multiplication. For example

$$
|0\rangle\langle0|= \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1&0 \\ 0&0 \end{pmatrix},\\
|0\rangle\langle1| = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0&1 \\ 0&0 \end{pmatrix},\\
|1\rangle\langle0| = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 0&0 \\ 1&0 \end{pmatrix},\\
|1\rangle\langle1| = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0&0 \\ 0&1 \end{pmatrix}.\\
$$

This also means that we can write any matrix purely in terms of outer products. In the examples above, we constructed the four matrices that cover each of the single elements in a single qubit matrix, and so we can write any other single qubit matrix in terms of them.

$$
M= \begin{pmatrix} m_{0,0}&m_{0,1} \\ m_{1,0}&m_{1,1} \end{pmatrix} = m_{0,0} |0\rangle\langle0|+ m_{0,1} |0\rangle\langle1|+ m_{1,0} |1\rangle\langle0|+ m_{1,1} |1\rangle\langle1|
$$

This property also extends to matrices for any number of qubits, $$n$$. We simply use the outer products of the corresponding $$n$$-bit strings.

### Spectral form

This provides us with a very useful way of writing unitary matrices, or even designing new ones that we want to implement. First we pick a set of orthogonal states that describe our qubits. For example, for two qubits we could simply choose $$\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}$$. Then we determine the state that the unitary rotates each of these states to \(or, if designing a unitary, the state that we want it to rotate them to\). Let's call these$$\{|u_{00}\rangle,|u_{01}\rangle,|u_{10}\rangle,|u_{11}\rangle\}$$. The unitary that performs this can then be written

$$
U = |u_{00}\rangle\langle00| + |u_{01}\rangle\langle01| + |u_{10}\rangle\langle10| +|u_{11}\rangle\langle11|
$$

In a form like this, we can directly read out the effect of the unitary on the basis states we can chosen.

This way of writing a unitary is not unique for each unitary. You can do it for every possible set of orthogonal input states. However, for at least one possible set of states it will take an especially simple form. These are the eigenstates of the matrix, for which

$$
U = \sum_j e^{ih_j} |h_j\rangle\langle h_j|
$$

Here the unitary takes each state of this basis, which we've called $$|h_j\rangle$$, and replaces it with $$e^{ih_j}|h_j\rangle$$. Since the $$e^{ih_j} |h_j\rangle$$ must themselves be valid quantum states, the  $$e^{ih_j}$$ must be complex numbers of magnitude 1. This therefore corresponds to the unitary simply inducing a global phase on its eigenstates. The non-trivial effects of this unitary will come for superpositions of these states, for which a relative phase may be induced. Note that we have written the phases $$e^{ih_j}$$ in the exponential for complex numbers, and so the $$h_j$$ must be real numbers.

Hermitian matrices also have well-defined eigenstates and eigenvalues, and can be written in the same form as the unitary matrix above.

$$
H = \sum_j h_j |h_j\rangle\langle h_j|
$$

In order to satisfy the constraint that $$H = H^\dagger$$, we must determine what properties are required for the eigenstates and eigenvalues.

For the eigenstates, we can see what happens when we take the inner product of a state with itself. For this we use the fact that the Hermitian conjugate of a product can be evalulated by taking the Hermitian conjugate of each factor, and then reversing the order of the factors. If we also note that the Hermitian conjugate of a ket is the corresponding bra, and vice-versa, we find

$$
(|h_j\rangle\langle h_j|)^\dagger = \langle (h_j|^\dagger) ~(|h_j\rangle^\dagger) = |h_j\rangle\langle h_j|
$$

So the inner product of a state with itself is inherently Hermitian. To ensure that $$H$$ is Hermitian as a whole, we therefore only need to require the eigenvalues $$h_j$$ to be real.

If you were wondering about the coincidence of notation used above for $$U$$ and $$H$$ in spectral form, this should hopefully begin to explain it. Essentially, these two types of matrix differ only in that one must have real numbers for eigenvalues, and the other must have complex exponentials of real numbers. This means that, for every unitary, we can define a corresponding Hermitian matrix. It must simply reuse the same eigenstates, and use the $$h_j$$ from each $$e^{ih_j}$$ as the corresponding eigenvalue.

Similarly, for each Hermitian matrix there exists a unitary. We simply reuse the same same eigenstates, and exponentiate the $$h_j$$ to create the eigenvalues $$e^{ih_j}$$. This can be expressed

$$
U = e^{iH}
$$

Here we have used the standard definition of how to exponentiate a matrix.This has exactly the properties we require: preserving the eigenstates and exponentiating the eigenvalues.

We can also build a whole family of unitaries for each given Hermitian, using

$$
U(\theta) = e^{i \theta H},
$$

where $$\theta$$ is an arbitrary real number. This allows us to interpolate between $$\theta=0$$ , which will be the identity matix, to $$\theta=1$$, which is $$U$$ . It also allow us to define a notion of a gate that is the square root of $$U$$: one that must be done twice to get the full effect of $$U$$. This would simply have $$\theta=1/2$$.

### Pauli decomposition

As we saw above, it is possible to write matrices entirely in terms of outer products

$$
M= \begin{pmatrix} m_{0,0}&m_{0,1} \\ m_{1,0}&m_{1,1} \end{pmatrix} = m_{0,0} |0\rangle\langle0|+ m_{0,1} |0\rangle\langle1|+ m_{1,0} |1\rangle\langle0|+ m_{1,1} |1\rangle\langle1|
$$

Now we will see that it also possible to write them completely in terms of Pauli operators. For this, the key thing to note is that

$$
\frac{1+Z}{2} = \frac{1}{2}\left[ \begin{pmatrix} 1&0 \\0&1 \end{pmatrix}+\begin{pmatrix} 1&0 \\0&-1 \end{pmatrix}\right] = |0\rangle\langle0|,\\\frac{1-Z}{2} = \frac{1}{2}\left[ \begin{pmatrix} 1&0 \\0&1 \end{pmatrix}-\begin{pmatrix} 1&0 \\0&-1 \end{pmatrix}\right] = |1\rangle\langle1|
$$

This shows that $$|0\rangle\langle0|$$ and $$|1\rangle\langle1|$$can be expressed using the identity matrix and $$Z$$. Now, using the property that $$X|0\rangle = |1\rangle$$, we can also produce

$$
|0\rangle\langle1| = |0\rangle\langle0|X = \frac{1}{2}(1+Z)~X = \frac{X+iY}{2},\\
|1\rangle\langle0| = X|0\rangle\langle0|  = X~\frac{1}{2}(1+Z) = \frac{X-iY}{2}.
$$

Since we have all the outer products, we can now use this to write the matrix in terms of Pauli matrices,

$$
M = \frac{m_{0,0}+m_{1,1}}{2}~1~+~\frac{m_{0,1}+m_{1,0}}{2}~X~+~i\frac{m_{0,1}-m_{1,0}}{2}~Y~+~\frac{m_{0,0}-m_{1,1}}{2}~Z.
$$

This example was for a general single qubit matrix, but the a corresponding result is true also for matrices for any number of qubits. We simply start from the observation that

$$
\left(\frac{1+Z}{2}\right)\otimes\left(\frac{1+Z}{2}\right)\otimes\ldots\otimes\left(\frac{1+Z}{2}\right) = |00\ldots0\rangle\langle00\ldots0|,
$$

and can then proceed in the same manner as above. In the end it can be shown that any matrix can be expressed in terms of tensor products of Pauli matrices,

$$
M = \sum_{P_1,\ldots,P_n \in \{1,X,Y,Z\}} C_{P_1\ldots,P_n}~~P_1 \otimes P_2\otimes\ldots\otimes P_n.
$$

For Hermitian matrices, note that the coefficients $$C_{P_1\ldots,P_n}$$ here will all be real.



Now we have some powerful tools to analyze quantum operations, let's look at the operations we will need to analyze for our study of universality.



