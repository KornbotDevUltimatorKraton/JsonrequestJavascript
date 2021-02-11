import os # For the operating system function ti control the automatic directory reader 
from xml.dom import minidom 
from xml.dom.minidom import parse 
import xml.etree.ElementTree as ET 
 # Reading the poxition of the catesian file to collect the shape and angle of the plane with accurate position 
#Modelloader = open('Catbot3.stp','r') # Reading raw data from step file input 
tree = ET.parse('stm32F103c8t6_1.lbr')
root = tree.getroot()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Child root for the xml reader  
for child in root: 
       print(child.tag,child.attrib)
print(root[0][0].text)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Searching reading grid 
for grid in root.iter('grid'):
     print(grid.attrib)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Package reading the layer  
for layers in root.iter('layer'):
         print(layers.attrib)
         print(len(layers.attrib))
         number = layers.get('number')

         print("Number:"+number)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Package reading part 
for package in root.iter('package'):
         print(package.attrib)
         desc = package.find('description').text
         print("Packages of MCU"+"\t"+desc.split(" ")[0])
         #Showing the list to of the all mcu to classify the right type of the mcu catigory
         listPackages = ['QFP','BGA','UFBGA','WLCSP','VQFPN','UFQFPN']   # List category of the packages to show the right data of each mcu package
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Package size for estimation function
         Packagedetails = desc.split(" ")
         print(Packagedetails)
         Packageseeker = desc.split(" ")[0].split("-")[1]
         GPIOs = desc.split(" ")[0].split("-")[0]  # Amout of pins on the microcontroller 
         e = Packagedetails[1] # Get the pitch of the part 
         span = Packagedetails[7] #Get the span of the square rounded chip 
              
         #Searching for package of the mcus 
         for i in range(0,int(len(listPackages))):  
             if str(listPackages[i]) in Packageseeker:
                   print("Found:"+listPackages[i],GPIOs,e,span) #Package check function 
 #Get the position back from the step file data 
def ThreedCatesian(x,y,z): 
      print(x,y,z) # Getting the position of the 3d data from the step file model  
      #Catesian data from the step file function 
      

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                      
'''
print('\n All Item data:')
print(root)
for elem in root:
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      # Get the darawing setting on the eagle xml code 
     Settingdata = str(elem[0]).split('at')
     Settingsplitdata = Settingdata[0].split('Element')
     print(Settingsplitdata[1])          
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     Data = str(elem[1]).split('at')
     Getelem = Data[0].split('Element')
     print(Getelem[1]) # Get the element in the item tree
'''      
     
     