from random import randint
carmen = {}

carmen[0] = [1,2,3]
carmen[1] = [4,5,6]
carmen[2] = [7,8,9]
carmen[3] = [10,11,12]
carmen[4] = [13,14,15]
carmen[5] = [16,17,18]


print(carmen)

stack = carmen.copy()

viewpoint_cam = stack.pop(randint(0, len(stack)-1))

print(viewpoint_cam)