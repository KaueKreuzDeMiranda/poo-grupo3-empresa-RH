def lerString(mensagem):
    return input(mensagem)

def lerInt(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\n--- Insira um valor válido! ---")

def lerFloat(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\n--- Insira um valor válido! ---")