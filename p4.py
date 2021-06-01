import pygame, math
from numpy import *

# coordinates array
vertex = array([[50,150,10],[50,0,10],[150,0,10],[150,0,100],[50,0,100],[150,150,10],[150,150,100],[50,150,100],[100,200,45]])
vertexM = array([[50,150,10,1],[50,0,10,1],[150,0,10,1],[150,0,100,1],[50,0,100,1],[150,150,10,1],[150,150,100,1],[50,150,100,1],[100,200,45,1]])

# global vars #
w, h = 800, 800
s = 50
d = 2.5
Vsx = Vsy = Vcx = Vcy = w/2
# holds x and y coordinates of original shape
Xs = []
Ys = []
# holds x and y coordinates of transformed shape
Xs2 = []
Ys2 = []

# transformation matrices #
# result matrix (matrix resulting from each transformation)
resultM = []
# translate matrix
translateM = array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# scale matrix
scaleM = array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
# rotate through x-axis matrix
rotateXM = array([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
# rotate through y-axis matrix
rotateYM = array([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]])
# rotate through z-axis matrix
rotateZM = array([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]])

# pygame vars
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# convert 3D coordinates to 2D coordinates using perspective projection
def perspectiveProjection(shapeArr,transformArr):
  # get x,y,z values from original shape array
  x = []
  y = []
  z = []
  x2 = []
  y2 = []
  z2 = []
  # loop through original shape
  for i in range(len(shapeArr)):
    for j in range(len(shapeArr[i])):
      if (j == 0):
        x += ([shapeArr[i][j]])
      if (j == 1):
        y += ([shapeArr[i][j]])
      if (j == 2):
        z += ([shapeArr[i][j]])
  # loop through transformed shape
  for i in range(len(transformArr)):
    for j in range(len(transformArr[i])):
      if (j == 0):
        x2 += ([transformArr[i][j]])
      if (j == 1):
        y2 += ([transformArr[i][j]])
      if (j == 2):
        z2 += ([transformArr[i][j]])
  # get Xs and Ys values (new 2D coordinates) using
  # perspective projection equations
  global Xs, Ys, Xs2, Ys2, s, d, Vsx, Vsy, Vcx, Vcy
  # loop through original shape
  for i in range(len(x)):
    Xs += ([(d * x[i]) / (s * z[i]) * Vsx + Vcx])
  for i in range(len(y)):
    Ys += ([(d * y[i]) / (s * z[i]) * Vsy + Vcy])
  # loop through transformed shape
  for i in range(len(x2)):
    Xs2 += ([(d * x2[i]) / (s * z2[i]) * Vsx + Vcx])
  for i in range(len(y2)):
    Ys2 += ([(d * y2[i]) / (s * z2[i]) * Vsy + Vcy])

def displayShape(Xs, Ys, Xs2, Ys2):
  pygame.init()
  window = pygame.display.set_mode((w,h))
  # this draws the original shape
  pygame.draw.line(window, white, (Xs[1],Ys[1]), (Xs[2],Ys[2]), 5)
  pygame.draw.line(window, white, (Xs[2],Ys[2]), (Xs[3],Ys[3]), 5)
  pygame.draw.line(window, white, (Xs[3],Ys[3]), (Xs[4],Ys[4]), 5)
  pygame.draw.line(window, white, (Xs[4],Ys[4]), (Xs[1],Ys[1]), 5)

  pygame.draw.line(window, white, (Xs[0],Ys[0]), (Xs[5],Ys[5]), 5)
  pygame.draw.line(window, white, (Xs[5],Ys[5]), (Xs[6],Ys[6]), 5)
  pygame.draw.line(window, white, (Xs[6],Ys[6]), (Xs[7],Ys[7]), 5)
  pygame.draw.line(window, white, (Xs[7],Ys[7]), (Xs[0],Ys[0]), 5)

  pygame.draw.line(window, white, (Xs[0],Ys[0]), (Xs[1],Ys[1]), 5)
  pygame.draw.line(window, white, (Xs[5],Ys[5]), (Xs[2],Ys[2]), 5)
  pygame.draw.line(window, white, (Xs[7],Ys[7]), (Xs[4],Ys[4]), 5)
  pygame.draw.line(window, white, (Xs[6],Ys[6]), (Xs[3],Ys[3]), 5)

  pygame.draw.line(window, white, (Xs[8],Ys[8]), (Xs[0],Ys[0]), 5)
  pygame.draw.line(window, white, (Xs[8],Ys[8]), (Xs[5],Ys[5]), 5)
  pygame.draw.line(window, white, (Xs[8],Ys[8]), (Xs[6],Ys[6]), 5)
  pygame.draw.line(window, white, (Xs[8],Ys[8]), (Xs[7],Ys[7]), 5)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        # this draws the transformed shape
        pygame.draw.line(window, green, (Xs2[1],Ys2[1]), (Xs2[2],Ys2[2]), 5)
        pygame.draw.line(window, green, (Xs2[2],Ys2[2]), (Xs2[3],Ys2[3]), 5)
        pygame.draw.line(window, green, (Xs2[3],Ys2[3]), (Xs2[4],Ys2[4]), 5)
        pygame.draw.line(window, green, (Xs2[4],Ys2[4]), (Xs2[1],Ys2[1]), 5)

        pygame.draw.line(window, green, (Xs2[0],Ys2[0]), (Xs2[5],Ys2[5]), 5)
        pygame.draw.line(window, green, (Xs2[5],Ys2[5]), (Xs2[6],Ys2[6]), 5)
        pygame.draw.line(window, green, (Xs2[6],Ys2[6]), (Xs2[7],Ys2[7]), 5)
        pygame.draw.line(window, green, (Xs2[7],Ys2[7]), (Xs2[0],Ys2[0]), 5)

        pygame.draw.line(window, green, (Xs2[0],Ys2[0]), (Xs2[1],Ys2[1]), 5)
        pygame.draw.line(window, green, (Xs2[5],Ys2[5]), (Xs2[2],Ys2[2]), 5)
        pygame.draw.line(window, green, (Xs2[7],Ys2[7]), (Xs2[4],Ys2[4]), 5)
        pygame.draw.line(window, green, (Xs2[6],Ys2[6]), (Xs2[3],Ys2[3]), 5)

        pygame.draw.line(window, green, (Xs2[8],Ys2[8]), (Xs2[0],Ys2[0]), 5)
        pygame.draw.line(window, green, (Xs2[8],Ys2[8]), (Xs2[5],Ys2[5]), 5)
        pygame.draw.line(window, green, (Xs2[8],Ys2[8]), (Xs2[6],Ys2[6]), 5)
        pygame.draw.line(window, green, (Xs2[8],Ys2[8]), (Xs2[7],Ys2[7]), 5)
      pygame.display.update()

