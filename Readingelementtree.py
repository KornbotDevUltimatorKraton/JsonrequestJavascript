import xml.etree.ElementTree as ET
tree = ET.parse('Examplexml.xml')
root = tree.getroot()
root.tag 
root.attrib
for child in root: 
       print(child.tag,child.attrib)
print(root[0][1].text)
for neighbor in root.iter('neighbor'): 
      print(neighbor.attrib)
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)