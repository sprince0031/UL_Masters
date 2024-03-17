Reference slides: [Temporal Difference(TD) Methods](https://learn.ul.ie/d2l/le/lessons/17967/topics/640660)
## On-policy vs Off-policy
### Cliff walking example
- Refer slide #16

### Cart-Pole Problem
- Refer slide #23
- High fidelity environments to simulate problems and develop a RL algorithm
- Sample code: [OpenAI Gym](https://gym.openai.com/envs/CartPole-v0/)
- Goal is to keep the pole upright for 200 steps.

### Look up and reflect
- [ ] SARSA
- [ ] Q-learning
- [ ] GYM environment 

---
### Assignment 2:
- Implement Cliff Walking Example using Sarsa and Q-learning.
	- Or solve the cart pole problem by implementing Q-learning on a neural network architecture?
- Work with the GYM environment.
- Classic 

---
### Potential Exam Questions:
- Explain why Q-learning generates an optimal path with a higher loss.
	- Look into how on vs off-policy affects this. 
- Q-learning is an off-policy algorithm. Why is it off-policy?
- Compare on-policy vs off-policy