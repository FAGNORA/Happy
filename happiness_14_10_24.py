import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os


# CSS pour réduire l'espace en haut de la page
st.markdown(
    """
    <style>
    /* Réduire l'espace vide au sommet de la page */
    .main .block-container {
        padding-top: 0rem;  /* Ajuster la valeur pour personnaliser */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Définition de variable
# 1- Images
# Définition de variable
# 1- Images
logo_WHR = Image.open('WHR.gif')
image_Panneau= Image.open('photo test.gif')
Logo_internet = Image.open('Internet.jpeg')
bonheur= Image.open('Bonheur.gif')
bandeau= Image.open('bandeau.jpeg')

#2 - Daframe

#df=pd.read_csv("world-happiness-report.csv")
#df_2021=pd.read_csv("world-happiness-report-2021.csv")
#df_global = pd.read_csv("C:/Users/fatim/Documents/df_global.csv")
# Charger les fichiers CSV depuis GitHub
# Charger les fichiers CSV depuis GitHub
df = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/world-happiness-report.csv")
df_2021 = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/world-happiness-report-2021.csv")
df_global = pd.read_csv("https://raw.githubusercontent.com/FAGNORA/Hapiness_World_Report/main/df_global.csv")
# **************************************************************Création des pages et des titres************************
pages=["Introduction","Exploration", "DataVisualization", "Pré Processing", "Modélisation", "Conclusion"]
#***************************************************************** Sidebar***********************************************

# CSS pour réduire l'espace vide en haut de la sidebar
st.markdown(
    """
    <style>
    /* Réduire l'espace vide en haut de la sidebar */
    .css-1d391kg {  /* Classe qui gère le conteneur de la sidebar */
        padding-top: 0rem;  /* Ajuster cette valeur pour changer l'espace */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    f"""
    <div style="
        #border: 2px solid #b80691; 
        #padding: 0px; 
        #border-radius: 50px;
        #background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:#262730;font-size:30px">Sommaire</h3>
    """, unsafe_allow_html=True)
st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
                    
new_image = logo_WHR.resize((150, 150))
st.sidebar.image(new_image)

 #Ajouter un lien
st.sidebar.markdown('[Lien vers le site du World Happiness Report](https://www.worldhappiness.report)')

page=st.sidebar.radio("Aller vers", pages)
#Cette partie met en forme la barre du coté
st.markdown("""
       <style>
         section[data-testid="stSidebar"] 
              {background-color: #faca2b;}
       </style>""", unsafe_allow_html=True) 
#Cette partie met en forme la barre du coté


# Texte à afficher
text = """
<span style="color:purple;">**Promotion Data-Analyst - Février 2024**<span>

"""

# Injection de CSS pour créer un encadré autour du texte
st.sidebar.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 10px; 
        border-radius: 25px;
        background-color: #f5b74c;
        text-align:center;">
        {text}
    """,
    unsafe_allow_html=True)

# *********************************************************************************************Début de la page d'Introduction###########
if page == pages[0] : 
    new_image = bandeau.resize((1200, 600))
    st.image(new_image)

    st.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>
    """, unsafe_allow_html=True)

