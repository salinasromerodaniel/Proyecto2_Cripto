from flask import Flask, render_template, request
from flask import g
from algosdk import account, algod, mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn
from algosdk.v2client import algod
import hashlib


app=Flask(__name__)

class HASH():
    hash = None

class API_KEY():
    api = None

class DIRECCION_S():
    direccion = None

class DIRECCION_R():
    direccion = None

class MNEMONIC():
    mnemonic = None

class LINK():
    link = None

class ID():
    id = None

Api_key = API_KEY()
Direccion_s = DIRECCION_S()
Direccion_r = DIRECCION_R()
Mnemonic = MNEMONIC()
Link_doc = LINK()
Hash_doc = HASH()
Id = ID()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu', methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        Api_key.api = request.form['api']
        Direccion_s.direccion = request.form['direccions']
        Mnemonic.mnemonic = request.form['mnemonic']
    return render_template('menu.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    return render_template('result.html')

@app.route('/crear', methods=["GET", "POST"])
def crear():
    Link_doc.link = request.form['linkdoc']
    Hash_doc.hash = request.form['hash']
    # Configuración del cliente de Algod
    client = algod.AlgodClient(
        algod_token="",
        algod_address="https://testnet-algorand.api.purestake.io/ps2",
        headers={"X-API-Key": Api_key.api}
    )
    # Generar una cuenta para el propietario del token
    address = Direccion_s.direccion
    private_key = mnemonic.to_private_key(Mnemonic.mnemonic)
    # Configurar los parámetros de la transacción
    params = client.suggested_params()
    # Parámetros del token
    asset_name = "Apunte"
    asset_unitname = "DOC"
    asset_total = 1  # Como es un NFT, solo se crea una unidad
    asset_decimals = 0  # Nuevamente, como es un NFT, no hay decimales
    # En asset_url puedes poner el hash de IPFS del documento que quieres demostrar propiedad
    asset_url = Link_doc.link
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
    mensaje = "Successfully sent transaction with txID: {}".format(txid)
    return render_template('crear.html', mensaje = mensaje)

@app.route('/eliminar', methods=["GET", "POST"])
def eliminar():
    return render_template('eliminar.html')

@app.route('/reseliminar', methods=["GET", "POST"])
def reseliminar():
    Id.id = request.form['id']
    # Configuración del cliente de Algod
    client = algod.AlgodClient(
        algod_token="",
        algod_address="https://testnet-algorand.api.purestake.io/ps2",
        headers={"X-API-Key": Api_key.api}
    )
    # Cuenta propietaria del NFT
    owner_address = Direccion_s.direccion
    owner_private_key = mnemonic.to_private_key(Mnemonic.mnemonic)
    # Obtén el ID del activo después de haberlo creado
    asset_id = Id.id
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
    mensaje = "Successfully sent transaction with txID: {}".format(txid)
    return render_template('reseliminar.html', mensaje = mensaje)

@app.route('/consultar', methods=["GET", "POST"])
def consultar():
    salida = []
    if request.method == "POST":
        Id.id = request.form.get('id')
        if Id.id is not None :
            # Configuración del cliente de Algod
            client = algod.AlgodClient(
                algod_token="",
                algod_address="https://testnet-algorand.api.purestake.io/ps2",
                headers={"X-API-Key": Api_key.api}
            )
            # Obtén el ID del activo después de haberlo creado
            asset_id = Id.id  # replace with your asset id
            try:
                # Intenta obtener información del activo
                asset_info = client.asset_info(asset_id)
                # Parámetros deseados
                desired_params = ['name', 'unit-name', 'total', 'creator', 'manager', 'reserve', 'freeze', 'clawback']

                # Verificar que los parámetros necesarios existen
                if 'params' in asset_info:
                    salida.append("Asset ID: {}".format(asset_id))
                    for param in desired_params:
                        if param in asset_info['params']:
                            salida.append(f"Asset {param}: {asset_info['params'][param]}")
                        else:
                            salida.append(f"Asset {param} not found.")

                    # Comprueba si el activo ha sido marcado para eliminación
                    if asset_info["params"]["reserve"] == "" and asset_info["params"]["freeze"] == "" and asset_info["params"]["clawback"] == "":
                        salida.append("This asset has been marked for deletion.")
                    else:
                        salida.append("This asset has not been marked for deletion.")
                else:
                    salida.append("Asset not found or it's no longer available.")
                
            except Exception as e:
                salida.append(f"No se encontró información del NFT: {e}")
        return render_template('consultar.html', salida=salida)
    return render_template('consultar.html')


@app.route('/optar', methods=["GET", "POST"])
def optar():
    return render_template('optar.html')

@app.route('/resoptar', methods=["GET", "POST"])
def resoptar():
    Id.id = request.form['id']
    # Configuración del cliente de Algod
    client = algod.AlgodClient(
        algod_token="",
        algod_address="https://testnet-algorand.api.purestake.io/ps2",
        headers={"X-API-Key": Api_key.api}
    )
    # Configurar los parámetros de la transacción
    params = client.suggested_params()
    # Asumamos que la cuenta que desea optar por el NFT tiene la dirección siguiente
    optin_address = Direccion_s.direccion
    # Asumamos que el activo que quieres optar tiene el ID 123456
    asset_id = Id.id
    # Crea la transacción de transferencia de activos para optar por el activo
    txn = AssetTransferTxn(
        sender=optin_address,
        sp=params,
        receiver=optin_address,
        amt=0,  # Especifique una cantidad de 0 para optar por el activo
        index=asset_id,
    )
    # Necesitas la clave privada de la cuenta que está optando por el activo para firmar la transacción
    optin_private_key = mnemonic.to_private_key(Mnemonic.mnemonic)
    stxn = txn.sign(optin_private_key)
    # Enviar la transacción
    txid = client.send_transaction(stxn)
    mensaje = "Successfully sent opt-in transaction with txID: {}".format(txid)
    return render_template('resoptar.html', mensaje = mensaje)

@app.route('/transferir', methods=["GET", "POST"])
def transferir():
    if request.method == "POST":
        Id.id = request.form.get('id')
        Direccion_r.direccion = request.form.get('direccionr')
        if Id.id is not None :
            # Configuración del cliente de Algod
            client = algod.AlgodClient(
                algod_token="",
                algod_address="https://testnet-algorand.api.purestake.io/ps2",
                headers={"X-API-Key": Api_key.api}
            )
            # Cuenta propietaria del NFT
            address = Direccion_s.direccion
            private_key = mnemonic.to_private_key(Mnemonic.mnemonic)
            # Cuenta receptora del NFT
            receiver_address = Direccion_r.direccion
            # Configurar los parámetros de la transacción
            params = client.suggested_params()
            # ID del activo (NFT)
            asset_id = Id.id  # Reemplaza con el ID del NFT que creaste
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
            mensaje = "Successfully sent transaction with txID: {}".format(txid)
            return render_template('transferir.html', mensaje=mensaje)
    return render_template('transferir.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)