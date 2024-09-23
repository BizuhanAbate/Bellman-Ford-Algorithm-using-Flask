# Bellman-Ford Algorithm using Flask
This is a python code of Bellman-Ford algorithm with Flask to make the code interactive.

# Description
Using Flask, I created a web interface that accepts input from users and provides responses based on the logic of Bellman-Ford algorithm.

The html form accepts the number of vertices, edges based on which a JavaScript function called addEdgeFields will dynamically adds input fields for the edges.
And also start, end and max-stops points will be accepted and then using Bellman-Ford algorithm,
it will calculate the minimum energy required to travel from the start station to the end station with at most max_stops.

# How to Run 
To run this Flask project on your local machine, 

first clone the repository from GitHub using the command:   git clone https://github.com/BizuhanAbate/Bellman-Ford-Algorithm-using-Flask.git,
and then navigate into the project directory with:   cd Bellman-Ford-Algorithm-using-Flask.

It's recommended to create a virtual environment to manage dependencies, 
which you can do with: python -m venv venv on Windows or python3 -m venv venv on macOS/Linux, followed by activating it.

To start the Flask server, since the Flask application name is BellmanWithFlask.py
For Windows (Command Prompt):   set FLASK_APP=BellmanWithFlask.py
For macOS/Linux (Bash Shell):   export FLASK_APP=BellmanWithFlask.py

This will allow you to access the address on your local machine. Therefore Open your browser and 
go to the above given address to see the form. 

Finally, deactivate the virtual environment with deactivate when you’re done.


# How to Interact with the form on the browser
Enter the number of vertices and edges.
Provide the start, end stations and the maximum stops.
Get the minimum energy required for the travel and a path that takes to follow the least expensive route. 