# Titre principal pour l'introduction
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Contexte</h3>', unsafe_allow_html=True)
    st.markdown("""
         <p style="text-align: justify;font-size:15px;">
         Le World Happiness Report est une publication annuelle élaborée par les Nations Unies, qui mesure et analyse le bonheur et le bien-être dans le monde entier.
         Ce rapport fournit une évaluation comparative du bonheur dans différents pays en s'appuyant sur des enquêtes menées auprès de populations diverses. 
         Les résultats du rapport sont basés sur des indicateurs clés tels que la satisfaction de vie, le soutien social, les libertés personnelles, 
         et la perception de la corruption, parmi d'autres facteurs.
         Le World Happiness Report a pour objectif principal de mieux comprendre les facteurs qui contribuent au bien-être des individus et des sociétés. 
         En évaluant les niveaux de bonheur à l'échelle mondiale, il permet d'identifier les tendances, les défis et les opportunités pour améliorer la qualité de vie. 
         Ce rapport est une ressource précieuse pour les décideurs politiques, les chercheurs, et les organisations internationales, 
         offrant des insights qui peuvent guider les politiques publiques et les initiatives en faveur du bien-être humain.
         </p>
     """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Objectifs </h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        À travers ce projet, nous visons à explorer et analyser les éléments factuels disponibles concernant le bien-être et le bonheur à l’échelle mondiale. 
        Sans nécessiter de connaissances préalables spécifiques en psychologie ou en sociologie, notre objectif est de rendre accessibles à un public curieux et non spécialisé des analyses basées sur des données fiables et librement accessibles.
        Nous répondrons aux problématiques suivantes :
        Les données disponibles permettent-elles de confirmer les variations dans les niveaux de bonheur à travers les pays ? Quels sont les indicateurs clés de ces variations ?
        Quel est le degré de corrélation entre les facteurs socio-économiques, culturels et les niveaux de bonheur reportés par les citoyens ?
        Quelles sont les tendances et les prédictions pour les niveaux de bonheur dans les décennies à venir ?
        </p>
    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Classification du problème </h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Ces questions de recherche nous amèneront à utiliser la plupart des compétences acquises au cours de notre formation :
        Grâce aux outils de Data Analyse et de Dataviz, nous allons déplacer, explorer, nettoyer, fusionner, visualiser et analyser les données disponibles.
        Les tests statistiques, ainsi que les régressions linéaires et polynomiales, nous permettront d’établir et d’analyser les corrélations entre les divers facteurs et les niveaux de bonheur.
        Grâce au machine learning, nous construirons un modèle prédictif des tendances futures du bonheur à travers les différentes régions.
        Enfin, un travail de recherche approfondi sera réalisé pour vérifier l’adéquation de nos résultats avec les études et les rapports existants.
        </p>
    """, unsafe_allow_html=True)


# Fin de la page d'Introduction#############

# zz redimensionnser une Image
#new_image = logo_WHR.resize((200, 200))
#st.image(new_image)
# zz

#****************************************************************************   Fin de la page d'Introduction  ***************


# ___________________________________________________________________________   Début de la page Exploration   ________________

if page == pages[1] : 
    st.markdown(
    f"""
    <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Analyse World Hapiness Report de 2005 à 2021</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)
