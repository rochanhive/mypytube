from pytube import YouTube
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
a=yt.streams
print(str(len(a))+"\n\n")
print(a[0].url)