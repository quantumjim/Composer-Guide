# Entanglement and Bell Tests

### 

One of the infamous counterintuitive ideas of quantum mechanics is that two systems that appear too far apart to influence each other can nevertheless behave in ways that, though individually random, are too strongly correlated to be described by any classical local theory.

To understand this, we have outlined a simple Bell test experiment here. Imagine you have two systems \(see blue and red systems below\). Within each there are two measurements performed: A, A′, B and B′, that have outcomes $$\pm 1$$.

In quantum computing, we usually prefer for our two outcomes to be called `0` and `1`. So we usually associate the $$+1$$ value in a Bell test with `0`, and the $$-1$$ value with `1`.

Bell showed that if these measurements are chosen correctly for a given entangled state, the statistics can not be explained by any local hidden variable theory, and that there must be correlations that are beyond classical.                         

![image0](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.01.47%20PMp7ywz1fvomuhxgvi.png)

In 1969 [John Clauser](https://en.wikipedia.org/wiki/John_Clauser), [Michael Horne](https://en.wikipedia.org/w/index.php?title=Michael_Horne&action=edit&redlink=1), [Abner Shimony](https://en.wikipedia.org/wiki/Abner_Shimony), and [Richard Holt](https://en.wikipedia.org/w/index.php?title=Richard_Holt_%28physicist%29&action=edit&redlink=1) derived a quantity based on the correlation function such as

$$
\langle AB\rangle = p_{++}+p_{--}-p_{+-}-p_{-+}.
$$

Here $$p_{+-}$$ is the probability that a measurement of A gives the result$$+1$$ while a measurement of B gives $$-1$$. The quantity they derived was

$$
C = \langle AB\rangle-\langle AB'\rangle+\langle A'B\rangle+\langle A'B'\rangle
$$

This has the property the property that correlations provided by local hidden variable theories wll always satisfy $$|C| \leq 2$$. This is known as the CHSH inequality.

It is simple to show that this inequality must be true if the theory obeys the following two assumptions, _locality_ and _realism_:

 **Locality**: No information can travel faster than the speed of light. There is a hidden variable $$\lambda$$ that defines all the correlations so that

$$
\langle AB \rangle = \sum_\lambda P(\lambda) A(\lambda) B(\lambda)
$$

Here $$A(\lambda)=\pm1$$ denotes the outcome of the measurement A when the hidden variable takes the value $$\lambda$$.

With correlations of this form, C becomes

$$
C = \sum_k P(\lambda) \left[ A(\lambda) \left( B(\lambda) - B'(\lambda)\right) + A'(\lambda) \left( B(\lambda) + B'(\lambda)\right)\right].
$$

**Realism**: All observables have a definite value independent of the measurement \($$+1$$ or $$-1$$\). 

This allows us to concretely state that, since the values $$B(\lambda)$$ and $$B'(\lambda)$$ are both definitely either $$+1$$ or $$-1$$, and so must either be true that $$B(\lambda)=B'(\lambda)$$, or that  $$B(\lambda)=-B'(\lambda)$$. This means that, for the two quantities ****$$|B(\lambda) - B'(\lambda)|$$ and ****$$|B(\lambda) + B'(\lambda)|$$, one must be 0 while the other is 2. Putting this result into C above shows us that each term in the sum can be no greater than $$P(\lambda) \times 2$$. Since the $$P(\lambda)$$ are probabilities and sum to 1, this means that $$|C| \leq 2$$.

Perfectly reasonable, right? However, it is possible for us to measure correlations with $$|C| > 2$$. How is this possible? The above assumptions must not be valid, and this is one of those astonishing counterintuitive ideas necessary to accept in the quantum world. Before you launch the scores below, let’s try to understand what is happening and how each observable is measured and combined to give $$|C|$$ .

The Bell experiment we provide uses the entangled state $$\left( |00\rangle+|11\rangle\right)/\sqrt{2}$$ , and the two measurements for system A are Z and X, while the two for B are $$W = H$$ and $$V = ZHZ$$.

.

![image5](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2012.31.29%20AMggfwizai6qen4s4i.png)

For an ideal implementation the four correlated expectation values give,

$$
\langle ZW \rangle = \langle ZV \rangle = \langle XW \rangle = \frac{1}{\sqrt{2}}, ~~~\langle XV \rangle = -\frac{1}{\sqrt{2}}
$$

These give us $$|C| = 2\sqrt{2}$$, which is greater than 2.

To run this experiment with our hardware, we need the following quantum circuit and 4 measurements.             

               

![image7](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%201.15.27%20AMj7c275k02qyf1or.png)

In the first part of the experiment, the qubits are initially prepared in the ground state $$|00\rangle$$ . The $$H$$ takes the first qubit to the equal superposition $$(|00\rangle+|10\rangle)/\sqrt{2}$$ . The CNOT gate flips the second qubit if the first is in state $$|1\rangle$$ , making the state $$(|00\rangle+|11\rangle)/\sqrt{2}$$ . This is the entangled state \(commonly called a _Bell state_\) required for this test. In OpenQASM

```text
\\ making a Bell state
h q[0]
cx q[0], q[1];
```

 In the first experiment, the measurements are of the observable $$Z$$ and $$W=H$$ . To rotate the measurement basis to the $$W$$ basis, we can use the following

```text
\\ W measurement
s q[1];
h q[1];
t q[1];
h q[1];
measure q[1] -> c[1];
```

The correlator $$\langle ZW\rangle$$ should be close to $$1/\sqrt{2}$$ . The $$V$$ measurement is similarly performed with

```text
\\ V measurement
s q[1];
h q[1];
tdg q[1];
h q[1];
measure q[1] -> c[1];
```

The $$X$$ measurements of the first qubit can be done in the normal way. Combining these, we can look at the results for each pair of measurements and calculate the correlation functions.

Below the results of this experiment on a real device.

![image8](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%201.15.37%20AMbfusp4upndrc0udi.png)

Try it out for yourself! Compare what we got with the simulations \(with both ideal and realistic parameters\).

