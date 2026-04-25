import streamlit as st
import heapq

# -----------------------------
# Uniform Cost Search Algorithm
# -----------------------------
def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [])]  # (cost, node, path)

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return None, float("inf")


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Uniform Cost Search (UCS)")

st.write("Enter graph edges in the format: A B 2 (means A to B with cost 2)")

edges_input = st.text_area(
    "Enter edges (one per line)",
    "A B 1\nA C 4\nB D 2\nC D 1\nD F 3\nB E 5\nE F 1"
)

start_node = st.text_input("Start Node", "A")
goal_node = st.text_input("Goal Node", "F")

if st.button("Find Shortest Path"):
    graph = {}

    # Build graph
    for line in edges_input.split("\n"):
        parts = line.split()
        if len(parts) != 3:
            continue

        src, dest, cost = parts[0], parts[1], int(parts[2])

        if src not in graph:
            graph[src] = []

        graph[src].append((dest, cost))

    # Run UCS
    path, cost = uniform_cost_search(graph, start_node, goal_node)

    # Output
    if path:
        st.success("Path Found: " + " -> ".join(path))
        st.write("Total Cost:", cost)
    else:
        st.error("No path found")
