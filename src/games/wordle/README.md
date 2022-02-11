<a name=top>

<a href="https://github.com/andre-motta/random" ><img width=1100
  src="https://github.com/andre-motta/random/blob/master/docs/img/banner.png"></a>
<hr>
<p>
&nbsp;
<a href="https://github.com/andre-motta/random">home</a> :&nbsp;:
<a href="https://github.com/andre-motta/random/blob/master/src/README.md">src</a> ::
<a href="https://github.com/andre-motta/random/blob/master/LICENSE.md">&copy; 2021</a>


<br>
<hr>


![Size](https://img.shields.io/github/repo-size/andre-motta/random?label=Size)
![Last Commit](https://img.shields.io/github/last-commit/andre-motta/random)
[![GitHub issues](https://img.shields.io/github/issues/andre-motta/random)](https://github.com/andre-motta/random/issues)
[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://github.com/license/ai-se/sneak/blob/main/LICENSE)

## What the hell is Wordle?[1]

Wordle is the viral word game that was recently acquired by the New York Times for a figure in the low millions.

<img src="https://www.cnet.com/a/img/SW9w37YfQPG8QgA8voATSKc22nM=/1092x0/2022/01/29/c4d41b24-8a7d-4413-844e-188b30a2bfa0/wordle-2022-030.jpg" width="582" height="388">

The game gives players six chances to guess a randomly selected five-letter word. As shown above, if you have the right letter in the right spot, it shows up green. A correct letter in the wrong spot shows up yellow. A letter that isn't in the word in any spot shows up gray. 

You can enter a total of six words, meaning you can enter five burner words from which you can learn hints about the letters and their placements. Then you get one chance to put those hints to use. Or you can try for performance and guess the word of the day in three, two or even one go.

*Section obtained from: [cnet.com](https://www.cnet.com/how-to/wordle-explained-everything-you-need-to-know-about-the-viral-word-game/)*

## Why a Wordle project?

One can think about wordle as a simple guessing game. However, this game can be looked at from an information theory point of view.

See, the list of all 5 letter words wordle accepts as input is freely available online. A [copy](data/words.txt) of this list can be found in this repo. The game returns to you plently of information through information on the presence of letters in the expected word, their position or misposition, or their non-presence.

I`ll let Mr. [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) explain, since he does a much better job than I will ever do:

[![Worlde by 3Blue1Brown](https://img.youtube.com/vi/v68zYyaEmEA/0.jpg)](https://www.youtube.com/watch?v=v68zYyaEmEA)

## Documentation

Documentation for the project can be found [here](docs/wordle_solver.md).

*This documentation was generated with the help of [Pycco](https://github.com/pycco-docs/pycco)*


## Languages

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
