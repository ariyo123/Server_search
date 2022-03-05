
import os
import shutil
from shutil import copytree, rmtree
#def nippos():
print('You are about to fetch logs containing certain infromation from all your servers')

name=input("Enter file name: ")

#store the IPs$path in this location in this format "//127.0.0.1/c$/python_work/FETCH_LOG/wrapper"
url='C:/python_work/FETCH_LOG_NAME/ipsnippos.txt'
#location of IPs to append to the file that will be copied
apend='C:/python_work/FETCH_LOG_NAME/ip_append.txt'
#read the the file-ip_append.txt
try:
    with open(apend, 'r') as appendage:
        append_urls=appendage.read()

        #file_object.close()
        
except:
    print(f"The file does not exist in the location")
else:
    #convert it to a list(a_ips)
    a_ips=append_urls.split('\n')
    #loop through the list 1 at a time
    for ip_pend in a_ips[:]:
        print(ip_pend)
        #read the the file-ipsnippos.txt
        try:
            with open(url, 'r') as file_object:
                urls=file_object.read()
                #file_object.close()
                
        except:
            print(f"The file does not exist in the location")
            
        else:
            #convert it to a list(ips)
            ips=urls.split('\n')
            #loop through the list 1 at a time
            for ip in ips[:]:
                #store the common name structure of the logs here
                print(ip)
                            #loop through the names 1 at a time
                for file in os.listdir(str(ip)):
                    print(file)
                    #check for a file that starts with the entered name            
                    if file.startswith((f"{name}")):
                        #print(file)
                        
                        src = f'{ip}/{name}'
                        print(src)
                        destination=f"C:/python_work/FETCH_LOG_NAME/content/{name}{ip_pend}"
                        dst = destination
                        #print(dst)
                        #if token is found in the log, the log is moved to a location called content in destination
                        
                        shutil.copy2(src, dst)
                        