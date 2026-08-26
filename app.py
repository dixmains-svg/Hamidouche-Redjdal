import streamlit as st

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CV - Hamidouche Redjdal",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       PAGE
       ======================================================== */

    .stApp {
        background-color: #f4f7fb;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ========================================================
       HEADER
       ======================================================== */

    .header {
        background: linear-gradient(
            135deg,
            #0b1f3a 0%,
            #164f86 100%
        );

        padding: 45px;
        border-radius: 22px;

        color: white;

        margin-bottom: 30px;

        box-shadow:
            0 12px 30px rgba(0, 0, 0, 0.15);
    }

    .header-name {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }

    .header-title {
        font-size: 22px;
        font-weight: 500;
        margin-bottom: 10px;
    }

    .header-subtitle {
        font-size: 16px;
        line-height: 1.8;
        opacity: 0.95;
    }

    /* ========================================================
       TITRES
       ======================================================== */

    .section-title {
        color: #0b1f3a;

        font-size: 28px;

        font-weight: 800;

        border-bottom:
            3px solid #164f86;

        padding-bottom: 8px;

        margin-top: 30px;

        margin-bottom: 20px;
    }

    /* ========================================================
       CARDS
       ======================================================== */

    .card {
        background-color: white;

        padding: 24px;

        border-radius: 16px;

        margin-bottom: 18px;

        box-shadow:
            0 5px 18px rgba(0, 0, 0, 0.07);
    }

    .card-title {
        color: #0b1f3a;

        font-size: 20px;

        font-weight: 800;

        margin-bottom: 8px;
    }

    .card-subtitle {
        color: #164f86;

        font-weight: 700;

        margin-top: 5px;
    }

    /* ========================================================
       EXPERIENCE
       ======================================================== */

    .experience {
        background-color: white;

        padding: 25px;

        border-radius: 16px;

        border-left:
            6px solid #164f86;

        margin-bottom: 10px;

        box-shadow:
            0 5px 18px rgba(0, 0, 0, 0.07);
    }

    .experience-title {
        color: #0b1f3a;

        font-size: 21px;

        font-weight: 800;
    }

    .experience-company {
        color: #164f86;

        font-size: 16px;

        font-weight: 700;

        margin-top: 6px;
    }

    .experience-period {
        color: #777;

        font-size: 14px;

        margin-top: 6px;

        margin-bottom: 15px;
    }

    /* ========================================================
       TAGS
       ======================================================== */

    .tag {
        display: inline-block;

        background-color: #e8f1fa;

        color: #0b1f3a;

        padding: 8px 14px;

        border-radius: 20px;

        margin: 4px;

        font-size: 14px;

        font-weight: 600;
    }

    /* ========================================================
       COMPETENCES
       ======================================================== */

    .skill {
        background-color: white;

        padding: 16px;

        border-radius: 12px;

        margin-bottom: 12px;

        box-shadow:
            0 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* ========================================================
       TIMELINE
       ======================================================== */

    .timeline-year {
        display: inline-block;

        background-color: #0b1f3a;

        color: white;

        padding: 6px 14px;

        border-radius: 20px;

        font-weight: bold;

        margin-bottom: 10px;
    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;

        color: #777;

        padding-top: 40px;

        padding-bottom: 20px;

        font-size: 13px;
    }

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .header {
            padding: 28px;
        }

        .header-name {
            font-size: 30px;
        }

        .header-title {
            font-size: 18px;
        }

        .header-subtitle {
            font-size: 14px;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# INFORMATIONS PERSONNELLES
# ============================================================

nom = "HAMIDOUCHE REDJDAL"

fonction = "Planificateur & Superviseur Logistique"

telephone = "00213775 73 79 30"

email = "hamidoucheredjdal@yahoo.fr"

adresse = "Tazmalt 06039, wilaya de Bejaia"

nationalite = "Algérienne"

situation = "Marié"

service_national = "Dégagé"


# ============================================================
# PROFIL
# ============================================================

profil = """
Dynamique, sérieux et ayant de bonnes compétences relationnelles,
avec 9 ans d'expérience dans le domaine de la logistique.

Je suis très à l'aise avec les outils informatiques et j'aimerais
mettre mes compétences et ma motivation au service de votre entreprise.

Je suis prêt à relever le défi.
"""


# ============================================================
# EXPERIENCES PROFESSIONNELLES
# ============================================================

experiences = [

    {
        "poste": "Superviseur techno-commercial",
        "periode": "01/2024 - à ce jour",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Analyser les besoins des clients.",
            "Établir des reporting d'activité quotidiens, mensuels et annuels.",
            "Apporter des solutions pertinentes et adaptées.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage."
        ]
    },

    {
        "poste": "Superviseur exploitation",
        "periode": "06/2022 - 01/2024",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Piloter et superviser les opérations de transport.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage.",
            "Planifier, organiser et contrôler l'activité d'une équipe.",
            "Réceptionner les commandes des clients et veiller à leur satisfaction.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Chargé de la planification",
        "periode": "02/2020 - 06/2022",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Préparer la disponibilité des ressources humaines et matérielles.",
            "Planifier les commandes de chaque client.",
            "Élaborer les reportings et les KPI liés à l'activité.",
            "Réceptionner et traiter les demandes de service commercial.",
            "Optimiser les ressources logistiques en termes de coûts et de délais.",
            "Administrer et générer les ordres de mission.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Coordinateur logistique",
        "periode": "02/2019 - 02/2020",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Élaborer et maintenir une parfaite coordination avec les autres services.",
            "Élaborer et mettre en place des indicateurs de suivi de transport.",
            "Gérer les partenariats avec les prestataires de transport.",
            "Piloter et contrôler les performances des activités à court, moyen et long terme.",
            "Veiller au respect des procédures de travail et de la réglementation."
        ]
    },

    {
        "poste": "Chargé de la programmation",
        "periode": "04/2016 - 10/2018",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Exécuter et suivre régulièrement la programmation et l'utilisation des ressources.",
            "Établir un planning optimal en optimisant les coûts et les délais.",
            "Anticiper les situations imprévues et prendre rapidement les décisions correctives.",
            "Étudier la faisabilité d'une mission avant d'affecter les ressources."
        ]
    }

]


