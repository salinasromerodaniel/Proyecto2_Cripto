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
owner_private_key = mnemonic.to_private_key("inmate better neutral bread tray adult rack army warrior peasant method close frozen hint galaxy balcony swing whale valve clerk until wash trip ability spare")

# ID del activo (NFT) a eliminar
asset_id = 234965190  # Reemplaza con el ID del NFT que deseas eliminar

# Parámetros de la transacción
params = client.suggested_params()

# Crear la transacción de eliminación del NFT
txn = AssetConfigTxn(
    sender=owner_address,
    sp=params,
    index=asset_id,
    strict_empty_address_check=False,  # Permitir la eliminación incluso si el saldo no está vacío
    manager=owner_address,
    reserve=owner_address,
    freeze=owner_address,
    clawback=owner_address,
    total=0  # Establecer la cantidad total a 0 para destruir el activo
)

# Firmar la transacción
signed_txn = txn.sign(owner_private_key)

# Enviar la transacción
txid = client.send_transaction(signed_txn)
print("Successfully sent transaction with txID: {}".format(txid))
