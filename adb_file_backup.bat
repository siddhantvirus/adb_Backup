ECHO OFF
adb devices
cd %HOMEPATH%/Desktop
md Backup
adb pull /sdcard/ %HOMEPATH%/Dektop/Backup
