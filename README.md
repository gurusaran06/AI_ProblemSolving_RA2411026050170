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

## Team Details

| Field | Details |
|-------|---------|
| Name | Gurusaran A |
| Assignment | AI Problem Solving-Map colouring — GitHub Submission |
| Problem | Problem 5: Map Coloring (CSP) |
| Language | Python |
| Framework | Streamlit |
| Deadline | 25th April 2026 |

---

## License

This project is submitted as part of an academic assignment. All rights reserved by the respective institution.
