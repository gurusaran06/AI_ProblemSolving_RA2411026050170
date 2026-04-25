import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------
# CSP Backtracking Algorithm
# -----------------------------
def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtracking(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment, neighbors):
            assignment[unassigned] = color
            result = backtracking(assignment, regions, colors, neighbors)
            if result:
                return result
            del assignment[unassigned]

    return None


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🗺️ Map Coloring Problem (CSP)")

st.write("Enter regions and their neighbors:")

regions_input = st.text_input("Regions (comma separated)", "A,B,C,D")

neighbors_input = st.text_area(
    "Neighbors (format: A:B,C)",
    "A:B,C\nB:A,C,D\nC:A,B,D\nD:B,C"
)

colors_input = st.text_input("Colors (comma separated)", "Red,Green,Blue")

if st.button("Solve Map Coloring"):

    regions = [r.strip() for r in regions_input.split(",")]
    colors = [c.strip() for c in colors_input.split(",")]

    neighbors = {}
    for line in neighbors_input.split("\n"):
        if ":" in line:
            region, neigh = line.split(":")
            neighbors[region.strip()] = [n.strip() for n in neigh.split(",")]

    solution = backtracking({}, regions, colors, neighbors)

    if solution:
        st.success("Solution Found!")

        for region, color in solution.items():
            st.write(f"{region} → {color}")

        # -----------------------------
        # Visualization
        # -----------------------------
        G = nx.Graph()

        for region in regions:
            G.add_node(region)

        for region, neighs in neighbors.items():
            for n in neighs:
                G.add_edge(region, n)

        color_map = [solution[node] for node in G.nodes()]

        pos = nx.spring_layout(G)

        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=2000, font_size=15)
        st.pyplot(plt)

    else:
        st.error("No valid coloring found!")