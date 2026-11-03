import streamlit as st

st.set_page_config(page_title="Hardware Expert System", layout="centered")

st.title("💻 Computer Hardware Diagnosis Expert System")
st.write("نظام خبير لتشخيص أعطال هاردوير الكمبيوتر (شغال على اللاب والموبايل)")

# قائمة الأسئلة الكاملة للمشروع
questions = [
    "1. Is the computer completely dead with no lights or fans?",
    "2. Does the laptop shut down immediately when unplugged from the charger?",
    "3. Does the motherboard emit continuous BEEP sounds upon startup?",
    "4. Are internal fans spinning, but the screen has NO signal?",
    "5. Do you see strange lines, glitches, or color distortion on the screen?",
    "6. Is the CPU cooling fan making a loud, buzzing, or grinding noise?",
    "7. Does the PC shut down automatically due to high temperature?",
    "8. Does the system crash with a Blue Screen (BSOD) randomly?",
    "9. Is the operating system extremely sluggish and freezing often?",
    "10. Are you hearing clicking noises from the hard drive or getting disk read errors?",
    "11. Are connected USB devices (mouse, keyboard, flash drives) not recognized?",
    "12. Is there no sound coming from the speakers or headphones at all?",
    "13. Is the Wi-Fi adapter missing or failing to connect to any network?",
    "14. Is the Bluetooth feature failing to turn on or pair devices?",
    "15. Does the monitor fail to detect the PC even when using a different cable?"
]

answers = []
for i, q in enumerate(questions):
    ans = st.radio(q, ["No", "Yes"], key=f"q_{i}")
    answers.append(ans)

if st.button("🔍 تشخيص العطل (Diagnose)"):
    st.subheader("📋 نتيجة التشخيص:")
    if answers[0] == "Yes":
        st.error("النتيجة: مشكلة في مصدر الطاقة (Power Supply) أو كابل الكهرباء.")
    elif answers[1] == "Yes":
        st.warning("النتيجة: البطارية تالفة بحاجة إلى تغيير أو مشكلة في دائرة الشحن.")
    elif answers[2] == "Yes":
        st.error("النتيجة: مشكلة في الرامات (RAM) أو كارت الشاشة غير مثبت جيداً.")
    elif answers[6] == "Yes":
        st.warning("النتيجة: ارتفاع حرارة البروسيسور (Overheating) وتحتاج لتنظيف المروحة وتغيير التبريد.")
    elif answers[9] == "Yes":
        st.error("النتيجة: الهارد ديسك تالف أو على وشك التوقف (Hard Drive Failure).")
    else:
        st.success("النتيجة: النظام يعمل بصورة طبيعية أو العطل برمجي وليس هاردوير.")