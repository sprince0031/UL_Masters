**Reference slides:** https://learn.ul.ie/d2l/le/lessons/17967/topics/627384
## Intro to CNNs
- A significantly smaller number of weights compared to the number of connections makes the learning task simpler.
- Pooling layer -> down sampling

### CNN architectures
#### LeNet
- LeNet-5 (architecture credited to Yan Lecun) for MNIST
	- Input 28x28x1
	- 32 filters
		- Therefore 28x28x32 pooling dimensions
		- 32 feature maps
	- After pooling -> 14x14x32 (14x14 -> 64 feature maps)
	- Number of kernels is different from the number of layers in the input
	- Final stage uses softmax to output probabilities for classifications.

#### AlexNet
- Popularised CNNs in computer vision by Alex Krihevsky, Ilya Sutskever and Geoff Hinton.
- Gold standard in computer vision.
	- Submitted to the 2012 ImageNet ILSVRC Challenge ImageNet ILSVRCin
	- Top 5 error of 16% compared to the runner-up with 26% error. Huge difference at the time.

#### GoogLeNet
- ILSVRC 2014 winner - CNN from Szegedy
- Significant reduction in training weights and training time.
- Top 5 error down to 6.7%

#### VGGNet
- Runner up in ILSVRC 2014 from Simonyan and Andrew Zisserman.
- Showed that depth of network is a critical component in performance.

#### ResNet
- Residual Network developed by Kaiming He et al. was the winner of ILSVRC 2015.
- Top 5 error down to 3.57%.

### Keras
API on top of Tensorflow which abstracts some of the functionality.

### Saturation
- Slides 30-31
- Saturation gives rise to vanishing gradient.
- Vanishing gradients make it difficult to know which direction to move to minimise error.

### ReLU (Rectified Linear Units)
- What constitutes to a good activation function?
	- Approximates a good linear function.
	- In actuality, it is a non-linear function allowing complex relationships in the data to be learned i.e., a function approximator that can work on non-linear data (because most data is non-linear)
	- It is a piece-wise approximation of a linear function.
#### Problems of the ReLU activation function:
- No gradient information when output of the neuron is negative.
- Suffers from a problem known as dying ReLUs.
	- During training, some neurons effectively "die", meaning they stop outputting anything below zero. 
- One of the causes of dying ReLUs is incorrect learning rates.
#### ELU
- ELU (Exponential Learning Unit) is a variation of the ReLU.
- Takes on negative values when z < 0.
- **Scaled ELU (SELU)**

### Converting
- Done to convert categorical data to numerical representations.
- Types:
	- **One-hot encoding**
	- **Dummy variable encoding**
	- Effect encoding
	- Binary encoding
	- BaseN encoding
	- Hash encoding
	- Target encoding

### Softmax
Ensures estimated probabilities for each possible class are between 0 and 1 and that they add up to 1.

### Linear Regression
- Slide #60

### Cross entropy
- Slide #61 - #68
- In example in slide #63, container 1 and 3 are more predictable while container 2 is less predictable as it is more of a 50-50.
	- ![[Pasted image 20240219112422.png]]
	- [Reference link | Towards Data Science](https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e)
	- **Result**: more the entropy, more difficult it is to predict i.e., if entropy closer to zero, it is more predictable and vice-versa.

### Drop out
- Slides #69 - #72.
- Drop out is one of 3 approaches to improve generalisation (reduce overfitting).
	- Other 2 techniques are:
		- L1 and L2 regularisation
		- Batch normalisation
			- Primary intent was to reduce vanishing gradients.
- Drop out is where 50% of neurons are turned off during training.
- Every neuron including the input neurons but always excluding the output neurons has a probability p of being temporarily “dropped out”.
- Happens only during training.

### General notes
- MSE is preferred loss function for linear regression.
- Claude Shannon associated with Information Theory.

**Suggested reading:** Aurélien Géron. Hands-On Machine Learning with ScikitLearn, Keras, and TensorFlow : Concepts, Tools, and Techniques to Build Intelligent Systems, 2nd Ed. 2019. O’Reilly

### To-do

#### Look up
- [ ] Categorical cross entropy vs Cross entropy
- [ ] ADAM optimiser (variation of EGD)
- [ ] Implement a CNN for MNIST
- [ ] Decision trees
	- [ ] A way to build up decision trees is using Claude Shannon's entropy.
#### CNN project
- Pick data sets that are more challenging.
- Compare differences with different activation function variations such as ReLU, ELU, SELU, etc.
- Compare between different optimisation functions that are being used.

**Tutorials will be important for exam**