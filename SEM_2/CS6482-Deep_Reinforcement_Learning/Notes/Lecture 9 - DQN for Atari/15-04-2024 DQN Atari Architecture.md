Reference slides: [DQN for Atari](https://learn.ul.ie/d2l/le/lessons/17967/topics/654775)

## General notes
- There are two networks (double DQN); target network and policy network.
	- Policy network - the network that is used to predict the next action.
	- Target network - a duplicate network used for error measure i.e, the target.
	- Good stackoverflow explanation as to why this is used: https://stackoverflow.com/a/54238556/5584011

## Q update for windy grid world
- Refer slide #4
- Q update rule:
	- ![[Pasted image 20240415102537.png]]
- [[04-04-2024 Lecture 10 Notes#TD Gammon (Tesaura, 1992)|TD Gammon (Tesaura, 1992)]]

## DQN Atari using experience replay
- Refer sides #9 (theory), #16 (code reference)
- Used to store samples of "experience" which are essentially mini batches of 4 transition frames each and we sample from these when we have enough from our trails
- Note: y<sub>j</sub> here represents the target state.
---
## Reading
- Chapter 6 - Sutton and Barto
- Look up the following before Thursday's class:
	- [ ] Catastrophic forgetting
	- [ ] Maximisation bias

---
## Potential exam questions
- Discuss about DQN for Atari (architecture, algorithm, loss function, performance).
- Write code for the implementation of "windy grid world". (chapter 6 in Sutton and Barto)
- Code related questions. 
	- For example, "what is model_target?" (refer slide #16).
> [!note]
> - There is a code mix up in slide #16 where model_target is used in place the action model and vice-versa. This is a potential exam question where this wrong code may be given and we might be asked to point out why it is wrong.

- Policy gradients.
- Things to expect from exam:
	- More focus on ethics and explainable AI from tutorial sessions.
	- More code heavy questions
---
## Pointers for Assignment 3
- Are we able to demonstrate the model learning with coding from scratch?
- Training a model to perform reasonably well on Atari games is not the main focus.
- Include a lot of plots that indicate learning.
- Choose one of the first 3 best performing game environments (KISS principle :P) - refer slide #12.
- Explore if changing the number of neurons in the hidden layer changes the performance significantly.

---
> [!note]
> Announcements
> - Assignment 2 deadline extended till 17<sup>th</sup> midnight.
> - Midterm extra 20% for everyone if feedback is not given by 18<sup>th</sup>. :crossed-fingers: