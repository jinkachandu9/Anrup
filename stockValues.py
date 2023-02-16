from bsedata.bse import BSE
def getStock(value):
    b=BSE()
    xml=b.getQuote(value)
    return float(xml.get('currentValue'))


