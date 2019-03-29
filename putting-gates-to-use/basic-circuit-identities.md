# Basic circuit identities

When we program quantum computers, our aim is always to build useful quantum circuits from the basic building blocks. But sometimes, we might not have all the basic building blocks we want. In this section, we'll look at how we can transform basic gates to each other, and how to use them to build some gates that are slightly more complex \(but still pretty basic\).

Many of the techniques discussed in this chapter where first proposed in [Barenco, et al. 1995](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.3457?cm_mc_uid=43781767191014577577895&cm_mc_sid_50200000=1460741020).

### Making a CZ from a CX

The controlled-Z  or $$CX$$ gate is another well used two-qubit gate. Just as the controlled-NOT applies an $$X$$ to its target qubit whenever its control is in state $$|1\rangle$$, the controlled- $$Z$$ applies a $$Z$$ in the same case. In QASM it can be invoked directly with

```c
\\ a controlled-Z
cz q[c], q[t];
```

Where c and t are the control and target qubits. But in IBMQ devices, the only kind of two-qubit gate that can be directly applied is the controlled-NOT. We therefore need a way to transform one to the other.

The process for this is quite simple. We know that the Hadamard has the effect

$$
H X H = Z,\\
H Z H = X.
$$

So all we need to do is precede and follow the CNOT with a Hadamard on the target qubit. This will transform any $$X$$ that it applies on that qubit into a $$Z$$ .

```text
\\ also a controlled-Z
h q[t];
cx q[c], q[t];
h q[t];
```

The same trick can be used to transform a $$CX$$ into a $$CZ$$.

More generally we can transform a single controlled-NOT into a controlled version of any rotation around the Bloch sphere by an angle $$\pi$$ , by simply preceding and following it with the correct rotations. For example, a controlled-$$Y$$.

```c
\\ a controlled-Y
s q[t];
cx q[c], q[t];
sdg q[t];
```

and a controlled-Hadamard

```c
\\ a controlled-H
u3(-pi/4,0,0) q[t];
cx q[c], q[t];
u3(pi/4,0,0) q[t];
```

### Swapping Qubits

Sometimes, we need to move information around in a quantum computer. For some ways of implementing qubits, this could be done by physically moving them. Another option is simply to move the state between two qubits. This is done by the SWAP gate.

```c
\\ swaps states of qubits a and b
swap q[a], q[b];
```

The command above directly invokes this gate, but let's see how we might make it using our standard gate set. For this, we'll need to consider a few examples.

 First, we'll look at the case that qubit a is in state $$|1\rangle$$ and qubit b is in state $$|0\rangle$$. For this we'll apply the following gates

```c
\\ swap a 1 from a to b
cx q[a], q[b]; \\ copies 1 from a to b
cx q[b], q[a]; \\ uses the 1 on b to rotate a to 0
```

This has the effect of giving is the state where it is now qubit b in state $$|1\rangle$$ and qubit a in state $$|0\rangle$$. In this case at least, we have done a SWAP.

Now let's take this state and SWAP back to the original one. Clearly, we can do this with the reverse of the above process

```c
\\ swap a q from b to a
cx q[b], q[a]; \\ copies 1 from b to a
cx q[a], q[b]; \\ uses the 1 on a to rotate b to 0
```

Note that in these two processes, the first gate of one would have no effect on the initial state of the other. For example, when we swap the $$|1\rangle$$ b to a, the first gate is `cx q[b], q[a]`. If this were instead applied to a state where no$$|1\rangle$$ was initially on b, it would have no effect.

Note also that for these two process, the final gate of one would have no effect on the final state of the other. For example, the final `cx q[b], q[a]` that is required when we swap the$$|1\rangle$$ from a to b has no effect on the state where the $$|1\rangle$$ is not on b.

With these observations, we can combine the two processes, by adding an ineffective gate from one onto the other. For example

```c
cx q[b], q[a];
cx q[a], q[b];
cx q[b], q[a];
```

We can think of this as a process that swaps a $$|1\rangle$$ from a to b, but with a useless `cx q[b], q[a]` at the beginning. We can also think of it as a process that swaps a $$|1\rangle$$ from b to a, but with a useless `cx q[b], q[a]` at the end. Either way, the result is a process that can do the swap both ways around.

It also has the correct effect on the $$|00\rangle$$ state. This is symmetric, and so swapping the states should have no effect. Since the controlled-NOT gates have no effect when their control qubits are $$|0\rangle$$, the process correctly does nothing.

