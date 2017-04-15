import os

def get_ip_address(url):
    
    command = "host " + url #host facebook.com
    process = os.popen(command) #runs that command
    results = str(process.read()) 
    
    marker = results.find('has address') + 12 #"facebook.com has address 69.171.230.68", extracts the address part
    
    return results[marker:].splitlines()[0] #splitlines so it only returns first address if there are multiple
    
print(get_ip_address("google.com"))