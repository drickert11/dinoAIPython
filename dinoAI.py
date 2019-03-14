import pyautogui as gui
import mss

gui.PAUSE = 0


def dist(left, top, width=200):
    with mss.mss() as shot:
        ss = shot.grab(dict(left=left, top=top, width=width, height=1))

    for x in range(0, ss.width, 2):
        p = ss.pixel(x, 0)
        if p != (247, 247, 247):
            break

    return x


if __name__ == '__main__':
    gui.moveTo(253, 394)
    gui.click()

    while True:
        low = dist(260, 390)
        high = dist(260, 377)

        if low < 100:
            gui.keyUp('down')
            gui.keyDown('up')
        elif high < 50:
            gui.keyDown('down')