The $$|11\rangle$$ state is also symmetric, and so needs a trivial effect from the swap. In this case, the first controlled-NOT gate in the process above will cause the second to have no effect, and the third undoes the first. So the whole effect is indeed trivial.

We have therefore found a way to decompose SWAP gates into our standard gate set of single qubit rotations and CX gates.

```c
\\ swaps states of qubits a and b
cx q[b], q[a];
cx q[a], q[b];
cx q[b], q[a];
```

It works for the states $$|00\rangle$$, $$|01\rangle$$, $$|10\rangle$$ and$$|11\rangle$$, and so also for all superpositions of them. It therefore swaps all possible two qubit states.

The same effect would also result if we changed the order of the controlled-NOT gates

```c
\\ swaps states of qubits a and b
cx q[b], q[a];
cx q[a], q[b];
cx q[b], q[a];
```

This is an equally valid way to get the controlled-NOT gate.

The derivation used here was very much based on the z basis states, but it could also be done by thinking about what is required to swap qubits in states $$|+\rangle$$ and $$|-\rangle$$. The resulting ways of implementing the SWAP gate will be completely equivalent to the ones here.

### Making the CXs we need from CXs we have

The gates in any quantum computer are driven by the physics of the underlying system. In IBMQ devices, the physics behind `cx`s means that they cannot be directly applied to all possible pairs of qubits. For those pairs for which a `cx` can be applied, it typically has a particular orientation. So one specific qubit must act as control, and the other must act as the target, without allowing us to choose.

#### Changing the direction of a CNOT

Let's deal with the second problem described above: If we have a controlled-NOT with control qubit $$c$$ and target qubit $$t$$, how can we make one for which qubit $$t$$ acts as the control and qubit $$c$$ is the target?

This question would be very simple to answer for the controlled-$$Z$$. For this gate, it doesn't matter which way around the control and target qubits are. So

```c
cz q[c], q[t];
```

has exactly the same effect as 

```c
cz q[t], q[c];
```

This means that we can think of either either one as the control, and the other as the target.

To see why this is true, let's remind ourselves of what the Z gate is,

$$
Z= \begin{pmatrix} 1&0 \\ 0&-1 \end{pmatrix}.
$$

We can think of this as multiplying the state by $$-1$$, but only when it is $$|1\rangle$$.

For a controlled-$$Z$$ gate, the control qubit must be in state $$|1\rangle$$for a $$Z$$ to be applied to the target qubit. Given the above property of $$Z$$, this only has an effect when the target is in state $$|1\rangle$$. We can therefore simply think of the controlled-$$Z$$ gate as one which multiplies the state of two qubits by $$-1$$, but only when they are in the state is $$|11\rangle$$.

This new interpretation is phrased in a perfectly symmtric way, and so shows that the labels of 'control' and 'target' are not necessary for this gate.

This property gives us a way to reverse the orientation of a controlled-NOT. We can first turn the controlled-NOT into a controlled-$$Z$$ by using the method described earlier: placing an `h` both before and after on the target qubit.

```c
// a cz
h q[t];
cx q[c], q[t];
h q[t];
```

Then since we are free to choose which way around to think of the action of a controlled-$$Z$$, we can choose to simply start thinking of t as the control and c as the target. Then we can transform this controlled-$$Z$$ into a corresponding controlled-NOT. We just need to place a Hadamard both before and after on the target qubit \(which is now qubit c\).

```c
// a cx with control qubit t and target qubit c
h q[c];
h q[t];
cx q[c], q[t];
h q[t];
h q[c];
```

And there we have it: we've turned around the controlled-NOT. All that is needed is a Hadamard on both qubits before and after.

The rest of this subsection is dedicated to another explantion of how to turn around a CX, with a bit more math and some different insight. Feel free to skip over it.

Here is another way to write the CX gate

$$
{\rm CX}_{c,t} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes X.
$$

Here the $$|1\rangle\langle1|$$ ensures that the second term only affects those parts of a superposition for which the control qubit c is in state $$|1\rangle$$. For those, the effect on the target qubit t is $$X$$. The first terms similarly address those parts of the superposition for which the control qubit is in state $$|0\rangle$$, in which case it leaves the target qubit unaffected.

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

With these we can factorize the parts of the controlled-NOT expressed with the $$|0\rangle$$ and $$|1\rangle$$state,

$$
{\rm CX}_{c,t} = I \otimes |+\rangle\langle+| ~~+~~  Z \otimes |-\rangle\langle-|
$$

