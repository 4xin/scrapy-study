__author__ = '4Thing'
import urllib2
import random
import threading
import thread
import Queue

user_agent_list = \
    [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

ip_list = []

ip_queue = Queue.Queue()

def run():
    user_agent = random.choice(user_agent_list)
    proxy = random.choice(ip_list)
    request = urllib2.Request('http://www.baidu.com/')
    request.add_header('User-Agent', user_agent)
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http':'http://%s/'%proxy}), urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)
    response = urllib2.urlopen(request, timeout=30)

    print response.geturl()

lock = thread.allocate_lock()

def run2():
    lock.acquire()
    user_agent = random.choice(user_agent_list)
    if(ip_queue.empty() == True):
        lock.release()
    ip = ip_queue.get()
    lock.release()
    request = urllib2.Request('http://www.baidu.com/')
    request.add_header('User-Agent', user_agent)
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http':'http://%s/'%ip}))
    urllib2.install_opener(opener)
    try:
        response = opener.open(request, timeout=30)
        print ip+":"+response.geturl()
    except:
        print 'something wrong!'

file = open("D:\Doc\ips.txt")
threads = []

def run3():
    while(True):
        run2()

for i in range(20):
    threads.append(threading.Thread(target=run3))

for line in file:
    ip_queue.put(line)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(False)
        t.start()
    while(ip_queue.empty() == False):
        pass
    print "over!"