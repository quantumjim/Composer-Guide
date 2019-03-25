# GHZ States

Perhaps even stranger than Bell states are their three-qubit generalization, the _GHZ states_. An example of one of these states is $$(|000\rangle-|111\rangle)/\sqrt{2}$$. A circuit to create this is

```c
h q[0];
z q[1];
cx q[0], q[1];
cx q[1], q[2];
```

If each qubit is measured in the z basis, the results will be half `000` and half `111`.

GHZ states are named after Greenberger, Horne, and Zeilinger, who were the first to study them in 1997. GHZ states are also known as “Schroedinger cat states” or just “cat states.”

In the 1990 paper by N. David Mermin, _What’s wrong with these elements of reality?_, the GHZ states demonstrate an even stronger violation of local reality than Bell’s inequality. Instead of a _probabilistic_ violation of an inequality, the GHZ states lead to a _deterministic_ violation of an equality.

![image0](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.42.45%20AMl8kxsz2b6cs4te29.png)

Imagine you have three independent systems which we denote by a blue, red, and green box. You are asked to solve the following problem: in each box there are two questions, labeled X and Y, that have only two possible outcomes, +1 or −1

With these we can consider products of the different results, such as $$XYY$$: the product of the X for the blue box, and the Ys for the red and green.

Try and find a set of values for the X and Y of each box that satisfies the following relations,

$$
XYY = YXY = YYX = 1, ~~~ XXX=-1.
$$

After a while you will realize this is not possible. The simple way to show this is the following: if we multiply the first three equations together and use the fact that $$Y^2=1$$ for any $$Y=\pm1$$, obtain $$XXX=1$$. This contradicts the fourth identity.

Amazingly enough, a GHZ state can provide a solution to this problem. Then we have to accept what quantum mechanics teaches us: there are not local hidden elements of reality associated with each qubit which predetermine the outcomes of measurements in the $$X$$ and $$Y$$ bases. So, as Mermin pointed out, the GHZ test described above contradicts the possibility of physics being described by local reality! As opposed to the Bell test, which provides only a statistical evidence for the contradiction, the GHZ test can rule out the local reality description with certainty after a single run of the experiment \(not including the effects of noise and imperfections in our system\).

Let's try this out. The circuit for creating the GHZ state is at the top of the page. To make the measurements in the $$X$$ and $$Y$$ basis we again rotate the measurement using the circuits you have seen before.

Even before we make the measurement, we can infer something about the results we'll get. For example, consider the $$XXX$$ measurement. If, rather than measuring $$X\otimesX\otimesX$$ on our qubits, we applied it as a sequence of gates. This will flip all three qubits of the GHZ state, and give the same state back but with a global minus sign. In other words, the GHZ state is a $$−1$$ eigenvector of a three-qubit Pauli operator $$X\otimesX\otimesX$$. This implies that $$XXX=−1$$ for each realization of the experiment.

Next consider the Pauli operator $$X\otimesY\otimesY$$. One can check that the GHZ state is a $$+1$$ eigenvector of this. Therefore, $$XYY=1$$ for each realization of the experiment. Likewise, $$YXY=1$$, and $$YYX=1$$.

One can verify this by running the experiments using the circuits provided below. Here you can see the results we got when we ran this experiment on the processor:

![image2](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2010.30.31%20PM5vv145poc8qfflxr.png)

The quantity $$M$$ here is one that would never be negative for local hidden variable theories. But, as you can see, it is clearly negative here.

