from pytube import Channel
import requests
import re


# enter categories here; the values in the dict will be written to the csv
categories = {'night': 1, 'dawn': 2, 'day': 3}


# allows you to filter all videos before going through them manually
def prefilter_video(video):
    return video.length > 60 * 10 and video.length < 60 * 120


def print_categories():
    for category, in_file_key in categories.items():
        print(f'\t ({category}) --> {in_file_key}')


# intermediate function to get the description of a video until PyTube fixes their bug
# https://github.com/pytube/pytube/issues/1626
def get_video_description(youtube_video_url: str):
    full_html = requests.get(youtube_video_url).text
    y = re.search(r'shortDescription":"', full_html)
    desc = ""
    count = y.start() + 19  # adding the length of the 'shortDescription":"
    while True:
        # get the letter at current index in text
        letter = full_html[count]
        if letter == "\"":
            if full_html[count - 1] == "\\":
                # this is case where the letter before is a backslash, meaning it is not real end of description
                desc += letter
                count += 1
            else:
                break
        else:
            desc += letter
            count += 1

    return desc


channel_url = input('Enter channel URL: ')
channel = Channel(channel_url)
videos = list(channel.videos)
filtered = [video for video in videos if prefilter_video(video)]

with open('output.csv', "w+") as output_file:
    for index, video in enumerate(filtered):
        video_description = get_video_description(video.watch_url)

        print()
        print(f'### video {index + 1} of {len(filtered)} ###')
        print(f'{video.title} ({video.length/60} minutes)')
        print()
        print(video_description)
        print()
        print('Which category does this video belong to:')
        print_categories()
        key = input('enter key or enter i to ignore: ')

        if key != 'i':
            output_file.write(f'{video.watch_url},{key}\n')