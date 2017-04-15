import os

def get_nmap(options, ip):
    
    command = "nmap " + options + " " + ip #nmap command
    process = os.popen(command) #runs it
    
    results = str(process.read()) #reads it
    
    return results
    
print(get_nmap('-F', '54.186.250.79'))