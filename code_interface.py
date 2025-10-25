import streamlit as st
import pandas as pd
import time
import random

# --- Configuration de la Page ---
st.set_page_config(
    page_title="SolarCanal - Démo Irrigation Intelligente",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Constantes du Projet ---
SEUIL_HUMIDITE_CRITIQUE = 30  # Pourcentage d'humidité critique
NOM_CULTURE = "Tomates Cerises (Rang n°5)"

# --- Fonction principale de simulation ---
def simuler_cycle_irrigation():
    # 1. État Initial (Simulation du capteur)
    st.subheader(f"📊 Données Temps Réel : {NOM_CULTURE}")
    
    # Simuler une humidité initiale sèche (sous le seuil)
    humidite_actuelle = random.randint(15, SEUIL_HUMIDITE_CRITIQUE - 5)
    temp_actuelle = random.randint(28, 35) # T° élevée
    
    # Affichage des métriques clés
    col1, col2, col3 = st.columns(3)
    col1.metric("💧 Humidité du Sol", f"{humidite_actuelle} %", help="Niveau d'eau nécessaire dans le sol.")
    col2.metric("🌡️ Température", f"{temp_actuelle} °C")
    col3.metric("☀️ Puissance Solaire", "100 W (Charge OK)")
    
    st.markdown("---")
    
    # 2. Logique de Décision et Alerte
    if humidite_actuelle < SEUIL_HUMIDITE_CRITIQUE:
        st.error(f"⚠️ ALERTE : Humidité critique ({humidite_actuelle} %)! Irrigation nécessaire.")
        
        # Le bouton d'action est ici l'élément central du pitch
        if st.button("▶️ ACTIVER IRRIGATION (DÉMO MANUELLE)", help="Simule l'ordre automatique envoyé à la vanne ESP32"):
            # 3. Phase d'Action (Effet WOW)
            
            st.warning("🔄 Ordre envoyé à l'ESP32... La vanne s'ouvre lentement.")
            time.sleep(1) # Délai pour l'effet visuel
            
            # Affichage du statut
            status_text = st.empty()
            status_text.info("✅ **IRRIGATION EN COURS** : L'eau s'écoule dans les sillons...")
            
            # Simulation du temps d'irrigation (juste 3 secondes pour la démo)
            for i in range(1, 4):
                status_text.info(f"💦 Irrigation en cours (Étape {i}/3)...")
                time.sleep(1)
            
            # 4. Phase Post-Irrigation (Mise à jour des données)
            st.balloons() # L'effet visuel de succès !
            status_text.success("🎉 Succès ! Irrigation terminée. La vanne se ferme.")
            
            # Simulation des nouvelles données après l'arrosage
            humidite_nouvelle = random.randint(55, 75)
            
            st.markdown("---")
            st.subheader("✅ Statut Post-Irrigation")
            st.success("Le niveau d'humidité est rétabli.")
            
            # Affichage des nouvelles métriques
            col_new1, col_new2 = st.columns(2)
            col_new1.metric("💧 Nouvelle Humidité", f"{humidite_nouvelle} %", f"↑ +{humidite_nouvelle - humidite_actuelle} %")
            col_new2.metric("🟢 Statut Vanne", "FERMÉE")

            st.write("Le système repasse en veille pour économiser l'énergie solaire.")
            
    else:
        # État normal (pas besoin d'arroser)
        st.success("💧 Humidité optimale. Système en veille pour l'économie d'eau.")
        st.write("Prochaine vérification dans 5 minutes (via l'ESP32).")

# --- Lancement du Dashboard ---
st.title("SolarCanal : Irrigation Intelligente par Canaux")
st.caption("Projet **Climathon** - Optimisation de l'eau en milieu agricole")
st.markdown("---")

simuler_cycle_irrigation()