def applyTransformation(dataMatrix, transformMatrix):
  global resultM
  resultM = dataMatrix.dot(transformMatrix)

def translate3D(Tx, Ty, Tz):
  global translateM
  translateM[3,0] = Tx
  translateM[3,1] = Ty
  translateM[3,2] = Tz

def scale3D(Sx, Sy, Sz):
  global scaleM
  scaleM[0,0] = Sx
  scaleM[1,1] = Sy
  scaleM[2,2] = Sz

def rotateX(angle):
  # assign sin and cos values to variables
  sinTheta = math.sin(math.radians(angle))
  cosTheta = math.cos(math.radians(angle))

  # change values in rotateXM matrix
  global rotateXM
  rotateXM[1,1] = cosTheta
  rotateXM[1,2] = sinTheta
  rotateXM[2,1] = -sinTheta
  rotateXM[2,2] = cosTheta

def rotateY(angle):
  # assign sin and cos values to variables
  sinTheta = math.sin(math.radians(angle))
  cosTheta = math.cos(math.radians(angle))

  # change values in rotateYM matrix
  global rotateYM
  rotateYM[0,0] = cosTheta
  rotateYM[0,2] = -sinTheta
  rotateYM[2,0] = sinTheta
  rotateYM[2,2] = cosTheta

def rotateZ(angle):
  # assign sin and cos values to variables
  sinTheta = math.sin(math.radians(angle))
  cosTheta = math.cos(math.radians(angle))

  # change values in rotateZM matrix
  global rotateZM
  rotateZM[1,1] = cosTheta
  rotateZM[1,2] = sinTheta
  rotateZM[2,1] = -sinTheta
  rotateZM[2,2] = cosTheta

def main():
  print()

  print("Select operation: \n" \
          "1. 3D Translate\n" \
          "2. 3D Scale\n" \
          "3. 3D Rotation on X-axis\n" \
          "4. 3D Rotation on Y-axis\n" \
          "5. 3D Rotation on Z-axis\n")
  command = input("Select from 1,2,3,4,5: ")
  if command == '1':
    userTx = int(input("Enter Tx: "))
    userTy = int(input("Enter Ty: "))
    userTz = int(input("Enter Tz: "))
    translate3D(userTx,userTy,userTz)
    applyTransformation(vertexM,translateM)
    perspectiveProjection(vertexM, resultM)
    displayShape(Xs, Ys, Xs2, Ys2)
  elif command == '2':
    userSx = int(input("Enter Sx: "))
    userSy = int(input("Enter Sy: "))
    userSz = int(input("Enter Sz: "))
    scale3D(userSx,userSy,userSz)
    applyTransformation(vertexM,scaleM)
    perspectiveProjection(vertexM,resultM)
    displayShape(Xs, Ys, Xs2, Ys2)
  elif command == '3':
    angle = int(input("Enter angle: "))
    rotateX(angle)
    applyTransformation(vertexM, rotateXM)
    perspectiveProjection(vertexM, resultM)
    displayShape(Xs, Ys, Xs2, Ys2)
    print(resultM)
  elif command == '4':
    angle = int(input("Enter angle: "))
    rotateY(angle)
    applyTransformation(vertexM, rotateYM)
    perspectiveProjection(vertexM, resultM)
    displayShape(Xs, Ys, Xs2, Ys2)
    print(resultM)
  elif command == '5':
    angle = int(input("Enter angle: "))
    rotateZ(angle)
    applyTransformation(vertexM, rotateZM)
    perspectiveProjection(vertexM, resultM)
    displayShape(Xs, Ys, Xs2, Ys2)
    print(resultM)
  else:
    print("INVALID INPUT")

main()
