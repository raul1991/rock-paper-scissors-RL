# Rock Paper Scissors Environment

It is just a simple version of a rock paper scissor game. However, to make the game deterministic
it takes in the move of the player and learns to maximize its wins.

# Running the jupyter notebook
For obvious reasons, you need to have jupyter, numpy installed in your system before running it.
Once done, you can start the notebook and run the example.

# What is happening in the output
You would see the following things in the output

- a matrix -> It represents the bot experience across multiple games against the player.

- exploiting/exploration -> The bot is fed with some initial experience (see np.uniform at the top) but it begins
with exploration when it thinks it does not have any experience and then starts exploiting the already gained experience.

- stats -> They just tell you of the moves of the player

# FAQ's

- Is the bot playing against pre-defined set of moves of the player ?

No. The player's move has been randomly generated and are then used by the bot to gain experience and win.

- This isn't how the game is played. Right ?

Good find. In this version of the game I take in the user move and then train the bot to optimize itself. In my
case the bot always wins after the training is complete but in the real game the bot will sometime DRAW as well
since the moves of the player is random.

- How do I run your sample ?

Install the dependencies and run the notebook placed in the repo.

- How to install this package ?

`pip3 install rock-paper-scissors`
