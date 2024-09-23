from flask import Flask, request, render_template

app = Flask(__name__)

# Function to calculate the Bellman-Ford result
def bellman_ford_with_stops(vertices, edges, start, end, max_stops):
    dist = [[float("inf")] * (vertices) for _ in range(max_stops + 2)]
    dist[0][start] = 0
    predecessor = [-1] * vertices

    for i in range(1, max_stops + 2):
        for u, v, w in edges:
            if dist[i-1][u] != float("inf") and dist[i-1][u] + w < dist[i][v]:
                dist[i][v] = dist[i-1][u] + w
                predecessor[v] = u

    min_dist = min(dist[i][end] for i in range(1, max_stops + 2))
    if min_dist == float("inf"):
        return None, None

    path = []
    current = end
    while current != start:
        path.append(current)
        current = predecessor[current]
    path.append(start)
    path.reverse()

    return min_dist, path

# Home route to display the form
@app.route('/')
def home():
    return render_template('form.html')

# Route to display the result after processing the input
@app.route('/result', methods=['POST'])
def result():
    num_vertices = int(request.form['num_vertices'])
    num_edges = int(request.form['num_edges'])
    
    # Collect the edges from the form input
    edges = []
    for i in range(num_edges):
        u = int(request.form[f'edge_{i}_source'])
        v = int(request.form[f'edge_{i}_destination'])
        w = int(request.form[f'edge_{i}_weight'])
        edges.append((u, v, w))

    start = int(request.form['start'])
    end = int(request.form['end'])
    max_stops = int(request.form['max_stops'])

    # Call the Bellman-Ford function with user input
    min_energy, path = bellman_ford_with_stops(num_vertices, edges, start, end, max_stops)

    if min_energy is None:
        return f"No valid path from station {start} to station {end} within {max_stops} stops."

    path_description = " -> ".join(map(str, path))
    return f"Minimum energy required: {min_energy} units.<br>Path: {path_description}"

if __name__ == "__main__":
    app.run(debug=True)
