# main.py
import subprocess
from Scripts.config_log import logger  # Importa el logger configurado

def run_script(script_name):
    try:
        subprocess.run(['python', f'Scripts/{script_name}'], check=True)
        logger.info(f'{script_name} ejecutado correctamente.')
    except subprocess.CalledProcessError as e:
        logger.error(f'Error al ejecutar {script_name}: {e}')

def main():
    scripts = [
        'main_dispatcher.py',
        'main_performer.py',
        'main_reporter.py'
    ]

    for script in scripts:
        run_script(script)

if __name__ == '__main__':
    main()
