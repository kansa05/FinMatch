# Machine learning Basics

## Core Idea

The computer learns a pattern from examples instead of being explictly programmed with every rule

It learns through **examples**

User A + Invevestment X -> liked
User B + Investment Y -> Disliked

The model will learn the **hidden patterns** such as people with these traits tend to like these investments with these traits

## What is Data
This is the example the model learns from 

Example: 
Person studied 2 hours → got 60
Person studied 4 hours → got 75
Person studied 6 hours → got 90

*Model Learns that more study hours usually mean higher scores*

## What is an output

The output is what a model predicts. 

Two Different Outputs: 
-- Regression
        Predicts a number using data
-- Classification: 
        Predicts a class or probability

**My project will focus on Classification**

##What is a feature
A feature is one specific piece of information the modle can use

Example: predicting an exam score
        Features can be: 
                hours studied
                hours slept
                attendance
                practice questions
        Each Feature gives the model a **clue**

**A feature is just one measurable input detail**

## What is a vector

A vector is a list of numbers

ML models need numbers to train

Example: 
        Student: 
            - Studied 5 hours
            - Slept 7 hours
            - **Did practice exams yes**

Vector Example: [5,7,1]

the 1 means YES, because the model does not understand catories, must encode into numbers 

**One-Hot Encoding** -- called this because you turn on exactly 1 value
High

Example: 
    risk = low 
    risk = Medium 
    risk = high 

**THESE ARE CATEGORIES**
Example Encoded(Using Binary): 
    low= [1,0,0] - means flip the low switch
    Medium = [0,1,0] - means flip the medium switch
    High= [0,0,1] - means flip the HIGH switch


## Feature Vector

A feature vector = All features for one example

Example: 
    User:
        - $5000
        - $300/month
        - medium risk
        - long-term
    User Vector will be [5000, 3000, 0,1,0, 1]  
    // This means [5000, 300, risk=[0,1,0], long_term=1]


## Model

A Model = a function that maps input to ouput

general formula is y = w1*x1 + w2x2 + b


b is the bias= the model's starting point before looking at any inputs
Example: 

score = 8*(study hours) + 2*(sleep) + b

## Weights

Weights = importance of each feature

Example: 
    w_study=8
    w_sleep=2

This means that study matters more than sleep, weights are learned automatically

We first set random weights, which get adjusted through different processes

##Learning Rate
Step size when updating weights, by how much you adjust the weights when updating

Small learning rate is stable but slow, but large learning rate is faster but may not be as stable

##Gradient Descent

Method to reduce loss by adjusting weights in the direction that reduces weight

Model uses this to figure out how to adjust to reduce error 

Gradient tells you the direction that increases error the most

new_weight = old_weight-learning_rate * gradient

##Epoch

An epoch is one full pass through the entire training dataset

Need many epoch's for multiple reviews 

Each epoch refines the weights further

##Overfitting

Overfitting happens when the model memorizes the training data instead of general patterns

It essentially is being lazy, memorizing instead of learning

For example: 

    User A -> likes stock X

    Model learns: User x likes stock X

Model does **NOT** learn the rules or recognize the patterns

*Overfitting = no generalization* 

## Underfitting

Underfitting happens when the model is too simple or hasn't learned enough

Model **cannot** capture patterns

Example: 

    Trying to predict exam score using only: Study Hours

    But ignoring: 
        Sleep
        difficulty
        ability

    May predict that the student will fail soley on studying


## Train/Test split

You split data so you can test if the model works on unseen examples

Need both **TRAINING** and **TESTING** data

## Tensor

A tensor is a structured container of numbers that ML models use to perform mathematical operations


Allows for Batch processing

## Neural Network

A neural network is a sequence of transformations that gradually convert input features into a predicattion

Step by Step run through

Step 1 with input x= [5000,300, 0, 1, 0, 1]
    - do z=W*x + b
    - This creates: 
        [3.2, -1.5, 0.7, ... ]
    - may create negative numbers
    - Each feature can either: 
        > Push the predication up(+)
        > push the predication down (-)

        this is just weighted combinations 
Step 2: Activation (ReLU)
    - ReLU gets rid of the negative values, it introduces non-linearlity
    - Shuts off useless weights (negative values come from the fact that this feature pushes the prediction down)

    - ReLU(x)=max(0,x)

    - Example: [3.2, -1.5, 0.7] → [3.2, 0, 0.7]


## Ranking System

Ranking converts raw prediction scores into ordered recommendations

The output scores for many outputs and then sorts 


## Full pipeline

1. Collect raw data
   (user input, item data)

2. Define features
   (what matters?)

3. Encode features
   (one-hot, numeric)

4. Build feature vectors
   (fixed-length numeric representation)

5. Combine inputs
   (user + item → one vector)

6. Convert to tensors
   (ready for model)

7. Pass through model
   (linear layers + activations)

8. Get prediction
   (score / probability)

9. Compare with actual label
   (if training)

10. Compute loss
    (how wrong?)

11. Compute gradients
    (which direction to change weights?)

12. Update weights
    (gradient descent)

13. Repeat over many epochs
    (learn patterns)

14. Switch to inference mode
    (no more training)

15. Score many items
    (for recommendation)

16. Rank items
    (sort by score)

17. Show results to user

18. Collect feedback
    (likes, clicks, etc.)

19. Add feedback to dataset

20. Retrain model