This gives us a whole new way to interpret the effect of the controlled-NOT. The $$Z \otimes |-\rangle\langle-| $$ term addresses the parts of a superposition for which qubit t is in state $$|-\rangle$$ and then applies a $$Z$$ gate to qubit c. The other term similarly does nothing to qubit $$c$$ when qubit $$t$$ is in state $$|+\rangle.$$ 

In this new interpretation, it is qubit t that acts as the control. It is the $$|+\rangle$$ and $$|-\rangle$$states that decide whether an action is performed, and that action is the gate $$Z$$. This sounds like a quite different gate to our familar controlled-NOT, and yet it is the controlled-NOT. These are two equally true descriptions of its effects.

Among the many uses of this property is the method to turn around a controlled-NOT. For example, consider applying a Hadamard to qubit c both before and after this controlled-NOT

```c
h q[c];
cx q[c], q[t];
h q[c];
```

This transforms the $$Z$$ in the $$Z \otimes |-\rangle\langle-| $$ term into an $$X$$, and leaves the other term unchanged. The combined effect is then a gate that applies an $$X$$ to qubit c when qubit t is in state $$|-\rangle$$. This is halfway to what we are wanting to build.

To complete the process, we can apply a Hadamard both before and after on qubit $$t$$. This transforms the $$|+\rangle$$ and $$|-\rangle$$ states in each term into $$|0\rangle$$ and $$|1\rangle$$. Now we have something that applies an $$X$$ to qubit c when qubit t is in state $$|1\rangle$$. This is exactly want we want: a controlled-NOT in reverse, with qubit t as the control and c as the target.

#### CX between distant qubits

Suppose we have a control qubit c and a target qubit t, and we want to do a controlled-NOT gate between them. If this gate is directly possible on a device, we can just do it. If it's only possible to do the controlled-NOT in the wrong direction, we can use the method explained above. But what if qubits c and t are not connected at all?

If qubits c and t are on completely different devices in completely different labs in completely different countries, you may be out of luck. But consider the case where it is possible to do a controlled-NOT between qubit c and an additional qubit a, and also allowed to do one between qubits a and t. The new qubit can then be used to mediate the interaction between c and t.

One way to do this is using the SWAP gate. We can simply SWAP a and t, do the controlled-NOT between c and a, and then swap a and t back again. The end result is that we have effectively done a controlled-NOT between c and t. The drawback of this method is that it costs a lot of controlled-NOT gates, with six needed to implement the two SWAPs.

Another method is to use the following sequence of gates.

```c
// a CX between qubits c and t, with no end effect on qubit a
cx q[a], q[t];
cx q[c], q[a];
cx q[a], q[t];
cx q[c], q[a];
```

To see how this works, first consider the case where qubit a is in state $$|0\rangle$$. The effect of the `cx q[c], q[a]` gates in this case are trivial. This leaves only the two `cx q[a], q[t]` gates, which cancel each other out. The net effect is therefore that nothing happens.

If qubit a is in state $$|0\rangle$$, things are not quite so simple. The effect of the `cx q[c], q[a]` gates is to toggle the value of qubit a: it turns any $$|0\rangle$$ in the state of qubit a into $$|1\rangle$$ and back again, and vice-versa.

This toggle effect affects the action of the two `cx q[a], q[t]` gates. It ensures that whenever one is controlled on a $$|0\rangle$$ and has trivial effect, the other is controlled on a $$|1\rangle$$ and applies an $$X$$ to qubit t. The end effect is that qubit a is left unchanged, but qubit t will always have had an $$X$$ applied to it.

Putting everything together, this means that an $$X$$ is applied to qubit t only when qubit c is in state $$|1\rangle$$. Qubit a is left unaffected. We have therefore engineered a controlled-NOT between qubits c and t. Unlike for the use of SWAP gates, this required only four controlled-NOT gates to implement.

It is similarly possible to engineer controlled-NOT gates when there is a longer chain of qubits required to connect our desired control and target. The methods described above simply need to be scaled up.

### Controlled rotations

We have already seen how to build controlled $$\pi$$ rotations from a single controlled-NOT gate. Now we'll look at how to build any controlled rotation.

First, let's consider arbitary rotations around the y axis. Specifically, consider the following sequence of gates \(recall that `u3(theta/2,0,0)` is the way to implement an $$R_y(\theta/2)$$ rotation in OpenQASM\).

```c
u3(theta/2,0,0) q[t];
cx q[c], q[t];
u3(-theta/2,0,0) q[t];
cx q[c], q[t];
```

