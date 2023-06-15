from algosdk import account, algod, mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn
from algosdk.v2client import algod
import hashlib


# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)


# Generar una cuenta para el propietario del token
address = "Y4NE6BC54JITBDIYIS5CVIYCW2TGC5GQBJXRJGD665R3KGWTP3HPFPJM7Y"
private_key = mnemonic.to_private_key("mnemonic")


# Configurar los parámetros de la transacción
params = client.suggested_params()


# Parámetros del token
asset_name = "Apunte"
asset_unitname = "DOC"
asset_total = 1  # Como es un NFT, solo se crea una unidad
asset_decimals = 0  # Nuevamente, como es un NFT, no hay decimales
# En asset_url puedes poner el hash de IPFS del documento que quieres demostrar propiedad
asset_url = "https://ipfs.io/ipfs/Prueba"
metadata= "Doc Title: Prueba"
asset_metadata = hashlib.sha256(metadata.encode()).digest()




# Crear la transacción
txn = AssetConfigTxn(
    sender=address,
    sp=params,
    total=asset_total,
    default_frozen=False,
    unit_name=asset_unitname,
    asset_name=asset_name,
    manager=address,
    reserve=address,
    freeze=address,
    clawback=address,
    url=asset_url,
    metadata_hash=asset_metadata,
    decimals=asset_decimals,
)


# Firmar la transacción
stxn = txn.sign(private_key)


# Enviar la transacción
txid = client.send_transaction(stxn)
print("Successfully sent transaction with txID: {}".format(txid))


