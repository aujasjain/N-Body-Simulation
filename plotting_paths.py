import timeit
import numpy as np
import initial

INITIAL_CONDITION = "solar_system"

# Default units is AU, days, and M_sun
TF = 200.0 * 365.24  # years to days
DT = 1.0
OUTPUT_INTERVAL = 1.0 * 365.24  # years to days
NUM_STEPS = int(TF / DT)

def main():
    # Get initial conditions
    mode = input("Type 'preset' or 'custom': ").strip().lower()

    if mode == "custom":
        system, labels, colors, legend = initial.get_user_defined_system()
    else:
        system, labels, colors, legend = initial.get_initial_conditions(INITIAL_CONDITION)
    # Initialize memory
    a = np.zeros((system.num_particles, 3))

    # Solution array
    sol_size = int(TF // OUTPUT_INTERVAL + 2)  # +2 for initial and final time
    sol_x = np.zeros((sol_size, system.num_particles, 3))
    sol_v = np.zeros((sol_size, system.num_particles, 3))
    sol_t = np.zeros(sol_size)
    sol_x[0] = system.x
    sol_v[0] = system.v
    sol_t[0] = 0.0
    output_count = 1

    # Launch simulation
    initial.print_simulation_info(
        system, TF, DT, NUM_STEPS, OUTPUT_INTERVAL, sol_size
    )
    next_output_time = output_count * OUTPUT_INTERVAL
    start = timeit.default_timer()
    for i in range(NUM_STEPS):
        initial.leapfrog(a, system, DT)

        current_time = i * DT
        if current_time >= next_output_time:
            sol_x[output_count] = system.x
            sol_v[output_count] = system.v
            sol_t[output_count] = current_time

            output_count += 1
            next_output_time = output_count * OUTPUT_INTERVAL

            print(f"Current time: {current_time:.2f} days", end="\r")

    sol_x = sol_x[:output_count]
    sol_v = sol_v[:output_count]
    sol_t = sol_t[:output_count]

    end = timeit.default_timer()

    print()
    print(f"Runtime: {end - start:.3g} seconds, Solution size: {output_count}")
    initial.animate_trajectory(sol_x, labels, colors, legend)

main()