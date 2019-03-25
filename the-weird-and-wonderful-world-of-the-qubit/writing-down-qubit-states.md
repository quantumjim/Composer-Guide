# Qubits as physical systems

What we have described and used in the sections so far is the abstract notion of a qubit. To realize quantum computation, we need to be able to implement this notion in a physical system.

The prototype quantum computer you interact with in the composer uses a physical type of qubit called a _superconducting transmon qubit_, which is made from superconducting materials such as niobium and aluminum, patterned on a silicon substrate. The two states $$|0\rangle$$ and $$|1\rangle$$represent two possible energy levels within this superconducting system. The $$|0\rangle$$ has the lowest energy, and so is something called the _ground state_ of the qubit.

Physically, for the superconducting qubit to behave as the abstract notion of the qubit, the device must be at drastically low temperatures. In the IBM Quantum Lab, we keep the temperature so cold \(15 milliKelvin in a dilution refrigerator\) that there is no ambient noise or heat to excite the superconducting qubit. Once our system has gotten cold enough, which takes several days, the superconducting qubit reaches equilibrium at the ground state $$|0\rangle$$.

In the future, quantum programmers will not notice what kind of physical systems and interactions their qubits and gates are built from. Current prototype devices, however, can sometimes experience spurious effects. Though we usually simply label this as 'noise', it does provide a glimpse at the physics behind the devices.

To see some evidence that $$|0\rangle$$ really is the ground state, try running the QASM below. Here, as in all quantum circuits, the qubit is initially prepared in the ground state $$|0\rangle$$. We then immediately follow this by the standard measurement. From a simulation \(or some cached examples\) you should find that the output always comes out as `0`. For a run on a real device there will be some randomness due to  imperfect measurements and/or residual heating of the qubit, but it should still output `0` with very high probability. 

```cpp
// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
measure q -> c;
```

To see what happens for a qubit in state $$|1\rangle$$, we need to be able to change the state of the qubit. This is done with the bit-flip gate, $$X$$, which flips the $$|0\rangle$$ to a  $$|1\rangle$$. Try running it, by implementing the complete QASM file below.

```cpp
// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
x q[0];
measure q -> c;
```

If you use the simulator, you will find the result `1` with certainty. This shows that the $$X$$ gate succeeded in preparing the state $$|1\rangle$$. If you use the real device, you'll see that the result `1` comes with high probability.

The crucial thing to notice from your results is that a $$|0\rangle$$ on the real device is more likely to output `0` than a $$|0\rangle$$ is to output `1`. The $$|1\rangle$$appears to experience less noise. This is precisely because $$|1\rangle$$ is the high state in our qubits. If noise gives it the chance, it will take the opportunity to 'fall down' to the lower energy  $$|0\rangle$$ state. So with these two simple experiments, you were able to probe the physics of our devices.

### Decoherence

Real quantum computers must deal with [decoherence](https://en.wikipedia.org/wiki/Quantum_decoherence), or the loss of information due to environmental disturbances \(noise\). The Bloch vector formalism we introduced in the previous section is sufficient to describe the state of the system under decoherence processes.

So far, all single qubit states we have seen have satisfied

$$
\langle X \rangle^2 + \langle Y \rangle^2 + \langle Z \rangle^2 = 1.
$$

These are known as [pure states](https://en.wikipedia.org/wiki/Quantum_state#Pure_states). They correspond to points on the surface of the Bloch sphere, and can be represented using vectors.

More generally, it is useful to represent states in terms of matrices. For a state vector $$|\psi\rangle$$, the corresponding matrix is given by the [outer product](../universality-of-quantum-computation/universality.md),

$$
\rho = |\psi\rangle\langle\psi|.
$$

States that cannot be represented as pure states are called [mixed states](https://en.wikipedia.org/wiki/Quantum_state#Mixed_states). The matrix for these is known as the [density matrix](https://en.wikipedia.org/wiki/Density_matrix), and can be written as a sum over pure states

$$
\rho = \sum_j p_j  |\psi_j\rangle\langle\psi_j|.
$$

These correspond to a point that sits inside the Bloch sphere,

$$
\langle X \rangle^2 + \langle Y \rangle^2 + \langle Z \rangle^2 \leq 1.
$$

Here these quantities can be calculated as $$\langle X \rangle = {\rm tr}(X \rho)$$, etc.

#### Energy relaxation and $$T_1$$ 

One important decoherence process is called _energy relaxation_, where the excited $$|1\rangle$$ state decays toward the ground state$$|0\rangle$$. The time constant of this process, , is an extremely important figure-of-merit for any implementation of quantum computing, and one in which IBM has made great progress in recent years, ultimately leading to the prototype quantum computer you are now using. Experiment with the circuits below to see how adding many repetitions of additional do-nothing Idle Idgates \(or Identity gates; these are gates that do nothing but wait\) before measurement causes the state to gradually decay towards $$|0\rangle$$.

Measuring $$T_1$$can be done using the composer, but it requires many circuits to be submitted. This is therefore a job that is better suited to the composer's programmatic sibling: [Qiskit](https://learnqiskit.gitbook.io/developers/).

#### Dephasing and $$T_2$$ 

Dephasing is another decoherence process, and unlike energy relaxation, it affects only superposition states. It can be understood solely in a quantum setting as it has no classical analog. The time constant $$T_2$$ includes the effect of dephasing as well as energy relaxation, and is another crucial figure-of-merit. Again, IBM has some of the world’s best qubits by this metric. Practice with the scripts below to investigate the Ramsey and echo experiments. A Ramsey experiment measures $$T_2^*$$ , which can be affected by slow noise, and the echo experiment removes some of this noise.

Because $$T_2$$ is such an important quantity, it is interesting to chart how far the community of superconducting qubits has come over the years. Here is a graph depicting $$T_2$$ versus time over the past two decades.

![image0](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/T2h1lc19xmqrdlsor.png)

