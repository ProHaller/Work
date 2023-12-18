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
                # Calculate similarity or "distance" based on shared attributes
                distance = calculate_distance(employee, colleague)
                if distance > 0:
                    G.add_edge(employee["name"], colleague["name"], weight=distance)
    return G


def calculate_distance(emp1, emp2):
    # Simple example: count of shared projects
    shared_projects = len(set(emp1["projects"]) & set(emp2["projects"]))
    return shared_projects


def visualize_graph(G):
    pos = nx.spring_layout(G)  # Using spring layout for visualization
    nx.draw(G, pos, with_labels=True)
    plt.show()


def main():
    data = read_json("employees.json")
    G = create_graph(data)
    visualize_graph(G)


if __name__ == "__main__":
    main()
