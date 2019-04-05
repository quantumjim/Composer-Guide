# Proving universality

Suppose we wish to implement the unitary

$$
U = e^{i(aX + bZ)}
$$

but the only gates we have are $$R_x(\theta) = e^{i \frac{\theta}{2} X}$$ and $$R_z(\theta) = e^{i \frac{\theta}{2} Z}$$ . The best way to solve this problem would be to use [Euler angles](https://en.wikipedia.org/wiki/Euler_angles). But let's instead consider a different method.

The Hermitian matrix in the exponential for $$U$$ is simply the sum of those for the $$R_x(\theta)$$ and $$R_z(\theta)$$ rotations. This suggests a naive approach to solving our problem: we could simply apply $$R_z(a)  = e^{i bZ}$$ followed by $$R_x(b)  = e^{i a X}$$. Unfortunately, because we are exponentiating matrices that do not commute, this apporach will not work. However, we could use the following modified version

$$
U = \lim_{n\rightarrow\infty} ~ \left(e^{iaX/n}e^{ibZ/n}\right)^n.
$$

Here we split $$U$$ up into $$n$$ small slices. For each slice, it is a good approximation to say that

$$
e^{iaX/n}e^{ibZ/n} = e^{i(aX + bZ)/n}
$$

The error in this approximation scales as $$1/n^2$$. When we combine the $$n$$ slices, we get an approximation of our target unitary whose error scales as $$1/n$$. So by simply increasing the number of slices, we can get as close to $$U$$ as we need. Other methods of creating the sequence are also possible to get even more accurate versions of our target unitary.

The power of this method is that it can be used in complex cases than just a single qubit. For example, consider the unitary 

$$
U = e^{i(aX\otimes X\otimes X + bZ\otimes Z\otimes Z)}.
$$

We know how to create the unitary $$e^{i\frac{\theta}{2} X\otimes X\otimes X}$$ from a single qubit $$R_x(\theta)$$ and two controlled-NOTs.

```text
cx q[0],q[2];
cx q[0],q[1];
u3(theta,pi/2,-pi/2) q[0];
cx q[0],q[1];
cx q[0],q[2];
```

With a few Hadamards, we can do the same for $$e^{i\frac{\theta}{2} Z\otimes Z\otimes Z}$$.

```text
h q[0];
h q[1];
h q[2];
cx q[0],q[2];
cx q[0],q[1];
u3(theta,pi/2,-pi/2) q[0];
cx q[0],q[1];
cx q[0],q[2];
h q[2];
h q[1];
h q[0];
```

This gives is the ability to reproduce a small slice of our new, three qubit $$U$$ ,

$$
e^{iaX\otimes X\otimes X/n}e^{ibZ\otimes Z\otimes Z/n} = e^{i(aX\otimes X\otimes X + bZ\otimes Z\otimes Z)/n}.
$$

As before, we can then combine the slices together to get an arbitrarily accurate approximation of $$U$$ .

This method continues to work as we increase the number of qubits, and also the number of terms that need simulating. Care must be taken to ensure that the approximation remains accurate, but this can be done in ways that require reasonable resources. Adding extra terms to simulate, or increasing the desired accuracy, only require the complexity of the method to increase polynomially.

Methods of this form can reproduce any unitary  $$U = e^{iH}$$ for which $$H$$ can be expressed as a sum of tensor products of Paulis. Since we have shown previously that all matrices can be expressed in this way, this is sufficient to show that we can reproduce all unitaries. Though methods may be better in practice, the main thing to take away from this chapter is that there is certainly a way to reproduce all multi-qubit unitaries using only the basic operations found on the composer, in OpenQasm, and in Qiskit. Quantum universality can be acheived.







