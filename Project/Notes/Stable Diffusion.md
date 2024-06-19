Learning/reference material:
- [How AI Image Generators Work (Stable Diffusion / Dall-E) - Computerphile](https://youtu.be/1CIpzeNxIhU?si=MBZ41RuibauenPCx)
- [Stable Diffusion in Code (AI Image Generation) - Computerphile](https://youtu.be/-lz30by8-sU?si=xJOrGS1gSXrzrIFi)
- [Coding Stable Diffusion from scratch in PyTorch](https://youtu.be/ZBKpAp_6TGI?si=MEI4zlu1xD0e02IY)
	- https://github.com/hkproj/pytorch-stable-diffusion
## What is it?
- On a very basic level, it is adding (Gaussian) noise to an image in steps and training a network to get the original image back from the noise. Then we can use random noise and get the model to generate an image that we want.
- Network is probably an encoder-decoder network.
  ![StableDiffusionProcessRepresentation_Simple.png](https://github.com/sprince0031/UL_Masters/blob/85d5a6f6636beff10cca8fad55b6e97796a1180c/Project/Images/StableDiffusionProcessRepresentation_Simple.png)

## Forward process
The _forward process_ or _diffusion process_ is a Markov chain that gradually adds Gaussian noise to the data according to a variance schedule (amount of noise added at each step) $\beta_{1}, ... ,\beta_{T}$ where $\beta \implies amount\ of\ noise$.

## $$q(X_{t}|X_{t-1}) := N(X_{t};\sqrt{1-\beta_{t}}X_{t-1}, \beta_{t}I)$$
where,  
	$X_{t}$ -> Image at time step $t$  
	$N$  -> Gaussian function  
	$\beta_{t}$  -> Amount of noise applied at time step $t$  
	$I$   ->   

### From original to image at any time step $t$
We can calculate the noisy image at any time step without calculating all the intermediate images by using the following formula.
## $$q(X_{t}|X_{0}) = N(X_{t};\sqrt{\bar{\alpha_{t}}}X_{0}, (1-\bar{\alpha_{t}})I)$$
where,  
	$\alpha_{t}$ -> $1-\beta_{t}$  
	$\bar{\alpha_{t}}$ -> $\Pi_{s=1}^t \alpha_{s}$  

## Reverse process
This is a Markov chain with learned Gaussian transitions starting at $p(X_{t}) = N(X_{t}; 0, I)$.
## $$p_{\theta}(X_{t-1}|X_{t}) := N(X_{t-1}; \mu_{\theta}(X_{t}, t), \Sigma_{\theta}(X_{t}, t))$$
where,  
	$\mu_{\theta}$ -> mean of distribution (learned by the network)  
	$\Sigma_{\theta}$ -> variance of distribution (fixed)  

## How do we generate new data?
- We take an image with random noise in it and ask the network to de-noise it to generate the new image.
- The trick here is that we add a "prompt" or context signal which will push the network to generate the image that is more aligned with what we ask of it via the prompt.
	- Thus a text prompt that describes what we want generated encodes the prompt (CLIP) which then provides token context that is associated with similar images the network has been trained on. Hence, the network tries to generate images that are aligned with this context.
	- For image-to-image, 

## U-NET
Paper ref: https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28
![U-NET_Architecture.png](https://github.com/sprince0031/UL_Masters/blob/85d5a6f6636beff10cca8fad55b6e97796a1180c/Project/Images/U-NET_Architecture.png)
