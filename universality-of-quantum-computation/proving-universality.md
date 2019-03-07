# Proving universality

Suppose we wish to implement the unitary

$$
U = e^{i(aX + bZ)}
$$



but the only gates we have are $$R_x(\theta) = e^{i \theta X}$$ and $$R_z(\theta) = e^{i \theta X}$$ . The best way to solve this problem would be to use [Euler angles](https://en.wikipedia.org/wiki/Euler_angles). Instead, we are going to consider a different method.

You may know that $$e^{i(a + b)} = e^{ia} e^{ib}$$. This suggests a naive approach to solving our problem: we could simply apply $$R_z(a) $$ followed by $$R_x(b) $$. Unfortunately, because we are exponentiating matrices rather than just numbers, and because the matrices do not commute, this apporach will not work. However, we could use the following modified approach

$$
U = \lim_{n\rightarrow\infty} ~ \left(e^{iaX/n}e^{ibZ/n}\right)^n
$$

Here we split $$U$$ up into $$n$$ small slices. For each slice, it is a good approximation to say that

$$
e^{iaX/n}e^{ibZ/n} = e^{i(aX + bZ)/n}
$$

The error in this approximation scales as $$1/n^2$$. When we combine the $$n$$ slices, we get an approximation of our target unitary whose error scales as $$1/n$$. So by simply increasing the number of slices, we can get as close to $$U$$ as we need. Other methods of creating the sequence are also possible to get even more accurate versions of our target unitary.

The approximate nature of this method could have been avoided for this simple, single qubit case. But the power of this method is that it can also be used for more complex cases. For example, consider the unitary 

$$
U = e^{i(aX\otimes X\otimes X + bZ\otimes Z\otimes Z)}
$$

We know how to create the unitary $$e^{i\theta X\otimes X\otimes X}$$ from a single qubit $$R_x(\theta)$$ and two controlled-NOTs.

```text
cx q[0],q[2];
cx q[0],q[1];
u3(thera,pi/2,-pi/2) q[0];
cx q[0],q[1];
cx q[0],q[2];
```

With a few Hadamards, we can do the same for $$e^{i\theta Z\otimes Z\otimes Z}$$.

```text
h q[0];
h q[1];
h q[2];
cx q[0],q[2];
cx q[0],q[1];
u3(thera,pi/2,-pi/2) q[0];
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

This method continues to work as we increase the number of qubits, and also the number of terms that need simulating. Care must be taken to ensure that the approximation remains accurate, but there's always a way to do it that requires only polynomial resoruces with respect to the nmber of terms to simulate, and the accuracy desired. We can therefore reproduce any unitary of the form $$U = e^{iH}$$ for which $$H$$ can be expressed as a sum of tensor products of Paulis. Since we have shown previously that all matrices can be expressed in this way, we are able to reproduce all unitaries. Quantum universality is acheived.







