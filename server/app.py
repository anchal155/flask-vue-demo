from flask import Flask, request, send_file, jsonify, url_for
import os
from flask_cors import CORS
import base64
from webvtt import WebVTT

app = Flask(__name__)
#CORS(app)  # Enable CORS for all routes

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# Save the video file
current_directory = os.getcwd()

#Upload subtitle file and video file and save it in \upload foler
@app.route('/api/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        # Check if both video and subtitle files are present in the request
        if 'video' not in request.files or 'subtitles' not in request.files:
            return jsonify({'error': 'Video and subtitles files are required'}), 400

        video_file = request.files['video']
        subtitle_file = request.files['subtitles']
        
        # Check file extensions
        allowed_video_extensions = ['mp4', 'avi', 'mov']
        allowed_subtitle_extensions = ['srt', 'vtt']
        
        video_extension = video_file.filename.rsplit('.', 1)[-1].lower()
        subtitle_extension = subtitle_file.filename.rsplit('.', 1)[-1].lower()
        
        if video_extension not in allowed_video_extensions:
            return jsonify({'error': 'Invalid video file extension'}), 400

        if subtitle_extension not in allowed_subtitle_extensions:
            return jsonify({'error': 'Invalid subtitle file extension'}), 400

        
        uploads_folder = os.path.join(current_directory, 'uploads')
        if not os.path.exists(uploads_folder):
            os.makedirs(uploads_folder)
            
        video_path = os.path.join(uploads_folder, video_file.filename)
        video_file.save(video_path)

        # Save the subtitle file
        subtitle_path = os.path.join(uploads_folder, subtitle_file.filename)
        subtitle_file.save(subtitle_path)
        
        # Read the contents of the subtitle file
        return 'the files are uploaded successfully'
    
#Get the Video file
@app.route('/api/getVideo/<filename>', methods = ['GET'])
def get_video(filename):

    uploads_folder = os.path.join(current_directory, 'uploads')
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)

    video_path = os.path.join(uploads_folder, filename)
    return send_file(video_path, mimetype='video/mp4')


# Get the Subtitle file in vtt format 
@app.route('/api/getSubtitles/<file>', methods = ['GET'])
def get_subtitles(file):
    uploads_folder = os.path.join(current_directory, 'uploads')
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)
        
    subtitle_path = os.path.join(uploads_folder, file)
    return send_file(subtitle_path, mimetype='text/vtt')


#save the subtitle file in asset folder on client's end
@app.route('/api/save-subtitle', methods=['POST'])
def save_subtitle():
    subtitle_content = request.get_data(as_text=True)
    if not subtitle_content:
        return jsonify({'error': 'Content is blank'}), 400
    
    parent_directory = os.path.dirname(current_directory)

    subtitle_path = os.path.join(parent_directory, 'client/src/assets', 'subtitle.vtt')
    with open(subtitle_path, 'w') as subtitle_file:
        subtitle_file.write(subtitle_content)

    return jsonify({'message':'Subtitle file saved successfully.', 'statusCode': 200})

if __name__ == '__main__':
    app.run(debug=True)