import streamlit as st
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ============================================================
# CONFIGURATION & CONSTANTES
# ============================================================

st.set_page_config(
    page_title="HAMIDOUCHE REDJDAL | CV",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

PHOTO = Path("photo.jpg")
PDF_PATH = Path("cv_hamidouche_redjdal.pdf")

nom = "HAMIDOUCHE REDJDAL"
telephone = "00213775 73 79 30"
email = "hamidoucheredjdal@yahoo.fr"
adresse = "Tazmalt 06039, wilaya de Bejaia"

# ============================================================
# FONCTION DE GÉNÉRATION DU PDF (Exécutée à chaque lancement)
# ============================================================

def generer_pdf(filepath):
    """Génère et écrase le fichier PDF à chaque exécution du script."""
    doc = SimpleDocTemplate(
        str(filepath),
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontSize=20, leading=24, textColor=colors.HexColor('#102a43'), spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle', parent=styles['Normal'],
        fontSize=12, leading=16, textColor=colors.HexColor('#1f5f8b'), spaceAfter=12
    )
    section_heading = ParagraphStyle(
        'SectionHeading', parent=styles['Heading2'],
        fontSize=13, leading=16, textColor=colors.HexColor('#102a43'), spaceBefore=10, spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyTextCustom', parent=styles['Normal'],
        fontSize=9, leading=13, textColor=colors.HexColor('#334e68')
    )

    story = []

    # En-tête
    story.append(Paragraph(f"<b>{nom}</b>", title_style))
    story.append(Paragraph("<b>Planificateur et Superviseur Logistique</b>", subtitle_style))
    story.append(Paragraph(f"📞 {telephone} &nbsp;|&nbsp; ✉️ {email} &nbsp;|&nbsp; 📍 {adresse}", body_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1f5f8b'), spaceAfter=12))

    # Profil
    story.append(Paragraph("PROFIL PROFESSIONNEL", section_heading))
    story.append(Paragraph(
        "Dynamique, sérieux et ayant de bonnes compétences relationnelles, avec 9 ans d'expérience "
        "dans le domaine de la logistique. Très à l'aise avec les outils informatiques, je souhaite "
        "mettre mes compétences au service d'une entreprise.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Expériences
    story.append(Paragraph("EXPÉRIENCES PROFESSIONNELLES", section_heading))
    exps = [
        ("Superviseur techno-commercial", "SPA TMF Logistics", "01/2024 - Présent", "Analyse des besoins clients, élaboration de reportings, contrôle des flux."),
        ("Superviseur exploitation", "SPA TMF Logistics", "06/2022 - 01/2024", "Supervision des opérations de transport, gestion d'équipe, planification."),
        ("Chargé de la planification", "SPA TMF Logistics", "02/2020 - 06/2022", "Optimisation des ressources logistiques, gestion des ordres de mission."),
        ("Coordinateur logistique", "SPA TMF Logistics", "02/2019 - 02/2020", "Mise en place d'indicateurs de suivi, coordination inter-services."),
        ("Chargé de la programmation", "SPA TMF Logistics", "04/2016 - 10/2018", "Planification des ressources et suivi de l'exécution des missions.")
    ]
    
    for poste, entreprise, periode, desc in exps:
        story.append(Paragraph(f"<b>{poste}</b> — <i>{entreprise}</i> ({periode})", body_style))
        story.append(Paragraph(f"• {desc}", body_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 6))

    # Formations
    story.append(Paragraph("DIPLÔMES & FORMATIONS", section_heading))
    forms = [
        ("2021", "Transport international des marchandises - CACI, Alger"),
        ("2020", "Planification et optimisation logistique - IIM, Bejaia"),
        ("2015", "Master 2 en Recherche Opérationnelle - Université de Bejaia"),
        ("2012", "Licence en Recherche Opérationnelle - Université de Bejaia")
    ]
    for annee, diplome in forms:
        story.append(Paragraph(f"<b>{annee}</b> : {diplome}", body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))

    # Compétences & Langues
    story.append(Paragraph("COMPÉTENCES & LANGUES", section_heading))
    story.append(Paragraph("<b>Compétences :</b> Pack Office, Matlab, LaTeX, Java, C++, Gestion Transport & Logistique, KPI.", body_style))
    story.append(Paragraph("<b>Langues :</b> Kabyle (Maternelle), Arabe (Excellent), Français (Bien), Anglais (Moyen).", body_style))

    # Génération effective du fichier PDF
    doc.build(story)

# RÉGÉNÉRATION SYSTÉMATIQUE À CHAQUE EXÉCUTION
generer_pdf(PDF_PATH)
