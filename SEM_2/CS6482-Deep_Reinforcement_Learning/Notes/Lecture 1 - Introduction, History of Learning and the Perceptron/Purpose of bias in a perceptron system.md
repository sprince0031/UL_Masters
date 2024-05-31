### What is a perceptron?
A perceptron is a simple linear classifier that computes a weighted sum of the inputs and passes it through an activation function (such as a step function) to produce an output.

### Purpose of bias
- The purpose of bias in a perceptron system is to **shift the decision boundary** away from the origin and make the model more flexible. 
- The bias is a constant term that is added to the weighted sum, which allows the perceptron to adjust the output independently of the inputs. 
- Without a bias, the perceptron can only represent linear functions that pass through the origin, which may limit its ability to learn complex patterns. 
- [With a bias, the perceptron can represent any linear function, which increases its expressive power](https://stackoverflow.com/questions/2480650/what-is-the-role-of-the-bias-in-neural-networks) [1](https://stackoverflow.com/questions/2480650/what-is-the-role-of-the-bias-in-neural-networks)[2](https://math.stackexchange.com/questions/2468570/machine-learning-perceptron-purpose-of-bias-and-threshold).

### Examples
- In this example, the perceptron is trained to perform the logical AND operation on two binary inputs. Without a bias, the perceptron cannot learn the correct function, as the decision boundary (the red line) has to go through the origin and cannot separate the positive (blue) and negative (orange) examples. With a bias, the perceptron can learn the correct function, as the decision boundary can shift to the right and correctly classify all the examples.

- In this example, the perceptron is trained to classify two classes of points (blue and orange) that are linearly separable. Without a bias, the perceptron can only learn a decision boundary that goes through the origin, which may not be optimal for the given data. With a bias, the perceptron can learn a decision boundary that can be anywhere in the plane, which may result in a better fit for the data.