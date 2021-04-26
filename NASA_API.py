import requests as re
import json
from PIL import Image
import webbrowser
baseurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
cam = input("Enter Camera from these options : FHAZ,RHAZ,MAST,CHEMCAM,MAHLI,MARDI,NAVCAM,PANCAM,MINITES\t")
def extract_url(cam):
    params_dict = {}
    params_dict['sol'] = 1000
    params_dict['camera'] = cam
    params_dict['api_key'] = '5mbUiyd61GivFSFomTYnuKy8gxgGT9gZHsPeEqIc'
    res = re.get(baseurl , params=params_dict)
    return res.json()['photos'][0]['img_src']
pic = extract_url(cam)
webbrowser.open(pic)
