import streamlit as st
from sklearn.naive_bayes import GaussianNB
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
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;margin-top:20px;">
<center><h3>Class Prediction</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


s1 = st.number_input("อายุของผู้ป่วย")
s2 = st.slider("เพศของผู้ป่วย (0 : หญิง | 1 : ชาย)",0,1)
s3 = st.slider("อาการเจ็บหน้าอก\n(1 : โรคหลอดเลือดหัวใจตีบทั่วไป | 2 : โรคหลอดเลือดหัวใจตีบผิดปรกติ | 3 : อาการปวดที่ไม่ใช่โรคหลอดเลือดหัวใจตีบ | 4 : ไม่มีอาการ)",1,4)
s4 = st.number_input("ความดันโลหิตขณะพัก (มม. ปรอท)")
s5 = st.number_input("cholestoral ใน mg/dl ดึงผ่านเซ็นเซอร์ BMI")
s6 = st.slider("น้ําตาลในเลือดขณะอดอาหาร > 120 มก./ดล. (1 = จริง 0 = เท็จ)",0,1)
s7 = st.slider("พักผลการตรวจคลื่นไฟฟ้าหัวใจ ( 0 : ปกติ | 1 : มีความผิดปกติของคลื่น ST-T | 2 : แสดงกระเป๋าหน้าท้องยั่วยวนซ้ายที่เป็นไปได้หรือแน่นอนตามเกณฑ์ของเอสเตส)",0,2)
s8 = st.number_input("อัตราการเต้นของหัวใจสูงสุดทําได้")
s9 = st.slider("การออกกําลังกายทําให้เกิดโรคหลอดเลือดหัวใจตีบ (1 = ใช่ 0 = ไม่ใช่)",0,1)
s10 = st.number_input("จุดสูงสุดก่อนหน้า")
s11 = st.slider("Slope",0,2)
s12 = st.slider("number of major vessels (0-3)",0,3)
s13 = st.slider("Thal rate",0,3)

