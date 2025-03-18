# Simulação de um aplicativo Python que usa uma chave de API
api_key = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  # Exemplo de token do GitHub
url = "https://api.exemplo.com/dados"

def fetch_data():
    print(f"Conectando à API com a chave: {api_key}")
    # Simulação de uma chamada à API
    return "Dados recebidos!"

if __name__ == "__main__":
    resultado = fetch_data()
    print(resultado)