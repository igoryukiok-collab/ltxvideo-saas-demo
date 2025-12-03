import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, required=True)
parser.add_argument("--output", type=str, required=True)
args = parser.parse_args()

# Simula o processo de geração do vídeo
print(f"Gerando vídeo com prompt: {args.prompt}")
time.sleep(5)  # Simula tempo de render
print(f"Vídeo salvo em {args.output}")

# Cria um arquivo vazio para simular saída
with open(args.output, "w") as f:
    f.write("Simulação de vídeo gerado")