# traitement des données

    #st.markdown('<h3 style="color:blue;">LES DONNEES</h3>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;">Source de nos données</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Les données sont accessibles sur Kaggle en accès libre,
        
        </p>
    """, unsafe_allow_html=True)

# Ajouter un lien
    st.markdown('[Accédez aux données du World Happiness Dataset sur Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness)')
    st.markdown('<h3 style="color:purple;">Présentation des données</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        world-happiness-report.csv regroupant les données d’un panel d'années de (2005 – 
        2020). 
        Le fichier world-happiness-report-2021.csv, contenant des données collectées pour 
        le Happiness Report pour l’année 2021.
        </p>
    """, unsafe_allow_html=True)

    #compteurs de lignes des tableaux pour les inserer dans le descriptif
    Nb_lignes,Nb_colonnes = df.shape
    Nb_lignes2021,Nb_colonnes2021 = df_2021.shape

    Intro_tableau = 'Veuillez choisir le Dataframe pour afficher les détails : '

    Tableau_1 = 'Fichier contenant les données entre 2005 à 2020'
    Tableau_2 = 'Fichier contenant les données de 2021'
    Tableaux = st.radio( Intro_tableau, (Tableau_1,Tableau_2))

    if Tableaux == Tableau_1 : 
   
   
        st.markdown('<h3 style="color:purple;"></h3>', unsafe_allow_html=True)
        st.markdown('<h5 style="color:purple;text-align:center;">world-happiness-report.csv</h5>', unsafe_allow_html=True)

        st.markdown(
    """
    Détail des colonnes du fichier contenant les données collectées sur la **période 2005 à 2020**.
    """
    )
        st.markdown(f"Le fichier contient {Nb_lignes} lignes et {Nb_colonnes} colonnes")
          
        st.write(
    """    
    | Titre des colonnes                | Type         | Présence de valeurs nulles | Explication de la donnée                                                                 |
    |-----------------------------------|--------------|----------------------------|------------------------------------------------------------------------------------------|
    | Country name                      | Objet         | Aucune valeur vide          | Nom du pays où les mesures ont été relevées.                                             |
    | Year                              | Chiffre entier| Aucune valeur vide          | Année durant laquelle la mesure a été réalisée.                                          |
    | Life ladder                       | Numérique     | Aucune valeur vide          | Mesure du bonheur sur une échelle allant de 0 à 10, moyenne des réponses obtenues.       |
    | Log GDP per capita                | Numérique     | 36 valeurs vides            | Mesure de la richesse produite par habitant ou PIB/habitant.                             |
    | Social support                    | Numérique     | 13 valeurs vides            | Mesure de l'assistance sociale. Indicateur de soutien en cas de difficulté.              |
    | Healthy life expectancy           | Numérique     | 55 valeurs vides            | Mesure de l'espérance de vie d'une personne dès la naissance.                            |
    | Freedom to make life choices      | Numérique     | 32 valeurs vides            | Mesure de la capacité à faire ses propres choix de vie.                                   |
    | Generosity                        | Numérique     | 89 valeurs vides            | Mesure de la générosité, ex : don effectué à un organisme de bienfaisance.                |
    | Perceptions of corruption         | Numérique     | 110 valeurs vides           | Mesure de la manière dont la corruption est perçue.                                      |
    | Positive affect                   | Numérique     | 22 valeurs vides            | Impact positif.                                                                         |
    | Negative affect                   | Numérique     | 16 valeurs vides            | Impact négatif.                                                                         |
    """
    )

    elif Tableaux == Tableau_2 : 

        st.markdown('<h3 style="color:purple;"></h3>', unsafe_allow_html=True)
        st.markdown('<h5 style="color:purple;text-align:center;">world-happiness-report-2021.csv</h5>', unsafe_allow_html=True)

    # Description des fichiers CSV
    #st.header('Contenu des fichiers')
    #st.subheader('world-happiness-report.csv')
    #st.subheader('world-happiness-report-2021.csv')
        st.markdown(
    """
    Détail des colonnes du fichier contenant les données collectées sur **l'année 2021** :
        """
    )
        st.markdown(f"Le fichier contient {Nb_lignes2021} lignes et {Nb_colonnes2021} colonnes")
       
        st.write(
    """   
    | Titre des colonnes                | Type         | Présence de valeurs nulles | Explication de la donnée                                                                 |
    |---------------------------------- |--------------|----------------------------|------------------------------------------------------------------------------------------|
    | Country name                      | Objet         | Aucune valeur vide          | Nom du pays.                                                                            |
    | Regional indicator                | Objet         | Aucune valeur vide          | Indicateur régional, zone géographique.                                                 |
    | Ladder score                      | Numérique     | Aucune valeur vide          | Mesure du bonheur sur un score d'échelle de 0 à 10.                                      |
    | Standard error of ladder score    | Numérique     | Aucune valeur vide          | Mesure de l'erreur type du score d'échelle.                                              |
    | Upperwhisker                      | Numérique     | Aucune valeur vide          | Limites supérieures de la distribution des scores du bonheur.                            |
    | Lowerwhisker                      | Numérique     | Aucune valeur vide          | Limites inférieures de la distribution des scores du bonheur.                            |
    | Logged GDP per capita             | Numérique     | Aucune valeur vide          | Mesure de PIB enregistré par habitant.                                                   |
    | Social support                    | Numérique     | Aucune valeur vide          | Mesure de l'aide, l'assistance sociale.                                                 |
    | Healthy life expectancy           | Numérique     | Aucune valeur vide          | Mesure de l'espérance de vie en bonne santé.                                            |
    | Freedom to make life choices      | Numérique     | Aucune valeur vide          | Mesure de la liberté de faire des choix de vie.                                          |
    | Generosity                        | Numérique     | Aucune valeur vide          | Mesure de la générosité.                                                                 |
    | Perceptions of corruption         | Numérique     | Aucune valeur vide          | Mesure de la perception de la corruption.                                                |
    | Ladder score in Dystopia          | Numérique     | Aucune valeur vide          | Mesure du bonheur sur un score d'échelle dans la Dystopie.                               |
    | Explained by: Log GDP per capita  | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par le PIB par habitant.                                       |
    | Explained by: Social support      | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par l'aide sociale par habitant.                               |
    | Explained by: Healthy life expectancy | Numérique | Aucune valeur vide          | Score du bonheur expliqué par l'espérance de vie.                                        |
    | Explained by: Freedom to make life choices | Numérique | Aucune valeur vide       | Score du bonheur expliqué par la liberté de faire des choix de vie.                      |
    | Explained by: Generosity          | Numérique     | Aucune valeur vide          | Score du bonheur expliqué par la générosité.                                             |
    | Explained by: Perceptions of corruption | Numérique | Aucune valeur vide        | Score du bonheur expliqué par la perception de la corruption.                            |
    | Dystopia + residual               | Numérique     | Aucune valeur vide          | La perception du bonheur dans la Dystopie.                                               |
    """
    )

    st.text("")
    st.text("")
    st.markdown("""
        <p style="text-align: justify;font-size:15px;">
        Visualiser les données des deux DataFrame 
        </p>
    """, unsafe_allow_html=True)

    st.button("Reset", type="primary")
    if st.button("Données de 2005 à 2020"):
        st.dataframe(df)
    elif st.button("Données de 2021"): 
        st.dataframe(df_2021)
    else : st.text("Aucun dataframe de choisi")
