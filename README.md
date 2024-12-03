# AI-Pathfinding-Algorithm-Implementation
A Python implementation of the A* pathfinding algorithm with multiple heuristic functions for path cost evaluation.

## Authors
- Bungein J Cheng

## Overview
This program implements the A* pathfinding algorithm to find optimal paths through weighted grids. It includes four different heuristic functions to evaluate path costs:

1. H1: All zeros (null heuristic)
2. H2: Manhattan distance
3. H3: Modified Manhattan distance (using max/min calculation)
4. H4: Manhattan distance with random error

## Key Components

### Node Class
- Represents a node in the pathfinding graph
- Stores position, parent node, and f, g, h values
- f = g + h (total cost)
- g = actual cost from start
- h = heuristic estimated cost to goal

### Heuristic Functions
- `h1_zero`: Returns 0 (baseline comparison)
- `h2_manhattan`: Calculates standard Manhattan distance
- `h3_modified_manhattan`: Uses max/min calculation variant
- `h4_manhattan_with_error`: Adds random error (-3 to +3) to Manhattan distance

### Main Algorithm
The `astar` function implements the A* pathfinding algorithm with:
- Input: maze (weighted grid), start position, end position, heuristic function
- Output: path cost, path coordinates, nodes created count, runtime in milliseconds

## Test Cases
Includes 5 test cases:
- 3 predefined mazes of varying sizes (5x5, 7x6, 10x10)
- 2 custom test mazes (10x10)

## Performance Metrics
The program measures and reports:
1. Path cost
2. Complete path coordinates
3. Number of nodes created
4. Runtime in milliseconds

## Output Format
- Individual test case results for each heuristic
- Summary tables comparing metrics across all test cases and heuristics

## Usage
Run the script directly:
```python
python PA1_mod2.py
```