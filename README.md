# Wordle-RL
**by: Victor Ardulov** 

## Introduction

This is a little sandbox for me to play with some ideas surrounding probabilistic decision-making. I thought wordle was a 
fascinating little game to try to train a machine learning algorithm to play. Largely this is a space to excersize my own RL
skills and coding techniques, but I maybe this will be the next AlphaGo who know. WIRED article incoming.

## Playing Wordle in Your Terminal

The first step that I took was to recreate the wordle game so now anyone can play it in their terminal to practice. This
is mostly a byproduct to the fact that I needed to create an "environment" for RL agent to interact with.

### Getting Started

*"If you want to bake an apple pie, you must first invent the universe"*

*-Karl Sagan*

-Victor Ardulov

But we won't start there... You will however need to make sure you have atleast [Python3.8](https://www.python.org/downloads/) installed and [Git](https://git-scm.com/). My recommendation is to
use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) or [Anaconda](https://www.anaconda.com/) python environment manager.

I'm going to assume anaconda is installed going forward since that is what I'm using. To setup the enviornment start with:
```bash
conda create -n wordle-rl python=3.8
conda activate wordle-rl
```

Then you're going to need to clone the repo and install the requirements:
```bash
git clone git@github.com:VArdulov/wordle-rl.git
pip install -r requirements
```

Assuming no errors, you should be able to now play Wordle in your terminal
```
python play_wordle.py
```

you can also use the `--turns` or `-t` flags to increase the number of turns you get to play

Here's an example of a game, inputs and outputs:
```
python play_wordle.py
You have 6 guesses remaining
Please enter your 5 letter guess: crane
⬛ ⬛ 🟩 ⬛ 🟩
c  r  a  n  e
You have 5 guesses remaining
Please enter your 5 letter guess: stage
🟨 ⬛ 🟩 ⬛ 🟩
s  t  a  g  e
You have 4 guesses remaining
Please enter your 5 letter guess: phase
🟩 🟩 🟩 🟩 🟩
p  h  a  s  e
Good job! it took you 3 turns to guess the correct word
```

if you want to practive with more attempts try out something like:
python play_wordle.py --turn 9
You have 9 guesses remaining
Please enter your 5 letter guess: hello
⬛ 🟨 ⬛ ⬛ 🟨
h  e  l  l  o
You have 8 guesses remaining
Please enter your 5 letter guess: world
⬛ 🟩 ⬛ ⬛ ⬛
w  o  r  l  d
You have 7 guesses remaining
Please enter your 5 letter guess: myold
⬛ 🟨 🟩 ⬛ ⬛
m  y  o  l  d
You have 6 guesses remaining
Please enter your 5 letter guess: frien
⬛ ⬛ ⬛ 🟩 ⬛
f  r  i  e  n
You have 5 guesses remaining
Please enter your 5 letter guess: icome
⬛ ⬛ 🟩 ⬛ 🟨
i  c  o  m  e
You have 4 guesses remaining
Please enter your 5 letter guess: to
Please enter your 5 letter guess: totak
⬛ 🟩 ⬛ ⬛ ⬛
t  o  t  a  k
You have 3 guesses remaining
Please enter your 5 letter guess: toyou
⬛ 🟩 🟨 🟨 ⬛
t  o  y  o  u
You have 2 guesses remaining
Please enter your 5 letter guess: again
⬛ ⬛ ⬛ ⬛ ⬛
a  g  a  i  n
You have 1 guesses remaining
Please enter your 5 letter guess: pliss
⬛ ⬛ ⬛ 🟨 ⬛
p  l  i  s  s
The word was sooey, better luck next time...


For now that's it hope you have fun with it!