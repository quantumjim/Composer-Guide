# The meaning of universality

What does it mean for a computer to do everything that it could possibly do? This was a question [tackled by Alan Turing](https://en.wikipedia.org/wiki/Universal_Turing_machine), before we even had a good idea of what a computer was.

To ask this question for our classical computers, and specifically for our standard digital computers, we need to strip away all the screens, speakers and fancy input devices. What we are left with is simply a machine that converts input bit strings into output bit strings. If a device can perform any such conversion, taking any arbitrary set of inputs and coverting them to an arbitrarily chose set of outputs, we call it _universal_.

It turns out that the requirements for universality on these devices are quite reasonable. The gates we needed to perform addition in [The atoms of computation](https://learnqiskit.gitbook.io/composerguide/) are also sufficient to implement any possible computation. In fact, just the classical NAND gate is enough, when combined together in sufficient quantities.

Though our current computers can do everything in theory, some tasks are too resource intensive in practice. In our study of how to add, we saw that the required resources scaled linearly with the problem size. For example, if we double the number of digits in the numbers, we double the number of small scale additions we need to make.

For many other problems, the required resources scale exponentially with the input size. Factorization is a prominent example. In [a recent study](https://eprint.iacr.org/2012/444.pdf), a 320 digit number took CPU years to factorize. For numbers that are not much larger, there isn't enough computing resources in the world to tackle them. Even though those same numbers could be added or multiplied on just a smartphone in a much more reasonable time.

Quantum computers will alleviate these problems by acheiving universality in a fundamentally different way. As we saw in [The unique properties of qubits](https://learnqiskit.gitbook.io/composerguide/getting-started-with-the-composer/chapter-2-the-unique-properties-of-qubits), the variables of quantum computing are not equivalent to those of standard computers. The gates that we use, such as those in the last section, go beyond what is possible for the gates of standard computers. Because of this, we can find ways to acheive results that could not be achieved otherwise.

Specific examples of this will be explored in future sections. For now, it is sufficient to simply define what universality is for a quantum computer. We can do this in a way that mirrors the definition discussed above. Just as digital computers convert sets of input bit strings to sets of output bit strings, unitary operations convert sets of orthogonal input states into orthogonal output states.

As a special case, these states could describe bit strings expressed in quantum form. If we can acheive any unitary, we can therefore acheive universality in the same way as for digital computers.

Another special case is that the input and output states could describe real physical systems. The unitary would then correspond to a time evolution. When expressed in an exponential form using a suitable Hermitian matrix, that matrix would correspond to the Hamiltonian. Acheiving any unitary would therefore correspond to simulating any time evolution, and engineering the effects of any Hamiltonian. This is also an important problem that is impractical for classical computers, but it comes out naturally as an application of quantum computers.

Universality for quantum computers is then simply this: the ability to acheive any desired unitary on any arbitrary number of qubits.

As for classical computers, we will need to split this big job up into managable chunks. We'll need to find a basic set of gates that will allow us to acheive this. As we'll see, the single and two qubit gates of the last section are sufficient to to this.









