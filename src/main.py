def sumar(a,b):
    return a + b


def validar_usuario(usuario, contraseña):
        usuarios_validos = {"usuario1": "contraseña123", "usuario2": "clave456"}
        return usuario in usuarios_validos and usuarios_validos[usuario] == contraseña

def validar_rut(rut):
    if not rut or not isinstance(rut, str):
        return False
    
    partes = rut.split('-')
    if len(partes) != 2:
        return False
    
    cuerpo, digito_verificador = partes

    if not cuerpo.isdigit() or not digito_verificador.isdigit():
        return False

    return len(cuerpo) == 8 and digito_verificador.isdigit()
