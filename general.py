#top level domain: url not counting www or http (e.g. facebook.com)

import os

def create_dir(directory):

    if not os.path.exists(directory): #check if folder has been created already or not
    
        os.makedirs(directory)
        
def write_file(path, data): #path is where, data is what
    
    f = open(path, 'w') #open file
    f.write(data) #writing data to this file
    f.close() #close the file