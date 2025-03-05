import json
import sys
import logging

# Configura o logging de forma centralizada
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    if len(sys.argv) < 2:
        logger.info("Erro: Nenhum JSON foi fornecido como argumento.")
        sys.exit(1)
    
    try:
        # Obtém o JSON passado como argumento
        nome = sys.argv[1]
        idade = sys.argv[2]
        
        logger.info(f"Olá, {nome}! Você tem {idade} anos.")

    except json.JSONDecodeError:
        logger.info("Erro: O argumento fornecido não é um JSON válido.")
        sys.exit(1)

if __name__ == "__main__":
    main()
