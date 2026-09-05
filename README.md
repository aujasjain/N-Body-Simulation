# N-Body Simulation
A Python based simulation of gravitational N-body systems using Newtonian physics

Inspired by https://alvinng4.github.io/grav_sim/.

## What it does:
- Simulates gravitational interactions in N-body systems  
- Supports both real solar system data and custom initial configurations  
- Visualizes trajectories in 3D

## What I changed:
- Redesigned the simulation to support user defined systems
- Implemented a Leapfrog integrator for stable long-term orbital evolution
- Replaced the original structure with a fixed timestep simulation
- Added a full user input system for defining particles (position, velocity, mass)
- Built real-time animation and video export functionality
- Reorganized the code to improve clarity and extensibility

## To run:
```bash
python main.py
