import streamlit as st
from streamlit_drawable_canvas import st_canvas

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="مفكرتي الاحترافية", layout="wide")
st.title("📝 مفكرة القلم الذكية (S-Note Clone)")
st.write("ابدأ الكتابة أو الرسم باستخدام قلم التابلت مباشرة")

# شريط الأدوات الجانبي لخيارات القلم
st.sidebar.header("🎨 أدوات التحكم")

# اختيار لون القلم
stroke_color = st.sidebar.color_picker("اختر لون القلم:", "#000000")

# اختيار سمك القلم
stroke_width = st.sidebar.slider("سمك الخط:", 1, 25, 3)

# اختيار نوع الأداة (رسم حر أم مسح)
drawing_mode = st.sidebar.selectbox(
    "الأداة الحالية:", ("freedraw", "transform", "rect", "circle")
)

# إنشاء لوحة الرسم (Canvas) وسط الشاشة
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#FFFFFF", 
    height=600,
    width=800,
    drawing_mode=drawing_mode,
    key="canvas",
)

# زر حفظ الملاحظة كصورة
if canvas_result.image_data is not None:
    st.sidebar.markdown("---")
    st.sidebar.subheader("💾 حفظ العمل")
    if st.sidebar.button("تصدير الملاحظة كصورة"):
        st.success("تم تجهيز الصورة بنجاح! يمكنك الضغط مطولاً عليها لحفظها.")
        st.image(canvas_result.image_data)
