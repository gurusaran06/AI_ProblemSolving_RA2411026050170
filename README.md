# AI Problem Solving — Map Coloring Problem (CSP)

> **AI_ProblemSolving** | Problem 5: Map Coloring Problem using Constraint Satisfaction Problem (CSP)

---

## Problem Description

In a map coloring scenario, different regions on a map must be colored such that **no two adjacent regions share the same color**. This is a classic **Constraint Satisfaction Problem (CSP)** in Artificial Intelligence.

### Objective
Given a set of regions and their neighboring relationships, assign a color to each region such that:
- No two adjacent regions have the same color
- A **minimum number of colors** is used (e.g., 3 or 4 colors)

### Sample Input
| Field | Value |
|-------|-------|
| Regions | A, B, C, D |
| Adjacency | A→B,C &nbsp; B→A,C,D &nbsp; C→A,B,D &nbsp; D→B,C |
| Colors Available | Red, Green, Blue |

### Sample Output
```
A → Red
B → Green
C → Blue
D → Red
```

---

## Algorithm Used

### Constraint Satisfaction Problem (CSP) — Backtracking Search

The solution uses **Backtracking Search** to solve the map coloring problem:

1. **Variable Selection**: Pick an unassigned region.
2. **Domain Values**: Try each available color.
3. **Constraint Check (`is_valid`)**: Ensure no neighboring region has the same color.
4. **Backtrack**: If no valid color exists, undo the last assignment and try a different color.
5. **Termination**: When all regions are assigned a valid color, the solution is found.

```
function BACKTRACKING(assignment, regions, colors, neighbors):
    if all regions assigned → return assignment
    pick unassigned region
    for each color in colors:
        if color is valid for region:
            assign color to region
            result = BACKTRACKING(...)
            if result → return result
            remove assignment (backtrack)
    return failure
```

**Time Complexity**: O(d^n) — where `d` = number of colors, `n` = number of regions  
**Space Complexity**: O(n) — recursion depth equals number of regions

---

## Execution Steps

### Prerequisites

Make sure you have Python 3.x installed. Then install the required libraries:

```bash
pip install streamlit networkx matplotlib
```

### Running the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use the App

1. **Enter Regions** — type comma-separated region names (e.g., `A,B,C,D`)
2. **Enter Neighbors** — one line per region in the format `Region:Neighbor1,Neighbor2` (e.g., `A:B,C`)
3. **Enter Colors** — comma-separated color names (e.g., `Red,Green,Blue`)
4. Click **"Solve Map Coloring"**
5. View the color assignment and the visual graph

---

## Folder Structure

```
AI_ProblemSolving/
│
├── Problem5_MapColoring/
│   ├── app.py              # Main Streamlit application
│   └── README.md           # This file
│
└── README.md               # Root README (overall project)
```

---

## Sample Output (Screenshots)

### Input Panel
- Regions: `A, B, C, D`
- Neighbors: `A:B,C | B:A,C,D | C:A,B,D | D:B,C`
- Colors: `Red, Green, Blue`

### Result
```
 Solution Found!
A → Red
B → Green
C → Blue
D → Red
```

### Graph Visualization
The app renders a **colored graph** using `networkx` and `matplotlib`, where each node is colored according to the CSP solution.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| Streamlit | Interactive web UI |
| NetworkX | Graph creation and layout |
| Matplotlib | Graph visualization |

---

## References

- Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach* (Chapter 6: CSP)
- [Streamlit Documentation](https://docs.streamlit.io)
- [NetworkX Documentation](https://networkx.org)

---

# Uniform Cost Search (UCS) Visualizer

A simple interactive web app built with **Streamlit** that lets you define a weighted graph and find the least-cost path between two nodes using the **Uniform Cost Search** algorithm.

---

## What It Does

- Accepts a weighted graph as plain-text edge definitions
- Runs Uniform Cost Search from a user-specified start node to a goal node
- Displays the optimal path and its total cost

---

## Algorithm

**Uniform Cost Search** is a graph traversal algorithm that always expands the lowest-cost node first. It guarantees the optimal (minimum-cost) path in graphs with non-negative edge weights, making it a practical alternative to BFS when edge costs are not uniform.

### How it works
1. Initialize a priority queue with the start node at cost 0
2. Pop the node with the smallest cumulative cost
3. If it's the goal, return the path and cost
4. Otherwise, push all unvisited neighbors with their updated costs
5. Repeat until the goal is found or the queue is empty

---

## Requirements

- Python 3.7+
- `streamlit`

Install dependencies:

```bash
pip install streamlit
```

---

## Running the App

```bash
streamlit run uniform_cost_search.py
```

Then open your browser at `http://localhost:8501`.

---

## Usage

### Edge Input Format

Enter one edge per line in the format:

```
<Source> <Destination> <Cost>
```

**Example:**

```
A B 1
A C 4
B D 2
C D 1
D F 3
B E 5
E F 1
```

> Note: The graph is **directed**. To make it undirected, add both directions (e.g., `A B 1` and `B A 1`).

### Fields

| Field      | Description                        | Default |
|------------|------------------------------------|---------|
| Start Node | The node to begin the search from  | `A`     |
| Goal Node  | The target node to reach           | `F`     |

### Output

-  **Path Found** — displays the path (e.g., `A -> B -> D -> F`) and the total cost
-  **No path found** — shown when the goal is unreachable from the start

---

## Project Structure

```
.
└── uniform_cost_search.py   # Main app — algorithm + Streamlit UI
```

---

## Example

Using the default input:

```
A B 1
A C 4
B D 2
C D 1
D F 3
B E 5
E F 1
```

**Start:** `A` → **Goal:** `F`

**Result:** `A -> B -> D -> F` with total cost `6`

---

## Limitations

- Edge weights must be **integers**
- Only supports **directed** graphs (add reverse edges manually for undirected)
- No cycle detection beyond the `visited` set (sufficient for non-negative weights)

## Team Details

| Field | Details |
|-------|---------|
| Team Member 1 | Gurusaran A - RA2411026050170 |
| Team Member 2 | Richard Antony J - RA2411026050168 |
| Assignment | AI Problem Solving-Map Colouring and Uniform Cost Search |
| Language | Python |
| Framework | Streamlit |
| Deadline | 25th April 2026 |

---

## License

This project is submitted as part of an academic assignment. All rights reserved by the respective institution.
