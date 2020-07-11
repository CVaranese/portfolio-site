name:  "Super Smash Bros. Melee AI"
description: "Creation of a Machine Learning Melee AI using Keras"
image: images/melee_thumb.jpg
feature: images/1200px-Finaldestination.jpg
---

## Project Description

For this project, two partners and I worked with a GameCube emulator in hopes of training a model that could
successfully play Super Smash Bros. Melee. After some initial setup of interfacing with the emulator using 
[libmelee](https://github.com/altf4/libmelee), we were able to create a Neural Network that would train itself simply
by playing against the in-game CPUs.

## Methods

Inially, we started out by using [OpenAI gym](https://gym.openai.com/) to familiarize ourselves with the basic concepts.
After adapting our learning algorithms with the help of [some papers](http://proceedings.mlr.press/v48/mniha16.pdf),
we were able to have an AI up and running with simple random outputs.


We used two networks - a value and a policy network. One would predict the expected reward at any point, and the other would
predict which controller input to give. After a specified number of games, the AI would compare its expected rewards to actual
rewards, and change the policy network's behavior accordingly.

## Results

In the end, this may have ended up being too ambitious of a project. The AI did show signs of intelligence, mostly with it
being able to recover if it happened to be off of the stage, but it never ended up being that good. Potentially, there may
have been a bug inside of the learning code, or we may just not have had adequate resources to be able to train it within a
reasonable time."
