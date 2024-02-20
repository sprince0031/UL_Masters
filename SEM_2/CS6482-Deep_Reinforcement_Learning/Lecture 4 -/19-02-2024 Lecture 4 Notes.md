**Reference slides:** https://learn.ul.ie/d2l/le/lessons/17967/topics/627387
### Main challenges of ML
1. Insufficient quantity of data
2. Non representative data
3. Poor quality data
	- Consider fixing errors manually by adding mean/median values, etc.
	- Discard outliers
4. irrelevant features
	- Feature engineering
		- feature selection
		- feature extraction
		- creating new features using model encoders, GANNs, etc
5. Overfitting the training data
	- How well can it generalise?
	- Perhaps a simpler linear model would have sufficed.
	- Happens when the model is too complex relative to the amount and quality of the training data.
		- Simplify the model using fewer parameters
		- Generalisation
6. Underfitting the training data
	- When the model is too simple to learn the underlying structure of the data.

### Weight initialisation
- Slides #10 - #12