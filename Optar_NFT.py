from algosdk import  algod, mnemonic
from algosdk.future.transaction import  AssetTransferTxn
from algosdk.v2client import algod



# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)


# Configurar los parámetros de la transacción
params = client.suggested_params()

# Asumamos que la cuenta que desea optar por el NFT tiene la dirección siguiente
optin_address = "FIMYONVZTTVTB5OWG2O7HZZWRCLJEUWDVDBJEBOT2Z223LOEOG47QLPIXE"

# Asumamos que el activo que quieres optar tiene el ID 123456
asset_id = 237621761

# Crea la transacción de transferencia de activos para optar por el activo
txn = AssetTransferTxn(
    sender=optin_address,
    sp=params,
    receiver=optin_address,
    amt=0,  # Especifique una cantidad de 0 para optar por el activo
    index=asset_id,
)

# Necesitas la clave privada de la cuenta que está optando por el activo para firmar la transacción
optin_private_key = mnemonic.to_private_key("plunge used oval copy access lecture apple black never false gossip ski area true velvet tomato hazard yellow ostrich topple journey kind arch abstract picture")
stxn = txn.sign(optin_private_key)

# Enviar la transacción
txid = client.send_transaction(stxn)
print("Successfully sent opt-in transaction with txID: {}".format(txid))



