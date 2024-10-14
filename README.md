# nback

![2back example](assets/wm-task.png)

This project implements an N-Back Test, a cognitive task used to measure a part of working memory and working memory capacity.

## Overview

The N-Back test is a continuous performance task that is commonly used in cognitive neuroscience to measure a part of working memory. The test presents a sequence of stimuli, and the participant must indicate when the current stimulus matches the one from n steps earlier in the sequence.

## Features

- Customizable N-Back parameters:
    - N-Back levels from 1 to 5 (nBackLevels = [1, 2, 3, 4, 5])
    - 50% chance of n-back match (matchProbability = 0.50)
    - 5-minute game duration (gameDuration = 300000 milliseconds)
    - 900 milliseconds persistence time for each stimulus (persistenceTime = 900)
    - 1000 milliseconds inter-stimulus interval (interStimulusInterval = 1000)
- Visual representation using a 3x3 grid
- Randomized dot positions
- Performance tracking
- Results exported as CSV file

## How to Use

1. Open `index.html` in a web browser.
2. Enter your Participant ID.
3. Select the desired N-Back level (1 to 5).
4. Click "Start Test" to begin.
5. A red dot will appear at random positions in the 3x3 grid.
6. Press the SPACEBAR if the current dot position matches the one 'n' steps back.
7. After completing the test, a CSV file with your results will be automatically downloaded.

## Data Analysis

Please refer to the Jupyter Notebook for data analysis and visualization:

https://colab.research.google.com/drive/1vbi5tAcaq8m-vng3HAZbrirPaPQAHZnM?usp=sharing

Karthikeyan, R., Smoot, M.R. & Mehta, R.K. Anodal tDCS augments and preserves working memory beyond time-on-task deficits. Sci Rep 11, 19134 (2021). https://doi.org/10.1038/s41598-021-98636-y

## Instructions

1. A red dot will appear at a random position in the 3x3 grid.
2. Your task is to remember the position of the dot 'n' steps back.
3. Press the SPACEBAR if the current dot position matches the one 'n' steps back.
4. After the game, a CSV file with your results will be downloaded.

## Contributing

Contributions to improve the N-Back Test are welcome. Please feel free to submit a Pull Request.

## License

MIT License

## Website

For more information, visit [nimRobotics.com](https://nimrobotics.com)

---

© 2024 Aakash Yadav
