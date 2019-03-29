# Quantum gates

To manipulate an input state we need to apply the basic operations of quantum computing. These are known as quantum gates. Here we'll give an introduction to all the gates that you'll find in the Composer and in OpenQASM. Most of the gates we'll be looking at act only on a single qubit. This means that their action can be understood simply in terms of the Bloch sphere.

### The Pauli operators

The simplest quantum gates are the Paulis: $$X$$, $$Y$$and $$Z$$. Their action is to perform a half rotation of the Bloch sphere around the x, y and z axes. They therefore have effects similar to the classical NOT gate or bit-flip. Specifically, the action of the $$X$$ gate on the states  $$|0\rangle$$ and $$|1\rangle$$is

$$
X |0\rangle = |1\rangle,\\ X |1\rangle = |0\rangle.
$$

The $$Z$$ gate has a similar effect on the states $$|+\rangle$$ and $$|-\rangle$$,

$$
Z |+\rangle = |-\rangle, \\ Z |-\rangle = |+\rangle.
$$

To implement these gates in QASM, we use

```c
x q[0]; \\ x on qubit 0
y q[0]; \\ x on qubit 0
z q[0]; \\ x on qubit 0
```

The matrix representations of these gates have already been shown in a previous section.

$$
X= \begin{pmatrix} 0&1 \\ 1&0 \end{pmatrix}\\
Y= \begin{pmatrix} 0&-i \\ i&0 \end{pmatrix}\\
Z= \begin{pmatrix} 1&0 \\ 0&-1 \end{pmatrix}
$$

There, their job was to help us make calculations regarding measurements. But since these matrices are unitary, and therefore define a reversible quantum operation, this additional interpretation of them as gates is also possible.

Note that here we referred to these gates as $$X$$, $$Y$$and $$Z$$ and `x`, `y` and `z`, depending on whether we were talking about their matrix represetation or which the way they are written in OpenQASM. Typically we will use the style of $$X$$, $$Y$$and $$Z$$when referring to gates in text or equations, and `x`, `y` and `z` when writing QASM code.

### Hadamard and S

The Hadamard gate is one that we've already used. It's a key component in performing an x measurement

```c
// x measurement of qubit 0
h q[0];
measure q[0] -> c[0];
```

Like the Paulis, the Hadamard is also a half rotation of the Bloch sphere. The difference is that it rotates around an axes located halfway between x and z. This gives it the effect of rotating states that point along the z axis to those pointing along x, and vice-versa.

$$
H |0\rangle = |+\rangle,~~~H |1\rangle = |-\rangle,\\
H |+\rangle = |0\rangle,~~~H |-\rangle = |1\rangle.
$$

This effect makes it an essential part of making x measurements. IBM quantum hardware, like most quantum hardware can only perform z measurements directly. Since the Hadamard moves x basis information to the z basis, it allows an indirect measurement of x.

The property that $$H |0\rangle = |+\rangle $$ also makes the Hadamard our primary means of generating superposition states. It's matrix form is,

$$
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1&1 \\ 1&-1 \end{pmatrix}.
$$

The $$S$$ and $$S^\dagger$$ gates have a similar role to play in quantum computation.

```text
s q[0];   \\ s gate on qubit 0
sdg q[0]; \\ s† on qubit 1
```

They are quarter turns of the Bloch sphere around the z axis, and so can be regarded as the two possible square roots of the $$Z$$ gate,

$$
S = \begin{pmatrix} 1&0 \\ 0&i \end{pmatrix},~~~S^\dagger = \begin{pmatrix} 1&0 \\ 0&-i \end{pmatrix}.
$$

The effect of the these gates is to rotate between the states of the x and y bases.

$$
S |+\rangle = |\circlearrowright\rangle,~~~S |-\rangle = |\circlearrowleft\rangle,\\
S^\dagger |\circlearrowright\rangle = |+\rangle,~~~S^\dagger |\circlearrowleft\rangle = |-\rangle.
$$

They are therefore used as part of y measurements.

```text
// y measurement of qubit 0
h q[0];
sdg q[0];
measure q[0] -> c[0];
```

The $$H$$, $$S$$ and $$S^\dagger$$ gates, along with the Paulis, form the so-called [Clifford group](../universality-of-quantum-computation/the-standard-gate-set.md) for a single qubit. They are extremely useful for many tasks in making and manipulating superpositions, and facilitating different kinds of measurements. But unlock the full potential of qubits, we need the next set of gates.

