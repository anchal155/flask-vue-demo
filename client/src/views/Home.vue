<template>
    <h1 class="text-center top-30">Flask Video Demo</h1>
    <div class="container">
      <div class="card top-30">
        <article class="card-body">
          <h4 class="card-title mb-4 mt-1">Upload Video</h4>
          <form @submit.prevent="submitForm" class="style1">
            <div v-for="(subtitle, index) in subtitles" :key="index">
              <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="subtitle.startTime" placeholder="Start Time (hh:mm:ss.sss)"  aria-label="Start Time (hh:mm:ss.sss)" aria-describedby="basic-addon2" required>
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="subtitle.endTime" placeholder="End Time (hh:mm:ss.sss)" aria-label="End Time (hh:mm:ss.sss)" aria-describedby="basic-addon2" required>
              </div>
              <div class="input-group">
                <textarea class="form-control" v-model="subtitle.text" placeholder="Subtitle Text"></textarea>
              </div>
            </div>
            <div class="form-group video-class">
              <input type="file" accept="video/*" ref="videoFile" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload" required  />
            </div>
            <div class="form-group my-class">
              <button type="submit" class="btn btn-primary" >Upload Video and Create Subtitles</button>
            </div>
          </form>
        </article>
      </div>
    </div>
</template>
<script>
    import axios from 'axios';
    export default {
    data() {
        return {
          showDisplayVideo: false,
          subtitles: [
              { startTime: '', endTime: '', text: '' }
          ],
          file: 'subtitle.vtt',
        };
    },
    methods: {
        submitForm() {
            const videoFile = this.$refs.videoFile.files[0];

            this.videoFileName = videoFile;
    
            // Create a new FormData instance
            const formData = new FormData();
            formData.append('video', videoFile);
    
            // Format the subtitle data into the desired structure
            const formattedSubtitles = this.subtitles
            .filter(subtitle => subtitle.startTime && subtitle.endTime && subtitle.text)
            .map(subtitle => {
                return {
                start: subtitle.startTime,
                end: subtitle.endTime,
                text: subtitle.text
                };
            });
            
            // Generate the subtitles file content
            const subtitlesContent = `WEBVTT\r\n${formattedSubtitles
            .map(subtitle => `${subtitle.start} --> ${subtitle.end}\n${subtitle.text}`)
            .join('')}`;
            
            // Append the subtitles data to the FormData
            formData.append('subtitles', new Blob([subtitlesContent], { type: 'text/vtt' }), this.file);
    
            // Submit the form data to the server
            axios.post('http://localhost:5001/api/upload', formData)
            .then(response => {
                console.log('Upload successful');
                this.showDisplayVideo = true;
                this.$router.push('/display');
            })
            .catch(error => {
                console.error('Upload failed:', error.message);
            });
        },
        addSubtitle() {
            this.subtitles.push({ startTime: '', endTime: '', text: '' });
        },
        removeSubtitle(index) {
            this.subtitles.splice(index, 1);
        },
      },
    };
</script>

<style scoped>
  button {
      margin-top:20px;
      margin-bottom: 30px;
  }

  .my-class{
      display: flex;
      justify-content: center;
      align-items: center;
  }

  .card {
      width:700px;
      margin: 0 auto;
      float: none;
      margin-bottom: 10px;
      border-radius: 50px;
      background-color: turquoise;

  }
  input { 
      margin-bottom: 20px;
  }
  h4{
      text-align: center;
  }
  .top-30{
      margin-top: 30px;
      padding-top: 30px;
  }
  #inputGroupFile04{
    margin-top:30px;
  }
  
</style>
