def sumar(a,b):
    return a + b


def validar_usuario(usuario, contraseña):
        usuarios_validos = {"usuario1": "contraseña123", "usuario2": "clave456"}
        return usuario in usuarios_validos and usuarios_validos[usuario] == contraseña
