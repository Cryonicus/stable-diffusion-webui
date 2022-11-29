### Conversion script for ckpt to safetensor with filedrop for convenience

This script is run by dragging and dropping a CKPT file onto ckpt-drop.bat
This will execute ckpt-to-tensor.py with the file you dropped
Once complete your <filename.ckpt> will have been converted to <filename.safetensor>
Your old file <filename.ckpt> will remain where it is, unchanged.

### BEFORE YOU RUN THIS SCRIPT

Start a command box and type "pip install safetensors" or click on "install_safetensor.bat"

Once installation is confirmed completed, you can run the conversion script. If you get
a path error, make sure you've set your environment path properly.
Here is a guide if you get stuck: https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables

###Thank you to Devalidating of the Stable Diffusion Discord for helping me out