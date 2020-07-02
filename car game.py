import sys, pygame, random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
red_car = pygame.image.load("red_car.png")
blue_car = pygame.image.load("blue_car.png")
pygame.mixer.music.load("car_speed.mp3")
pygame.mixer.music.play(-1)
size = width,height = (400,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game = True


speed = 1
divider_gap = 50
divider_width = 20
divider_height = 100
divider_start = -(divider_gap+divider_height)-speed
car_padding = 50
car_width = width/4 
car_height = height/4
car_start_x = car_padding
car_start_y = height-(car_height)-10
position_x = position_y = 0
sensitivity = 2
opp_cars = 0
opp_cars_x=[]
opp_cars_y=[]
opp_cars_speed = 2
opp_cars_timing = 100#random.randint(200,1000)
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_LEFT:
                position_x = -sensitivity
                        
                    
            if event.key == pygame.K_RIGHT:
                position_x = sensitivity

            if event.key == pygame.K_UP:
                position_y = -sensitivity

            if event.key == pygame.K_DOWN:
                position_y = sensitivity

            if event.key == 32 :

                flag=True
                while(flag):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == 32 :
                            flag=False
        if event .type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and position_x==-sensitivity:
                position_x = 0
                        
                    
            if event.key == pygame.K_RIGHT and position_x == sensitivity:
                position_x = 0

            if (event.key == pygame.K_UP and position_y == -sensitivity) or (event.key == pygame.K_DOWN and position_y == sensitivity):
                position_y = 0
            

                        
    car_start_x += position_x
    car_start_y += position_y
    divider_start += speed
    if(car_start_x <= 5 or car_start_x >= width - car_width - 5 ):
        position_x = 0
    if car_start_y <= 0 or car_start_y >= height - car_height :
        position_y = 0
    if(divider_start >= -speed):
        divider_start = -(divider_gap+divider_height)-speed
    opp_cars_timing -= 1
    if opp_cars==0  and opp_cars_timing == 0 :
        opp_cars=1
        opp_cars_x.append(random.randint(6,width-6-car_width))
        opp_cars_y.append(-car_height)
        opp_cars_timing = random.randint(car_height*8,car_height*15)
    elif opp_cars_timing == 0 :
        opp_cars +=1
        opp_cars_x.append(random.randint(6,width-6-car_width))
        opp_cars_y.append(-car_height)
        opp_cars_timing = random.randint(car_height*8,car_height*15)
    for i in range(opp_cars):
        opp_cars_y[i] += opp_cars_speed
    try:
        if opp_cars_y[0] > height:
            opp_cars-=1
            opp_cars_x = opp_cars_x[1:]
            opp_cars_y = opp_cars_y[1:]
    except:
        t=0
    
    for i in range(opp_cars):
        if abs(opp_cars_x[i] - car_start_x) < car_width and abs(opp_cars_y[i]-car_start_y)<car_height:
            game = False
            
    screen.fill(black)
    for i in range(10):
        pygame.draw.rect(screen, white,[width//2-divider_width//2,divider_start+i*(divider_height+divider_gap),divider_width,divider_height] )
    #pygame.draw.rect(screen, white, [car_start_x,car_start_y,car_width,car_height])
    screen.blit(red_car,(car_start_x,car_start_y))
    pygame.draw.rect(screen, red, [0,0,5,height])
    pygame.draw.rect(screen, red, [width-5,0,5,height])
    for i in range(opp_cars):
        #pygame.draw.rect(screen, blue, [opp_cars_x[i],opp_cars_y[i],car_width,car_height])
        screen.blit(blue_car,(opp_cars_x[i],opp_cars_y[i]))
    pygame.display.flip()
    clock.tick(200)
pygame.quit()

