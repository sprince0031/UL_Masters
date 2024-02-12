[Lecture slides for reference](https://learn.ul.ie/d2l/le/lessons/17967/topics/616811)
### What is learning?
#### According to Tom Mitchel
<>

### Learning in terms of neural biology
- There are about 83 billion neurons in the human body.
- There are about a 100 trillion synaptic connections.
![[Biological neuron structure.png]]

### Decision surface of a Perceptron
- Not all functions are linearly separable.
	- This was a cause for the AI winter.
- Perceptron training rule
	- o = w0 + w1x

### Gradient descent -  the delta rule
- Minimising the error with respect to the weight vectors to achieve the optimal weights. 
- The gradient is the direction used to update the weights during training.
- Derivation of the formula - refer slide #11
- Algorithm - refer slide #12
- There are 2 types of gradient descent
	- Batch mode
		- In the slide #14 - correction: E(Uppercase 'D' -> refers to the entire training set)
		- One update for the entire set
	- Incremental 
		- Update for each set of weights

### Multi-Layer Perceptrons (MLPs)
- Need to re-purpose the gradient descent algorithm for hidden layers in an MLP architecture.
- Henry Rowely's MLP architecture for face detection
	- ![[Rowley's MLP Architecture for face detection.png]]
	- Got 70-80% of accuracy
	- Could not increase the accuracy by much more with the MLP architecture.

### Activation functions
- MLP typically uses the sigmoid activation function.
- Refer slide #16
	 ![[Perceptron architecture.png]]

### Backpropagation algorithm
Refer slides #17 - #21
- Architecture in slide #21 is an example where we can augment training data using hidden layers that can compress features.

### Learning Rate
- Learning rate determines how much to change the weights to arrive at the optimal error rate.
- High learning rate performs well at first but then fails to reach the optimal minimum. 
- Slow learning rate takes too long to arrive at the optimal minimum.
- Hence a decaying learning rate where it starts high and then decays its rate is used to optimise this. 

### Look up
- Guidance for initialisation of weights.
- Which type of gradient descent is better? Batch mode or incremental? Assume computational resources is not an issue. (potential mid term question)
- Briefly discuss the reasons for Rowley's MLP architecture for face detection. Why did he position the neurons the way he did.
- Who were the 3 authors that back-propogation was associated with?
	- David Rumelhart, Geoffrey Hinton (godfather of AI), Ronald Williams (1986) - https://www.linkedin.com/pulse/history-neural-networks-datta-dharanikota/
	- Geoffrey Hinton resigned from the board of AI at Google in light of ethical concerns with AI.
- How to characterise training data? How much data is sufficient? Is the data generalised over a binomial distribution?
- Current pathway that AI is on, does it pose a threat to humanity? If there are threats, how do we counteract them?