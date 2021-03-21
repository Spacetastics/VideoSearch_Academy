from googleapiclient.discovery import build
import config

urlcopy = "https://www.youtube.com/watch?v="
yt = build('youtube', 'v3', developerKey=config.key)
videoid = []


class Search:
    def __init__(self, tx, nm, ln):
        self.__topic = tx
        self.__num = nm
        self.__leng = ln

    pass


idea = input("Enter School Topic")
l = input("Enter Number of Videos")
o = input("Enter Length")
n = Search(idea, l, o)
numR = int(l)

k = yt.search().list(
    part='snippet',
    q=idea,
    topicId="/m/01k8wb",
    type = 'video',
    videoDuration = o,
    order='relevance',
    relevantLanguage = "en",
    maxResults=numR
).execute()

print(k)

for result in k.get("items", []):
    videoid.append("%s" % (result["id"]["videoId"]))

print ("\n".join(videoid))

for i in range(numR):
    print (urlcopy + videoid[i])
