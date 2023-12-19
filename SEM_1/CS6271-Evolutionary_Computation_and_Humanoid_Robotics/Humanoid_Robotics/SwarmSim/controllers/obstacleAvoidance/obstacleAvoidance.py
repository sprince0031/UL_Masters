from controller import Robot

TIME_STEP = 64
robot = Robot()
        
WHEEL_RADIUS = 0.005

ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_rear_right', 'ds_rear_left']
for i in range(4):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
left_motor = robot.getDevice('wheel_motor_left')
right_motor = robot.getDevice('wheel_motor_right')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.5 * WHEEL_RADIUS)
right_motor.setVelocity(-0.5 * WHEEL_RADIUS)

target_left_encoder = 1000
target_right_encoder = -1000

avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    # left_encoder = left_motor.getPosition() / WHEEL_RADIUS
    # right_encoder = right_motor.getPosition() / WHEEL_RADIUS
    # if left_encoder >= target_left_encoder and right_encoder <= target_right_encoder:
        # left_motor.setVelocity(0)
        # right_motor.setVelocity(0)
        # break
    leftSpeed = 2.0
    rightSpeed = 2.0
    # if avoidObstacleCounter > 0:
        # avoidObstacleCounter -= 1
        # leftSpeed = -4.0
        # rightSpeed = 0.0
    # else:  # read sensors
        # for i in range(4):
            # if ds[i].getValue() < 550.0:
                # avoidObstacleCounter = 100
    left_motor.setVelocity(leftSpeed)
    right_motor.setVelocity(rightSpeed)