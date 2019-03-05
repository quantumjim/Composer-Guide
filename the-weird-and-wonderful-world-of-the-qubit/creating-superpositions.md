# Implementing measurements

In the last section, we talked about superposition states. Now it is time to make one. The simplest way to do this is with the Hadamard gate, $$H$$. In the Composer, this is the blue gate labeled $$H$$.

![](../.gitbook/assets/screen-shot-2018-12-05-at-14.46.07.png)

To make your first superposition, just use the circuit shown below. It starts, as always, with a qubit in the $$|0\rangle$$ state. It then applies an $$H$$ gate to this, and does a standard measurement straight after. Run this example, and see what you find.

```cpp
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
h q;
measure q -> c;
```

This results should give a `0` around half the time, and a `1` the rest of the time. Much like flipping a fair coin, the results should be fairly close to 50/50 \(running on the real device will give less-than-ideal results, due to noise and errors\).

This shows us one possible application of quantum computers: generating random numbers. But don't take the coin flipping analogy too literally. Randomness in quantum mechanics is due to a very different process. To see this, run the experiment again, but this time with two $$H$$ gates in succession. If the $$H$$ gate were the analog of a coin flip, this would mean flipping it twice. When you flip a coin twice in a row, you would still expect a 50/50 distribution. Below is a Qasm for this experiment that you can run.

```cpp
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
h q;
h q;
measure q -> c;
```

If you are expecting the same effects as a double coin flip, the results will be suprising. Unlike the classical case, the result is certain to be `0`. The double Hadamard returned the qubit to the $$|0\rangle$$state. Quantum randomness is not simply like a classical random coin flip.

Now let's figure out what happened in these two experiments using our vector and matrix notation. The Hadamard is represented by the matrix

$$
H =\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.
$$

 The effect of a single $$H$$ gate is therefore to transform a $$|0\rangle$$state into a certain superposition state

$$
H |0\rangle = H \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

We call this the $$|+\rangle$$ state. It is written in Dirac notation as

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt{2}}.
$$

If we measure this directly, the qubit is forced to choose between $$|0\rangle$$ and $$|1\rangle$$ with equal probability. So that's why we see the random result.

For the case of the two Hadamards, there are two stories we can tell that explain what happened. They are equivalent and both equally valid.

In the first, we simply ask what happens when an $$H$$ is applied to the $$|+\rangle$$ state. If you apply the $$H$$matrix to this state, you find that it transforms $$|+\rangle$$ to $$|0\rangle$$, and and so the second $$H$$ completely undoes the effect of the first.

For the second story, we will need an alternative way to measure qubit states. This is called the _x basis measurement_. Since the z basis measurement is done in the composer using a box with a 'z' inside, you might expect that the x measurement has a similar box with an 'x'. But this is not the case. The physics of our qubits means that we can only directly perform one type of measurement. All others must be done indirectly, by using gates immediately before measurement to prepare the qubit. Here's what we need for an x measurement.

![](../.gitbook/assets/screen-shot-2018-11-30-at-15.03.18.png)

This is a Hadamard immediately before the measurement, which gives us a way to rethink our two Hadamard circuit. Instead of two Hadamards, we can think of it as one Hadamard that creates the $$|+\rangle$$ state, followed by an x measurement.

So what happens when you do an x measurement of a $$|+\rangle$$ state? We already know the result from before. We get the outcome `0` with certainty.

There is also a state that gives us a `1` with certainty when making an x measurement. For this we simply do the same as before, but apply the Hadamard to the $$|1\rangle$$ state instead.

```cpp
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit

x q; // prepare a |1⟩ state using an x gate
h q; // apply a Hadamard

//perform an x measurement
h q;
measure q -> c;
```

The first Hadamard transforms the $$|1\rangle$$into a new kind of superposition. From the matrix form of the gate, we find that this is

$$
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt{2}}.
$$

The second Hadamard is part of an x measurement of the $$|-\rangle$$ state. By running the experimement, you'll find out what the result of this is. An x measurement of $$|-\rangle$$ always outputs a `1`.

The  $$|+\rangle$$ and  $$|-\rangle$$  states therefore play the same role for the x measurement as $$|0\rangle$$ and $$|1\rangle$$ do for the z measurement. Each represents a basis, with which we can express all other states as superpositions.

$$
|0\rangle=\frac{|+\rangle+|-\rangle}{\sqrt{2}}.
$$

For this reason, we shouldn't think of  $$|0\rangle$$ and $$|1\rangle$$ as the only two definite states, and that everything else is somehow random. Every possible superposition state is just as deterministic, as long as you find the right way of measuring it. And for a different way of measuring, every state can be completely random.

This is the main thing to take away from this section:

* a physical system in a definite state can still behave randomly.

This is the first of the key principles of the quantum world. It needs to become your new intuition, as it is what makes quantum systems different to classical systems.

{% hint style="info" %}
After a z measurement, the qubit is always in the state  $$|0\rangle$$ or $$|1\rangle$$. After an x measurement, it should always be in the state $$|+\rangle$$ and  $$|-\rangle$$. But this is not true for the way we have defined the x measurement in this section. 

Think about the following.

1. What needs to be added to create a full x measurement?
2. Why was the version we used here still valid for our arguments?
{% endhint %}





