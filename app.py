import streamlit as st

# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================
st.set_page_config(
    page_title="CV - Brahim Terki",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SELECTION DE LA LANGUE DANS LA SIDEBAR
# ============================================================
langue = st.sidebar.selectbox(
    "🌐 Langue / Language",
    ["Français", "English"]
)

# ============================================================
# DICTIONNAIRE MULTILINGUE
# ============================================================
TEXTES = {
    "Français": {
        "nav": [
            "🏠 Accueil", "👤 Profil", "💼 Expériences", 
            "🎓 Diplômes & Formations", "🛠️ Compétences", 
            "🌐 Langues", "⭐ Centres d'intérêt", "📞 Contact"
        ],
        "titre_poste": "Planificateur et Superviseur Logistique",
        "profil_court": (
            "Dynamique, sérieux et ayant de bonnes compétences relationnelles, "
            "avec 9 ans d'expérience dans le domaine de la logistique. "
            "Très à l'aise avec les outils informatiques, je souhaite mettre "
            "mes compétences et ma motivation au service d'une entreprise "
            "et relever de nouveaux défis professionnels."
        ),
        "stat_exp": "Expérience",
        "stat_exp_val": "9 ans",
        "stat_postes": "Postes",
        "stat_dip": "Formations",
        "stat_langues": "Langues",
        "experience_actuelle": "Poste Actuel",
        "actuel_periode": "01/2024 - À ce jour",
        "competences_techniques": "Compétences Techniques",
        "competences_orga": "Compétences Organisationnelles",
        "certifications": "Certifications & Attestations",
        "activites": "Activités sportives & bénévolat",
        "contact_prompt": "N'hésitez pas à me contacter pour toute opportunité !",
        "exp_list": [
            {
                "titre": "Planificateur et Superviseur Logistique",
                "entreprise": "Entreprise Agroalimentaire",
                "periode": "01/2024 - À ce jour",
                "lieu": "Béjaïa, Algérie",
                "taches": [
                    "Planification et suivi des approvisionnements et livraisons.",
                    "Gestion et optimisation de la flotte de transport.",
                    "Supervision des équipes logistiques et gestion des stocks."
                ]
            },
            {
                "titre": "Responsable de Stock et Distribution",
                "entreprise": "Société de Distribution",
                "periode": "06/2019 - 12/2023",
                "lieu": "Béjaïa, Algérie",
                "taches": [
                    "Supervision du magasinage et contrôle de l'inventaire.",
                    "Coordination avec l'équipe commerciale pour les commandes prioritaires."
                ]
            }
        ],
        "form_list": [
            {"annee": "2023", "diplome": "Attestation en Gestion des Stocks & ERP"},
            {"annee": "2018", "diplome": "Diplôme en Logistique et Transport"},
            {"annee": "2015", "diplome": "Baccalauréat"}
        ],
        "langues_list": [
            {"nom": "Arabe", "niveau": "Langue maternelle / Native"},
            {"nom": "Kabyle", "niveau": "Langue maternelle / Native"},
            {"nom": "Français", "niveau": "Courant / Fluent"},
            {"nom": "Anglais", "niveau": "Intermédiaire / Intermediate"}
        ]
    },
    "English": {
        "nav": [
            "🏠 Home", "👤 Profile", "💼 Experience", 
            "🎓 Education & Training", "🛠️ Skills", 
            "🌐 Languages", "⭐ Interests", "📞 Contact"
        ],
        "titre_poste": "Logistics Planner & Supervisor",
        "profil_court": (
            "Dynamic, reliable, and possessing strong interpersonal skills, "
            "with 9 years of experience in the logistics field. "
            "Highly proficient with IT tools, I aim to apply my skills and motivation "
            "to serve a growing company and take on new professional challenges."
        ),
        "stat_exp": "Experience",
        "stat_exp_val": "9 years",
        "stat_postes": "Positions",
        "stat_dip": "Education",
        "stat_langues": "Languages",
        "experience_actuelle": "Current Position",
        "actuel_periode": "01/2024 - Present",
        "competences_techniques": "Technical Skills",
        "competences_orga": "Organizational Skills",
        "certifications": "Certifications & Training",
        "activites": "Sports & Volunteer Activities",
        "contact_prompt": "Feel free to reach out for any opportunities!",
        "exp_list": [
            {
                "titre": "Logistics Planner & Supervisor",
                "entreprise": "Agro-industrial Company",
                "periode": "01/2024 - Present",
                "lieu": "Béjaïa, Algeria",
                "taches": [
                    "Planning and tracking supplies and deliveries.",
                    "Fleet management and route optimization.",
                    "Supervising logistics teams and inventory management."
                ]
            },
            {
                "titre": "Stock & Distribution Manager",
                "entreprise": "Distribution Company",
                "periode": "06/2019 - 12/2023",
                "lieu": "Béjaïa, Algeria",
                "taches": [
                    "Warehousing supervision and inventory control.",
                    "Coordination with sales team for priority shipments."
                ]
            }
        ],
        "form_list": [
            {"annee": "2023", "diplome": "Certificate in Stock Management & ERP"},
            {"annee": "2018", "diplome": "Diploma in Logistics & Transport"},
            {"annee": "2015", "diplome": "High School Diploma (Baccalaureate)"}
        ],
        "langues_list": [
            {"nom": "Arabic", "niveau": "Native"},
            {"nom": "Kabyle", "niveau": "Native"},
            {"nom": "French", "niveau": "Fluent"},
            {"nom": "English", "niveau": "Intermediate"}
        ]
    }
}

# Variable raccourci vers les données de la langue choisie
t = TEXTES[langue]

# ============================================================
# STYLES CSS PERSONNALISÉS
# ============================================================
st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.2rem; color: #4B5563; font-weight: 500; margin-bottom: 1.5rem; }
    .section-title { font-size: 1.4rem; font-weight: 600; color: #1E3A8A; border-bottom: 2px solid #E5E7EB; padding-bottom: 0.3rem; margin-top: 1rem; margin-bottom: 1rem; }
    .card { background-color: #F9FAFB; padding: 1.2rem; border-radius: 8px; border-left: 4px solid #1E3A8A; margin-bottom: 1rem; }
    .card-title { font-size: 1.1rem; font-weight: 600; color: #1F2937; }
    .card-sub { font-size: 0.9rem; color: #6B7280; font-style: italic; margin-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION MENU LATÉRAL
# ============================================================
st.sidebar.markdown("---")
page = st.sidebar.radio("NAVIGATION", t["nav"])

# Header fixe haut de page
st.markdown("<div class='main-title'>Brahim TERKI</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-title'>{t['titre_poste']}</div>", unsafe_allow_html=True)

# ============================================================
# PAGES DE L'APPLICATION
# ============================================================

# --- ACCUEIL ---
if page in ["🏠 Accueil", "🏠 Home"]:
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        # Remplacer par st.image("photo.jpg") si vous avez une photo locale
        st.info("📷 Photo de profil")
        
    with col_info:
        st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
        st.write(t["profil_court"])
        
    st.markdown("---")
    
    # Indicateurs clés
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(t["stat_exp"], t["stat_exp_val"])
    c2.metric(t["stat_postes"], len(t["exp_list"]))
    c3.metric(t["stat_dip"], len(t["form_list"]))
    c4.metric(t["stat_langues"], len(t["langues_list"]))

# --- PROFIL ---
elif page in ["👤 Profil", "👤 Profile"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <p>{t['profil_court']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- EXPÉRIENCES ---
elif page in ["💼 Expériences", "💼 Experience"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    
    for exp in t["exp_list"]:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{exp['titre']}</div>
            <div class="card-sub">{exp['entreprise']} | {exp['periode']} | {exp['lieu']}</div>
        </div>
        """, unsafe_allow_html=True)
        for tache in exp["taches"]:
            st.write(f"- {tache}")
        st.write("")

# --- DIPLÔMES & FORMATIONS ---
elif page in ["🎓 Diplômes & Formations", "🎓 Education & Training"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    
    for item in t["form_list"]:
        st.markdown(f"**{item['annee']}** : {item['diplome']}")

# --- COMPÉTENCES ---
elif page in ["🛠️ Compétences", "🛠️ Skills"]:
    st.markdown(f"<div class='section-title'>{t['competences_techniques']}</div>", unsafe_allow_html=True)
    st.progress(0.90, text="Gestion des stocks & Approvisionnements (90%)")
    st.progress(0.85, text="Planification & Supervision Flotte (85%)")
    st.progress(0.80, text="Outils Informatiques / ERP / Excel (80%)")
    
    st.markdown(f"<div class='section-title'>{t['competences_orga']}</div>", unsafe_allow_html=True)
    st.write("✔️ Gestion d'équipe & Leadership")
    st.write("✔️ Sens de la communication & Relationnel")
    st.write("✔️ Rigueur & Organisation")

# --- LANGUES ---
elif page in ["🌐 Langues", "🌐 Languages"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    for lang in t["langues_list"]:
        st.write(f"• **{lang['nom']}** : {lang['niveau']}")

# --- CENTRES D'INTÉRÊT ---
elif page in ["⭐ Centres d'intérêt", "⭐ Interests"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    st.write("⚽ Sports d'équipe")
    st.write("📚 Lecture & Veille technologique")
    st.write("🚗 Voyages")

# --- CONTACT ---
elif page in ["📞 Contact"]:
    st.markdown(f"<div class='section-title'>{page}</div>", unsafe_allow_html=True)
    st.info(t["contact_prompt"])
    st.write("📧 **Email** : brahim.terki@example.com")
    st.write("📱 **Téléphone** : +213 X XX XX XX XX")
    st.write("📍 **Adresse** : Béjaïa, Algérie")
