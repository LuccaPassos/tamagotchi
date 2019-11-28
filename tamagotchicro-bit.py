from microbit import *
import random

f = Image("09090:09090:00000:90009:09990")
l_f = Image("90900:90900:00000:90009:09990")
r_f = Image("00909:00909:00000:90009:09990")

sk = Image("09090:09090:00000:09090:90909")
sk_ = Image("00000:00000:00000:09090:90909")

s = Image("09090:09090:00000:09990:90009")
s1 = Image("00000:99099:00000:09990:90009")
s2 = Image("00000:99099:30000:09990:90009")
s3 = Image("00000:99099:03003:39990:90009")
s4 = Image("00000:99099:30030:09993:90009")
s5 = Image("09090:09090:00003:39990:90009")
s6 = Image("09090:09090:00000:09993:90009")

ok = Image("09090:09090:00000:99999:00000")
l_ok = Image("90900:90900:00000:99999:00000")
r_ok = Image("00909:00909:00000:99999:00000")

cross = Image("00900:00900:99999:00900:00900")

ouch = Image("00000:99099:00000:90009:09990")
mad = Image("90009:09090:00000:09990:90009")

eye_ok = [l_ok, r_ok]
eye_f = [l_f, r_f]
cry = [s, s1, s2, s3, s4, s5, s6]
mnu = [Image.PACMAN, cross]

tme = running_time()
hp = 100
hpp = 100
sik = False

def nml():
    display.show(ok)
    sleep(500)
    if random.randrange(5) == 2:
        display.show(random.choice(eye_ok))
        sleep(2500)

def sk_f():
    display.show(sk)
    sleep(400)
    if random.randrange(10) == 5:
        display.show(sk_)
        sleep(100)

def idle():
    display.show(f)
    sleep(300)
    if random.randrange(8) == 5:
        display.show(random.choice(eye_f))
        sleep(500)

def dead():
    age = running_time()
    while True:
        display.show(sk_)
        sleep(1000)
        display.scroll(age//1000)
        sleep(1000)

def sad():
    display.show(cry, delay=400)
    sleep(300)

def play():
    global hpp
    hpp += 10
    display.scroll("play")

def heal():
    global sik
    sik = False
    display.scroll("heal")

mnu2 = [play, heal]

def menu():
    i = 0
    sleep(1000)
    while True:
        display.show(mnu[i])
        sleep(200)
        if button_a.is_pressed() and button_b.is_pressed():
            mnu2[i]()
            break
        if button_a.is_pressed():
            for j in range(6):
                display.show(mnu[i].shift_left(j))
                sleep(70)
            i = (i - 1) % 2
            for j in range(6, 0, -1):
                display.show(mnu[i].shift_right(j))
                sleep(70)
        if button_b.is_pressed():
            # sleep(200)
            for j in range(6):
                display.show(mnu[i].shift_right(j))
                sleep(70)
            i = (i + 1) % 2
            for j in range(6, 0, -1):
                display.show(mnu[i].shift_left(j))
                sleep(70)

def hpp_():
    global tme
    global hpp
    if (running_time() - tme) > 10000:
        tme = running_time()
        if random.randrange(10) == 1:
            hpp -= 10

def slp():
    while True:
        display.show(Image.ASLEEP)
        z = accelerometer.get_z()
        sleep(500)
        n = accelerometer.get_z()
        if n > z + 30 or n < n - 30 :
            break

def stt():
    if hpp >= 70:
        idle()
    elif hpp < 70 and hpp >= 40:
        nml()
    elif hpp < 40 and hpp >= 10:
        sad()
    else:
        dead()

sl = False

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        menu()
    if sik is True:
        sk_f()
    else:
        if pin0.is_touched():
            display.show(Image.HEART)
            sleep(1000)
            hpp += 2
        if sl is False:
            z = accelerometer.get_z()
            n = running_time()
            sl = True
        if (running_time() - n) > 60000:
            sl = False
            if n < z + 10 or n > n - 100:
                slp()
        if accelerometer.was_gesture('shake'):
            display.show(mad)
            hpp -= 20
            sleep(3000)
        if accelerometer.was_gesture('face down'):
            sik = True
        while button_a.is_pressed() or button_b.is_pressed():
            display.show(ouch)
        stt()
    hpp_()