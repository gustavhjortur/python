import re
def process_ls(output):
    listi = list( filter(lambda n: n[0:1] != 'd', (list( x for x in output.split('\n'))) ) )
    numb = int
    safn = []
    for x in listi:
        x = " ".join(x.split())
        x = " ".join(x.split('\''))
        x = " ".join(x.split(']'))
        x = " ".join(x.split('['))
        numb = int(*map(int, re.split(' ', x.strip())[4:5]))
        safn.append([numb, str(re.split(' ', x.strip(), maxsplit=8)[-1])] )
    safn.sort(reverse=True)
    l2 = sorted(safn, key=lambda x: (x[1]).lower())
    l3 = sorted(l2, key=lambda x: x[0], reverse=True)
    l = []
    for x in l3:
        x = re.sub('\]', '', str(x))
        x = re.sub('\[', '', str(x))
        x = re.sub('\"', '', str(x))
        l2 += (str(re.split(', ', str(x), maxsplit=2)[-1]))
        l.append((re.split(', ', (x), maxsplit=2)[-1]))
    lis = []
        for x in l:
            lis.append( re.sub(r'\'', '', x) )
    return lis



("""-rw------- 1 root utmp 8832 Apr 20 14:40 btmp
drwxr-xr-x 2 root root 4096 Jun 16 13:02 cups
-rw------- 1 root root 32064 Jul 11 02:09 faillog
drwxr-xr-x 2 root root 4096 Apr 30 23:57 httpd 
drwxr-xr-x 3 root root 4096 Apr 1 02:30 journal 
-rw-r--r-- 1 root root 292584 Jul 11 02:09 lastlog 
drwxr-xr-x 2 root root 4096 Mar 14 19:20 old 
-rw-r--r-- 1 root root 168414 Jul 16 02:47 pacman.log 
-rw-r--r-- 1 root root 58496034 Jul 16 21:32 pm-powersave.log 
-rw-r--r-- 1 root root 1506989 Jul 16 21:31 pm-suspend.log 
-rw-r--r-- 1 root root 2328 Jul 9 23:25 slim.log 
drwxr-xr-x 2 root root 4096 Mar 9 01:43 speech-dispatcher 
drwxr-xr-x 2 root root 4096 Jul 10 15:14 wicd 
-rw-rw-r-- 1 root utmp 1873536 Jul 16 21:35 wtmp 
-rw-rw-rw- 1 root root 59826 Jul 5 02:24 xdg-open.log 
-rw-r--r-- 1 root root 92976 Jul 16 21:31 Xorg.0.log 
-rw-r--r-- 1 root root 41264 Jul 9 23:23 Xorg.0.log.old 
-rw-r--r-- 1 root users 30651 Apr 17 09:43 Xorg.1.log""",)



("""-rw------- 1 suprdewd users 3385 Jul 17 03:24 Description.html 
-rw-r--r-- 1 suprdewd users 11 Jul 17 03:25 env and stuff meow 
drwx--x--x 2 suprdewd users 4096 Jul 17 02:25 images 
-rw-r--r-- 1 suprdewd users 168 Jul 17 03:21 sol.py 
drwxr-xr-x 2 suprdewd users 4096 Jul 17 03:26 tests 
-rw-r--r-- 1 suprdewd users 2160 Jul 17 02:25 tests.txt""",)
