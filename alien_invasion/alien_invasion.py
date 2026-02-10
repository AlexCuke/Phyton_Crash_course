import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:    
    #Класс длл управления ресурсами и поведением игры
    def __init__(self): #Инициализиурет игры и переменные
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()                            #обьект класса НАстройки 
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #Устанавливаем разрешение экрана
        #self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_weight=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")        #Подпись окна
        self.stats=GameStats(self)                          #обьект класса GameStats
        self.ship=Ship(self)                                #обьект класса Корабль
        self.bullets=pygame.sprite.Group()                  #группа обьектов класса пули
        self.aliens=pygame.sprite.Group()                   #группа обьектов класса пришельцы
        self._create_fleet()
        self.game_active=False
        self.play_button=Button(self,"Play")
        
    def run_game(self):
    #Основной цикл игры
        while True:
            self._check_events()                    #Проверка состония кнопки
            if self.game_active:                    ####Если игра запущена
                self.ship.update()                  #Нарисовать корабль
                self._update_bullets()              #Нарисовать пули
                self._update_aliens()               #Нарисовать пришельцев
            self._update_screen()                   #Обновление экрана
            self.clock.tick(60)

            
    def _check_events(self):                        #Проверка состояния кнопки     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #Выход
                sys.exit()
            elif event.type == pygame.KEYDOWN:      #Нажатие на клавишу
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:          #Отпускание клавиши
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            button_clicked=self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.game_active:
                self.stats.reset_stats()
                self.game_active= True
                self.bullets.empty()
                self.aliens.empty() 
                self._create_fleet()
                self.ship.center_ship()    
                pygame.mouse.set_visible(False)           
    def _check_keydown_events(self,event):          #Поведение кнопки при нажатие кнопок 
            if event.key == pygame.K_RIGHT:         #вПРАВО
                self.ship.moving_right=True
            elif event.key == pygame.K_LEFT:        #ВЛЕВО
                self.ship.moving_left=True   
            elif event.key == pygame.K_q:           #ВЫХОД
                sys.exit()
            elif event.key == pygame.K_SPACE:       #ПРОБЕЛ
                self._fire_bullet()
                
    def _check_keyup_events(self, event):           #Поведение кнопки при  отжатии кнопок 
                if event.key == pygame.K_RIGHT:     #вПРАВО
                    self.ship.moving_right=False   
                elif event.key == pygame.K_LEFT:    #ВЛЕВО
                    self.ship.moving_left=False   
                    
    def _fire_bullet(self):                         #создает новый снаряд и добалвяет в группу Bullet
        if len(self.bullets)<self.settings.bullets_allowed: 
            new_bullet=Bullet(self)                 
            self.bullets.add(new_bullet)   
            
    def _update_bullets(self):                      #обновляет позиции снарядов
        self.bullets.update()
        for bullet in self.bullets.copy():          #удаление снарядов за пределеами экрана
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)     
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            
    def _update_screen(self):                            #Обновление экрана
            self.screen.fill(self.settings.bg_color)     #Заливка экрана экрана
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)
            if not self.game_active:
                self.play_button.draw_button()
            pygame.display.flip()
            
    def _create_fleet(self):                                                #Пришельцы
        alien=Alien(self)                                                   #обьект класса пришелец
        alien_width,alien_heigth=alien.rect.size
        current_x,current_y=alien_width,alien_heigth
        while current_y < (self.settings.screen_height-3*alien_heigth):
            while current_x < (self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_heigth
            
    def _create_alien(self,x_position,y_position):      #Создание пришельца
        new_alien=Alien(self)                           #обьект класса Корабль
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
    
    def _update_aliens(self):                           #обновляет позиции пришельцев
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany( self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left-=1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active =False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
            
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()
    
    