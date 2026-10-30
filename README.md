#  Automotive CAN Bus Controller (Python & SocketCAN)

![Badge Python](https://img.shields.io/badge/Language-Python_3-blue.svg)
![Badge Security](https://img.shields.io/badge/Focus-Automotive%20Cybersecurity-red.svg)
![Badge Platform](https://img.shields.io/badge/Platform-Linux%20%2F%20SocketCAN-lightgrey.svg)

##  Aperçu du Projet
Ce projet est une démonstration de manipulation d'un réseau de bord automobile (Car Hacking) par l'injection automatisée de paquets sur un bus CAN virtuel. 

Contrairement à de simples attaques de type "Replay" manuelles, j'ai développé un outil personnalisé en Python interagissant directement avec l'interface `vcan0` via SocketCAN pour prendre le contrôle programmé du tableau de bord.

##  Fonctionnalités du Script (`scenario.py`)
Le script exécute un scénario d'attaque/contrôle automatisé gérant le **multitâche** (multithreading/gestion asynchrone des trames) :
*  **Injection de vitesse progressive :** Manipulation de l'aiguille du compteur de vitesse de manière fluide.
*  **Synchronisation des clignotants :** Activation contrôlée des indicateurs visuels.
*  **Maintien d'état (Keep-alive) :** L'aiguille de vitesse reste stable pendant que les clignotants sont actifs, imitant un comportement réseau réaliste face au bruit de fond du CAN.

##  Stack Technique
* **Langage :** Python 3 (SocketCAN)
* **Système :** Linux (Kali)
* **Outils d'analyse :** `can-utils`
* **Simulation :** ICSim (Instrument Cluster Simulator)

##  Comment reproduire la simulation

### 1. Préparer l'interface virtuelle CAN
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
### 2. Lancer le simulateur ICSim
*(j ai mis dans deux terminaux séparés)*
```bash
./icsim vcan0
./controls vcan0
```
### 3. Exécuter le script de contrôle Python
```
python3 scenario.py
```
##  Obstacles surmontés
* **Gestion du bruit réseau :** Le simulateur générant un trafic de fond constant, le principal défi a été de maintenir l'injection des trames de contrôle (vitesse, clignotants) sans être écrasé par le bruit, résolu en ajustant la fréquence d'envoi des paquets via Python.
  
### ⚠️ Avertissement Légal
Ce projet a été réalisé à des fins strictement éducatives. Les techniques démontrées ne doivent jamais être appliquées sur un véhicule réel en circulation ou sans l'autorisation explicite du propriétaire.
