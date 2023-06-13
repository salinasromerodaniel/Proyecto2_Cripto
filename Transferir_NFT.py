from algosdk import mnemonic
from algosdk.future.transaction import AssetTransferTxn
from algosdk.v2client import algod

# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)

# Cuenta propietaria del NFT
sender_address = "Y4NE6BC54JITBDIYIS5CVIYCW2TGC5GQBJXRJGD665R3KGWTP3HPFPJM7Y"
sender_private_key = mnemonic.to_private_key("inmate better neutral bread tray adult rack army warrior peasant method close frozen hint galaxy balcony swing whale valve clerk until wash trip ability spare")

# Cuenta receptora del NFT
recipient_address = "FIMYONVZTTVTB5OWG2O7HZZWRCLJEUWDVDBJEBOT2Z223LOEOG47QLPIXE"

# ID del activo (NFT)
asset_id = 234965190  # Reemplaza con el ID del NFT que creaste

# Parámetros de la transacción
params = client.suggested_params()

# Crear la transacción de transferencia del NFT
txn = AssetTransferTxn(
    sender=sender_address,
    sp=params,
    receiver=recipient_address,
    amt=0,  # Transferir una cantidad de 0 para transferir el NFT completo
    index=asset_id
)

# Firmar la transacción
signed_txn = txn.sign(sender_private_key)

# Enviar la transacción
txid = client.send_transaction(signed_txn)
print("Successfully sent transaction with txID: {}".format(txid))
