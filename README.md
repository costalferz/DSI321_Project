# Setting Up
* create requirement.txt, tell dependencies you need (docker file will read this file later)
```
pandas
requests
lxml
html5lib
beautifulsoup4
```
* install dependencies for Jupyter
```bash
pip install -r requirement.txt 
```
* create Dockerfile
```Dockerfile
FROM python:3.8
WORKDIR /code
COPY . .
COPY requirement.txt  requirement.txt
RUN pip install -r /code/requirement.txt
# เหมือนจะขาดไปหนึ่งบรรทัด
```

* create conjob.yaml (see detail in link)
https://github.com/wasit7/dsi321_2023/blob/main/week13/conjob.yaml
* modify schedule cronjob to every 6 hours
* warning : this step requires publish your docker image to docker hub 
```yaml
schedule: "* * * * *"   # modify to every 6 hours
image: kran13200/simple-scripy:latest # use your docker hub
```
* create metadata.json  (see detail in link) : you have to modified information corresponding to your information - warning : name should be unique small letter and title should be big letter  
https://github.com/wasit7/dsi321_2023/blob/main/week13/metadata.json
* name and title should be name of your dataset and contain your group code
```json
    "name": "thailand_gdp03",   # must change this line
    "title": "THAILAND_GDP_03", # must change this line
```

# Data Source
* Weather Data Source : https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false
* pandas can load HTML table tag with single function
```python
# from URL
dfs = pd.read_html("https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false")
# from .env : WEB_SCRIPY MUST PRE-DEFINE IN .env
import os
dfs = pd.read_html(os.getenv("WEB_SCRIPY"))
```


# Data Preparation and Metadata
* before write python code in script that send to deploy in real server, you must test and confirm your code in Jupyter.
* copy .env-template to .env
```
cp .env-template .env      #ubuntu / mac
copy .env-template .env    #window
```
* specify TOKEN (permission to access ckan, see in code week 12), CKAN_URL, WEB_SCRIPY URL in .env
```
TOKEN=xxxxxxxxxxx   # ใส่ TOKEN
CKAN_URL=https://ckan.data.storemesh.com
WEB_SCRIPY=yyyyyyyyy # ใส่ URL web สำหรับ scrap 
```
* create your new Jupyter notebook file 
* load data source from google sheet link above
* use pandas to ETL data and transform into appropriate structure and export to df.CSV

# Send Data to CKAN Dataset

* this set step require metadata.json and function to send 
## Create dataset only one time
* you may create dataset in Jupyter with code like week 12 

## Upload data
* see detail in scripy.py

# Publish to Docker hub
* You must have docker hub account
* Try to publish your image to docker hub
* in .yaml file use your image instead

# Kubernates CronJob
* modified cronjob in metadata.json at schedule
* deploy to kubernetes server see detail in week 9

# Data Visualization and Interpretation
*need help!*

# Project References
* https://www.iqair.com/th/air-pollution-data-api
* [Air Quality Index (AQI)](https://en.wikipedia.org/wiki/Air_quality_index)
* [API Reference](https://api-docs.iqair.com/)
* [Crontab Editor](https://crontab.guru/#*_*/6_*_*_*)
* [Weather Data Source](https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false)