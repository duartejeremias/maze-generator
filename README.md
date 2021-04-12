![Capture](https://user-images.githubusercontent.com/50424889/114473541-58d6ee80-9bec-11eb-95e6-6737de1a1e8c.PNG)
# Maze Generator
Program that generates a maze given a length and width

## How to run

If using an ide:
```sh
Place every file in a folder and run main.py
```

If running on terminal:
```sh
python main.py
```

## How it works
* Given a length, width and density of walls, the program will run until it generates a maze with **at least** one 
possible solution.
* Has 2 types of generation, fast (path is generated first and then the walls) and slow (walls are generated first and 
  then the path)
* Contains an implementation of the A* path-finding algorithm to solve generated maze.

### Side notes

* The bigger the area of the maze and density of walls, the longer the program will take to finish because the 
 availability of free spaces will lower (in other words, there will be no solution more often than not).

* If given density of walls is 100% (or 1.0), the maze will always be impossible because all would-be free spaces will 
 be walls.

* If the start and end point get generated next to each other, there won't be a path because the solution is trivial 
 (this could make a 100% density maze possible).

* It's my first time making a pygame UI to support my project, in other words, UI is a little bit wanky, if you have any
 suggestions to make it better please send them or do them yourself for me to checkout!

## Author
* Duarte Jeremias