If the control qubit is in state $$|0\rangle$$, all we have here is a `u3(theta/2,0,0)` immediately followed by its inverse, `u3(-theta/2,0,0)`. The end effect is trivial. If the control qubit is in state $$|1\rangle$$, however, the `u3(-theta/2,0,0)` is effectively preceded and followed by an X gate. This has the effect of flipping the direction of the y rotation and making a second `u3(theta/2,0,0)`. The net effect in this case is therefore to make a controlled version of the rotation $$R_y(\theta)$$ . 

This method works because the x and y axis are orthogonal, which causes the x gates to flip the direction of the rotation. It therefore similarly works to make a controlled $$R_z(\theta)$$ . A controlled $$R_x(\theta)$$ could similarly be made using  controlled-NOT  gates.

We can also make a controlled version of any single qubit rotation, $$U$$. For this we simply need to find three rotations A, B and C and a phase $$\alpha$$ such that

$$
ABC = I, ~~~e^{i\alpha}AXBXC = U
$$

We then use  controlled-NOT  gates to cause the first of these relations to happen whenever the control is in state $$|0\rangle$$, and the second to happen when the control is state $$|1\rangle$$. An $$R_z(\alpha)$$ rotation is also used on the control to get the right phase, which will be important whenever there are superposition states.

```c
a q[t];
cx q[c], q[t];
b q[t];
cx q[c], q[t];
c q[t];
u1(alpha) q[c];
```

![](../.gitbook/assets/zzzabc.png)

Here a, b and c are gates that implement $$A$$ , $$B$$ and $$C$$ , and must be defined via a subroutine. For example, if we wanted A to be $$R_x(\pi/4)$$, the subroutine would be defined as

```c
gate a qubit
{
        u3(pi/4,pi/2,-pi/2) qubit;
}
```

### The Toffoli

The Toffoli gate is a three qubit gate with two controls and one target. It performs an X on the target only if both controls are in the state $$|0\rangle$$. The final state of the target is then equal to either the AND or the NAND of the two controls, depending on whether the initial state of the target was $$|0\rangle$$ or $$|1\rangle$$. Toffoli can also be thought of a controlled-controlled-NOT, and is also called the CCX gate.

```c
ccx q[c], q[t];
```

To see how to build it from single and two qubit gates it is actually easiest to show how to build something even more general: an arbitary controlled-controlled-U for any single qubit rotation U. For this we need to define controlled versions of $$V = \sqrt{U}$$ and $$V^\dagger$$. In the OpenQASM code below, we assume that subroutines `cv` and `cvdg` have been defined for these, respectively. The controls are qubits a and b, and the target is qubit t.

```c
cv q[b], q[t];
cx q[a], q[b];
cvdg q[b], q[t];
cx q[a], q[b];
cv q[a], q[t];
```

![](../.gitbook/assets/zzzuv.png)

