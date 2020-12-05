import pytube,os,ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

video_list = []

print("Enter the URL's You Want To Download")

while True:

    url = input("")

    if url == "stop":

        break

    video_list.append(url)
    
    # print(video_list)

for x, video in enumerate(video_list):

    v = pytube.YouTube(video)

    stream = v.streams.get_by_itag(22)

    print(f"Downloading video {x}...")

    stream.download()

    print("Downloaded")

