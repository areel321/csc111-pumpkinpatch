#pumpkin graphic
from graphics import * 

def main():
  win = GraphWin('pumpkin', 400, 400)
  win.setBackground('white')
  win.setCoords(-100, -100, 100, 100)

  #pumpkin body
  outside = Oval(Point(-80, 50), Point(80, -70))
  outside.setWidth(0)
  outside.setFill(color_rgb(242, 140, 40))
  outside.draw(win)

  inner1 = Oval(Point(-60, 50), Point(60, -70))
  inner1.setWidth(0)
  inner1.setFill('orange')
  inner1.draw(win)

  inner2 = Oval(Point(-30, 50), Point(30, -70))
  inner2.setWidth(0)
  inner2.setFill(color_rgb(255, 191, 0))
  inner2.draw(win)

  #stem 
  stem1 = Polygon(Point(-20, 65), Point(5, 65), Point(0, 50))
  stem1.setOutline(color_rgb(28, 120, 17 ))
  stem1.setFill('green')
  stem1.draw(win)

  #face 
  left_eye = Polygon(Point(-30, 10), Point(-10, 10), Point(-20, 30))
  left_eye.setFill('black')
  left_eye.draw(win)

  right_eye = Polygon(Point(30, 10), Point(10, 10), Point(20, 30))
  right_eye.setFill('black')
  right_eye.draw(win)

  mouth = Polygon(Point(-30, -30), Point(30, -30), Point(0, -50))
  mouth.setFill('black')
  mouth.draw(win)

if __name__ == "__main__":
    main()
