from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

# https://developers.google.com/search/apis/indexing-api/v3/prereqs#header_2
JSON_KEY_FILE = "inc/excellent-well-362109-c135d343d86b.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

def indexURL(url):
    # print(type(url)); print("URL: {}".format(url));return;

    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    
    u = url
    # print("U: {} type: {}".format(u, type(u)))

    content = {}
    content['url'] = u.strip()
    content['type'] = "URL_UPDATED"
    json_ctn = json.dumps(content)    
    # print(json_ctn);return

    response, content = http.request(ENDPOINT, method="POST", body=json_ctn)

    result = json.loads(content.decode())
    output = dict()
    # For debug purpose only
    if("error" in result):
        output['error']= "Error({} - {}): {}".format(result["error"]["code"], result["error"]["status"], result["error"]["message"])
        output['success'] = False
    else:
        output['meta_url'] = " {}".format(result["urlNotificationMetadata"]["url"])
        output['url'] = " {}".format(result["urlNotificationMetadata"]["latestUpdate"]["url"])
        output['type'] =" {}".format(result["urlNotificationMetadata"]["latestUpdate"]["type"])
        output['time'] = " {}".format(result["urlNotificationMetadata"]["latestUpdate"]["notifyTime"])
        output['success'] = True

    return output

"""
data.csv has 2 columns: URL and date.
I just need the URL column.
"""
# csv = pd.read_csv("data.csv")
# csv[["URL"]].apply(lambda x: indexURL(x, http))