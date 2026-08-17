from flask import Flask, render_template, request
import csv, re, threading, webbrowser
from collections import defaultdict
import requests

app = Flask(__name__)

YOUTUBE_API_KEY = "AIzaSyBBTJkDOqIPxJqID8duvCy5WEoz9j6qxxs"

def get_youtube_video(pose_name):
    query = f"{pose_name} yoga mudra"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}&maxResults=1"
    try:
        response = requests.get(url)
        data = response.json()
        if data['items']:
            video_id = data['items'][0]['id']['videoId']
            return f"https://www.youtube.com/embed/{video_id}"
    except Exception as e:
        print("YouTube error:", e)
    return None

def load_yoga_data(csv_path):
    data = defaultdict(list)
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
    return data

YOGA_DATA = load_yoga_data('poses.csv')

# ✅ Index route with form and result display
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        query = request.form.get('disease', '').strip().lower()
        for disease, poses in YOGA_DATA.items():
            if disease.lower() == query:
                for pose in poses:
                    pose['video_url'] = get_youtube_video(pose['pose'])
                result = {'disease': disease, 'poses': poses}
                break
        if not result:
            result = {'error': 'No yoga poses found for this disease.'}
    return render_template('index.html', search_result=result, YOGA_DATA=YOGA_DATA)

if __name__ == '__main__':
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True)


