# py-number-guess
Ever played that game where someone thinks of a number and you have to guess it while they say if it's higher or lower? <br />
Well I've basically made that in python but everything is a little more complicated than it should be. :D 

This was made using a chromebook out of pure boredom so I wasn't able to import any libraries. <br />
The whole script runs in the terminal.


# How to Play
- choose a difficulty
  - easy: 1-100
  - medium: 1-1000
  - hard: 1-10000
  - insane: 1-1000000
  - you can also enter any number to make that the maximum
- guess the number, and it will tell you if you need to go higher or lower
- don't worry about going out of range or guessing the same number twice - it will not count toward your score

In the difficulty select, you can see your high scores (or low scores i guess) with `hs`. <br />
All commands are shown with `help` in the difficulty select. <br /> 
Here is an example: <br />
```
> hs 100
your high score for 100 is 3
> hs
100 ---- 3
1000 --- 9
>
```

In the guessing phase, you can type `give up` to reveal the number and end the round. <br />
You can also close the program at any time with `close`, `exit`, or `quit`.

### NOTE:
This program will reference a file named `numguess_hs.json` in your ROOT directory. <br />
If it does not exist, one will be created for you. <br />
You may change the value of the `json_path` variable if you already have one named that for whatever reason
