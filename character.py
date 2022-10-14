from pico2d import *
state = {'STAY': 0, 'RUNNING' : 1,'JUMPING':2}
direction = {'LEFT': 0, 'RIGHT':1 }

class CupHead:
    def __init__(self):
        self.x, self.y = 400, 90
        self.stay_frame = 0
        self.run_frame = 0
        self.jump_frame = 0
        self.image = load_image('stay.png')
        self.state = state['STAY']
        self.direction = direction['RIGHT']
        self.jumpSpeed = 0
        self.dirx = 0
        self.mass = 2 # 무게
        
    def update(self):
        if (self.state == state['RUNNING'] ):
            self.image = load_image('run_right.png') #오른쪽으로 달리고 있는 이미지
            self.run_frame = (self.run_frame +1) % 16
        elif(self.state == state['STAY']):
            self.image = load_image('stay.png') #왼쪽 보는 stay이미지
            self.stay_frame = (self.stay_frame +1) %5
        elif(self.state == state['JUMPING']):

            self.image = load_image('jumping.png')
            self.jump_frame = (self.jump_frame +1) % 8

            if self.jumpSpeed > 0:
                 F = (0.5 * self.mass * (self.jumpSpeed **2))
            else:
                 F = -(0.5 * self.mass * (self.jumpSpeed **2))

          
            self.y += round(F)
            self.jumpSpeed -= 1

            if self.y < 90:
                self.y = 90
                self.state = state['STAY']
                self.jumpSpeed = 8

        self.x = self.x + self.dirx * 5
    
    def draw(self):


        if (self.state == state['STAY']):
            if (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(self.stay_frame * 169,330, 169, 225, 0, 'n', self.x-10, self.y, 169,225)
            elif(self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(self.stay_frame * 169,330, 169, 225, 0, 'h', self.x+10, self.y, 169,225)
    

        if (self.state == state['RUNNING']):
            if (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(self.run_frame * 190, 0,190, 239, 0,'h',self.x, self.y,190,239) ## 달리기 오른쪽으로 #달리기 이미지
            elif(self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(self.run_frame * 190, 0,190, 239, 0,'n',self.x, self.y,190,239)
    
        if (self.state == state['JUMPING']):
            if (self.direction == direction['RIGHT']):
                self.image.clip_composite_draw(self.jump_frame * 151, 0, 151, 179, 0, 'n', self.x, self.y, 151, 179) ## 330 간격으로 bottom 잡기 stay 이미지
            elif (self.direction == direction['LEFT']):
                self.image.clip_composite_draw(self.jump_frame * 151, 0, 151, 179, 0, 'h', self.x, self.y, 151, 179)

          
class Potato_Monster:
    def __init__(self):
        self.frame = 0
        self.sin = 5
        self.image = load_image('potato.png')
        self.ddong = load_image('ddong.png')
        self.attack = load_image('potato_attack.png')
        self.print = 0
        self.x,self.y = 750,300
    def update(self):
        self.frame = (self.frame + 1) % self.sin
    def draw(self):
        #self.appear_motion()

        self.attack_draw()
        if(self.print>=12):
            self.ddong_draw()
            
    def appear_motion(self):
        pass
    def ddong_draw(self):

        self.x -= 100
        self.ddong.clip_draw(self.frame * 134, 1,133,138,self.x,100)
    def attack_draw(self):
        self.sin = 12
        self.attack.clip_draw(self.frame * 542, 0, 542, 590, 880, self.y)
        self.print += 1

