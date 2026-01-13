import can
import time

# Connexion
try:
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print(" Vcan0 activé avec succes!")
except:
    print("Erreur vcan0")
    exit()

def envoyer_mixte(id_cligno, action_cligno, valeur_raw_vitesse):
    # GESTION VITESSE 
    high_byte = (valeur_raw_vitesse >> 8) & 0xFF  # Partie haute
    low_byte  = valeur_raw_vitesse & 0xFF         # Partie basse

    # ID 244 : Vitesse
    data_vitesse = [0x00, 0x00, 0x00, high_byte, low_byte, 0x00, 0x00, 0x00]
    msg_v = can.Message(arbitration_id=0x244, data=data_vitesse, is_extended_id=False)
    bus.send(msg_v)

    # GESTION CLIGNOTANT 
    # ID 188 : Clignotants
    data_cligno = [action_cligno, 0x00, 0x00, 0x00]
    msg_c = can.Message(arbitration_id=0x188, data=data_cligno, is_extended_id=False)
    bus.send(msg_c)

# CONFIGURATION 
VITESSE_MAX = 12000  
PAS = 60             # Vitesse de montée de l'aiguille
TEMPS_CLIGNO = 0.5   # Vitesse du clignotant 

try:
    start_time = time.time()
    
    while True:
        # PHASE 1 : MONTÉE + Glignotement GAUCHE 
        print(" Montée vers 100+ km/h (Gauche)")
        for i in range(0, VITESSE_MAX, PAS):
            
          
            now = time.time()
            if (now % (TEMPS_CLIGNO * 2)) < TEMPS_CLIGNO:
                cligno = 0x01 # Allumé (Gauche)
            else:
                cligno = 0x00 # Eteint
            
            envoyer_mixte(0x188, cligno, i)
            time.sleep(0.01) # PAUSE 

        #  PHASE 2 : DESCENTE + glignotement DROITE 
        print(" Descente progressive (Droite)")
        for i in range(VITESSE_MAX, 0, -PAS):
            
            now = time.time()
            if (now % (TEMPS_CLIGNO * 2)) < TEMPS_CLIGNO:
                cligno = 0x02 # Allumé (Droit)
            else:
                cligno = 0x00 # Eteint
                
            envoyer_mixte(0x188, cligno, i)
            time.sleep(0.01) # PAUSE 

except KeyboardInterrupt:
    print("\n Fin.")
