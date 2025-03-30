import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

page_bg_color = """
<style>
/* تغيير خلفية التطبيق بالكامل */
[data-testid="stAppViewContainer"] {
background-color: #1e1e1e; /* لون داكن */
}
/* تغيير لون الشريط الجانبي */
[data-testid="stSidebar"] {background-color: #333333; /* لون أغمق */}

/* تغيير لون العناوين */
h1, h2, h3, h4, h5, h6 {color: #FF6500;}

/* تغيير لون Selectbox */
select {background-color: #444444 !important; /* لون داكن */
color: #FF6500 !important; /* لون النص */
border-radius: 5px !important; /* تدوير الحواف */
padding: 5px !important;}

/* تغيير لون الأزرار */
button {background-color: #3C3D37 !important; /* لون أزرق */
color: #FF6500 !important; /* لون النص داخل الزر */
border-radius: 10px !important; /* تدوير الحواف */
}
/* تغيير لون النص */
body, p, div {color: #FF6500;}

/* تغيير لون الشريط العلوي */
header {background-color: #1e1e1e !important; /* لون داكن */}
/* إخفاء الخط العلوي الأحمر */
[data-testid="stHeader"] {background-color: #1e1e1e !important;}

/* تغيير لون خلفية القائمة المنسدلة */
div[data-testid="stSelectbox"] div[role="combobox"] {
background-color: black !important; /* الخلفية سوداء */
color: white !important; /* النص أبيض */
border-radius: 5px !important; /* تدوير الحواف */
padding: 5px !important;
}

/* تغيير لون العناصر داخل القائمة المنسدلة */
div[data-testid="stSelectbox"] div[data-testid="stDropdownContainer"] {
background-color: black !important; /* الخلفية سوداء */
color: white !important; /* النص أبيض */
}

/* تغيير لون العناصر عند التحديد */
div[data-testid="stSelectbox"] div[data-testid="stDropdownContainer"] div {
background-color: black !important;
color: white !important;
}


</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

def main_page():


    st.title("skills analsis")
    df = pd.read_csv('skill_counts.csv', encoding='ISO-8859-1')


    num_skills = st.sidebar.slider('Select the number of skills to display', min_value=1, max_value=50, value=20)

    if st.sidebar.button('Check'):

        skill_counts_top = df.head(num_skills)
        
        plt.figure(figsize=(10, 5))
        skill_counts_top.set_index('skill', inplace=True)
        colors = sns.color_palette("Oranges", num_skills)
        colors = list(reversed(sns.color_palette("Oranges", num_skills)))
        ax = plt.gca()
        plt.gca().set_facecolor('#1e1e1e') 
        fig = plt.gcf()
        fig.patch.set_facecolor('#1e1e1e')
        skill_counts_top['count'].plot(kind='bar', title=f'Top {num_skills} Skills', color=colors)
        plt.xlabel('Skill')
        plt.ylabel('Count')
        plt.xticks(rotation=90)

        st.pyplot(plt)

def second_page():
    st.title("Governorates Analysis")


    colors = sns.color_palette("Oranges", 10)
    main_color = colors[5]

    df2 = pd.read_csv('test.csv', encoding='ISO-8859-1')
    governorate = df2['governorate'].unique()
    governorates = st.selectbox('Select the Governorates', governorate)

    col1, col2 = st.columns(2)
    filtered_df = df2[df2['governorate'] == governorates]

    with col1:

        plt.figure(figsize=(20, 12))
        ax = plt.gca()
        plt.gca().set_facecolor('#1e1e1e')
        fig = plt.gcf()
        fig.patch.set_facecolor('#1e1e1e')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.title.set_color('white')
        get_top_10_companies_by_average_experience = (filtered_df.groupby('company_name')['Average_Experience'].mean().sort_values(ascending=False).head(10))

        colors_exp = sns.color_palette("Oranges", len(get_top_10_companies_by_average_experience))[::-1]
        
        get_top_10_companies_by_average_experience.plot(kind='bar', title='Top 10 Companies by Average Experience',color=colors_exp)
        st.pyplot(plt)


        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_facecolor('#1e1e1e')
        fig.patch.set_facecolor('#1e1e1e')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.title.set_color('white')
        filtered_df.plot(kind='scatter', x='min_experience', y='max_experience', s=32, alpha=0.8, color=main_color, ax=ax)

        ax.spines[['top', 'right']].set_visible(False)
        st.pyplot(fig)


    with col2:

        plt.figure(figsize=(12, 6))
        ax = plt.gca()
        plt.gca().set_facecolor('#1e1e1e')
        fig = plt.gcf()
        fig.patch.set_facecolor('#1e1e1e')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.title.set_color('white')
        exp_counts = filtered_df['Experience'].value_counts()
        colors_exp_dist = list(reversed(sns.color_palette("Oranges", len(exp_counts))))
        
        exp_counts.plot(kind='bar', title=f'Experience Distribution in {governorates}',color=colors_exp_dist)
        st.pyplot(plt)

        plt.figure(figsize=(12, 6))
        ax = plt.gca()
        plt.gca().set_facecolor('#1e1e1e')
        fig = plt.gcf()
        fig.patch.set_facecolor('#1e1e1e')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.title.set_color('white')
        top_ten_companies = filtered_df['company_name'].value_counts().head(10)
        colors_top_companies = list(reversed(sns.color_palette("Oranges", len(exp_counts))))
        
        top_ten_companies.plot(kind='bar', title='Top 10 Companies',color=colors_top_companies)
        st.pyplot(plt)
    filtered_df1 = filtered_df.drop(columns=['location', 'skills','min_experience','max_experience','Average_Experience'])
    styled_df = filtered_df1.style.set_properties(
        **{
            'background-color': '#1e1e1e', 
            'color': '#FF6500',  
            'border-color': '#1e1e1e' 
        }
    ).set_table_styles(
        [
            {"selector": "thead th", "props": [("background-color", "#333"), ("color", "white"), ("font-size", "14px"), ("text-align", "center")]}
        ]
    ).hide(axis="index")


    table_style = """
        <style>
        table { margin-left: auto; margin-right: auto; width: 80%; }
        th, td { text-align: center; padding: 10px; }
        </style>
    """
    st.markdown(table_style, unsafe_allow_html=True)
    st.write(styled_df.to_html(), unsafe_allow_html=True)

page = st.sidebar.selectbox("Select the type of analysis", ["skills analysis", "Governorates analysis"])

if page == "skills analysis":
    main_page()
else:
    second_page()
