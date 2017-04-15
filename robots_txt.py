#tells search engine crawlers to find parts of a website or not

import urllib.request
import io

def get_robots_text(url):
    
    if url.endswith('/'): #if the url ends with slash
        path = url #leave it the same
    else:
        path = url + '/' #add the slash
        
    req = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(req, encoding = 'utf-8')
    
    return data.read()