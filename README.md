
# Advent of Code 2023 
This is my real first shot at Python. 

# Day 1
First time into python was quite a bit of a challenge.
From my POV kind of weird syntax, but definitely more user-friendly than for example Java. Going to keep going with Python and maybe switch to Go

The first task was pretty easy. Just some simple ASCII and stuff

The second task was one of the hardest things I've ever tried. I got the right answer for the example input on their website, but not for my input

The error was that some numbers that directly began with a number weren't processed correctly, and therefore my variable ```currentMax``` wasn't set correctly. 

For example, ```5hdakjshdkjahsd``` was 50 instead of 55, which resulted in calculation errors.

# Day 2
Feeling a bit more confident in what im doing

The first task was pretty easy, first I tried around with some regex, but later i found out a simple ```find()``` did the trick. Probably a bit to complex, I might refactor the code for the sake of convenience. 

There is probably a better solution for my handling with the variable ```invalid```. Couldn't think of any other solution that didn't require rewriting my entire code.

The second task was pretty easy too, just added some logic behind the lowest possible values for ```minRedInt, minBlueInt, minGreenInt```

# Day 3
This task was pretty difficult

The first task was probably one of the hardest programming puzzles I've every tried to solve. I thought of doing some things with a matrix, by adding the ASCII codes from the single characters and comparing them with the wanted numbers but i couldn't quite wrap my head around it, so i just fiddled around with some string manipulation, regex search and a fair bit of logic.

There is probably a way easier way to do this, but this is it.