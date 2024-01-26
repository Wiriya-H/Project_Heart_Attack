import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./data/heart.xlsx')

html_0 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(df.head(10))

html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>The relationship between (sex) and (Sleep Disorder)</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

fig = plt.figure(figsize=(18, 15))
gs = fig.add_gridspec(3, 3)
gs.update(wspace=0.5, hspace=0.25)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[0, 2])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[1, 2])
ax6 = fig.add_subplot(gs[2, 0])
ax7 = fig.add_subplot(gs[2, 1])
ax8 = fig.add_subplot(gs[2, 2])

background_color = "#ffe6e6"
color_palette = ["#800000", "#8000ff", "#6aac90", "#5833ff", "#da8829"]
fig.patch.set_facecolor(background_color)
ax0.set_facecolor(background_color)
ax1.set_facecolor(background_color)
ax2.set_facecolor(background_color)
ax3.set_facecolor(background_color)
ax4.set_facecolor(background_color)
ax5.set_facecolor(background_color)
ax6.set_facecolor(background_color)
ax7.set_facecolor(background_color)
ax8.set_facecolor(background_color)

# Title of the plot
ax0.spines["bottom"].set_visible(False)
ax0.spines["left"].set_visible(False)
ax0.spines["top"].set_visible(False)
ax0.spines["right"].set_visible(False)
ax0.tick_params(left=False, bottom=False)
ax0.set_xticklabels([])
ax0.set_yticklabels([])
ax0.text(0.5, 0.5,
         'Count plot for various\n categorical features\n_________________',
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=18, fontweight='bold',
         fontfamily='serif',
         color="#000000")

# Function to create count plot using bar
def create_count_plot(ax, data, x, palette):
    ax.bar(data[x].value_counts().index, data[x].value_counts().values, color=palette)
    ax.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    ax.set_xlabel("")
    ax.set_ylabel("")

# Sex count
ax1.text(0.3, 165, 'Sex', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax1, df, 'sex', color_palette)
ax1.set_xticks([0, 1])
ax1.set_xticklabels(["Female(0)", "Male(1)"])

# Exng count
ax2.text(0.3, 160, 'Exng', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax2, df, 'exng', color_palette)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(["No(0)","Yes(1)"])

# Caa count
ax3.text(1.5, 120, 'Caa', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax3, df, 'caa', color_palette)
ax3.set_xticks([0, 1,2,3,4])


# Cp count
ax4.text(1.5, 120, 'Cp', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax4, df, 'cp', color_palette)
ax4.set_xticks([0,1,2,3])
ax4.set_xticklabels(["Typical angina(1)","Atypical angina(2)","nopain(3)","asymptomatic(4)"], rotation=15)

# Fbs count
ax5.text(0.5, 200, 'Fbs', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax5, df, 'fbs', color_palette)
ax5.set_xticks([0, 1])
ax5.set_xticklabels(["False(0)","True(1)"])

# Restecg count
ax6.text(0.75, 120, 'Restecg', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax6, df, 'restecg', color_palette)
ax6.set_xticks([0, 1,2])
ax6.set_xticklabels(["normal(0)","ST-T abnormality (1)","LV hypertrophy(2)"], rotation=15)

# Slp count
ax7.text(0.85, 120, 'Slp', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax7, df, 'slp', color_palette)
ax7.set_xticks([0, 1,2])

# Thall count
ax8.text(1.2, 120, 'Thall', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
create_count_plot(ax8, df, 'thall', color_palette)
ax8.set_xticks([0, 1, 2, 3])

# Remove spines
for s in ["top", "right", "left"]:
    ax1.spines[s].set_visible(False)
    ax2.spines[s].set_visible(False)
    ax3.spines[s].set_visible(False)
    ax4.spines[s].set_visible(False)
    ax5.spines[s].set_visible(False)
    ax6.spines[s].set_visible(False)
    ax7.spines[s].set_visible(False)
    ax8.spines[s].set_visible(False)


st.pyplot(fig)

html_2 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>The relationship between (Age) and (Sleep Disorder)</h3></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")



group_age = df.groupby(['Age', 'Sleep Disorder']).size().reset_index(name='count')
st.bar_chart(group_age, x='Age', y='count', color='Sleep Disorder', height=400)

html_3 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>The relationship between (BMI) and (Sleep Disorder)</h3></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})
fig, ax = plt.subplots(figsize=(20, 10))
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=['#FF9EAA', '#FFD0D0', '#5CD2E6', '#3085C3'])
plt.axis('equal') 
st.pyplot(fig)

html_4 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>The relationship between (Occupation) and (Sleep Disorder)</h3></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
st.markdown("")
group_age = df.groupby(['Occupation', 'Sleep Disorder']).size().reset_index(name='count')
st.bar_chart(group_age, x='Occupation', y='count', color='Sleep Disorder', height=400)