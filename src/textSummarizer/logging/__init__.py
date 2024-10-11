import os
import sys
import logging

# Configuration de la chaîne de formatage du logger
logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Création du répertoire de logs s'il n'existe pas
os.makedirs(log_dir, exist_ok=True)

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Enregistrement dans un fichier
        logging.StreamHandler(sys.stdout)   # Affichage sur la sortie standard
    ]
)

# Création d'une instance de logger
logger = logging.getLogger("textSummarizerLogger")
