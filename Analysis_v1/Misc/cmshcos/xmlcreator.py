import xml.etree.ElementTree as xml

def indent(elem, level=0):
        from xml.etree import ElementTree as xml
'''
copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
it basically walks your tree and adds spaces and newlines so the tree is
printed in a nice way
'''
def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

# https://github.com/python/cpython/commit/63673916464bace8e2147357395fdf3497967ecb
def sort_attributes(root):
    for el in root.iter():
        attrib = el.attrib
        #print el, attrib
        if len(attrib) > 1:
            attribs = sorted(attrib.items())
            attrib.clear()
            attrib.update(attribs)


'''
function to build an example tree containing cars and ships
CFGBrickset is the root node
'''
def buildTree():
  CFGBrickset = xml.Element("CFGBrickset")

  CFGBrick = xml.SubElement(CFGBrickset, "CFGBrick")
  #cars.set("Type", "American")

  #CFGBrick = xml.Element('Parameter', type="string", name="INFOTYPE") 
  #CFGBrick.set("type", "string")
  #CFGBrick.set("name", "INFOTYPE")

  Parameter = xml.SubElement(CFGBrick, "Parameter", type="string", name="INFOTYPE")
  #Parameter.set("type", "string")
  #Parameter.set("name", "INFOTYPE")
  Parameter.text = "HBTDCLUT"

  Parameter2 = xml.SubElement(CFGBrick, "Parameter", type="string", name="CREATIONSTAMP")
  Parameter2.text = "2020-9-7"

  Parameter3 = xml.SubElement(CFGBrick, "Parameter", type="string", name="CREATIONTAG")
  Parameter3.text = "HBburnin1p3Gsel18"

  Parameter4 = xml.SubElement(CFGBrick, "Parameter", type="string", name="RBX")
  Parameter4.text = "HB1"

  rm = []
  qie = []
  rm.extend(range(1,6))
  for irm in rm:
        maxR = 64
        if irm == 5:
                maxR = 17
        qie.extend(range(1,maxR))
        #print irm, qie

  for irm in rm:
        for i in qie:
                #<Data qie="9" rm="3" elements="1" encoding="hex">Oxf Oxc Oxd Oxe</Data>
                #<Data qie="9" rm="3" elements="1" encoding="dec">37 1 1 8 8</Data>
                Data = xml.SubElement(CFGBrick, "Data", qie="%s"%(str(i)), rm="%s"%(str(irm)), elements="1", encoding="hex")
                Data.text = "Oxf Oxc Oxd Oxe"
                #sort_attributes(CFGBrick)
  #sort_attributes(CFGBrick) 
  indent(CFGBrickset)

  tree = xml.ElementTree(CFGBrickset)

  tree.write("HBTDCLUT.xml", xml_declaration=True, encoding='utf-8', method="xml")

'''
main function, so this program can be called by python program.py
'''
if __name__ == "__main__":
  buildTree()
