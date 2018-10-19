#!/usr/bin/python
  
import threading
import subprocess
import time

url_list = ['http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
	'http://10.0.2.67/media/hls/BlindSideHQ15000kb/BlindSideHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BlusbroHQ15000kb/BlusbroHQ15000kb-index.m3u8',
        'http://10.0.2.67/media/hls/CaddyshackSupperHQ1080p30/CaddyshackSupperHQ1080p30-index.m3u8',
        'http://10.0.2.67/media/hls/BravehartHQ15000kb/BravehartHQ15000kb-index.m3u8']
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
for thread in threads:
        thread.join()
