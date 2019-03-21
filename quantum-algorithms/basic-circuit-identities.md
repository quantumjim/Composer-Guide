# Basic circuit identities

When we program quantum computers, our aim is always to build useful quantum circuits from the basic building blocks. But sometimes, we might not have all the basic building blocks we want. In this section, we'll look at how we can transform basic gates to each other, and how to use them to build some gates that are slightly more complex \(but still pretty basic\).

### Making a CZ from a CX

The controlled-Z  or `cz` gate is another well used two-qubit gate. Just as the `cx` applies an `x` to its target qubit whenever its control is in state $$|1\rangle$$, the `cz`applies a `z` in the same case. In QASM it can be invoked directly with

```text
\\ a controlled-Z
cz q[c], q[t];
```

Where `c` and `t` are the control and target qubits. But in IBMQ devices, the only kind of two-qubit gate that can be directly applied is the`cx`. We therefore need a way to transform one to the other.

The process for this is quite simple. We know that the Hadamard has the effect

$$
H X H = Z,\\
H Z H = X.
$$

So all we need to do is precede and follow the CNOT with a Hadamard on the target qubit. This will transform any `x` that it applies on that qubit into a `z`.

```text
\\ also a controlled-Z
h q[t];
cx q[c], q[t];
h q[t];
```

The same trick can be used to transform a `cx` into a `cz`.

### Swapping Qubits

Sometimes, we need to move information around in a quantum computer. For some ways of implementing qubits, this could be done by physically moving them. Another option is simply to move the state between two qubits. This is done by the SWAP gate.

```text
\\ swaps states of qubits a and b
swap q[a], q[b];
```

To see how we might make this, let's consider a few examples

 First, we'll look at the case that qubit a is in state $$|1\rangle$$ and qubit b is in state $$|0\rangle$$. For this we'll apply the following gates

```text
\\ swap a 1 from a to b
cx q[a], q[b]; \\ copies 1 from a to b
cx q[b], q[a]; \\ uses the 1 on b to rotate a to 0
```

This has the effect of giving is the state where it is now qubit b in state $$|1\rangle$$ and qubit a in state $$|0\rangle$$. In this case at least, we have done a SWAP.

Now let's take this state and SWAP back to the original one. Clearly, we can do this with the reverse of the above process

```text
\\ swap a q from b to a
cx q[b], q[a]; \\ copies 1 from b to a
cx q[a], q[b]; \\ uses the 1 on a to rotate b to 0
```

Note that in these two processes, the first gate of one would have no effect on the initial state of the other. For example, when we swap the $$|1\rangle$$ a to b, the first gate is `cx q[a], q[b]`. If this were instead applied to a state where no$$|1\rangle$$ was initially on a, it would have no effect.

Note also that for these two process, the final gate of one would have no effect on the final state of the other. For example, the final `cx q[b], q[a]` that is required when we swap the$$|1\rangle$$ from a to b has no effect on the state where the $$|1\rangle$$ is not on b.





### Making the CXs we need from CXs we have

The gates in any quantum computer are driven by the physics of the underlying system. In IBMQ devices, the physics behind `cx`s means that they cannot be directly applied to all possible pairs of qubits. For those pairs for which a `cx` can be applied, it typically has a particular orientation. So one specific qubit must act as control, and the other must act as the target, without allowing us to choose.

#### Changing the direction of a CNOT

Let's deal with the second problem described above: If we have a `cx` with control qubit $$c$$ and target qubit $$t$$, how can we make one for which qubit $$t$$ acts as the control and qubit $$c$$ is the target?

This question would be very simple to answer for the `cz`. For this gate, it doesn't matter which way around the control and target qubits are. So

```text
cz q[c], q[t];
```

has exactly the same effect as 

```text
cz q[t], q[c];
```

This means that we can think of either either one as the control, and the other as the target.

To see why this is true, let's remind ourselves of what the Z gate is,

$$
Z= \begin{pmatrix} 1&0 \\ 0&-1 \end{pmatrix}.
$$

We can think of this as multiplying the state by $$-1$$, but only when it is $$|1\rangle$$.

For a CZ gate, the control qubit must be in state $$|1\rangle$$for a Z to be applied to the target qubit. Given the above property of Z, this only has an effect when the target is in state $$|1\rangle$$. We can therefore simply think of the CZ gate as one which multiplies the state of two qubits by $$-1$$, but only when they are in the state is $$|11\rangle$$.

This new interpretation is phrased in a perfectly symmtric way, and so shows that the labels of 'control' and 'target' are not necessary for this gate.

