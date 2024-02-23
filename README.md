# label-img
A Krita plugin for image labeling.

### install
1. Download ZIP
2. Unzip files
3. Place it in the following directory:<br>
   **Windows - %APPDATA%\krita\pykrita<br>
   Linux - ~/.local/share/krita/pykrita<br>
   Apple - ~/Library/Application Support/Krita/pykrita**

### enable
1. Enable plugin:<br>
   **Settings > Configure Krita > Python Plugin Manager > Label IMG**
2. Restart Krita
3. Open docker:<br>
   **Settings > Dockers > Label IMG**
4. Set shortcut:<br>
   **Settings > Configure Krita > Keyboard Shortcuts > Scripts > Label IMG > (Go Left & Go Right)**
5. Disable Acceleration (This setting sometimes crashed Krita):<br>
   **Settings > Configure Krita > Display > Canvas Acceleration > Canvas Graphics Acceleration**
6. Disable autosaving & backup (This setting affects file reading):<br>
   **Settings > General > File Handling > (Enable Autosaving & Create a Backup File on Saving)**

### usage
1. Open a random image.
1. Copy and paste the image folder directory to docker.<br>
   **eg. D:/path/to/image/folder**
2. Copy and paste the label folder directory to docker.<br>
   This directory should have blank images when initiated.<br>
   Images should also have 3 bands.<br>
   **eg. D:/path/to/label/folder**

### notice
1. Test on Krita 5.1 & Krita 5.2.