# ============================================================
# FORMATIONS
# ============================================================

formations = [

    {
        "annee": "2021",
        "titre": "Formation en Transport international des marchandises",
        "organisme": "Chambre algérienne de commerce et d'industrie, Alger - Algérie"
    },

    {
        "annee": "2020",
        "titre": "Formation en Planification et optimisation logistique",
        "organisme": "Institut international de Management, Bejaia - Algérie"
    },

    {
        "annee": "2019",
        "titre": "Formation en Logistique et transport",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2019",
        "titre": "Formation en Gestion des temps et des priorités",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2018",
        "titre": "Formation en Gestion des opérations de transport",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2015",
        "titre": "Master 2 en Recherche opérationnelle - Option : fiabilité et évaluation des Performances des Réseaux",
        "organisme": "Université Abderrahmane Mira, Bejaia - Algérie"
    },

    {
        "annee": "2012",
        "titre": "Licence en Recherche Opérationnelle - Option : Aide à la décision",
        "organisme": "Université Abderrahmane Mira, Bejaia - Algérie"
    },

    {
        "annee": "2012",
        "titre": "Attestation de stage en gestion portuaire",
        "organisme": "Entreprise portuaire de Bejaia, Bejaia - Algérie"
    },

    {
        "annee": "2008",
        "titre": "Diplôme Baccalauréat - Option : Science de la nature et de la vie",
        "organisme": "Lycée Mohamed Boudiaf, Tazmalt - Algérie"
    }

]


# ============================================================
# COMPETENCES
# ============================================================

competences = [

    "Pack Office : Excel, Word, PowerPoint, Outlook",

    "Matlab, LaTeX, Photoshop, Illustrator, InDesign",

    "HTML, Java, Delphi, C++",

    "Planification et optimisation logistique",

    "Gestion des opérations de transport",

    "Supervision des opérations de transport",

    "Gestion des ressources humaines et matérielles",

    "Élaboration des KPI et reporting",

    "Gestion des ordres de mission",

    "Optimisation des coûts et des délais",

    "Coordination entre les différents services",

    "Suivi des flux entrants et sortants"

]


# ============================================================
# LANGUES
# ============================================================

langues = [
    "Kabyle",
    "Arabe",
    "Français",
    "Anglais"
]


# ============================================================
# CENTRES D'INTERET
# ============================================================

interets = [
    ("✈️", "Voyage"),
    ("⚽", "Passion pour le sport"),
    ("🤝", "Activités associatives"),
    ("🎬", "Cinéma"),
    ("🎨", "Arts créatifs"),
    ("💻", "Informatique")
]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="header">

        <div class="header-name">
            HAMIDOUCHE REDJDAL
        </div>

        <div class="header-title">
            🚚 Planificateur & Superviseur Logistique
        </div>

        <div class="header-subtitle">

            Master 2 en Recherche Opérationnelle
            <br><br>

            Logistique &nbsp; • &nbsp;
            Transport &nbsp; • &nbsp;
            Planification &nbsp; • &nbsp;
            Supervision &nbsp; • &nbsp;
            Optimisation

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MENU
# ============================================================

