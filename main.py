#HUC凌落辰 qq:3533933845
#charset="utf-8" 2023.7.26

import pygame
import sys
from time import sleep

class Ikun:
    def __init__(self):
        self.path = "./music"  #默认路径

    def main(self):
        pygame.display.set_caption("By Peng")
        pygame.init()  #pygame模块初始化
        pygame.mixer.init()  #音频模块初始化
        pygame.display.set_mode((1000,500))

        while True:
            run.check_event()  #调用键盘监控函数

    def check_event(self):
        while True:
            for event in pygame.event.get():  #监控按键
                if event.type == pygame.QUIT:  #退出程序
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #监控按下按键
                    if event.key == pygame.K_j: #监控按下按键j
                        print("按下j键")
                        pygame.mixer.music.load(self.path+"j.wav")
                        pygame.mixer.music.play(1)
                    if event.key == pygame.K_n:#监控按下按键n
                        print("按下n键")
                        pygame.mixer.music.load(self.path+"n.wav")
                        pygame.mixer.music.play(1)
                    if event.key == pygame.K_t:  #监控按下按键t
                        print("按下t键")
                        pygame.mixer.music.load(self.path+"t.wav")
                        pygame.mixer.music.play(1)
                    if event.key == pygame.K_m:  #监控按下按键m
                        print("按下m键")
                        pygame.mixer.music.load(self.path+"m.wav")
                        pygame.mixer.music.play(1)





if __name__ == "__main__":
    run = Ikun()   #调用类
    run.main()   #调用主函数

