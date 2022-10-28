import pygame
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
clock = pygame.time.Clock()
# 게임실행 메인함수 
def runGame():
    global gamepad, clock

    doneFlag = False
    while not doneFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
        
        #게임 화면을 검은색으로 채우고 화면을 업데이트 함
        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

#게임 초기화 함수
def initGame():
    global gamepad, clock_getres

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("MyGalaga")
    clock = pygame.time.Clock()

initGame()
runGame()


