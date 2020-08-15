import time
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Listener,KeyCode
from pynput.mouse import Button,Controller


def switcher(tc):
    #print(tc)
    return {
        'm':f"p{tc[1]}",
        'pm':f"p{tc[2]};pm({tc[1]})",
        'rm':f"p{tc[2]};rm({tc[1]})",
        'sc':f"p{tc[2]};sc{tc[1]}",
        'pk':f"pk({tc[1]})",
        'rk':f"rk({tc[1]})"
    }.get(tc[0],'exit(0)')
    #print(a)
    #return a


class mainstring():
    def __init__(self,startstring):
        self.mainstring = list()
        self.startstring = startstring
        self.timestring = list()
        self.timestring.append(time.monotonic())
        #self.firsttime=time.monotonic()
    def addstring(self,tmpstr):
        try:
            self.mainstring.append(tmpstr)
            self.timestring.append(time.monotonic())
        except:
            print('error')
    def savetofile(self,stopstring):
        filename='C:/Users/msi/Desktop/phyton_dev/auto_folder/'+input('enter your file name:')+'.py'
        infile = open(filename,'w')
        infile.write(self.startstring+'\n')
        optimize=bool(input('Optimize mouse move?(y/n):').lower() in ['y','yes'])
        def timeequal(timea,timeb):
            return f";t({timea-timeb})" if timea!=timeb else ''
        for x,y,z in zip(self.mainstring,self.timestring[1:],self.timestring[:-1]):
            if (not optimize) or ('m' not in x):
                stringtoadd=switcher(x)+timeequal(y,z)+'\n'
                print(stringtoadd,end='')
                infile.write(stringtoadd)
        infile.write(stopstring)
        infile.close()
        import subprocess
        subprocess.call(['C:\\Users\\msi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', filename])
mainstring=mainstring('''from time import sleep as t
from pynput.keyboard import Key,Listener,KeyCode,Controller as KeyboardController
from pynput.mouse import Button,Controller as MouseController
m = MouseController();k = KeyboardController()

def p(x,y):m.position=(x,y)

pm=m.press;rm=m.release;sc=m.scroll
pk=k.press;rk=k.release''')
mo = Controller()
keypress=dict()
def on_move(x, y):
    mainstring.addstring(('m',(x,y),False))
def on_click(x, y, button, pressed):
    mainstring.addstring(('pm' if pressed else 'rm',button ,(x,y) ))
def on_scroll(x, y, dx, dy):
    mainstring.addstring(('sc',(dx,dy),(x,y)))
def on_press(key):
    if key not in keypress:
        keypress[key]=False
    if not keypress[key]:
        keypress[key]=True
        mainstring.addstring(('pk',key,False))
def on_release(key):
    if keypress[key]:
        mainstring.addstring(('rk',key,False))
        keypress[key]=False
    if key == keyboard.Key.esc:
        listener.stop()
        return False
print('start in')
time.sleep(1)
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print('Press \'Esc\' for Stop')
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
try :
    mainstring.savetofile('''print('Done')
t(3)''')
    print('save success')
except:
    print('save error')
time.sleep(3)
exit(0)



