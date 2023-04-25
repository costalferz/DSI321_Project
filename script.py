import pandas as pd
import requests
import json, os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
## create package
def sendMetaToCkan(url_ckan, api_key, ckan_meta):
    headers = {
        'content-type': 'application/json',
        'Authorization': api_key,
    }

    url = '{}/api/action/package_create'.format(url_ckan)
    respond = requests.post(url, data=json.dumps(ckan_meta), headers=headers)
    res_text = respond.content.decode('utf-8').replace('\n','br')
    print(res_text)
    
## Upload File
def uploadFileToCkan(url_ckan, api_key, file_meta, path_input):
    headers = {'X-CKAN-API-Key': api_key}
    url = '{}/api/action/resource_create'.format(url_ckan)
    with open(path_input, "rb") as f:
        form_file = {'upload': f}
        respond = requests.post(url, data=file_meta, headers=headers, files=form_file)
        res_text = respond.content.decode('utf-8').replace('\n','br')
        print(res_text)
        print('<b>File has been uploaded</b>')

df_original = pd.read_html(os.getenv("WEB_SCRIPY"), encoding='utf-8')
df = df_original[0].iloc[1:, 1:].copy() 
df.columns = df_original[0].iloc[0, 1:]
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

df.to_csv("./data/data-scripy.csv",index=False, encoding='utf-8-sig')

ckan_meta = json.load(open('metadata.json',encoding='utf-8'))


url_ckan = os.getenv("CKAN_URL")  # ใส่ ip ของ ckan server ตรงนี้
api_key = os.getenv("TOKEN_ADMIN") 


file_meta = {
    'package_id': ckan_meta['name'],
    'name': f'data-scripy',
}

path_input = "./data/data-scripy.csv"
# sendMetaToCkan(url_ckan, api_key, ckan_meta)

uploadFileToCkan(url_ckan, api_key, file_meta, path_input)
