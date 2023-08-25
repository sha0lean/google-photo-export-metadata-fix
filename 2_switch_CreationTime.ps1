# Chemin vers le dossier racine
$rootFolder = "C:\Users\shao\Pictures\GOOGLE PHOTOS"

# Fonction récursive pour mettre à jour les dates de création
function Update-CreationDates($folderPath) {
    $imageFiles = Get-ChildItem $folderPath -File | Where-Object { $_.Extension -match '\.(jpg|png|jpeg|mp4|avi|mov|flv)$' }

    foreach ($imageFile in $imageFiles) {
        # Obtenir la date de modification actuelle du fichier
        $modificationTime = $imageFile.LastWriteTime

        # Mettre à jour la date de création du fichier avec la date de modification
        $imageFile.CreationTime = $modificationTime

        Write-Host "La date de création de $($imageFile.FullName) a été mise à jour avec la date de modification ($modificationTime)."
    }

    $subFolders = Get-ChildItem $folderPath -Directory
    foreach ($subFolder in $subFolders) {
        Update-CreationDates $subFolder.FullName
    }
}

# Appeler la fonction pour commencer la mise à jour des dates
Update-CreationDates $rootFolder

Write-Host "Toutes les images dans tous les dossiers et sous-dossiers ont été mises à jour."
