from xml.etree import cElementTree
import requests

def parse_rss():
  response = requests.get('path.xml')
  parsed_xml = cElementTree.fromstring(response.content)
  items = []
  for node in parsed_xml.iter():
    if node.tag == 'item':
      item = {}
      for item_node in list(node):
        if item_node.tag == 'title':
          item['title'] = item_node.text
        if item_node.tag == 'link':
          item['link'] = item_node.text
          items.append(item)
    return items[:10]

