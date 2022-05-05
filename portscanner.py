import nmap
import ipaddress
import re
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
print(r"""

 _  __    _    ____    _    _     ___ 
| |/ /   / \  | __ )  / \  | |   |_ _|
| ' /   / _ \ |  _ \ / _ \ | |    | | 
| . \  / ___ \| |_) / ___ \| |___ | | 
|_|\_\/_/   \_\____/_/   \_\_____|___|""")

print("\n****************************************")
print("\n*******Port Scanner By Neelavardhan*****")
#creating Function for 
def common():
    port=[21,22,53,80,139,443,445,1433,7104,7102]
    print("Port     Status         Service Name      Version")
    print("----      ------        ------------       --------")
    for i in range(0,10):
        try:
            result=nm.scan(ip,str(port[i]),arguments='-sV -Pn')
            port_status=(result['scan'][ip]['tcp'][port[i]]['state'])
            service=(result['scan'][ip]['tcp'][port[i]]['name'])
            version=(result['scan'][ip]['tcp'][port[i]]['version'])
            product=(result['scan'][ip]['tcp'][port[i]]['product'])
            if(port_status=="open"):
                print(f"{port[i]}          {port_status}             {service}           {product}{version}")
            i=i+1
        except:

            print(f"Cannot scan port{port[i]}.")
            break
    
#Function for range of ports
def Range():
    print("Port     Status         Service Name      Version")
    print("----      ------        ------------       --------")   
    for port in range(min_port,max_port+1):
        try:
            result=nm.scan(ip,str(port),arguments='-sV -Pn')
            port_status=(result['scan'][ip]['tcp'][port]['state'])
            service=(result['scan'][ip]['tcp'][port]['name'])
            version=(result['scan'][ip]['tcp'][port]['version'])
            product=(result['scan'][ip]['tcp'][port]['product'])
            if(port_status=="open"):
                print(f"{port}          {port_status}             {service}           {product}{version}")
                       
        except:

                                print(f"Cannot scan port{port}.")
             

#function for All Ports
def All():
    print("Port     Status         Service Name      Version")
    print("----      ------        ------------       --------")
    for port in range(1,65536):
        try:
            result=nm.scan(ip,str(port),arguments='-sV -Pn')
            port_status=(result['scan'][ip]['tcp'][port]['state'])
            service=(result['scan'][ip]['tcp'][port]['name'])
            version=(result['scan'][ip]['tcp'][port]['version'])
            product=(result['scan'][ip]['tcp'][port]['product'])
                                
            if(port_status=="open"):
                                         
                print(f"{port}          {port_status}             {service}           {product}{version}")
        except:
            print(f"Cannot scan port{port}.")

#function for Specific ports
def SPorts():
    port=int(input("Enter specific port:"))
    if(port>0 & port<=65535):
        print("port is Valid.")
        print("Port     Status         Service Name      Version")
        print("----      ------        ------------       --------")
        try:
                    result=nm.scan(ip,str(port),arguments='-sV -Pn')
                    port_status=(result['scan'][ip]['tcp'][port]['state'])
                    service=(result['scan'][ip]['tcp'][port]['name'])
                    version=(result['scan'][ip]['tcp'][port]['version'])
                    product=(result['scan'][ip]['tcp'][port]['product'])
                    if(port_status=="open"):
                        print(f"{port}          {port_status}             {service}           {product}{version}")
                    
        except:
                    print(f"Cannot scan port{port}.")



#Taking Ip Address from user
while True:
        ip=input("\nEnter IP:")
        if ip_pattern.search(ip):
           print(f"{ip} is valid")
           break
        else:
           print(f"{ip} is invalid")
nm = nmap.PortScanner()
print("Select Option.\n")
print("1.Range of Ports")
print("2.All ports")
print("3.Specific Port")
print("4.common port")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in('1','2','3','4'):
        if choice=='1':
            min_port=int(input("Enter min port:"))
            max_port=int(input("Enter max port:"))
            if(min_port>0 & min_port<=65535):
                if(max_port>0 & max_port<=65535):
                    Range()
                    
        elif choice=='2':
            All()
            break
        elif choice=='3':
            SPorts()
            
        elif choice=='4':
            common()
   
