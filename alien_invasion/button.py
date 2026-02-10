import pygame.font


class Button:
    
    def __init__(self, ai_game,msg):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=self.screen.get_rect()
        
        self.width, self.height=200 ,50
        self.button_color = (0,135,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        
        self.rect=pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(msg)        

    def prep_msg(self,msg):#Преобразует в прямоугольник
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):                      #рисует путую кнолпку
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)