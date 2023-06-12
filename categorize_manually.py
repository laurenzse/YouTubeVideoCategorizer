from pytube import Channel

# enter categories here; the values in the dict will be written to the csv
categories = {'night': 1, 'dawn': 2, 'day': 3}

# allows you to filter all videos before going through them manually
def prefilter_video(video):
    return video.length > 60 * 10 and video.length < 60 * 120

def print_categories():
    for category, in_file_key in categories.items():
        print(f'\t ({category}) --> {in_file_key}')

channel_url = input('Enter channel URL: ')
channel = Channel(channel_url)
videos = list(channel.videos)
filtered = [video for video in videos if prefilter_video(video)]

with open('output.csv', "w+") as output_file:
    for index, video in enumerate(filtered):
        print()
        print(f'### video {index + 1} of {len(filtered)} ###')
        print(f'{video.title} ({video.length/60} minutes)')
        print()
        print(video.description)
        print()
        print('Which category does this video belong to:')
        print_categories()
        key = input('enter key or enter i to ignore: ')

        if key != 'i':
            output_file.write(f'{video.watch_url},{key}\n')