import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col1, col2, col3 = st.columns([1.5, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./pic/home.png")

with col3:
    st.write("")


html_1 = """
<div style="background-color:#0E1117;margin-top:40px;padding:5px;border-radius:5px;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h4 style ="filter: drop-shadow(0px 0px 5px #89c5fb);">ระบบวิเคราะห์สุขภาพการนอนหลับและไลฟ์สไตล์โดยใช้เทคนิคเหมืองข้อมูล</h4><h5  style ="filter: drop-shadow(0px 0px 5px #89c5fb);">The system analyzes health, sleep and lifestyle using data mining techniques</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

html_2 = """
<div style="background-color:#0E1117;padding:15px;">
<center></center><left><h6 style="text-indent: 30px;line-height: 1.5;">การรักษาสุขภาพการนอนมีความสำคัญสำหรับความเป็นอยู่ของบุคคลทั้งทางร่างกายและจิตใจทุกวัย การนอนไม่เพียงเติมพลังให้ร่างกายและสมองเท่านั้น แต่ยังมีผลที่สำคัญต่อระบบฮอร์โมน การฟื้นตัวของร่างกาย และส่งเสริมสุขภาพจิตใจด้วย การนอนไม่เพียงพอสามารถทำให้ความต้านทานลดลง, มีปัญหาการคิด, และการเรียนรู้มีผลกระทบ นอนน้อยยังเสี่ยงต่อโรคต่างๆ เช่น โรคอ้วน, โรคหัวใจ, วิตกกังวล, หรือโรคจิตเร้าอารมณ์, และภาวะซึมเศร้า การวิเคราะห์ข้อมูลการนอนเป็นทางการเพื่อให้คนทั่วไปทราบถึงปัญหาของตนเอง การใช้ 3 เทคนิคในการวิเคราะห์ได้แก่ เพื่อนบ้านใกล้สุด (K-nearest Neighbors), ต้นไม้ตัดสินใจ (Decision Tree), และ นาอีฟเบย์ (Naive Bayes) เป็นเครื่องมือที่มีประสิทธิภาพในการนำข้อมูลมาวิเคราะห์ ผลการวิเคราะห์นี้จะช่วยให้บุคคลที่สนใจสามารถเข้าใจถึงสถานะของการนอนของตนเอง และสามารถตัดสินใจดำเนินการรักษาหรือปรับเปลี่ยนพฤติกรรมการนอนในทางที่เหมาะสม เพื่อรักษาสุขภาพทั้งร่างกายและจิตใจให้มีคุณภาพดีที่สุด ผลการวิเคราะห์พบว่าเทคนิค Decision Tree มีความแม่นยำสูงที่สุดที่ระดับ 0.89, ตามด้วย Naive Bayes ที่มีความแม่นยำที่ 0.88 และ K-nearest Neighbors ที่มีความแม่นยำที่ 0.87 จากผลลัพธ์นี้, ผู้วิจัยจึงเลือกใช้ Decision Tree เป็นเทคนิคในการพัฒนาระบบทำนายสถานะการนอนของผู้ใช้งานในเว็บไซต์ ทั้งนี้, ผู้ใช้งานสามารถทดสอบระบบเพื่อตรวจสอบสถานะการนอนของตนเองได้</h6></left>
<center></center><left><h6 style="text-indent: 30px;line-height: 1.5;">Maintaining good sleep health is crucial for overall well-being, both physically and mentally, at all ages. Sleep not only replenishes energy for the body and brain but also plays a significant role in hormone regulation, body recovery, and mental health promotion. Insufficient sleep can lead to weakened immunity, cognitive problems, and impaired learning. Additionally, inadequate sleep is associated with various health risks, such as obesity, heart disease, anxiety disorders, depression, and even conditions like sleep disorders.

Analyzing sleep data formally can provide valuable insights into an individual's sleep issues. Using three effective techniques—K-nearest Neighbors, Decision Tree, and Naive Bayes—facilitates the analysis process. These tools efficiently process data to help individuals understand their sleep patterns better. Sleep deprivation can result in reduced resistance, cognitive difficulties, and increased susceptibility to various diseases.

The results of the analysis indicate that Decision Tree has the highest accuracy level at 0.89, followed by Naive Bayes at 0.88 and K-nearest Neighbors at 0.87. Based on these findings, researchers have chosen to implement the Decision Tree technique to develop a predictive system for users' sleep status on a website. Users can utilize this system to assess their own sleep status and make informed decisions to improve their sleep habits, ultimately enhancing both physical and mental well-being.</h6></left>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

### Visualization ###

df = pd.read_excel('./data/heart.xlsx')

html_3 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")
st.write(df.head(10))

html_4 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count plot for various categorical features</h3></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
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

html_5 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count of the target</h3></center>
</div>
"""
st.markdown(html_5, unsafe_allow_html=True)
st.markdown("")



fig = plt.figure(figsize=(18, 7))
gs = fig.add_gridspec(1, 2)
gs.update(wspace=0.3, hspace=0.15)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])

background_color = "#ffe6e6"
color_palette = ["#800000", "#8000ff", "#6aac90", "#5833ff", "#da8829"]
fig.patch.set_facecolor(background_color)
ax0.set_facecolor(background_color)
ax1.set_facecolor(background_color)

# Title of the plot
ax0.text(0.5, 0.5, "Count of the target\n___________",
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=18,
         fontweight='bold',
         fontfamily='serif',
         color='#000000')

ax0.set_xticklabels([])
ax0.set_yticklabels([])
ax0.tick_params(left=False, bottom=False)

# Target Count
ax1.text(0.35, 130, "Output", fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
ax1.bar(df['output'].value_counts().index, df['output'].value_counts().values, color=color_palette)
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.set_xticks([0, 1])
ax1.set_xticklabels(["Low chances of attack(0)", "High chances of attack(1)"])

# Remove spines
for s in ["top", "left", "right"]:
    ax0.spines[s].set_visible(False)
    ax1.spines[s].set_visible(False)
st.pyplot(fig)
