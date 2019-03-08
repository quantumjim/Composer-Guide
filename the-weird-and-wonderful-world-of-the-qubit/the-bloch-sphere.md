# Pauli matrices and the Bloch sphere

In this section we'll further develop the topics introduced in the last, and introduce a useful visualization of single qubit states.

### Pauli matrices

Wherever there are vectors, matrices are not far behind. The three important matrices for qubits are known as the Pauli matrices.

$$
X= \begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix}\\
Y= \begin{pmatrix} 0&-i \\ i&0 \end{pmatrix}\\
Z= \begin{pmatrix} 1&0 \\ 0&-1 \end{pmatrix}
$$

These have many useful properties, as well as a deep connection to the x, y and z measurements. Specifically, we can use them to calculate the three quantities used in the last section,

$$
\langle a | X | a\rangle = p^x_0 (|a\rangle)-p^x_1(|a\rangle),\\
\langle a | Y | a\rangle = p^y_0 (|a\rangle)-p^y_1(|a\rangle),\\
\langle a | Z | a\rangle = p^z_0 (|a\rangle)-p^z_1(|a\rangle).
$$

These quantities are known as the expectation values of the three matrices. In calculating them, we make use of standard [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication#Definition).

Typically, we prefer to use a more compact notation for the quantities above. Since we usually know what state we are talking about in any given situation, we don't explicitly write it in. This allows us to write $$\langle X \rangle = \langle a|X|a \rangle$$, etc. Our statement from the last section, regarding the conservation of certainty for an isolated qubit, can then be written

$$
\langle X \rangle^2 + \langle Y \rangle^2 + \langle Z \rangle^2 = 1.
$$

### The Bloch sphere

Let's take a moment to think a little about the numbers $$\langle X \rangle$$,  $$\langle Y \rangle$$ and  $$\langle Z \rangle$$. Though their values depend on what state our qubit is in, they are always constrained to be no larger than 1, and no smaller than -1. They also collectively obey the condition written above.

There are another set of numbers that behave in the same way. 

First, take a sphere. For this, we can describe every point on the surface of the sphere in terms of it's x, y and z coordinates. We'll place the origin of our coordinate system at the center of the sphere. The coordinates are then constrained by the radius in both directions: they can be no greater than $$r$$ , and no less than $$-r$$ . For simplicity, let's set the radius to be $$r=1$$.

For any point, the distance from the surface of the sphere can be determined by the 3D version of Pythagorus' theorem. Specifically, $$x^2 + y^2 + z^2$$. For points on the surface, this distance is always 1.

So now we have three numbers that can each be no greater than 1, no less than -1, and for which the sum of the squares is always 1. All exactly the same as $$\langle X \rangle$$,  $$\langle Y \rangle$$ and  $$\langle Z \rangle$$. They even have pretty much the same names as these values. This allows us to visualize any single qubit state as a point on the surface of a sphere. We call this the Bloch sphere.

![](../.gitbook/assets/image.png)

We usually associate $$|0\rangle$$ with the north pole, $$|1\rangle$$ with the south and the states for the x and y measurements around the equator. Any pair of orthogonal states correspond to antipodes on this sphere.

As we'll see in future sections, the Bloch sphere makes it easier to understand single qubit operations. Each moves points around on the surface of the sphere, and so can be interpreted as a simple rotation.

