import pygame as pg
pg.init()

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
check_d = False
check_a = False
check_w = False
check_s = False
d = 0
a= 0
w = 0
s = 0
posX = 100
posY = 100
while(1):
    screen.fill((255, 255, 255))
    pg.draw.rect(screen,(67,205,128),(posX+d-a,posY-w+s,100,100))
    if check_w:
        print(w)
        w += 1
        pg.time.delay(1)
    if check_d:
        print(d)
        d += 1
        pg.time.delay(1)
    if check_s:
        print(s)
        s += 1
        pg.time.delay(1)
    if check_a:
        print(a)
        a += 1
        pg.time.delay(1)
        
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            print("Key W down")
            check_w = True
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม W
            print("Key W up")
            check_w = False
        

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            check_d = True
        if event.type == pg.KEYUP and event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม D
            print("Key D up")
            check_d = False


        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
            print("Key S down")
            check_s = True
        if event.type == pg.KEYUP and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม S
            print("Key S up")
            check_s = False
        

        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
            print("Key A down")
            check_a = True
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A up")
            check_a = False

        