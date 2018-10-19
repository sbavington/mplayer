#!/usr/bin/python
  
import threading
import subprocess
import time

url_list = ['http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8',
            'http://10.0.4.200/CaddyshackSupperHQ1080p30_730-.m3u8']
threads = []

def play_hls(url,lognum):
        command = ['mplayer','-identify', '-framedrop','-nocache', '-vo','null','-ao','null',url]
        p = subprocess.call(command)

for url in url_list:
        lognum = 0
	time.sleep(2)
        t = threading.Thread(name = 'mplayer',target = play_hls, args = (url,lognum))
        t.start()
        threads.append(t)
while True:
    for thread in threads:
        thread.join()

