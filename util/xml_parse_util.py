from lxml import etree


def xml_parse(xmlStr):
    xml = etree.XML(xmlStr)
    return etree.tostring(xml, pretty_print=True).decode("utf-8")


def xml_compress(xmlStr):
    xml = etree.XML(xmlStr)
    return etree.tostring(xml).decode("utf-8")
