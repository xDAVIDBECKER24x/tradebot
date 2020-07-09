from novadax import RequestClient as NovaClient


def getAccessKey():
    accessKey = "fde2f5bd-1f6a-4f31-aad5-cceb0abd813c"
    return accessKey


def getPrivateKey():
    secretKey = "hBq5LZgtFJVisjOHSY5cr4EZgu1hKM80"
    return secretKey


novaClient = NovaClient(getAccessKey(), getPrivateKey())

#result = novaClient.get_ticker("LINK_BRL")
#currency = "LINK"
#print(result)