This property gives us a way to reverse the orientation of a `cx`. We can first turn the `cx` into a `cz` by using the method described earlier: placing an `h` both before and after on the target qubit.

```text
// a cz
h q[t];
cx q[c], q[t];
h q[t];
```

Then since we are free to choose which way around to think of the action of a `cz`, we can choose to simply start thinking of `t` as the control and `c` as the target. Then we can transform this `cz` into a corresponding `cx`. We just need to place an `h` both before and after on the target qubit \(which is now qubit `c`\).

```text
// a cx with control qubit t and target qubit c
h q[c];
h q[t];
cx q[c], q[t];
h q[t];
h q[c];
```

And there we have it: we've turned around the `cx`. All that is needed is an `h` on both qubits before and after.

The rest of this subsection is dedicated to another explantion of how to turn around a CX, with a bit more math and some different insight. Feel free to skip over it.

Here is another way to write the CX gate

$$
{\rm CX}_{c,t} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes X.
$$

Here the $$|1\rangle\langle1|$$ ensures that the second term only affects those parts of a superposition for which the control qubit $$c$$ is in state $$|1\rangle$$. For those, the effect on the target qubit $$t$$  is $$X$$. The first terms similarly address those parts of the superposition for which the control qubit is in state $$|0\rangle$$, in which case it leaves the target qubit unaffected.

Now let's do a little maths. The $$X$$ gate has eigenvalues $$\pm 1$$ for the states $$|+\rangle$$ and $$|-\rangle$$. The $$I$$ gate has an eigenvalue of $$1$$ for all states including  $$|+\rangle$$ and $$|-\rangle$$. So we can write them in spectral form as

$$
X = |+\rangle\langle+| ~~-~~ |-\rangle\langle-|,~~ ~~~ I = |+\rangle\langle+| ~~+~~ |-\rangle\langle-|
$$

Substituting these into the expression above gives us

$$
{\rm CX}_{c,t} = |0\rangle\langle0| \otimes |+\rangle\langle+| ~~+~~  |0\rangle\langle0| \otimes |-\rangle\langle-| ~~+~~ |1\rangle\langle1| \otimes |+\rangle\langle+| ~~-~~  |1\rangle\langle1| \otimes |-\rangle\langle-|
$$

Using the states $$|0\rangle$$ and $$|1\rangle$$ we can write the $$Z$$ gate in spectral form, and also use an alternative \(but completely equivalent\) spectral form for $$I$$,

$$
Z = |0\rangle\langle0| ~-~ |1\rangle\langle1|, ~~~ I = |0\rangle\langle0| ~+~ |1\rangle\langle1|.
$$

With these we can factorize the parts of the `cx` expressed with the  $$|0\rangle$$ and $$|1\rangle$$state,

$$
{\rm CX}_{c,t} = I \otimes |+\rangle\langle+| ~~+~~  Z \otimes |-\rangle\langle-|
$$

This gives us a whole new way to interpret the effect of the `cx`. The $$Z \otimes |-\rangle\langle-| $$ term addresses the parts of a superposition for which qubit $$t$$ is in state $$|-\rangle$$ and then applies a $$Z$$ gate to qubit $$c$$. The other term similarly does nothing to qubit $$c$$ when qubit $$t$$ is in state $$|+\rangle.$$ 

In this new interpretation, it is qubit $$t$$ that acts as the control. It is the $$|+\rangle$$ and $$|-\rangle$$states that decide whether an action is performed, and that action is the gate $$Z$$. This sounds like a quite different gate to our familar `cx`, and yet it is the `cx`. These are two equally true descriptions of its effects.

Among the many uses of this property is the method to turn around a `cx`. For example, consider applying a Hadamard to qubit $$c$$ both before and after this `cx`

```text
h q[c];
cx q[c], q[t];
h q[c];
```

This transforms the $$Z$$ in the $$Z \otimes |-\rangle\langle-| $$ term into an $$X$$, and leaves the other term unchanged. The combined effect is then a gate that applies an $$X$$ to qubit $$c$$ when qubit $$t$$ is in state $$|-\rangle$$. This is halfway to what we are wanting to build.

To complete the process, we can apply a Hadamard both before and after on qubit $$t$$. This transforms the $$|+\rangle$$ and $$|-\rangle$$ states in each term into $$|0\rangle$$ and $$|1\rangle$$. Now we have something that applies an $$X$$ to qubit $$c$$ when qubit $$t$$ is in state $$|1\rangle$$. This is exactly want we want: a `cx` in reverse, with $$t$$ as the control and $$c$$ as the target.



