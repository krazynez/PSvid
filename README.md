# Simple and easy app to convert videos to PS brand consoles including the PS2, PSP, PS3 and PSVITA. PSvid uses ffmpeg to do these conversion.

Options:
- High compatibility: compatible with the PSP, PS3 and PSVITA.
			Fast encoding, lower resolution.
- Medium compatibility: compatible with PS3 and PSVITA.
			Medium speed, standard resolution (SDTV).
- Low compatibility: compatible only with PS3.
			Slow speed, HD resolution.
- Others: different formats (PS2, iPhone, iPad, iPod Classic and Android).
			Experimental and Untested.

Notes:
- If your using Windows you have to install python first:
  http://www.python.org/download/releases/2.7.2/
- Ffmpeg source code can be found in: www.ffmpeg.org/download.html
- Newer versions of ffmpeg doesn't come with libfaac support, see below for a workaround.
- Ffmpeg installation with libfaac support:
	- Windows: ffmpeg for windows is bundled with PSvid, no problems there.
	- Source code: download the source code from www.ffmpeg.org/download.html
		compile it with the option --enable-libfaac .
	- Wine: you can use the win32 version provided with wine:
		sudo chmod +x ffmpeg.exe
		sudo ln -s ffmpeg.exe /usr/bin/ffmpeg
	- Ubuntu: you can use the medibuntu repositories to install ffmpeg and libavcodec-extra-52:
		sudo wget --output-document=/etc/apt/sources.list.d/medibuntu.list http://www.medibuntu.org/sources.list.d/$(lsb_release -cs).list && sudo apt-get --quiet update && sudo apt-get --yes --quiet --allow-unauthenticated install medibuntu-keyring && sudo apt-get --quiet update && sudo apt-get install ffmpeg libavcodec-extra-52

