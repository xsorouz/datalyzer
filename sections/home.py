# ============================================================
# Fichier : sections/home.py
# Objectif : Page d’accueil professionnelle, claire et zen
# Auteur : Xavier Rousseau
# ============================================================

import streamlit as st
from PIL import Image
from io import BytesIO
import base64
from utils.ui_utils import show_footer
from config import APP_NAME, PALETTE_ZEN


def run_home():
    """Affiche la page d'accueil principale de l'application Datalyzer"""

    # === Chargement + centrage HTML de l'image d’accueil ===
    image_path = "static/images/headers/hearder_temple.png"
    try:
        img = Image.open(image_path).resize((900, 220))
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode()

        st.markdown(
            f"""
            <div style='display: flex; justify-content: center; margin-bottom: 1.5rem;'>
                <img src="data:image/png;base64,{base64_img}" alt="Bannière Datalyzer" 
                     style="border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);" />
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.warning(f"Erreur d’image d’accueil : {e}")

    # === Citation zen d’introduction ===
    st.markdown(f"""
        <div style="text-align: center; font-style: italic; font-size: 14px; color: {PALETTE_ZEN['accent']}; margin-bottom: 1rem;">
            "La clarté naît de la structure." — Datalyzer
        </div>
    """, unsafe_allow_html=True)

    # === Titre principal et description courte ===
    st.markdown(f"""
        <h1 style='color:{PALETTE_ZEN["primaire"]}; margin-bottom: 0.5rem;'>
            {APP_NAME}
        </h1>
        <p style='font-size: 16px; color:{PALETTE_ZEN["texte"]}; margin-top: 0;'>
            Une plateforme sobre et efficace pour explorer, nettoyer et structurer vos données tabulaires.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # === Bloc "Pour bien démarrer" ===
    st.markdown(f"""
        <div style="background-color:{PALETTE_ZEN['fond_section']};
                    border-radius: 10px;
                    padding: 1rem 1.5rem;
                    margin-bottom: 2rem;
                    box-shadow: 0 1px 6px rgba(0,0,0,0.06);
                    color: {PALETTE_ZEN['texte']};">
            <strong>Pour bien démarrer :</strong> commencez par importer vos données via l’onglet <em>Chargement</em>,
            puis explorez, corrigez et exportez un jeu prêt à l’analyse.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # === Aperçu global ===
    st.markdown("### Aperçu de l'application")

    # === Trois colonnes équilibrées ===
    col1, col2, col3 = st.columns(3)

    # === Bloc 1 : Fonctionnalités principales ===
    with col1:
        st.markdown(f"""
            <div style="background-color: {PALETTE_ZEN['fond_section']};
                        border-radius: 10px;
                        padding: 1.2rem;
                        min-height: 280px;
                        box-shadow: 0 1px 6px rgba(0,0,0,0.06);">
                <h4 style="color:{PALETTE_ZEN['secondaire']}; margin-top:0;">Fonctionnalités principales</h4>
                <ul style="line-height: 1.6; font-size: 15px; color: {PALETTE_ZEN['texte']}">
                    <li>Import : CSV, Excel, JSON, Parquet</li>
                    <li>Exploration intuitive des variables</li>
                    <li>Nettoyage : doublons, types, valeurs manquantes</li>
                    <li>Analyse : ACP, clustering, corrélations</li>
                    <li>Suggestions de préparation automatique</li>
                    <li>Export multi-format des jeux corrigés</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # === Bloc 2 : Données ===
    with col2:
        st.markdown(f"""
            <div style="background-color: {PALETTE_ZEN['fond_section']};
                        border-radius: 10px;
                        padding: 1.2rem;
                        min-height: 280px;
                        box-shadow: 0 1px 6px rgba(0,0,0,0.06);">
                <h4 style="color:{PALETTE_ZEN['secondaire']}; margin-top:0;">Données</h4>
                <ul style="line-height: 1.5; font-size: 14px; color:{PALETTE_ZEN['texte']}">
                    <li>Chargement : CSV, XLSX, Parquet</li>
                    <li>Jointures : fusion intelligente sur clés</li>
                    <li>Export : formats propres et exploitables</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # === Bloc 3 : Analyse ===
    with col3:
        st.markdown(f"""
            <div style="background-color: {PALETTE_ZEN['fond_section']};
                        border-radius: 10px;
                        padding: 1.2rem;
                        min-height: 280px;
                        box-shadow: 0 1px 6px rgba(0,0,0,0.06);">
                <h4 style="color:{PALETTE_ZEN['secondaire']}; margin-top:0;">Analyse</h4>
                <ul style="line-height: 1.5; font-size: 14px; color:{PALETTE_ZEN['texte']}">
                    <li>Exploration : types, distributions, manquants</li>
                    <li>Typage : correction semi-automatique</li>
                    <li>Qualité : doublons, erreurs, valeurs vides</li>
                    <li>Multivariée : ACP, corrélations, clustering</li>
                    <li>Ciblée / catégorielle : regroupements</li>
                    <li>Suggestions : colonnes à corriger ou exclure</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # === Pied de page standard ===
    show_footer(author="Xavier Rousseau", github="xsorouz", version="1.0")
