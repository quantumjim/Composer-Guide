# Getting to know your qubits

As we've seen, there are multiple ways to extract an output from a qubit. The two methods we've use so far are the z and x measurements.

```text
// z measurement of qubit 0
measure q[0] -> c[0];

// x measurement of qubit 0
h q[0];
measure q[0] -> c[0];
```

There are many possible states that our qubits can be in. For some, they might give certain outputs with certainty. For others, the output might be random. To continue learning about qubits, we need a way to write down these states. We need some notation, and we need some math.

### The z basis

First, let's think about the z measurement. There is a state for which it is certain that this will output a `0`. We need a name for this state. Let's be unimaginative and call it $$0$$ . Similarly, the qubit state that is certain to output a `1` will be called $$1 $$ .

These two states are entirely disjoint. They are completely mutually exclusive. Either the qubit definitely outputs a `0`, or it definitely outputs a `1`.There is no overlap.

One way to represent this with mathematics is using two orthogonal vectors.

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} ~~~~ |1\rangle =\begin{pmatrix} 0 \\ 1 \end{pmatrix}.
$$

This is a lot of notation to take in all at once. First let's unpack the weird $$|$$ and  $$\rangle$$ . Their job is essentially just to remind us that we are talking about the vectors that represent qubit states labelled $$0$$ and $$1$$. This helps us distinguish them from things like the bit states `0` and `1` or the numbers 0 and 1. It is part of the bra-ket notation, introduced by Dirac.

If you are not familiar with vectors, they are essentially just lists of numbers. If we write them as a vertical list, as we have done above, they are called _column vectors_. In Dirac notation, they are also called _kets_.

 Horizontal lists are called 'row vectors'. In Dirac notation, these are called _bras_ and are represented with a $$\langle$$ and a $$|$$.

$$
\langle 0| = \begin{pmatrix} 1 & 0\end{pmatrix} ~~~~ \langle 1| =\begin{pmatrix} 0 & 1 \end{pmatrix}.
$$

Vectors also come with a set of rules on how to manipulate them. These define what it means to add two vectors, or to multiple two vectors. For example, to add two vectors we need them to be the same type and the same length. Then we add each element in one list to the corresponding element in the other.

$$
\begin{pmatrix} a_0 \\ a_1 \end{pmatrix} +\begin{pmatrix} b_0 \\ b_1 \end{pmatrix}=\begin{pmatrix} a_0+b_0 \\ b_0+b_1 \end{pmatrix}.
$$

Multiplying vectors is a bit more tricky, since there are multiple ways we can do it. For now we just need the so-called 'inner product'.

$$
\begin{pmatrix} a_0 & a_1 \end{pmatrix} \times \begin{pmatrix} b_0 \\ b_1 \end{pmatrix}= a_0~b_0 + a_0~b_1.
$$

Note that the right hand side of this equation contains only normal numbers being multipled and added in a normal way. The inner product of two vectors therefore yields just a number. As we'll see, we can interpret this as a measure of how similar the vectors are.

This requires the first vector to be a bra and the second to be a ket. In fact, this is where their names come from. Dirac wanted to write the inner product in a way that looked something like $$\langle a | b \rangle$$, which looks like the names of the vectors enclosed in brackets. Then he worked backwards to split the bracket into a bra and a ket.

If you try out the inner product on the vectors we already know, you'll find

$$
\langle 0 | 0\rangle = \langle 1 | 1\rangle = 1,\\
\langle 0 | 1\rangle = \langle 0 | 1\rangle = 0.
$$

Here we are using a concise way of writing the inner products where, for example $$\langle 0 | 1 \rangle = \langle 0 | \times | 1 \rangle$$. From the top line, we see that the value 1 comes out of the product whenever we do it for the bra and ket versions of the same vector. When done with two orthogonal vectors, as on the bottom line, we get the outcome 0.

### The x basis

We know that there are states for which the z measurement is equally likely to output `0` or `1`. What might these look like in the language of vectors? A good place to start would be something that is just as close to $$|0\rangle$$as it is to $$|1\rangle$$,

$$
\begin{pmatrix} x \\ x \end{pmatrix}
$$

Here we've used $$x$$ as it's not yet clear which exact number we should put here. For that, we need to think about the inner product,

$$
\begin{pmatrix} x & x \end{pmatrix} \times \begin{pmatrix} x \\ x \end{pmatrix}= 2x^2.
$$

We can get any value for the inner product that we want, just by choosing the appropriate value of $$x$$. So let's choose for the inner product to give the value 1. This is what we got for the inner products of $$|0\rangle$$and $$|1\rangle$$with themselves, so let's make it true for all states.

This condition is known as the normalization condition, and it results in $$x=\frac{1}{\sqrt{2}}$$ . Now we know what our new state is, so here's a few ways of writing it down.

$$
\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{ |0\rangle + |1\rangle}{\sqrt{2}}
$$

This state is essentially just $$|0\rangle$$and $$|1\rangle$$added together and then normalized. So we will give it a name to reflect that orgin. We call it $$|+\rangle$$ .



