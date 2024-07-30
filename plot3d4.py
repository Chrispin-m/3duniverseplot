import plotly.graph_objects as go
import random

# Define a function to generate both blue and internal points
def generate_3d_world_with_internal(iterations, num_internal_points_per_iteration):
    blue_points = []
    internal_points = []
    edges = [3, 6, 9]
    edges2 = [3, 6, 9]
    numbers = [1, 2, 4, 5, 7, 8, 10, 14, 16, 20, 28, 32, 40, 56]
    
    # Initialize max values to track bounds for internal points
    x_max = edges[0]
    y_max = edges[1]
    z_max = edges[2]
    
    for i in range(3):
        # Generate blue points
        x = edges[0]
        y = edges[1]
        z = edges[2]
        blue_points.append((x, y, z))
        
        # Update max values
        x_max = max(x_max, edges[i % len(edges2)])
        y_max = max(y_max, edges[(i + 1) % len(edges2)])
        z_max = max(z_max, edges[(i + 2) % len(edges2)])

        if edges[0]==3:
            edges2=[12,18,24]
            edges=edges2
        else:
            edges2=edges
            edges[0] = edges[1] + edges[1]
            edges[1]= edges2[0]*4
            edges[2] = edges[0] + edges[0]
        edges=edges[:3]
        print(edges)
        print(edges2)
        
        # Generate internal points within bounds of the current blue point
        for _ in range(num_internal_points_per_iteration):
            try:
                x_internal = random.choice([num for num in numbers if num < x])
                y_internal = random.choice([num for num in numbers if num < y])
                z_internal = random.choice([num for num in numbers if num < z])
                internal_points.append((x_internal, y_internal, z_internal))
            except:
                continue


    return blue_points, internal_points

# Parameters
iterations = 10
num_internal_points_per_iteration = 1000

# Generate points
blue_points, internal_points = generate_3d_world_with_internal(iterations, num_internal_points_per_iteration)

# Extract x, y, and z coordinates for the main points
x_coords = [point[0] for point in blue_points]
y_coords = [point[1] for point in blue_points]
z_coords = [point[2] for point in blue_points]

# Extract x, y, and z coordinates for the internal points
internal_x_coords = [point[0] for point in internal_points]
internal_y_coords = [point[1] for point in internal_points]
internal_z_coords = [point[2] for point in internal_points]

# Create the 3D scatter plot
fig = go.Figure()

# Add main points
fig.add_trace(go.Scatter3d(
    x=x_coords, y=y_coords, z=z_coords,
    mode='markers',
    marker=dict(size=5, color='blue'),
    name='Main Points'
))

# Add internal points
fig.add_trace(go.Scatter3d(
    x=internal_x_coords, y=internal_y_coords, z=internal_z_coords,
    mode='markers',
    marker=dict(size=3, color='green'),
    name='Internal Points'
))

# Connect the main points with threads
for i in range(len(blue_points) - 1):
    fig.add_trace(go.Scatter3d(
        x=[blue_points[i][0], blue_points[i + 1][0]],
        y=[blue_points[i][1], blue_points[i + 1][1]],
        z=[blue_points[i][2], blue_points[i + 1][2]],
        mode='lines',
        line=dict(color='red', width=2),
        showlegend=False
    ))

# Connect internal complementary points
def add_complementary_lines(points, fig):
    colors = ['magenta', 'cyan', 'yellow', 'black', 'orange', 'purple']
    for i, point in enumerate(points):
        comp_index = (i + len(points) // 2) % len(points)
        fig.add_trace(go.Scatter3d(
            x=[point[0], points[comp_index][0]],
            y=[point[1], points[comp_index][1]],
            z=[point[2], points[comp_index][2]],
            mode='lines',
            line=dict(color=random.choice(colors), width=1),
            showlegend=False
        ))

add_complementary_lines(internal_points, fig)

# Set labels and title
fig.update_layout(
    scene=dict(
        xaxis_title='X axis (edges)',
        yaxis_title='Y axis (edges)',
        zaxis_title='Z axis (edges)'
    ),
    title='3D World Growth Simulation with Internal Points',
    showlegend=True
)

# Show the plot
fig.show()