if st.button("ทำนายผล"):

   X=df.drop(["output"],axis=1)
   y=df["output"]

   nb_model = GaussianNB()
   nb_model.fit(X, y)


   x_input = np.array([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]])

   out = nb_model.predict(x_input)

   if out[0]== 0 :
          
      html_3 = """
      <div style="background-color:#0E1117;padding:20px;border: 3px solid #ffffff;">
      <center><h3 style="border-bottom: 3px solid #ffffff;">โอกาสหัวใจวายน้อย</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคหัวใจวาย (Coronary Artery Disease, CAD) เป็นภาวะที่เกิดจากการสะสมของเส้นเลือดในหัวใจ (หลอดเลือดในหัวใจ) ทำให้การไหลของเลือดที่จำเป็นสำหรับการให้สารอาหารและออกซิเจนให้กับกล้ามเนื้อหัวใจลดลง สาเหตุหลักของโรคหัวใจวายคือการสะสมของตะกอนไขมันและแร่ธาตุในเส้นเลือดในหัวใจ (เช่น เนื้อเยื่อไขมัน, เซลล์เลือดขาว, และแคลเซียม) ซึ่งทำให้เกิดลิ่ม (plaque) ในเส้นเลือด ลิ่มนี้จะทำให้เส้นเลือดตีบ และสามารถทำให้เกิดอาการหัวใจวาย นี่คือบางวิธีที่อาจช่วยลดโอกาสหัวใจวาย</h6></left>
      <ul>
         <li>รับประทานอาหารที่สุขภาพดี:การบริโภคอาหารที่รวมถึงผัก, ผลไม้, และอาหารที่มีไขมันไม่เบาหรือไขมันดีสามารถช่วยลดความเสี่ยง</li>
         <li>ออกกำลังกาย:การมีกิจกรรมทางกายเป็นประจำ อย่างน้อย 150 นาทีต่อสัปดาห์ เช่น เดินเร็ว, วิ่ง, หรือว่ายน้ำ</li>
         <li>ควบคุมน้ำหนัก:การรักษาน้ำหนักที่เหมาะสมสามารถช่วยลดโอกาสหัวใจวาย</li>
         <li>การเลิกสูบบุหรี่:การเลิกสูบบุหรี่จะช่วยลดความเสี่ยงของโรคหัวใจวาย</li>
         <li>ควบคุมและรักษาโรคประจำตัว:การควบคุมโรคเบาหวาน, ความดันโลหิต, และโรคอื่น ๆ ที่เป็นปัจจัยเสี่ยง</li>
         <li>การบริหารจัดการสเตรส:การใช้เทคนิคการบริหารจัดการสเตรส เช่น การฝึกสมาธิหรือการทำโยคะ</li>
         <li>การดื่มแอลกอฮอล์อย่างมีสติ:การดื่มแอลกอฮอล์ในปริมาณที่ปลอดภัยมีผลต่อการลดความเสี่ยง</li>
         <li>การตรวจสุขภาพประจำปี:การตรวจสุขภาพประจำปีเพื่อตรวจสอบสุขภาพโดยรวมและความเสี่ยงต่อโรค</li>
         <li>การนอนหลับเพียงพอ:การนอนหลับประจำวันในปริมาณที่เหมาะสมสามารถส่งเสริมสุขภาพหัวใจ</li>
         <li>การหลีกเลี่ยงการบริโภคอาหารที่มีสารอาหารไม่ดี:ลดการบริโภคอาหารที่มีโคเลสเตอรอลสูง, น้ำตาล, และเกลือ</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การปฏิบัติตนตามแนวทางดังกล่าวจะช่วยลดโอกาสที่จะเป็นโรคหัวใจวายและส่งเสริมสุขภาพหัวใจที่แข็งแรง. อย่าลืมปรึกษาแพทย์หากคุณมีปัญหาสุขภาพหรือต้องการคำแนะนำเพิ่มเติมเกี่ยวกับการรักษาและป้องกันโรคหัวใจวาย</h6></left>
      </div>
      """
      st.markdown(html_3, unsafe_allow_html=True)
      st.markdown("")

   elif out[0]==1:
          
          
      html_4 = """
      <div style="background-color:#0E1117;padding:20px;border: 3px solid #ffffff;">
      <center><h3 style="border-bottom: 3px solid #ffffff;">โอกาสหัวใจวายมาก</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">โรคหัวใจวาย (Coronary Artery Disease, CAD) เป็นภาวะที่เกิดจากการสะสมของเส้นเลือดในหัวใจ (หลอดเลือดในหัวใจ) ทำให้การไหลของเลือดที่จำเป็นสำหรับการให้สารอาหารและออกซิเจนให้กับกล้ามเนื้อหัวใจลดลง สาเหตุหลักของโรคหัวใจวายคือการสะสมของตะกอนไขมันและแร่ธาตุในเส้นเลือดในหัวใจ (เช่น เนื้อเยื่อไขมัน, เซลล์เลือดขาว, และแคลเซียม) ซึ่งทำให้เกิดลิ่ม (plaque) ในเส้นเลือด ลิ่มนี้จะทำให้เส้นเลือดตีบ และสามารถทำให้เกิดอาการหัวใจวาย นี่คือบางวิธีที่อาจช่วยลดโอกาสหัวใจวาย</h6></left>
      <ul>
         <li>รับประทานอาหารที่สุขภาพดี:การบริโภคอาหารที่รวมถึงผัก, ผลไม้, และอาหารที่มีไขมันไม่เบาหรือไขมันดีสามารถช่วยลดความเสี่ยง</li>
         <li>ออกกำลังกาย:การมีกิจกรรมทางกายเป็นประจำ อย่างน้อย 150 นาทีต่อสัปดาห์ เช่น เดินเร็ว, วิ่ง, หรือว่ายน้ำ</li>
         <li>ควบคุมน้ำหนัก:การรักษาน้ำหนักที่เหมาะสมสามารถช่วยลดโอกาสหัวใจวาย</li>
         <li>การเลิกสูบบุหรี่:การเลิกสูบบุหรี่จะช่วยลดความเสี่ยงของโรคหัวใจวาย</li>
         <li>ควบคุมและรักษาโรคประจำตัว:การควบคุมโรคเบาหวาน, ความดันโลหิต, และโรคอื่น ๆ ที่เป็นปัจจัยเสี่ยง</li>
         <li>การบริหารจัดการสเตรส:การใช้เทคนิคการบริหารจัดการสเตรส เช่น การฝึกสมาธิหรือการทำโยคะ</li>
         <li>การดื่มแอลกอฮอล์อย่างมีสติ:การดื่มแอลกอฮอล์ในปริมาณที่ปลอดภัยมีผลต่อการลดความเสี่ยง</li>
         <li>การตรวจสุขภาพประจำปี:การตรวจสุขภาพประจำปีเพื่อตรวจสอบสุขภาพโดยรวมและความเสี่ยงต่อโรค</li>
         <li>การนอนหลับเพียงพอ:การนอนหลับประจำวันในปริมาณที่เหมาะสมสามารถส่งเสริมสุขภาพหัวใจ</li>
         <li>การหลีกเลี่ยงการบริโภคอาหารที่มีสารอาหารไม่ดี:ลดการบริโภคอาหารที่มีโคเลสเตอรอลสูง, น้ำตาล, และเกลือ</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การปฏิบัติตนตามแนวทางดังกล่าวจะช่วยลดโอกาสที่จะเป็นโรคหัวใจวายและส่งเสริมสุขภาพหัวใจที่แข็งแรง. อย่าลืมปรึกษาแพทย์หากคุณมีปัญหาสุขภาพหรือต้องการคำแนะนำเพิ่มเติมเกี่ยวกับการรักษาและป้องกันโรคหัวใจวาย</h6></left>
      </div>
      """
      st.markdown(html_4, unsafe_allow_html=True)
      st.markdown("")

     