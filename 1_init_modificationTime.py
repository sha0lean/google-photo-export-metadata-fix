import os
import json
from datetime import datetime

# Chemin vers le dossier racine contenant les médias
root_folder = 'C:\\Users\\shao\\Pictures\\GOOGLE PHOTOS'

# Liste des extensions de fichiers image et vidéo
image_extensions = ['.jpg', '.png', '.jpeg']
video_extensions = ['.mp4', '.avi', '.mov', '.flv']  # Ajoutez d'autres extensions au besoin

# Fonction récursive pour mettre à jour les dates de modification
def update_creation_dates(folder):
    for root, _, files in os.walk(folder):
        for media_file in files:
            if any(media_file.lower().endswith(ext) for ext in image_extensions + video_extensions):
                # Obtient le nom du média (avec extension)
                media_name = os.path.splitext(media_file.lower())[0]

                # Construit le chemin complet vers le fichier média et son fichier JSON associé
                media_path = os.path.join(root, media_file)
                json_path = os.path.join(root, f"{media_file}.json")

                if os.path.exists(json_path):
                    # Charger le contenu du fichier JSON correspondant
                    with open(json_path, 'r') as json_file:
                        data = json.load(json_file)

                    # Extraire la date de photoTakenTime du JSON
                    media_taken_timestamp = data.get('photoTakenTime', {}).get('timestamp')

                    if media_taken_timestamp:
                        # Convertir le timestamp en objet datetime (UTC)
                        media_taken_datetime = datetime.utcfromtimestamp(int(media_taken_timestamp))

                        # Afficher la date de modification initiale du fichier média
                        initial_modification_time = datetime.utcfromtimestamp(os.path.getmtime(media_path))

                        # Mettre à jour la date de modification du fichier média avec la date photoTakenTime
                        os.utime(media_path, (os.path.getatime(media_path), media_taken_datetime.timestamp()))

                        # Afficher les informations sur le fichier modifié
                        print(f"\n--------------------------------------------------------------------------")
                        print(f"  Fichier :                     {media_file}\n")
                        print(f"  initial modification_time :   {initial_modification_time}")
                        print(f"      new modification_time :   {media_taken_datetime}")
                    else:
                        # Si pas de date photoTakenTime, afficher un message et passer au prochain fichier
                        print(f"\n------------------------------------------------------------")
                        print(f"\nLe fichier JSON                 {json_path} ne contient pas de photoTakenTime.")
                        continue

                else:
                    # Si aucun fichier JSON associé trouvé, afficher un message
                    print(f"\nAucun fichier JSON trouvé pour {media_file}.json.")

# Appeler la fonction pour commencer la mise à jour des dates
update_creation_dates(root_folder)

print("\nProcessus terminé.")
