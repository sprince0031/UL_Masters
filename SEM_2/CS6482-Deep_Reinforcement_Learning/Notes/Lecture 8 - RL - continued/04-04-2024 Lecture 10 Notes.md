Reference slides: [Temporal Difference (TD) Methods](https://learn.ul.ie/d2l/le/lessons/17967/topics/640660)
## Q Learning - Tabular method
- Look up gridworld sample code
- <span style="background:#d3f8b6">What changes would need to be done to the mentioned gridworld tabular code to implement SARSA?</span>
	- action_next = chose_action(item_next)
	- Q\[State]\[Action] += alpha * (Reward + (gamma * Q\[state_next]\[action_next] - Q\[State]\[Action]))
- <span style="background:#d3f8b6">Why is Q generally "better" than SARSA?</span>
	- SARSA optimises sub-optimal actions and tries to learn from it.
	- Q is better because it uses off-policy. It resolves this by separating from behaviour policy which is sub-optimal from the behaviour being learnt.

## RL recap - Temporal Difference
- Markov Decision Process (MDP)
- Model is a high fidelity simulator.
- Problem: no general access to a high level of 
- v & q? -> policy evaluation

### Algs
#### Dynamic Programming
- Bootstraping
	- Next guess is based on the previous guess.
#### Monte carlo
- Model free

#### Temporal Difference
- Combines best of both mote carlo and DP. 
	- Is model free and also bootstraps
- Cornerstone of RL
- Function estimator minimises the error, delta
- $$V(s) = \frac{1}{6},\frac{2}{6},\frac{3}{6},\frac{4}{6},\frac{5}{6}$$ (mistake in the slide titled, MC v TD(0). There are only 5 value states and not 6.)
- <span style="background:#d3f8b6">Why is Q off-policy?</span>
	- max term
	- term in square bracket is the error
- SARSA has less negative reward but computes the path sub optimally while Q has greater negative reward which computes the path optimally.
- <span style="background:#d3f8b6">What happens if the number of episodes are set to infinity?</span>

### TD Gammon (Tesaura, 1992)
- Why are board games used in RL? Because it is a constrained space with a defined set of state space.
- State space for backgammon is **$10^{20}$**.
- What are the features that are representative of the board?
- Using gradient information to make the update i.e, nature of the update depends on the gradient, **$Z_{t}$**.

## Deep Q-Networks
- Proposed by Google's DeepMind team in NIPS 2013 paper "Playing Atari with Deep Reinforcement Learning".
- Could use the same architecture to train on different Atari games.
- Loss function reduces error between predicted and target.
	- Loss function uses gradient descent.
- DQN is highly unstable.

#### Cartpole
- Code reference: https://learn.ul.ie/d2l/le/lessons/17967/topics/647781
- In code, step 0 => left and 1 => right
	- return 0 if a < 0 else 1 => move left if pole is falling to the left (so that the pole can move back to the right), else move right.
---
# DQN Variations
Reference slides: [DQN Variants](https://learn.ul.ie/d2l/le/lessons/17967/topics/654776)

## Issues with DQN
- Issue is catastrophic forgetting i.e, model forgetting experiences that it has previously learnt.
## DQN: Fixed Q-Value Targets
- Two networks.
	- Prediction network
	- Target network

## Maximisation bias in Q-learning

## Double Q-learning
- Where did the value "1.3" come from? (slide #9)

## DQN Atari: Architecture
- Input 84 x 84 x 4 (4 images concatenated to capture trajectories)
---
### Notes for Assignment 2
- Cover dueling DQN, 