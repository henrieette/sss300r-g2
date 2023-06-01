import time
from gpiozero import CamJamKitRobot, DistanceSensor

pintrigger = 17
pinecho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho,trigger=pintrigger)

hownear = 15.0
reverstime= 0.5
turntime=0.75

leftmotorspeed=0.5
rightmotorspeed=0.5

motorforward=(leftmotorspeed,rightmotorspeed)
motorbackwards=(-leftmotorspeed,-rightmotorspeed)
motorleft=(leftmotorspeed,0)
motorright=(0,rightmotorspeed)

def isnearobtacle(localhownear):
	distance=sensor.distance*100
	
	print("IsNearObstacle: " +str(distance))
	if distance<localhownear:
		return True
	else:
		return False
		
def avoideobstacle():
	print("Backwards")
	robot.value=motorbackwards
	time.sleep(reverstime)
	robot.stop()
	
	print("right")
	robot.value=motorright
	time.sleep(turntime)
	robot.stop()
	
try:
	while True:
		robot.value=motorforward
		time.sleep(0.1)
		if isnearobtacle(hownear):
			robot.stop()
			avoideobstacle()
			
except KeyboardInterrupt:
	robot.stop()
