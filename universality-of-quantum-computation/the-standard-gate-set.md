# The standard gate set

For every possible realization of fault-tolerant quantum computing, there is a set of quantum operations that are most straightforward to realize. Often these consist of multiple so-called Clifford gates, combing with a few single qubit gates that do not belong to the Clifford group. In this section we'll introduce these concepts, in preparation for showing that they are universal.

### Clifford gates

Some of the most impotant quantum operations are the so called Clifford operations. A prominent example is the Hadamard gate

$$
H = |+\rangle\langle0|~+~ |-\rangle\langle1| = |0\rangle\langle+|~+~ |1\rangle\langle+|.
$$

Above this gate is expressed using outer products, as desribed in the last section. When expressed in this form, it's famous effect becomes obvious: it takes $$|0\rangle$$, and rotates it to $$|+\rangle$$. More generally, we can say it rotates the basis states of the z measurement, $$\{ |0\rangle,|1\rangle \}$$ , to the basis states of the x measurement,  $$\{ |+\rangle,|-\rangle \}$$, and vice-versa.

Expressed in this way, we can see the Hadamard as being able to move information around a qubit. It swaps any information that would previously be accessed by an x measurement with that accessed by a z measurement. Indeed, one of the most important jobs of the Hadamard is to do exactly this. We use it when wanting to make an x measurement, given that we can only physically make z measurements.

```text
// x measurement of qubit 0
h q[0];
measure q[0] -> c[0];
```

The Hadamard can also be used to change the way that other operations function. For example

$$
H X H = Z,\\
H Z H = X.
$$

By doing a Hadamard before and a after an $$X$$ , we cause the action it previously applied to the z basis states to be transferred to the z basis states instead. The combined effect is then identical to that of a $$Z$$. Similarly, the Hadamards cause a $$Z$$ to behave as an $$X$$.

Similar behaviour can be seen for the $$S$$ gate and its Hermitian conjugate,

$$
S X S^{\dagger} = Y,\\
S Y S^{\dagger} = -X,\\
S Z S^{\dagger} = Z.
$$

This has a similar effect to the Hadamard, except that it swaps $$X$$ and $$Y$$  instead of  $$X$$ and $$Z$$. In combination with the Hadamard, we could then make composite gate that shifts information between y and z. This therefore gives us full control over single qubit Paulis.

The property of transforming Paulis into other Paulis is the defining feature of Clifford gates. Stated explicitly for the single qubit case: if $$U$$ is a Clifford and $$P$$ is a Pauli, $$U P U^{\dagger}$$ will also be a Pauli. For Hermitian gates, like the Hadamard, we can simply use $$U P U$$.

Further examples of single qubit Clifford gates are the Paulis themselves. These do not transform the Pauli they act on. Instead they simply assign a phase of $$-1$$ to the two that they anticommute with. For example,

$$
Z X Z = -Y,\\
Z Y Z = -X,\\
Z Z Z= ~~~~Z.
$$

You have have noticed that a similar phase also arose in the effect of the $$S$$ gate. By combining this with a Pauli, we could make a composite gate to that would cancel this phase, and swap $$X$$ and $$Y$$in a way more similar to the Hadamard's swap of s $$X$$ and $$Z$$.

For multiple qubit Clifford gates, the defining property is that they transform tensor products of Paulis to other tensor products of Paulis. For example, the most prominent two qubit Clifford gate is the controlled-NOT. The property of this that we will make use of in this chapter is

$$
{\rm CX}_{1,2}~ (X \otimes 1)~{\rm CX}_{1,2} = X \otimes X.
$$

This effectively 'copies' an $$X$$ from the control qubito over to the target.

The process of sandwiching a matrix between a unitary and its Hermitian conjugate is known as conjugation by that unitary. This process transforms the eigenstates of the matrix, but leaves the eigenvalues unchanged. The reason why conjugation by Cliffords can transform between Paulis is because all Paulis share the same set of eigenvalues.

### Non-Clifford gates

The Clifford gates are very important, but they are not powerful on their own. In order to do any quantum computation, we need gates that are not Cliffords. Three important examples are arbitrary rotations around the three axes of the qubit,   $$R_x(\theta)$$, $$R_y(\theta)$$ and  $$R_z(\theta)$$. These are implemented in QASM with

```text
u3(theta,pi/2,-pi/2); \\ rx rotation on qubit 0
u3(theta,0,0) q[0];   \\ ry rotation on qubit 0
u1(theta) q[0];       \\ rz rotation on qubit 0
```

Let's focus on $$R_x(\theta)$$. As we saw in the last section, any unitary can be expressed in an exponential form using a Hermitian matrix. For this gate, we find

$$
R_x(\theta) = e^{i \frac{\theta}{2} X}.
$$

The last section also showed us that the unitary and its corresponding Hermitian matrix have the same eigenstates. In this section, we've seen that conjugation by a unitary transforms eigenstates and leaves eigenvalues unchanged. With this in mind, it can be shown that

$$
U R_x(\theta)U^\dagger = e^{i \frac{\theta}{2} ~U X U^\dagger}.
$$

By conjugating this rotation by a Clifford, we can therefore transform it to the same rotation around another axis. So even if we didn't have a direct way to perform  $$R_y(\theta)$$ and  $$R_z(\theta)$$, we could do it with $$R_x(\theta)$$combined with Clifford gates. This technique of boosting the power of non-Clifford gates by combing them with Clifford gates is one that we make great use of in quantum computing.

Certain examples of these rotations have specific names. Rotations by $$\theta = \pi$$ around the x, y and z axes are X, Y and Z, respectively. Rotations by $$\theta = \pm \pi/2$$ around the z axis are S and $$S^†$$, and rotations by $$\theta = \pm \pi/4$$ around the z axis are T and $$T^†$$

### Composite gates

As another example of combing $$R_x(\theta)$$ with Cliffords, let's conjugate it with a controlled-NOT.

$$
CX_{1,2} ~(R_x(\theta) \otimes 1)~ CX_{1,2} = CX_{1,2} ~ e^{i \theta ~ (X\otimes 1)}~ CX_{1,2} = e^{i \theta ~CX_{1,2} ~ (X\otimes 1)~ CX_{1,2}} = e^{i \theta  ~ X\otimes X}
$$

This transforms our simple, single qubit rotation into a much more powerful two qubit gate. This is not just equivalent to performing the same rotatoon independently on both qubits. Instead, it is a gate capable of generating and manipulating entangled states.

We needn't stop There. We can use the same trick to extend the operation to to any number of qubits. All that's needed is more conjugates by the controlled-NOT to keep copying the $$X$$ over to new qubits.

Furthermore, we can use single qubit Cliffords to transform the Pauli on different qubits. For example, in our two qubit example we could conjugate by $$S$$ on the second qubit to turn the $$X$$ there into a $$Y$$ ,

$$
S ~e^{i \theta  ~ X\otimes X}~S^\dagger = e^{i \theta  ~ X\otimes Y}.
$$

With these techniques, we can make complex entangling operations that act on any arbitrary number of qubits, of the form

$$
U = e^{i\theta ~ P_1\otimes P_2\otimes...\otimes P_n}, ~~~ P_j \in \{I,X,Y,Z\}.
$$

This all goes to show that combing the single and two qubit Clifford gates with rotations around the x axis gives us a powerful set of possibilities. It only remains to show that we can use them to do anything.

