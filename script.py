import urllib.request
import urllib.parse
import re

#read songs
f = open("songs.txt", "r")
urlsss = open("url.txt", "a")
for x in f:
    query_string = urllib.parse.urlencode({"search_query" : x})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    video_ids = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + video_ids[0])
    urlsss.write("http://www.youtube.com/watch?v=" + video_ids[0] + '\n')
urlsss.close()

# youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 -s url.txt
