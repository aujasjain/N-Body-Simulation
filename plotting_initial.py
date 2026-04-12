import initial

INITIAL_CONDITION = "solar_system"

def main():    
    system, labels, colors, legend = initial.get_initial_conditions(INITIAL_CONDITION)
    print("Number of particles:", system.num_particles)
    print("Initial positions (AU):\n", system.x)
    print("Initial velocities (AU/day):\n", system.v)
    print("Masses (M_sun):\n", system.m)
    print("Gravitational constant (AU^3 / day^2 / M_sun):", system.G)
        
    initial.plot_initial_conditions(system = system, labels = labels, colors = colors, legend = legend)

main()
