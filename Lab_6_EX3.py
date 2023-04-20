import pygame as pg
pg.init()



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.keep = text
        self.num = False
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.keep = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    
                    self.text += event.unicode
                    
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def recollect(self):
        return self.keep
    
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

    def isclick(self):
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(150, 150, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(150, 300, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(450, 150, 140, 32) # สร้าง InputBox3
input_box4 = InputBox(330, 400, 140, 32)
input_boxes = [input_box1, input_box2, input_box3, input_box4] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

# ///////////////////////////////////////////////////////////////////////

font = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
text = font.render('FRA 142', True, (255,255,255), (0,0,0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (win_x // 2, 50)


textF = font.render('Fristname', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRectF = text.get_rect() # text size
textRectF.center = (220, 120)

textL = font.render('Lastname', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRectL = text.get_rect() # text size
textRectL.center = (520, 120)

textA = font.render('Age', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRectA = text.get_rect() # text size
textRectA.center = (220, 270)

textS = font.render('Submit', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRectS = text.get_rect() # text size
textRectS.center = (435, 416)

textt = font.render('', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRectt = text.get_rect() # text size
textRectt.center = (435, 450)
# ///////////////////////////////////////////////////////////////////////



while run:
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)
    screen.blit(textF, textRectF)
    screen.blit(textL, textRectL)
    screen.blit(textA, textRectA)
    screen.blit(textS, textRectS)
    screen.blit(textt, textRectt)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        if input_box4.isclick():
            textt = font.render('Hello ' + input_box1.text +'  '+  input_box3.text +'  '+ 'You are  ' + input_box2.text + '  years old.', True, (0,0,0), (255,255,255))
        for box in input_boxes:
            box.handle_event(event)
            if box.active and input_box2 == box:
                input_box2.num = True
            else:
                input_box2.num = False
                
        
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()