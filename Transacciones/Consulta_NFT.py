from algosdk.v2client import algod

# Configuración del cliente de Algod
client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "6cvGrbkG7J0CAdxAzHZN6pRqLLodXql5LbCTGYQi"}
)

# Obtén el ID del activo después de haberlo creado
asset_id = 237621761  # replace with your asset id

try:
    # Intenta obtener información del activo
    asset_info = client.asset_info(asset_id)
    # Parámetros deseados
    desired_params = ['name', 'unit-name', 'total', 'creator', 'manager', 'reserve', 'freeze', 'clawback']

    # Verificar que los parámetros necesarios existen
    if 'params' in asset_info:
        print("Asset ID: {}".format(asset_id))
        for param in desired_params:
            if param in asset_info['params']:
                print(f"Asset {param}: {asset_info['params'][param]}")
            else:
                print(f"Asset {param} not found.")

        # Comprueba si el activo ha sido marcado para eliminación
        if asset_info["params"]["reserve"] == "" and asset_info["params"]["freeze"] == "" and asset_info["params"]["clawback"] == "":
            print("This asset has been marked for deletion.")
        else:
            print("This asset has not been marked for deletion.")
    else:
        print("Asset not found or it's no longer available.")
    
except Exception as e:
    print(f"Failed to fetch asset info: {e}")


