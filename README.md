# PyRansom

## ENGLISH
PyRansom is a POC of ransomware in python. Its sole purpose is educational, by trying to prove the ease of creating this type of malware. 

## FRANCAIS
PyRansom est un POC de ransomware en python. Son unique but est éducatif, en voulant prouver la facilité de création de ce type de malware. Le type de chiffrement utilisé est AES.

Il a été créer dans le cadre du projet de site web [Pignus](https://github.com/BlackEagle001/Pignus).

### Législation
L'exécution de ce logiciel est à la responsabilitée de l'utilisateur. Son unique but est éducatif. Veuillez l'utiliser sur un système informatique vous appartenant ou dont vous avez l'autorisation du propriétaire et il est illégale de l'exploiter sur tout autre système informatique.

### Ficheirs
#### Ransomware
Le malware correspond au fichier [encrypt.py](encrypt.py). C'est ce fichier qui chiffre les fichiers de l'utilisateur (par défaut, le bureau). Le seul paramètre vitale à modifier est `HOST` (ligne 13) et correspond à l'adresse ip du serveur du hackeur ou son nom de domaine.

#### Serveur
Le fichier [server.py](server.py) correspond au serveur du hackeur. Il récupère le FQDN de la victime, le vecteur d'initialisation (iv) et la clef de chiffrement utilisé pour chiffrer les données.

#### Déchiffrement
Le fichier [decrypt.py](decrypt.py) permet de déchiffrer les données à partir du vecteur d'initialisation et de la clef, tous deux passés en arguments. Il doit être exécuté depuis le dossier chiffré ou celui-ci doit être passé en argument à l'aide de l'option `-d` ou `--directory`.