# ___________________________________________________________________________   Fin de la page Exploration     __________________


#  ....................................................................................  Fin de la page Modélisation  ..........................................
#                                                                                        Debut de la CONCLUSION
if page == pages[4] : 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Conclusion</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)


    # Conclusion
    st.markdown('<h3 style="color:purple;">Peut-on prédire le bonheur ?</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    L'exclusion des variables 'Country Name' et 'Regional Indicator' a conduit à une dégradation 
    des performances des deux modèles, suggérant que ces variables apportaient des informations 
    importantes pour prédire la variable cible. Il est donc recommandé de conserver les variables 
    'Country name' et 'Regional indicator' dans les modèles, sauf si une simplification est impérative 
    pour d'autres raisons (comme la réduction du temps de calcul ou la simplification du modèle).
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h3 style="color:purple;">Pour conclure sur cette partie</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    En conclusion, bien que l'exclusion de variables puisse parfois simplifier le modèle, dans ce 
    cas particulier, ces variables semblent contenir des informations cruciales pour la 
    prédiction du bonheur. Il serait judicieux d'explorer davantage pourquoi ces variables sont 
    importantes et de considérer des techniques alternatives pour gérer leur impact sur le modèle tout 
    en maximisant la précision des prédictions. En ce qui concerne les métriques, la RMSE est recommandée 
    pour évaluer la précision des prédictions du bonheur. Le Modèle le Plus Performant est le Random Forest, 
    surtout lorsque les variables 'Country name' et 'Regional indicator' sont incluses. Il a des scores de 
    MSE, MAE, R², et RMSE meilleurs comparés à Gradient Boosting.
    </p>
    """, unsafe_allow_html=True)

    # Affichage de l'image
    new_image = bonheur.resize((1500, 1500))
    st.image(new_image, caption='Analyse du Bonheur', use_column_width=True)
    #                                                                                        Debut de la CONCLUSION
if page == pages[5] : 
    st.markdown(
        f"""
        <div style="
        border: 2px solid #b80691; 
        padding: 0px; 
        border-radius: 50px;
        background-color: #f5b74c;
        text-align:center;">
        <h3 style="color:purple;font-size:30px">Conclusion</h3>

    """, unsafe_allow_html=True)
    st.markdown('<h3 style="color:purple;"> </h3>', unsafe_allow_html=True)


    # Conclusion
    st.markdown('<h3 style="color:purple;">Peut-on prédire le bonheur ?</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    L'exclusion des variables 'Country Name' et 'Regional Indicator' a conduit à une dégradation 
    des performances des deux modèles, suggérant que ces variables apportaient des informations 
    importantes pour prédire la variable cible. Il est donc recommandé de conserver les variables 
    'Country name' et 'Regional indicator' dans les modèles, sauf si une simplification est impérative 
    pour d'autres raisons (comme la réduction du temps de calcul ou la simplification du modèle).
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h3 style="color:purple;">Pour conclure sur cette partie</h3>', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: justify; font-size:15px;">
    En conclusion, bien que l'exclusion de variables puisse parfois simplifier le modèle, dans ce 
    cas particulier, ces variables semblent contenir des informations cruciales pour la 
    prédiction du bonheur. Il serait judicieux d'explorer davantage pourquoi ces variables sont 
    importantes et de considérer des techniques alternatives pour gérer leur impact sur le modèle tout 
    en maximisant la précision des prédictions. En ce qui concerne les métriques, la RMSE est recommandée 
    pour évaluer la précision des prédictions du bonheur. Le Modèle le Plus Performant est le Random Forest, 
    surtout lorsque les variables 'Country name' et 'Regional indicator' sont incluses. Il a des scores de 
    MSE, MAE, R², et RMSE meilleurs comparés à Gradient Boosting.
    </p>
    """, unsafe_allow_html=True)

    # Affichage de l'image
    new_image = bonheur.resize((1500, 1500))
    st.image(new_image, caption='Analyse du Bonheur', use_column_width=True)

