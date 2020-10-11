import urllib.request
import json

import os

CHANNEL_ID='UCKSVUHI9rbbkXhvAXK-2uxA'

def get_all_video_in_channel(channel_id):

    api_key = os.getenv('API_KEY')

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        headers = {'User - Agent': 'Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.36(KHTML, like Gecko)Chrome / 41.0.2228.0 Safari / 537.3'}

        req = urllib.request.Request(url, headers = headers)

        inp = urllib.request.urlopen(req)

        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links



video_list = get_all_video_in_channel(CHANNEL_ID)

print(len(video_list))