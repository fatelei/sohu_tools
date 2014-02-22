#-*-coding: utf8-*-

"""
generate sohunews api params
"""

from lxml import etree


def generate_params(obj):
    """
    build xml tree
    """
    root = etree.Element("info")
    attribute = obj.__dict__

    for k, v in attribute.iteritems():
        child = etree.SubElement(root, k)
        child.text = v
    xml = etree.tostring(root, xml_declaration=True, encoding="GBK", standalone="yes").replace("\n", "")
    return xml


def convert_xml_to_json(xml):
    """
    convert xml to json
    """
    pass