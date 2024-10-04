# PYTHON
## Guide d'installation pour applications web interactives en python.

## Prérequis
###### Author: Ludovic.M

### 1. Installer Python
Python est nécessaire pour exécuter des scripts. Vous pouvez installer la dernière version de Python à partir du site officiel :

- [Télécharger Python](https://www.python.org/downloads/)

Assurez-vous d'ajouter Python au PATH lors de l'installation.

### 2. Installer PyCharm
PyCharm est un IDE puissant pour le développement Python. Pour l'installer, rendez-vous sur la page de téléchargement de PyCharm :

- [Télécharger PyCharm](https://www.jetbrains.com/pycharm/download/)

Vous pouvez choisir entre la version Community (gratuite) ou la version Professionnelle.

## Installation des dépendances

Une fois Python installé, vous pouvez installer les bibliothèques nécessaires pour votre projet.

### 3. Installer Streamlit
Streamlit est une bibliothèque Python pour créer des applications web interactives. Pour l'installer, exécutez la commande suivante dans votre terminal :

```bash
pip3 install streamlit
pip3 install pandas matplotlib
```

### Lancer le projet
```bash
streamlit hello
streamlit run main.py
```