### Other single qubit gates

We've already seen the $$X$$, $$Y$$and $$Z$$ gates, which are rotations around the x , y and z axes by a specific angle. More generally we can extend this concept to rotations by an arbitrary angle $$\theta$$ . This gives us the gates $$R_x(\theta)$$, $$R_y(\theta)$$ and  $$R_z(\theta)$$.

The angle is expressed in radians, so the Pauli gates correspond to $$\theta=\pi$$ . Their square roots require half this angle, $$\theta=\pm \pi/2$$, and so on.

In OpenQASM, these rotations can be implemented via the `u3` and `u1` gates.

```text
u3(theta,pi/2,-pi/2); \\ rx rotation on qubit 0
u3(theta,0,0) q[0];   \\ ry rotation on qubit 0
u1(theta) q[0];       \\ rz rotation on qubit 0
```

Two specific examples of $$R_z(\theta)$$ have their own names: those for $$\theta=\pm \pi/4$$. These are the square roots of $$S$$, and are known as $$T$$ and $$T^\dagger$$.

```text
t q[0];   \\ t gate on qubit 0
tdg q[0]; \\ t† on qubit 1
```

Their matrix form is

$$
T = \begin{pmatrix} 1&0 \\ 0&e^{i\pi/4}\end{pmatrix},~~~T^\dagger = \begin{pmatrix} 1&0 \\ 0&e^{-i\pi/4} \end{pmatrix}.
$$

All single qubit operations are compiled down to the gates $$U_1$$ , $$U_2$$  and $$U_3$$  before running on real hardware. For that reason they are sometimes called the _physical gates_. Let's let's have a more detailed look at them. The most general is

$$
U3(\theta,\phi,\lambda) = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) 
  & e^{i\lambda+i\phi}\cos(\theta/2) \end{pmatrix}.
$$

This has the effect of rotating a qubit in the initial $$|0\rangle$$ state to one with an arbitrary superposition and relative phase,

$$
U_3|0\rangle =  \cos(\theta/2)|0\rangle + \sin(\theta/2)e^{i\phi}|1\rangle.
$$

The $$U_1$$ gate is known as the phase gate and is essentially the same as $$R_z(\lambda)$$, it's relationship with $$U_3$$, and its matrix form, are,

$$
U_1(\lambda) = U_3(0,0,\lambda) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\lambda} \end{pmatrix}.
$$

In IBM Q hardware, this gate is implemented as a frame change and takes zero time.

The second gate is $$U_2$$, and has the form,

$$
U_2(\phi,\lambda) = U_3(\pi/2,\phi,\lambda) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -e^{i\lambda} \\ e^{i\phi} & e^{i\lambda+i\phi} \end{pmatrix}.
$$

From this gate, the Hadamard is done by $$H= U_2(0,\pi)$$ . In IBMQ hardware, this is implemented by a pre- and post-frame change and a $$X_{\pi/2}$$ pulse.

### Multiqubit gates

To create quantum algorithms that beat their classical counterparts, we need more than isolated qubits. We need ways for them to interact. This is done by multiqubit gates.

The most prominent multiqubit gates are the two qubit CNOT and the three qubit Toffoli. These have already been introduced in [The atoms of computation](../getting-started-with-quantum-circuits/chapter-1-the-atoms-of-computation.md). These essentially perform reversible versions of the classical XOR and AND gates, respectively.

```text
cx q[0],q[1];       \\ CNOT controlled on qubit 0 with qubit 1 as target
ccx q[0],q[1],q[0]; \\ Toffoli controlled on qubits 0 and 1 with qubit 2 as target
```

We can also interpret the CNOT as performing an $$X$$ on its target qubit, but only when it's control qubit is in state $$|1\rangle$$, and doing nothing when the control is in state $$|0\rangle$$. We can similarly define gates that work in the same way, but instead peform a $$Y$$ or $$Z$$ on the target qubit depending on the$$|0\rangle$$and $$|1\rangle$$ states of the control.

```text
cy q[0],q[1];  \\ controlled-Y, controlled on qubit 0 with qubit 1 as target
cz q[0],q[1];  \\ controlled-Z, controlled on qubit 0 with qubit 1 as target
```

The Toffoli gate can be interpreted in a similar manner, except that it has a pair of control qubits. Only if both are in state $$|1\rangle$$ is the $$X$$ applied to the target.

