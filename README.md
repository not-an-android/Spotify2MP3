# Spotify2MP3

## Description

Downloads a Spotify playlist into a folder of MP3 tracks using Python3.

## Linux Setup

- Install Python3: `sudo apt install python3`
- Clone the repository: `git clone https://github.com/not-an-android/Spotify2MP3.git`, or download the zip
- Move into the repository directory: `cd Spotify2MP3`
- Install the requirements: `pip3 install -r requirements.txt`
- Install ffmpeg: `sudo apt install ffmpeg` (you can use a package manager of your choice)
- Go to <https://developer.spotify.com/dashboard> and click on "**CREATE AN APP**" (you can name it whatever you want)
- Run the program: `python3 spotify2mp3.py`, it will prompt you for your **Client ID** and **Client Secret**, both of which you can get from the application dashboard (**DO NOT SHARE YOUR CLIENT SECRET WITH ANYONE!**)
- The program will then prompt you for your playlist URI, go to <https://open.spotify.com> and click on the playlist you want to download
- Copy the sequence of characters at the end of the URL and paste them into the program

## Windows Setup

The only difference in setup between Windows and Linux is the download and setup of python and ffmpeg.

- Download and install Python3: <https://www.python.org/downloads> or search for Python3 on the Microsoft Store
- Download ffmpeg: <https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z>
- Extract the 7z archive using 7zip (<https://www.7-zip.org/download.html>) or any other supported extractor
- Add the absolute path of ffmpeg.exe (C:\\Users\\**[USER_NAME]**\\**[FFMPEG_DOWLOAD_LOCATION]**\bin\ffmpeg.exe) to PATH

Don't forget to replace **[USER_NAME]** & **[FFMPEG_DOWNLOAD_LOCATION]** with your user name and the location of your ffmpeg folder, respectively.

### Help

How to add to PATH in Windows 10: <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>

## Optional (Might not work on windows)

If you don't wish to be prompted for your client's credentials every time you run the program, you can replace the values in the .env.example file with your **Client ID** and **Client Secret** and rename the file to ".env".

## Credits

This program was not originally created by me. I only fixed, modified & build upon the work of github.com/JayChen35.