st.sidebar.title("📄 MON CV")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Accueil",
        "👤 Profil",
        "💼 Expériences",
        "🎓 Formations",
        "🛠️ Compétences",
        "🌐 Langues",
        "⭐ Centres d'intérêt",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### 🚚 DOMAINES

    **Logistique**

    **Transport**

    **Planification**

    **Supervision**

    **Optimisation**
    """
)


# ============================================================
# ACCUEIL
# ============================================================

if menu == "🏠 Accueil":

    st.markdown(
        '<div class="section-title">👤 Présentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

            <p style="
                font-size:18px;
                line-height:1.9;
                text-align:justify;
            ">
                {profil}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # STATISTIQUES

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Expérience", "9 ans")

    with col2:
        st.metric("Expériences", "5")

    with col3:
        st.metric("Formations", "9")

    with col4:
        st.metric("Langues", "4")

    # DOMAINES

    st.markdown(
        '<div class="section-title">🎯 Domaines d’expertise</div>',
        unsafe_allow_html=True
    )

    domaines = [
        "Logistique",
        "Transport",
        "Planification",
        "Supervision",
        "Optimisation",
        "KPI & Reporting",
        "Gestion des ressources",
        "Ordres de mission",
        "Relation client"
    ]

    for domaine in domaines:

        st.markdown(
            f'<span class="tag">✓ {domaine}</span>',
            unsafe_allow_html=True
        )

    # POSTE ACTUEL

    st.markdown(
        '<div class="section-title">💼 Poste actuel</div>',
        unsafe_allow_html=True
    )

    dernier = experiences[0]

    st.markdown(
        f"""
        <div class="experience">

            <div class="experience-title">
                {dernier["poste"]}
            </div>

            <div class="experience-company">
                🏢 {dernier["entreprise"]}
            </div>

            <div class="experience-period">
                📅 {dernier["periode"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROFIL
# ============================================================

elif menu == "👤 Profil":

    st.markdown(
        '<div class="section-title">👤 Profil professionnel</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

            <p style="
                font-size:18px;
                line-height:2;
                text-align:justify;
            ">
                {profil}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📋 Informations personnelles</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    👤 Identité
                </div>

                <br>

                <b>Nom :</b>
                <p>{nom}</p>

                <b>🇩🇿 Nationalité :</b>
                <p>{nationalite}</p>

                <b>💍 Situation familiale :</b>
                <p>{situation}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    📋 Informations
                </div>

                <br>

                <b>📍 Adresse :</b>
                <p>{adresse}</p>

                <b>📋 Service national :</b>
                <p>{service_national}</p>

                <b>💼 Fonction :</b>
                <p>{fonction}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# EXPERIENCES
# ============================================================

elif menu == "💼 Expériences":

    st.markdown(
        '<div class="section-title">💼 Expériences professionnelles</div>',
        unsafe_allow_html=True
    )

    for index, experience in enumerate(experiences, start=1):

        st.markdown(
            f"""
            <div class="experience">

                <div class="experience-title">
                    {index}. {experience["poste"]}
                </div>

                <div class="experience-company">
                    🏢 {experience["entreprise"]}
                </div>

                <div class="experience-period">
                    📅 {experience["periode"]}
                </div>

                <b>Principales missions :</b>

            </div>
            """,
            unsafe_allow_html=True
        )

        for mission in experience["missions"]:

            st.markdown(
                f"✓ {mission}"
            )


# ============================================================
# FORMATIONS
# ============================================================

elif menu == "🎓 Formations":

    st.markdown(
        '<div class="section-title">🎓 Diplômes et formations</div>',
        unsafe_allow_html=True
    )

    for formation in formations:

        st.markdown(
            f"""
            <div class="card">

                <div class="timeline-year">
                    {formation["annee"]}
                </div>

                <div class="card-title">
                    {formation["titre"]}
                </div>

                <div class="card-subtitle">
                    🏫 {formation["organisme"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# COMPETENCES
# ============================================================

elif menu == "🛠️ Compétences":

    st.markdown(
        '<div class="section-title">🛠️ Compétences professionnelles</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for index, competence in enumerate(competences):

        if index % 2 == 0:

            with col1:

                st.markdown(
                    f"""
                    <div class="skill">
                        ✅ {competence}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            with col2:

                st.markdown(
                    f"""
                    <div class="skill">
                        ✅ {competence}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# LANGUES
# ============================================================

elif menu == "🌐 Langues":

    st.markdown(
        '<div class="section-title">🌐 Langues</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    for index, langue in enumerate(langues):

        with cols[index]:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">

                    <div style="
                        font-size:38px;
                        margin-bottom:10px;
                    ">
                        🌐
                    </div>

                    <div style="
                        font-size:20px;
                        font-weight:bold;
                        color:#0b1f3a;
                    ">
                        {langue}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "Les niveaux de maîtrise des langues ne sont pas précisés "
        "dans les informations fournies."
    )


# ============================================================
# CENTRES D'INTERET
# ============================================================

elif menu == "⭐ Centres d'intérêt":

    st.markdown(
        '<div class="section-title">⭐ Centres d’intérêt</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for index, (icone, interet) in enumerate(interets):

        with cols[index % 3]:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">

                    <div style="
                        font-size:40px;
                        margin-bottom:10px;
                    ">
                        {icone}
                    </div>

                    <div style="
                        font-size:17px;
                        font-weight:bold;
                        color:#0b1f3a;
                    ">
                        {interet}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# CONTACT
# ============================================================

elif menu == "📞 Contact":

    st.markdown(
        '<div class="section-title">📞 Contact</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    📱 Téléphone
                </div>

                <p>{telephone}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    📧 Email
                </div>

                <p>{email}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="card">

            <div class="card-title">
                📍 Adresse
            </div>

            <p>{adresse}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Curriculum Vitae • HAMIDOUCHE REDJDAL

        <br><br>

        Planification • Logistique • Transport • Supervision

    </div>
    """,
    unsafe_allow_html=True
)
