from algosdk.v2client import algod

# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)

# ID del activo (NFT) que fue eliminado
asset_id = 234965190  # Reemplaza con el ID del NFT que fue destruido

# Obtener información actualizada del activo
asset_info = client.asset_info(asset_id)
if asset_info is None:
    print("The NFT has been destroyed.")
else:
    print("The NFT still exists.")
