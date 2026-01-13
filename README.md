 🚗 ICSim CAN Bus Controller

Ce projet est une démonstration de simulation de vehicule hacking par l'injection de paquets sur un bus CAN virtuel.

 🎯 Objectif
Contrôler un tableau de bord de voiture simulé (Instrument Cluster Simulator) en utilisant Python et SocketCAN.

 🛠️ Fonctionnalités
Le script `scenario.py` exécute un scénario automatisé :
- **Injection de vitesse progressive** (Accélération fluide jusqu'à 140km/h).
- **Synchronisation des clignotants** (Logique temporelle sans bloquer le thread principal).
- **Gestion multitâche** : L'aiguille reste fluide  pendant que les clignotants sont lents (2Hz).

## 💻 Prérequis
- Linux (Kali)
- Outils : `can-utils`, `ICSim`
- Interface : `vcan0`

## 🚀 Comment lancer
```bash
# 1. Préparer le vcan0
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# 2. Lancer le script en ouvrant un autre terminal
python3 can_exploit.py
