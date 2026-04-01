import hashlib
import secrets

def hash_padrao(entrada:str):

    entrada = str(entrada)
    entrada_bytes = None

    if not isinstance(entrada, bytes):
        entrada_bytes = entrada.encode('utf-8')

    try:
        return hashlib.sha256(entrada_bytes)
    except Exception as e:
        raise(e)

def comparar_hashes(hash0, hash1):
    try:
        return secrets.compare_digest(hash0, hash1)
    except Exception as e:
        print(e)
        return False