By tracing through each value of the two control qubits, you can convince yourself that a Ugate is applied to the target qubit if and only if both controls are 1. Using ideas we have already described, you could now implement each controlled-Vgate to arrive at some circuit for the doubly-controlled-Ugate. It turns out that the minimum number of controlled-NOT gates required to implement the Toffoli gate is 6 \[[Shende and Markov, 2009](http://dl.acm.org/citation.cfm?id=2011799)\].

![](../.gitbook/assets/zzzttt.png)

The Toffoli is not th unique way to implement an AND gate with quantum computing. We could also define other gates that have the same effect, but which also introduce relative phases. In these cases, we can implement the gate with fewer controlled-NOTs.

For example, suppose let's spend a controlled-NOT to create a controlled-Hadamard.

```c
gate ch c, t
{
        u3(-pi/4,0,0) t;
        cx c,t;
        u3(pi/4,0,0) t;
}
```

We'll also use the controlled-$$Z$$ gate, which costs the same as acontrolled-NOT, to implement the following circuit.

```c
ch q[a], q[t];
cz q[b], q[t];
ch q[a], q[t];
```

For the state $$|00\rangle$$ on the two controls, this does nothing to the target. For $$|11\rangle$$ the target experiences a $$Z$$ gate that si both preceded and followed by an H. The net effect is an$$X$$ on the target. For the states $$|01\rangle$$ and $$|10\rangle$$ the target experiences either just the two Hadamards \(which cancel each other out\) or just the $$Z$$ \(which only induces a relative phase\). This therefore also reproduces the effect of an AND, because the value of the target is only changed for the $$|11\rangle$$ state on the controls. But it does it with the equivalent of just three controlled-NOT gates.

### Arbitrary rotations from H and T

The qubits in current devices are subject to noise, which basically consists of gates that are done by mistake. Simple things like temperature, stray magnetic fields or activity on neighbouring qubits can make things happen that we didn't intend.

For large applications of quantum computers, it will be neccesary to encode our qubits in a way that protects them from this noise. This is done by making gates much harder to do by mistake, or to implement in a manner that is slightly wrong.

This is unfortunate for the single qubit rotations  $$R_x(\theta)$$, $$R_y(\theta)$$ and $$R_z(\theta)$$. It is impossible to implent an angle $$\theta$$ with perfect accuracy, such that you are sure that you are not accidentally implementing something like $$\theta + 0.0000001$$. There will always be a limit to the accuracy we can achieve. This will always be larger than is tolarable for large circuits where the imperfections will build up. We will therefore not be able to implement these rotations directly in fault-tolerant quantum computers, but will instead need to build them in a much more deliberate manner.

Fault-tolerant schemes typical perform these rotations using multiple applications of just two gates: $$H$$ and $$T$$.

The T gate can be expressed in OpenQASM as

```c
t q[0]; // T gate on qubit 0
```

It is a rotation around the z axis by $$\theta = \pi/4$$, and so be expressed mathematically as $$R_z(\pi/4) = e^{i\pi/4~Z}$$ .

In the following we assume that the $$H$$ and $$T$$ gates are effectively perfect. This can be engineered by suitable methods for error correction and fault-tolerance.

Using the Hadamard, and the methods discussed in the last chapter, we can use the T gate to create a similar rotation around the x axis.

```c
h q[0];
t q[0];
h q[0];
```

Now let's put the two together. Let's make the gate $$R_z(\pi/4)~R_x(\pi/4)$$.

```c
h q[0];
t q[0];
h q[0];
t q[0];
```

Since this is a single qubit gate, we can think of it as a rotation around the Bloch sphere. That means that it is a rotation around some axis by some angle. We don't need to think about the axis too much here, but it clearly won't be simply x, y or z. More important is the angle.

The crucial property of the angle for this rotation is that it is irrational. You can prove this yourself with a bunch of math, but you can also see the irrationality in action by applying the gate. Repeating it n times results in a rotation around the same axis by a different angle. Due to to the irrationality, the angles that result from different repetitions will never be the same.

We can use this to our advantage. Each angle will be somewhere between $$0$$ and $$2\pi$$. Let's split this iterval up into $$n$$ slices of width $$2\pi/n$$. For each repetition, the resulting angle will fall in one of these slices. If we look at the angles for the first $$n+1$$ repetitions, it must be true that at least one slice contains two of these angles. Let's use $$n_1$$ to denote the number of repetitions required for the first, and $$n_2$$ for the second.

With this, we can prove something about the angle for $$n_2-n_1$$ repetitions. This is effectively the same as doing $$n_2$$ repetitions, followed by the inverse of $$n_1$$ repetitions. Since the angles for these are not equal \(because of the irrationality\) but also differ by no greater than $$2\pi/n$$ \(because they correspond to the same slice\) the angle for $$n_2-n_1$$ repetitions satisfies

$$
\theta_{n_2-n_1}  \neq 0, ~~~~-\frac{2\pi}{n}  \leq \theta_{n_2-n_1} \leq \frac{2\pi}{n} .
$$

We therefore have the ability to do rotations around small angles. We can use this to rotate around angles that are as small as we like, just by increasing the number of times we repeat this gate.

By using many small angle rotations, we can also rotate by any angle we like. This won't always be exact, but it is guaranteed to be accurate up to $$2\pi/n$$, which can be made as small as we like. We therefore now have power over the inaccuracies in our rotations.

So far, we only have the power to do these arbitrary rotations around one axis. For a second axis, we simply do the $$R_z(\pi/4)$$ and $$R_x(\pi/4)$$ rotations in the opposite order.

```c
h q[0];
t q[0];
h q[0];
t q[0];
```

The axis that corresponds to this rotation is not the same as that for the gate considered previously. We therefore now have arbitrary rotation around two axes, which can be used to generate any arbitrary rotation around the Bloch sphere. We are back to being able to do everything, though it costs quite a lot of $$T$$ gates.

It is because of this kind of application that $$T$$ gates are so prominent in quantum computation. In fact, the complexity of algorithms for fault-tolerant quantum computers is often quoted in terms of how many $$T$$ gates they'll need. This motivates the quest to achieve things with a few $$T$$ gates as possible. Note that the discussion above was simply intended to prove that $$T$$ gates can be use in this way, and does not represent the most efficient method we know.



 

