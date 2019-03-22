# GHZ States

Perhaps even stranger than Bell states are their three-qubit generalization, the _GHZ states_. An example of one of these states is 12√\(\|000⟩−\|111⟩\). The measured results should be half \|000⟩and half \|111⟩

. GHZ states are named after Greenberger, Horne, and Zeilinger, who were the first to study them in 1997. GHZ states are also known as “Schroedinger cat states” or just “cat states.”

In the 1990 paper by N. David Mermin, _What’s wrong with these elements of reality?_, the GHZ states demonstrate an even stronger violation of local reality than Bell’s inequality. Instead of a _probabilistic_violation of an inequality, the GHZ states lead to a _deterministic_violation of an equality.

![image0](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.42.45%20AMl8kxsz2b6cs4te29.png)Imagine you have three independent systems which we denote by a blue, red, and green box. You are asked to solve the following problem: in each box there are two questions, labeled Xand Y, that have only two possible outcomes, +1or −1

. You must come up with a solution to the following set of identities.XYY=1.

YXY=1

.

YYX=1

.

XXX=−1

.

Try it!

After a while you will realize this is not possible. The simple way to show this is the following: if we multiply the first three equations together, we can simplify squared quantities and obtain XXX=1

, which contradicts the fourth identity.

Amazingly enough, a GHZ state can provide a solution to this problem. Then we have to accept what quantum mechanics teaches us: there are not local hidden elements of reality associated with each qubit which predetermine the outcomes of measurements in the Xand Y

bases. So, as Mermin pointed out, the GHZ test described above contradicts the possibility of physics being described by local reality! As opposed to the Bell test, which provides only a statistical evidence for the contradiction, the GHZ test can rule out the local reality description with certainty after a single run of the experiment \(not including the effects of noise and imperfections in our system\).

![image1](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.42.54%20AMjqrs28j545p6tj4i.png)To make this state we use the following circuit, which is slightly different to the standard way of creating a GHZ \(in our hardware the CNOT gates are constrained in their orientation\). In the first part of the circuit, the ground state is taken to a superposition12\(\|001⟩+\|011⟩+\|101⟩+\|111⟩\). The two CNOTs now entangle all the qubits into the state 12\(\|001⟩+\|010⟩+\|100⟩+\|111⟩\). The final three Hadamard gates map this to the GHZ state 12√\(\|000⟩−\|111⟩\).

To make the measurements in the Xand Ybasis we again rotate the measurement using the circuits you have seen before. For example, consider the XXXmeasurement. Note that flipping all three qubits of the GHZ state gives the same state with the minus sign. In other words, the GHZ state is a −1eigenvector of a three-qubit Pauli operatorXXX

. This implies

XXX=−1

for each realization of the experiment. Next consider the Pauli operatorXYY. One can check that the GHZ state is a +1eigenvector ofXYY

. Therefore,

XYY=1

for each realization of the experiment. Likewise,

YXY=1, and YYX=1

.

One can verify this by running the experiments using the circuits provided below.Here you can see the results we got when we ran this experiment on the processor:

                    ![image2](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2010.30.31%20PM5vv145poc8qfflxr.png)EXAMPLE CIRCUITS:The first circuit shown below creates a GHZ state and then measures all qubits in the standard basis. The measured results should be half000and half 111. The remaining four circuits describe the GHZ test. Each circuit prepares the GHZ state and then measures the three qubits by choosing the measurement bases according to YYX,YXY, XYY, and XXXrespectively.

