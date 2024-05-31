Reference slides:
- A: [Policy Gradient Approach](https://learn.ul.ie/d2l/le/lessons/17967/topics/659920)
- B: [Reinforce using Policy Gradients - Part 2](https://learn.ul.ie/d2l/le/lessons/17967/topics/662670)
## Policy Gradient Approaches
- Searching the policy space using
	- brute search
	- genetic algorithms
	- gradient descent, etc
### Reinforce Algorithm (Williams 1992)
- The 4 steps (slide # A.8)
- Note that we need to <u>compute</u> and not apply.
- We don't directly apply the exploration vs exploitation here because we don't have anything to balance/decide when to do what. 
- Slide #14
	- all_final_rewards -> action gradients
- Critique for this alg -> it is sample inefficient.
## Policy gradient - general notes
- Exploration vs exploitation is balanced by using probabilities.
	- Uses softmax at the output layer for setting probabilities of outputs
	- If one policy has 0.1 means that it will be selected less number of times comparatively to other policies that may have higher probabilities.
- Advantages to PG (slide #):
	- Applies to continuous action space.
	- Good for situations where the problem is non-deterministic.
	- Can converge on stochastic optimal policies (here stochastic means the reward function changes over time)
- PG -> loss function defined as
	- ![[Pasted image 20240422112058.png]]
## Cross-Entropy
- Variation of Reinforce
- Cross-Entropy method basically the Reinforce algorithm if point #3 on slide # B.16 is used.
- Critique -> Not balancing exploration vs exploitation.
	- Binary approach to setting action probabilities of 0/1 based on bad/good outcomes.
- Compared to Reinforce, there is no negative gradient.

## Variation 3 for Reinforce algorithm
- Use cross entropy loss as loss function.

## Difference of Reinforce with Q learning
- Slide # B.20-22
- No explicit exploration is needed.
- No replay buffer needed 
	- Point #4 in the slide is wrong. Because it converges faster, it **DOES NOT** require more interaction with the environment.
- No target network needed

## Module summary
![[Module Summary 1.png]]
- Dynamic Programming -> model in this context means model of the world
- Bootstrapping in terms of RL -> backing up
	- Updates weights in real time.

![[Module Summary 2.png]]
---
## Reading
- [ ] Tom Mitchell - Inductive Decision Trees

---
## Potential exam questions
- Reinforce algorithm
	- Walk through the algorithm - 4 steps
	- In slide #11, explain how discount_rewards([10,0,-50]) will return [-22, -40, -50]
	- How is it different from than Q learning?
- Is policy gradient on-policy? 
	- https://datascience.stackexchange.com/questions/31046/why-are-policy-gradients-on-policy
- Give definition of AI (reference author(s) - Tom Mitchell).  Differentiate from machine learning.
- How do you compute the error when it comes to DQN?