from moviepy.editor import *

def gif(fullClip,start,end,name):
    clip = fullClip.subclip(start,end).resize(.65 )
    clip.write_gif(name, fps=15)
 

def addAudio(fullClip,text,start,end,x,y,fSize,sWidth,font):
    
    leftClip = fullClip.subclip(0,start)
    editClip = fullClip.subclip(start,end)
    rightClip = fullClip.subclip(end)
    textit = (TextClip(text,
                     fontsize=fSize, color='white',
                     font=font, interline = -25,
                     stroke_color='black', stroke_width=sWidth)
            .set_pos((x,y))
            .set_duration(editClip.duration))

    compoisition = CompositeVideoClip([editClip,textit])
    return concatenate_videoclips([leftClip,compoisition,rightClip])

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
    sentences = []
    sentenceData = []
    fonts = []
    for x in xrange(numSentences):
            sentences.append(raw_input().strip())

    for x in xrange(numSentences):
            sentenceData.append([float(x) for x in raw_input().strip().split()])

    for x in xrange(numSentences):
            fonts.append(raw_input().strip());
    
    for x in xrange(numSentences):
            clip = addAudio(clip,sentences[x],sentenceData[x][0],sentenceData[x][1],
                            sentenceData[x][2],sentenceData[x][3],sentenceData[x][4],
                            sentenceData[x][5],fonts[x])

    for x in xrange(1,len(clipPoints)):
        gif(clip,clipPoints[x-1],clipPoints[x],clipName[:-4]+str(x)+"clip256.gif")
