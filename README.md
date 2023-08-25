# Google Photo export metadata fix

Script Python et PowerShell pour résoudre le problème des dates de création de l'export Google Photo.

En gros j'ai exporté 500Go de photos et tout s'est exporté avec la date de création du jour (2023).
Les dates de création initiale sont stockées dans le fichier `photo.png.json` associé.

J'ai utilisé un script python pour prendre cette date et la stocker dans la Date de modif
Ensuite un script Powershell pour copier la date de modif dans la date création.

Powershell est necessaire car c'est la seule solution pour modifier la date de Création.

Cordialement
