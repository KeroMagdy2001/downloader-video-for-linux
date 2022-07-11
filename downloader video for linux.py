from pytube import YouTube
from pytube import Playlist
import sys



#color

G = '\033[1;1;32m' # green
Y = '\033[1;33m'   # yellow
B = '\033[94m'   # blue
R = '\033[1;1;91m'   # red
W = '\033[0m'    # white

#downloading video for linux = DVFL

print('''%s 
                        Ｔｈｉｓ Ｔｏｏｌ Ｈｅｌｐ Ｙｏｕ Ｔｏ Ｄｏｗｎｌｏａｄ Ａｕｄｉｏ ， Ｖｉｄｅｏ ａｎｄ Ｐｌａｙｌｉｓｔ 
%s\n''' % (Y,W))

print('''%s
              _                     _                 _ _                     _     _                   __             _ _                  
             | |                   | |               | (_)                   (_)   | |                 / _|           | (_)                 
           __| | _____      ___ __ | | ___   __ _  __| |_ _ __   __ _  __   ___  __| | ___  ___  ___  | |_ ___  _ __  | |_ _ __  _   ___  __
          / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` | | '_ \ / _` | \ \ / / |/ _` |/ _ \/ _ \/ __| |  _/ _ \| '__| | | | '_ \| | | \ \/ /
         | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| | | | | | (_| |  \ V /| | (_| |  __/ (_) \__ \ | || (_) | |    | | | | | | |_| |>  < 
          \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|_|_| |_|\__, |   \_/ |_|\__,_|\___|\___/|___/ |_| \___/|_|    |_|_|_| |_|\__,_/_/\_\\
                                                                 __/ |                                                                      
                                                                |___/%s                                                                       

''' % (R,W))


print('''
                                                        %s【Ｃｏｄｅｄ　Ｂｙ　Ｋｅｒｏ　Ｍａｇｄｙ】%s
''' % (R,W))
    
 
#try:

print('''
    choises:\n
    \t[1] Download an only audio.
    \t[2] Download a video.
    \t[3] Download a playlist.
''')

global ask
ask = int(input("Enter the number of choises: "))


global link
link = input("Enter URL: ")
if link == '':
    print('Sorry,The input is empty')
    sys.exit()



#path_of_file

global path_of_file
path_of_file = input("Enter Path Of File: ")

if path_of_file == '':
    print('Sorry,The input is empty')
    sys.exit()


#for_one_and_two name of this function means download only for audio and single video not for playlist

def for_one_and_two():
    global yt
    yt = YouTube(link)

    #about video
    
    print("About Video: ")
    print("\tTitle: " , yt.title)
    print("\tAuthor: " , yt.author)
    
    
    #about the duration of video
    
    duration = yt.length
    
    hours = int(duration/60/60)
    duration -= hours*60*60
    minutes = int((duration)/60)
    duration -= minutes*60
    seconds = int(duration)
    
    print("\tDuration:",f"{hours} : {minutes} : {seconds}")
    
    #except:
    #    print('%s\nWrong, Reprocess The Process1%s' % (R,W))
    

#this part is concerned with download audio


if ask == 1:
    for_one_and_two()
    print('Downloading audio...\n')
    only_audio = yt.streams.filter(mime_type="audio/mp4" , only_audio=True)
    onlyaudio = only_audio.last()
    download = onlyaudio.download(output_path=path_of_file)
    print("%s\n Done !\nAudio Downloaded %s" % (Y,W))
    sys.exit()
        
             

try:
    #to choose a spciefic resolution 


    print('''
    example of resolution:
    [1] 360p
    [2] 480p
    [3] 720p
    [4] 1080p
    [5] 1440p
    [6] 2160p
    [7] 4320p
    ''')
    

    ask_for_resolution = input('choose a spciefic resolution: ')
    if ask_for_resolution == '':
        print('Sorry,The input is empty')

    try:
        if ask_for_resolution == '1':
            ask_for_resolution = '360p'

        elif ask_for_resolution == '2':
            ask_for_resolution = '480p'

        elif ask_for_resolution == '3':
            ask_for_resolution = '720p'

        elif ask_for_resolution == '4':
            ask_for_resolution = '1080p'

        elif ask_for_resolution == '5':
            ask_for_resolution = '1440p'

        elif ask_for_resolution == '6':
            ask_for_resolution = '2160p'

        elif ask_for_resolution == '7':
            ask_for_resolution = '4320p'

        else:
            print('Wrong Resolution')

    except:
        print("A Wrong Value")
except:
    print('%s\n Wrong, Reprocess The Process2 \nTry To Change Resolution%s' % (R,W))


try:

    #this part is concerned with download a single video

    if ask == 2:
        for_one_and_two()
        print('Downloading a video...\n')
        resolution_of_moniter = yt.streams.filter(progressive=True , file_extension='mp4' , resolution=ask_for_resolution )#.desc()
        resolution = resolution_of_moniter.last()
        video = resolution.download(output_path=path_of_file)
        print("%s\n Done !\nVideo Downloaded %s" % (Y,W))

except:
    print('%s\n Wrong, Reprocess The Process3 \nTry To Change Resolution%s' % (R,W))

    #this part is concerned with download a playlist of videos


try:
    if ask == 3:

        #url = input("Enter URL: ")
        #
        #if url == '':
        #    print('Sorry,The input is empty')
        #    sys.exit()

        print('Downloading a playlist...\n')

        playlist = Playlist(link)

        print("About Video: ")
        print(f'\tTitle: {playlist.title}\n')

        print('Number of videos in playlist: %s\n' % len(playlist.video_urls))


        for video in playlist.videos:
            name_of_video = video.title

            print('[+]',name_of_video,'\tCompleted!')

            resolution_of_moniter = video.streams.filter(progressive=True , file_extension='mp4' , resolution=ask_for_resolution)#.desc()
            resolution = resolution_of_moniter.last()
            video = resolution.download(output_path=path_of_file)
        print("%s\n Done !\nPlaylist Downloaded %s" % (Y,W))
    
    #for url in playlist.video_urls[:3]:
    #    print(url)

except:
    print('%s\n Wrong, Reprocess The Process4 \nTry To Change Resolution%s' % (R,W))