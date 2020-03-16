import pybullet as p
import time
import pybullet_data
import re
pattern = re.compile(r"base_motor\d*_\d*")
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("/media/vaibhav/New Volume/ML/Mini Project-II/review2/hexapod/hexapod.urdf",cubeStartPos, cubeStartOrientation)
num_joints = p.getNumJoints(boxId)
#print(p.getJointInfo(boxId,-1)[0],p.getJointInfo(boxId,-1)[1].decode('UTF-8'))
for i in range(num_joints):
  #print(p.getJointInfo(boxId,i)[0],p.getJointInfo(boxId,i)[1].decode('UTF-8'))
  name = p.getJointInfo(boxId,i)[1].decode('UTF-8')
  if pattern.match(name):
    print(p.getJointInfo(boxId,i)[0])
p.disconnect()