<template>
    <div class="container top-50">
        <video id="videoElement" :width="450"  :src="videoUrl" type="video/mp4" controls>
        </video>
    </div>
    <div>
  </div>
</template>
  
  <script>
    import axios from 'axios';
    
    export default {
        name: 'DisplayVideo',
        props:['file'],
        data() {
            return {
                videoUrl: '',
                subtitlesContent: null,
                videoFileName: '',
                SubtitleFileName: ''
            }
        },
        async mounted() {

            const  getfileNames = axios.get('http://localhost:5001/api/getFilename');
            const response = await getfileNames;

            var data = response.data.files;
            this.videoFileName = data["videoFile"];
            this.SubtitleFileName = data["subtitleFile"];
            
            const getSubtitles = axios.get('http://localhost:5001/api/getSubtitles/' + this.SubtitleFileName);
            const getVideo = axios.get('http://localhost:5001/api/getVideo/' + this.videoFileName);

            const responses = await Promise.all([getSubtitles, getVideo]);
            const subtitlesResponse = responses[0];
            const videoResponse = responses[1];

            // getting the file content and the url path for video display
            this.subtitlesContent = subtitlesResponse.data;
            this.videoUrl = videoResponse.config.url;

            this.saveSubtitleToAssets(this.subtitlesContent);
        },
        methods: {
            saveSubtitleToAssets(subtitles) {
                fetch('http://localhost:5001/api/save-subtitle', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/octet-stream',
                    },
                    body: subtitles,
                })
                .then(response => {
                    if (response.ok) {
                        console.log('Subtitle file saved successfully.');

                        // After saving the subtitle file, dynamically create the subtitle track
                        const trackElement = document.createElement('track');
                        trackElement.kind = 'captions';
                        trackElement.srclang = 'en';
                        trackElement.label = 'Video Captions';
                        trackElement.src = 'src/assets/subtitle.vtt';
                        trackElement.default = true;

                        // Get the video element by its ID or any other appropriate selector
                        const videoElement = document.getElementById('videoElement');

                        // Append the track element to the video element
                        videoElement.appendChild(trackElement);
                        
                    } else {
                        console.error('Subtitle file save failed.');
                    }
                })
                .catch(error => {
                    console.error('Subtitle file save failed:', error);
                });
                
            }
        },
    }
  </script>
  <style scoped>
    video {
        width: 100%;
    }
    .top-50{
        margin-top: 50px;
    }
  </style>
  