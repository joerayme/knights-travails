# The Knight's Travails

A program to find the shortest path between two points on a chess board for a knight.

## Decisions

Originally thought that Dijkstra's algorithm might be the way to go but I eventually realised that, given each of the moves is equally weighted, it would be essentially a breadth-first search of the tree which is a simpler algorithm to implement.

Currently all the code lives in one file as it's quite simple but if it were to expand at all I would probably look to start splitting things out.

## Requirements

* Python 3

## Running

To run the program, execute it and pass the start and end positions as arguments:

    ./knights_travails.py A1 B2

To run the tests, use the `unittest` module:

    python3 -m unittest discover
