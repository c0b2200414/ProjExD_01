import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_2 = pg.transform.flip(bg_img, True, False)

    kk_image = pg.image.load("ex01/fig/3.png")
    kk_image = pg.transform.flip(kk_image, True, False)
    kk_list = [kk_image, pg.transform.rotozoom(kk_image, 10, 1)]


    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0] )
        screen.blit(bg_img_2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])


        screen.blit(kk_list[(tmr // 50) % 2], [300, 200])


        pg.display.update()
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()