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
address = "Y4NE6BC54JITBDIYIS5CVIYCW2TGC5GQBJXRJGD665R3KGWTP3HPFPJM7Y"
private_key = mnemonic.to_private_key("mnemonic")

# Cuenta receptora del NFT
receiver_address = "FIMYONVZTTVTB5OWG2O7HZZWRCLJEUWDVDBJEBOT2Z223LOEOG47QLPIXE"


# Configurar los parámetros de la transacción
params = client.suggested_params()

# ID del activo (NFT)
asset_id = 237621761  # Reemplaza con el ID del NFT que creaste

# Crea la transacción de transferencia de activos
txn = AssetTransferTxn(
    sender=address,
    sp=params,
    receiver=receiver_address,
    amt=1,  # Transfiere 1 unidad del activo, ya que es un NFT
    index=asset_id,
    revocation_target=None,  # Este campo es necesario para transferencias de activos en Algorand
)

# Firmar la transacción
stxn = txn.sign(private_key)

# Enviar la transacción
txid = client.send_transaction(stxn)
print("Successfully sent transaction with txID: {}".format(txid))
