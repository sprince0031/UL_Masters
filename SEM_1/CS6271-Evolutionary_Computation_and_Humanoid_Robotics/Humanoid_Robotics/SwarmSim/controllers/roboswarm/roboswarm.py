from controller import Robot, Motor, Supervisor
import pso

WHEEL_RADIUS = 0.05
AXLE_LENGTH = 0.3

robot = Robot()
supervisor = Supervisor()

box = supervisor.getFromDef('box')
box_translation_field = box.getField('translation')

robots = []
motors = []
for i in range(4):
    robot_node = supervisor.getFromDef('robot' + str(i))
    robots.append(robot_node)
    left_motor = robot_node.getDevice('left wheel motor')
    right_motor = robot_node.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    motors.append((left_motor, right_motor))

def fitness_function(params):
    # Set the speed of the robots based on the PSO parameters
    for i in range(4):
        left_speed = params[i * 2]
        right_speed = params[i * 2 + 1]
        motors[i][0].setVelocity(left_speed * WHEEL_RADIUS)
        motors[i][1].setVelocity(right_speed * WHEEL_RADIUS)

    # Get the current position of the box
    box_translation = box_translation_field.getSFVec3f()

    # Calculate the distance between the box and the marked location
    distance = ((box_translation[0] - 2) ** 2 + (box_translation[2] - 2) ** 2) ** 0.5

    # Calculate the time taken to move the box
    time = robot.getTime()

    # Return the fitness value
    return distance + time

# Define the PSO parameters
num_particles = 10
num_dimensions = 8
max_iterations = 100
bounds = [(-1, 1)] * num_dimensions

# Run the PSO algorithm
best_params, best_fitness = pso.run_pso(fitness_function, num_particles, num_dimensions, max_iterations, bounds)

# Print the best parameters and fitness value
print('Best parameters:', best_params)
print('Best fitness:', best_fitness)
