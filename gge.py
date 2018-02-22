from moviepy.editor import *


def gif(fullClip,start,end,name):
    print "giffed,", name, start, end
    clip = fullClip.subclip(start,end).resize(.83)
    clip.write_gif(name, fuzz=3, fps=15)
 

if __name__ == "__main__":
    clipName = raw_input().strip()
    clipping = raw_input().strip()
    if (clipping == 'True'):
        area = [int(x) for x in raw_input().strip().split()]
        clip = (VideoFileClip(clipName)
            .crop(x1=area[0],x2=area[2], y1= area[1],y2=area[3]))
    else:
        clip = VideoFileClip(clipName)
    
    clipPoints = [float(x) for x in raw_input().strip().split()]
    numSentences = int(raw_input().strip())

    for x in xrange(1,len(clipPoints)):
        print clipPoints[x-1], clipPoints[x]
        gif(clip,clipPoints[x-1],clipPoints[x],clipName[:-4]+str(x)+"clip.gif")
