flask-vue-demo
Scaffold a Vue project with Vite Create and render Vue components in the browser Create a Single Page Application (SPA) with Vue components Connect a Vue application to a Flask back-end for uploading video with custom subtitles Develop a RESTful API with Flask for saving video and subitle file in the /uploads folder Style Vue Components with Bootstrap Use the Vue Router to create routes and render components

For Flask Setup :

mkdir flask-vue $ cd flask-vue-crud just clone this repo inside this directory, you will get one client folder and one server folder go inside server directory and make venv py -m venv env $ source env/bin/activate if windows ./env/Scripts/Activate

pip install Flask==2.2.3 Flask-Cors==3.0.10

flask run --port=5001 --debug

Now For Vue Setup :

Go inside the client directory :

run npm install run npm run dev

the app will be running on port 5173

For demo purpose I have added a static video which is there in upload folder you can just try to copy on your local at some other place and upload the same file by deleteing from the server /uploads folder

also the static subtitle file name should be same like subtitle.vtt which will be saved in /uploads folder and in client it is getting save in /assets folder via API call

Once done the app is ready