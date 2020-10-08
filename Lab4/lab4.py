import http.client
import urllib.parse

key = "AT68QYQ94MQEWXL3" # Put your API Key here
def write_info():
    params = urllib.parse.urlencode({'field1': "L3-T-5",'field2': "yisheng.li@cmail.ca",'field3': "a",'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers) 
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")
        
if __name__ == "__main__":
        write_info()
