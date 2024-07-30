# 3D World Growth Simulation with Internal Points

## Overview

This project generates and visualizes a 3D simulation of a universe using the numbers 3, 6, and 9, which are integral to understanding the structure of the universe and the concept of the multiverse. The simulation consists of "blue" points that represent key locations or boundaries in the 3D space, and "green" points that are generated within these boundaries to illustrate a more complex internal structure.

## Description

The simulation uses the following concepts:

- **Blue Points:** These are the main points that define the edges of the 3D space. They are generated based on the numbers 3, 6, and 9, with each iteration expanding the boundaries to create a growing grid of edges.
- **Internal Points:** These points are generated within the boundaries defined by the blue points. They are chosen randomly but constrained to be less than the current boundaries of each blue point. This provides a visual representation of how internal structures can fit within larger frameworks.

### Key Functions

- `generate_3d_world_with_internal(iterations, num_internal_points_per_iteration)`: This function generates both the blue points and internal points. It iterates to expand the edges of the 3D world, updating the boundaries and generating internal points within these bounds.

- `generate_internal_points(num_points, x_max, y_max, z_max)`: Generates internal points within given maximum x, y, and z bounds. This function ensures that internal points are always within the edges defined by the blue points.

### Plot Description

1. **Main Points (Blue):** Represent the core locations or boundaries of the 3D space. These points are plotted in blue and are connected by red lines to illustrate the structure.

2. **Internal Points (Green):** Scatter points within the bounds of the main points. These are plotted in green to show how smaller structures fit within the larger framework.

3. **Complementary Lines:** Additional lines connect internal points in various colors to visualize connections and relationships within the internal structure.

### Plot Interpretation

The plot helps illustrate a multiverse concept where the primary universe (represented by the blue points) has internal structures (the green points) that fit within it. As the boundaries expand, new internal points are generated, creating a complex and evolving 3D structure. The numbers 3, 6, and 9 are used to represent the fundamental edges of this universe, showing how these numbers can expand to create a rich and interconnected structure. 

Numbers 3, 6, and 9 hold a special place in the universe due to their unique interplay with other numbers, creating a captivating pattern that stands apart from the rest. While other numbers such as 1, 2, 4, 5, 7, and 8 cycle through predictable patterns—where 1+1=2, 2+2=4, 4+4=8, 5+5=10 and 1+0 gets us back to 1, 7+7=14 (4+1=5) (8+8=16 and 6+1=7) and this pattern happens infinitly without 3,6, and 9 ever appearing.The trio of 3, 6, and 9 create a harmonious loop of their own. For instance, 3 added to itself gives 6, and 6 doubled returns to 3 (since 6+6=12, and 1+2=3). In contrast, 9 is exceptional; it remains unchanged when added to itself (9+9=18, and 1+8=9) - 9 is actually the only independent number a "GOD" number - these three numbers are also known as the "Holy Trinity Numbers". This cyclical independence of 9, paired with the complementary nature of 3 and 6, creates a special pattern that isn't seen with other numbers. This interplay hints at a deeper, almost mystical structure to the numbers 3, 6, and 9, setting them apart in their own unique dimension - So I had this crazy idea that since the universe started these numbers have been at the center of it all and clearly the center is actually these numbers as simulated - it cuts the three dimensional cube into a perfect half and points or other numbers around it can grow harmonious around this line without coaliations.

### Running the Code

To run the code and generate the 3D plot, ensure you have the `plotly` library installed:

```bash
pip install plotly
```

Then, execute the script to visualize the 3D world simulation:

```bash
python plot3d4.py
```
