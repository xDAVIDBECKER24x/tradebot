from novadax import RequestClient as NovaClient


def getAccessKey():
    accessKey = "xxx"
    return accessKey


def getPrivateKey():
    secretKey = "xxx"
    return secretKey


novaClient = NovaClient(getAccessKey(), getPrivateKey())

#result = novaClient.get_ticker("LINK_BRL")
#currency = "LINK"
#print(result)
