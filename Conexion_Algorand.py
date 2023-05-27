import algosdk.v2client.algod as algod
import ipfshttpclient

algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "pMVxEd580O2alV37M9fXD37jWdasSRPE2jTEj1xv"}
)
#status = algod_client.status()
#print(status)
client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001/http")  # Establece la conexión con el nodo local de IPFS
print(client)