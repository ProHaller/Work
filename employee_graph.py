import json

import matplotlib.pyplot as plt
import networkx as nx


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def create_graph(data):
    G = nx.Graph()
    for employee in data["employees"]:
        G.add_node(employee["name"], attr=employee)
        for colleague in data["employees"]:
            if employee["name"] != colleague["name"]:
                # Attributes for edge types
                edge_attrs = {
                    "shared_projects": len(
                        set(employee["projects"]) & set(colleague["projects"])
                    ),
                    "same_team": len(set(employee["teams"]) & set(colleague["teams"])),
                    "same_location": employee["office_location"]
                    == colleague["office_location"],
                }
                # Only add an edge if there is some shared attribute
                if any(edge_attrs.values()):
                    G.add_edge(employee["name"], colleague["name"], **edge_attrs)
    return G


def visualize_graph(G):
    pos = nx.spring_layout(G)  # Using spring layout for visualization

    # Drawing nodes
    nx.draw_networkx_nodes(G, pos)

    # Drawing edges with different styles for each relationship type
    shared_projects_edges = [
        (u, v) for u, v, d in G.edges(data=True) if d["shared_projects"] > 0
    ]
    same_team_edges = [(u, v) for u, v, d in G.edges(data=True) if d["same_team"] > 0]
    same_location_edges = [
        (u, v) for u, v, d in G.edges(data=True) if d["same_location"]
    ]

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=shared_projects_edges,
        edge_color="blue",
        label="Shared Projects",
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=same_team_edges,
        edge_color="green",
        style="dashed",
        label="Same Team",
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=same_location_edges,
        edge_color="red",
        style="dotted",
        label="Same Location",
    )

    # Drawing labels
    nx.draw_networkx_labels(G, pos)

    # Show legend
    plt.legend()
    plt.show()


def main():
    data = read_json("employees.json")
    G = create_graph(data)
    visualize_graph(G)


if __name__ == "__main__":
    main()
