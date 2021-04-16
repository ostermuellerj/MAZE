import cv2
import numpy as np

with open("sizes.txt") as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in open("sizes.txt")]
for i in range(len(lines)):
	lines[i]=lines[i].split(" ")
	lines[i][0]=int(lines[i][0])
	lines[i][1]=int(lines[i][1])

def doMaze(h, w):
	x0=0
	y0=0

	moves=[] #[right, down, left, up]
		
	grid=np.zeros((h*2+1,w*2+1))
	grid[1::2,1::2]=255
	stack=[]
	current=[y0,x0]
	grid[y0*2+1,x0*2+1]=128
	finished=False

	def checkMoves(y,x):
		if x<w-1 and grid[y*2+1,x*2+3]==255: 
			moves.append("right")
		if y<h-1 and grid[y*2+3,x*2+1]==255: 
			moves.append("down")
		if grid[y*2+1,x*2-1]==255: 
			moves.append("left")
		if grid[y*2-1,x*2+1]==255: 
			moves.append("up")
			
	def doMove(y,x):
		#print(moves)
		grid[current[1]*2+1,current[0]*2+1]=254
		s=np.random.choice(moves)
		stack.append([x,y])
		if s == "right": 
			grid[y*2+1,x*2+2]=255
			current[0]=x+1
			current[1]=y
		if s == "down":	
			grid[y*2+2,x*2+1]=255
			current[0]=x
			current[1]=y+1
		if s == "left": 
			grid[y*2+1,x*2]=255
			current[0]=x-1
			current[1]=y
		if s == "up": 
			grid[y*2,x*2+1]=255
			current[0]=x
			current[1]=y-1
		delMoves()
		grid[current[1]*2+1,current[0]*2+1]=254
		checkMoves(current[1],current[0])

	def delMoves():
		for i in range(len(moves)):
			del moves[0]

	checkMoves(current[1],current[0])
	#while len(moves)>0:
	#	doMove(current[1],current[0])
	#print(moves)

	while finished!=True:
	#	print(len(stack))
		if len(moves)>0:
			#print("00000")
			doMove(current[1],current[0])
		elif len(stack)>0:
			current=stack.pop(len(stack)-1)
			checkMoves(current[1],current[0])
			#print(len(stack))
			#print("1111111")
		if len(stack)==0:
			finished=True
	print("~~~~~~~~~~~~")

	cv2.imwrite("output/generated/maze_%s_%s.png" % (w,h),grid)
	#cv2.imshow("grid", grid)
	#cv2.waitKey(0)
	#cv2.imshow("maze - Copy.png", copy)
	#cv2.waitKey(0)
	cv2.destroyAllWindows()

for i in range (len(lines)):
	print(lines[i][1],int(lines[i][0]))
	doMaze(lines[i][0],lines[i][1])
#doMaze(80,80)
