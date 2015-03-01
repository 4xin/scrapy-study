__author__ = '4Thing'

import urllib2
import threading
import thread
import Queue

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
ip_queue = Queue.Queue()
threads = []
lock = thread.allocate_lock()
file = open("D:\Doc\ips.txt")
for line in file:
    ip_queue.put(line.rstrip())

def authIP():
    while(ip_queue.empty() == False):
        lock.acquire()
        ip = ip_queue.get()
        lock.release()
        request = urllib2.Request('http://www.baidu.com/')
        request.add_header('User-Agent', user_agent)
        opener = urllib2.build_opener(urllib2.ProxyHandler({'http':'http://%s/'%ip}))
        try:
            response = opener.open(request, timeout=30)
            if(response.geturl().find("baidu")):
                print ip+":"+" is valid!"
        except:
            pass

for i in range(20):
    threads.append(threading.Thread(target=authIP))

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(False)
        t.start()
    while(ip_queue.empty() == False):
        pass