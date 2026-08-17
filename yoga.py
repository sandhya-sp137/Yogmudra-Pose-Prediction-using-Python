from flask import Flask, render_template, request
import csv
import re
import threading
import webbrowser
from collections import defaultdict
import requests

app = Flask(__name__)

YOUTUBE_API_KEY = "AIzaSyBBTJkDOqIPxJqID8duvCy5WEoz9j6qxxs"

def get_youtube_video(pose_name):
    query = f"{pose_name} yoga mudra"
    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}&maxResults=1"
    )
    try:
        response = requests.get(url)
        data = response.json()
        if 'items' in data and data['items']:
            video_id = data['items'][0]['id']['videoId']
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            print(f"[YouTube] Fetched video for {pose_name}: {embed_url}")
            return embed_url
    except Exception as e:
        print(f"YouTube API Error for '{pose_name}':", e)
    return None

def load_yoga_data(csv_path):
    data = defaultdict(list)
    try:
        with open(csv_path, encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                steps = re.split(r'\s*\d+\.\s*', row['Steps'].strip())
                steps = [s.strip() for s in steps if s.strip()]
                data[row['Disease'].strip()].append({
                    'pose': row['Yoga Pose'].strip(),
                    'image_path': row['Image Path'].strip(),
                    'pressure_point': row['Pressure Points'].strip(),
                    'steps': steps
                })
    except FileNotFoundError:
        print(f"Error: '{csv_path}' not found.")
    return data

YOGA_DATA = load_yoga_data('poses.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        query = request.form.get('disease', '').strip().lower()
        for disease, poses in YOGA_DATA.items():
            if disease.lower() == query:
                pose_list = []
                for pose in poses:
                    video_url = get_youtube_video(pose['pose'])
                    pose_list.append({
                        'pose': pose['pose'],
                        'image_path': pose['image_path'],
                        'pressure_point': pose['pressure_point'],
                        'steps': pose['steps'],
                        'video_url': video_url
                    })
                result = {'disease': disease, 'poses': pose_list}
                break
        if not result:
            result = {'error': 'No yoga poses found for this disease.'}
    return render_template('index.html', search_result=result, YOGA_DATA=YOGA_DATA)

if __name__ == '__main__':
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True)
