from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json
apikey = 'AIzaSyBaoFpxyCOFBLD91lzsfBnF0D-Q5IREpa8' #API Key
playlist_id = ''
service = build('youtube', 'v3', developerKey=apikey)

#Get upload playlist ID
channelId = input('>>> Channel ID: ')
channelId_ = service.channels().list(
        part='contentDetails',
        id=channelId
    ).execute()
playlist_id = channelId_['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Retrieve video IDs from the playlist
video_ids = []
next_page_token = None

while True:
    playlist_response = service.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        fields='items(snippet(resourceId(videoId)))',
        maxResults=50000  # maximum allowed per page
    ).execute()
    
    # Extract video IDs from the current page
    for item in playlist_response.get('items', []):
        video_id = item['snippet']['resourceId']['videoId']
        video_ids.append(video_id)
    
    next_page_token = playlist_response.get('nextPageToken')
    if not next_page_token:
        break

# Now, fetch snippets for these video IDs in batches (max 50 per request)
snippets = []
for i in range(0, len(video_ids), 50):
    batch_ids = video_ids[i:i+50]
    video_response = service.videos().list(
        part='snippet',
        id=','.join(batch_ids),
        fields='items(snippet(title,description,tags))'
    ).execute()
    # Add each video's snippet to our list
    snippets.extend(video_response.get('items', []))

# Write the list of snippets to sample.json as a JSON array
with open('sample.json', 'w') as f:
    json.dump(snippets, f, indent=4)

print("Snippets for all videos have been saved to sample.json")

def upload_video(self, file_path, title, description, category_id, privacy_status='private'):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': privacy_status
        }
    }
    media = MediaFileUpload(file_path, resumable=True)
    request = self.youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )
    response = request.execute()
    return response
