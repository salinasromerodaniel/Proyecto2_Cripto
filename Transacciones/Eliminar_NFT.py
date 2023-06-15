from algosdk import mnemonic
from algosdk.future.transaction import AssetConfigTxn
from algosdk.v2client import algod

# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)

# Cuenta propietaria del NFT
owner_address = "Y4NE6BC54JITBDIYIS5CVIYCW2TGC5GQBJXRJGD665R3KGWTP3HPFPJM7Y"
owner_private_key = mnemonic.to_private_key("mnemonic")

# Obtén el ID del activo después de haberlo creado
asset_id = 237714955

# Configurar los parámetros de la transacción
params = client.suggested_params()

# Crear la transacción
txn = AssetConfigTxn(
    sender=owner_address,
    sp=params,
    index=asset_id,
    manager=None,
    reserve=None,
    freeze=None,
    clawback=None,
    strict_empty_address_check=False,
)

# Firmar la transacción
stxn = txn.sign(owner_private_key)

# Enviar la transacción
txid = client.send_transaction(stxn)
print("Successfully sent transaction with txID: {}".format(txid))

