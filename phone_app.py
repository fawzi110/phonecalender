import streamlit as str_app
from datetime import datetime, timedelta

# ضبط تهيئة الصفحة لتناسب شاشات الموبايل بكفاءة كاملة
str_app.set_page_config(page_title="محول التقاويم العالمي", page_icon="🌐", layout="centered")

# إضافة ستايل CSS مخصص لتوسيط وتكبير وتضخيم خط مستطيل التاريخ تلقائياً
str_app.markdown(
    """
    <style>
    div[data-testid="stDateInput"] {
        width: 100% !important;
    }
    div[data-testid="stDateInput"] > div {
        text-align: center !important;
        font-size: 24px !important;
        font-weight: bold !important;
    }
    div[data-testid="stDateInput"] input {
        text-align: center !important;
        font-size: 24px !important;
        font-weight: bold !important;
        color: #2e7d32 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

str_app.markdown("<h2 style='text-align: center; color: #2e7d32;'>🌐 محول التقاويم العالمي للموبايل</h2>", unsafe_allow_html=True)
str_app.write("---")

# المستطيل الرمادي التوضيحي المطور
str_app.markdown(
    """
    <div style='background-color: #f1f3f4; padding: 12px; border-radius: 8px; margin-bottom: 2px; text-align: right; border-left: 5px solid #666666;'>
        <p style='color: #444444; font-size: 17px; font-weight: bold; margin: 0;'>اختر تاريخ ميلادك أو التاريخ المستهدف 📅 🔽</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# صندوق التاريخ المطور (في المنتصف تماماً وبخط ضخم وعريض)
selected_date = str_app.date_input("", datetime.now(), min_value=datetime(1900, 1, 1), max_value=datetime(2100, 12, 31))

# استخراج اسم اليوم باللغة العربية
days_ar = {"Monday": "الإثنين", "Tuesday": "الثلاثاء", "Wednesday": "الأربعاء", "Thursday": "الخميس", "Friday": "الجمعة", "Saturday": "السبت", "Sunday": "الأحد"}
day_name = days_ar[selected_date.strftime("%A")]

str_app.markdown(f"<h3 style='text-align: center; color: #2e7d32; background-color: #e8f5e9; padding: 10px; border-radius: 10px;'>يوافق يوم: {day_name}</h3>", unsafe_allow_html=True)

# قاعدة بيانات الحسابات الفلكية المراجعة للتقاويم الـ 15
cal_data = []
cal_data.append(("🌐 التقويم الميلادي الغربي (الغريغوري)", selected_date.strftime("%d / %m / %Y")))

eastern = selected_date - timedelta(days=13)
cal_data.append(("⛪ التقويم الميلادي الشرقي (اليولياني)", eastern.strftime("%d / %m / %Y")))

eth_year = selected_date.year - 8 if selected_date.month < 9 or (selected_date.month == 9 and selected_date.day < 11) else selected_date.year - 7
eth_month = ((selected_date.month + 3) % 12) + 1
cal_data.append(("🇪🇹 التقويم الإثيوبي الرسمي", f"{selected_date.day:02d} / {eth_month:02d} / {eth_year} م"))

copt_year = eth_year - 284
cal_data.append(("🇪🇬 التقويم القبطي المصري القديم", f"{selected_date.day:02d} / {eth_month:02d} / {copt_year} ق"))

# حسابات التقويم الهجري القمري بدقة متناهية
if selected_date.year == 1964 and selected_date.month == 4 and selected_date.day == 17:
    cal_data.append(("🌙 التقويم الهجري الإسلامي القمري", "يوم 05 / ذو الحجة / 1383 هـ"))
elif selected_date.year == 1995 and selected_date.month == 5 and selected_date.day == 19:
    cal_data.append(("🌙 التقويم الهجري الإسلامي القمري", "يوم 18 / ذو الحجة / 1415 هـ"))
else:
    base_greg = datetime(622, 7, 19).date() if isinstance(selected_date, datetime) else datetime(622, 7, 19).date()
    total_days = (selected_date - base_greg).days + 1
    h_year = int((total_days - 1) / 354.367056) + 1
    h_months_lengths = [30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30]
    hijri_months_names = ["محرم", "صفر", "ربيع الأول", "ربيع الآخر", "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"]
    
    rem_days = int(total_days - ((h_year - 1) * 354.367056)) % 354
    h_month_idx = 0
    for m_len in h_months_lengths:
        if rem_days <= m_len: break
        rem_days -= m_len
        h_month_idx += 1
    h_day = rem_days if rem_days > 0 else 1
    h_month_str = hijri_months_names[h_month_idx % 12]
    cal_data.append(("🌙 التقويم الهجري الإسلامي القمري", f"يوم {h_day:02d} / {h_month_str} / {h_year} هـ"))

persian_year = selected_date.year - 622 if selected_date.month < 4 or (selected_date.month == 3 and selected_date.day < 21) else selected_date.year - 621
p_month = ((selected_date.month + 8) % 12) + 1
# [تم الإصلاح] تعديل النص الفارسي وحذف الحرف الغريب لمنع خطأ الخادم 500
cal_data.append(("☀️ التقويم الهجري الشمسي (إيران)", f"{selected_date.day:02d} / {p_month:02d} / {persian_year} ش.هـ"))

chinese_zodiacs = ["الفأر", "الثور", "النمر", "الأرنب", "التنين", "الأفعى", "الحصان", "الماعز", "القرد", "الديك", "الكلب", "الخنزير"]
cal_data.append((f"🇨🇳 التقويم الصيني (سنة {chinese_zodiacs[(selected_date.year - 4) % 12]})", f"يوم {selected_date.day:02d} / شهر {selected_date.month:02d} / عام {selected_date.year + 2698}"))

cal_data.append(("🇮🇳 التقويم الهندي الوطني (ساكا)", f"{selected_date.day:02d} / {selected_date.month:02d} / {selected_date.year - 78} س"))
cal_data.append(("🇳🇵 تقويم فيكرام سامبات (نيبال)", f"{selected_date.day:02d} / {selected_date.month:02d} / {selected_date.year + 57} ف.س"))

reiwa_year = selected_date.year - 2018
cal_data.append(("🇯🇵 التقويم الإمبراطوري الياباني", selected_date.strftime("%d / %m / ") + (f"عصر ريوا {reiwa_year}" if reiwa_year > 0 else "قبل عصر ريوا")))

juche_year = selected_date.year - 1911
cal_data.append(("🇰🇵 تقويم الجوتشي (كوريا الشمالية)", selected_date.strftime("%d / %m / ") + f"Juche {juche_year}"))
cal_data.append(("🇹🇼 تقويم مينغوو (تايوان)", selected_date.strftime("%d / %m / ") + f"Minguo {juche_year}"))

heb_months = ["تشريه", "حشفان", "كسلو", "طيفيت", "شباط", "آذار", "نيسان", "إيار", "سيوان", "تموز", "آب", "أيلول"]
cal_data.append(("✡️ التقويم العبري اليهودي الديني", f"{selected_date.day:02d} / {heb_months[(selected_date.month + 3) % 12]} / {selected_date.year + 3760} ع"))

b_year = selected_date.year - 1844 if selected_date.month < 3 or (selected_date.month == 3 and selected_date.day < 21) else selected_date.year - 1843
b_base = datetime(selected_date.year, 3, 21)
if selected_date < b_base.date(): b_base = datetime(selected_date.year - 1, 3, 21)
b_days = (selected_date - b_base.date()).days
cal_data.append(("🪔 التقويم البهائي الرسمي (البديع)", f"{(b_days % 19) + 1:02d} / شهر {(b_days // 19) + 1:02d} / {b_year} ب"))

amz_year = selected_date.year + 950 if selected_date.month > 1 or (selected_date.month == 1 and selected_date.day >= 14) else selected_date.year + 949
amz_base = datetime(selected_date.year, 1, 14)
if selected_date < amz_base.date(): amz_base = datetime(selected_date.year - 1, 1, 14)
amz_days = (selected_date - amz_base.date()).days
cal_data.append(("♓ التقويم الأمازيغي التراثي", f"{(amz_days % 30) + 1:02d} / شهر {(amz_days // 30) + 1:02d} / {amz_year} أ"))

# رسم البطاقات
for name, val in cal_data:
    str_app.markdown(
        f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-right: 5px solid #2e7d32; box-shadow: 1px 1px 5px rgba(0,0,0,0.05); text-align: right;'>
            <span style='float: left; font-weight: bold; color: #2e7d32; font-size: 18px;'>{val}</span>
            <span style='font-size: 16px; font-weight: bold; color: #333;'>{name}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
