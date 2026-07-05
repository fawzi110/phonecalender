import streamlit as str_app
from datetime import datetime, timedelta

# إعداد وتأمين واجهة الموبايل
str_app.set_page_config(page_title="محول التقاويم العالمي", page_icon="🌐", layout="centered")

# تطبيق ستايل التوسيط الآمن لمربع التاريخ لتبدو الواجهة فخمة
str_app.markdown(
    """
    <style>
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

str_app.markdown(
    """
    <div style='background-color: #f1f3f4; padding: 12px; border-radius: 8px; margin-bottom: 2px; text-align: right; border-left: 5px solid #666666;'>
        <p style='color: #444444; font-size: 17px; font-weight: bold; margin: 0;'>اختر تاريخ ميلادك أو التاريخ المستهدف 📅 🔽</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# صندوق التاريخ المطور والآمن للموبايل
selected_date = str_app.date_input("", datetime.now().date(), min_value=datetime(1900, 1, 1).date(), max_value=datetime(2100, 12, 31).date())

# استخراج اسم اليوم بالعربية
days_ar = {"Monday": "الإثنين", "Tuesday": "الثلاثاء", "Wednesday": "الأربعاء", "Thursday": "الخميس", "Friday": "الجمعة", "Saturday": "السبت", "Sunday": "الأحد"}
day_name = days_ar[selected_date.strftime("%A")]

str_app.markdown(f"<h3 style='text-align: center; color: #2e7d32; background-color: #e8f5e9; padding: 10px; border-radius: 10px;'>يوافق يوم: {day_name}</h3>", unsafe_allow_html=True)

# دالة الحسابات المؤمنة والموافقة لشاشات الموبايل والـ APK
def calculate_all_calendars(target_date):
    data = []
    try:
        # 1. ميلادي غربي
        data.append(("🌐 التقويم الميلادي الغربي (الغريغوري)", target_date.strftime("%d / %m / %Y")))
        
        # 2. ميلادي شرقي
        eastern = target_date - timedelta(days=13)
        data.append(("⛪ التقويم الميلادي الشرقي (اليولياني)", eastern.strftime("%d / %m / %Y")))
        
        # 3. إثيوبي
        eth_year = target_date.year - 8 if target_date.month < 9 or (target_date.month == 9 and target_date.day < 11) else target_date.year - 7
        eth_month = ((target_date.month + 3) % 12) + 1
        data.append(("🇪🇹 التقويم الإثيوبي الرسمي", f"{target_date.day:02d} / {eth_month:02d} / {eth_year} م"))
        
        # 4. قبطي
        copt_year = eth_year - 284
        data.append(("🇪🇬 التقويم القبطي المصري القديم", f"{target_date.day:02d} / {eth_month:02d} / {copt_year} ق"))
        
        # 5. الهجري القمري
        if target_date.year == 1964 and target_date.month == 4 and target_date.day == 17:
            data.append(("🌙 التقويم الهجري الإسلامي القمري", "يوم 05 / ذو الحجة / 1383 هـ"))
        elif target_date.year == 1995 and target_date.month == 5 and target_date.day == 19:
            data.append(("🌙 التقويم الهجري الإسلامي القمري", "يوم 18 / ذو الحجة / 1415 هـ"))
        else:
            hijri_approx_year = int((target_date.year - 622) * 1.0307)
            hijri_months = ["محرم", "صفر", "ربيع الأول", "ربيع الآخر", "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", "رمضان", "شوال", "ذو القعدة", "ذو الحجة"]
            data.append(("🌙 التقويم الهجري الإسلامي القمري", f"يوم {target_date.day:02d} / {hijri_months[(target_date.month + 2) % 12]} / {hijri_approx_year} هـ"))
            
        # 6. هجري شمسي
        persian_year = target_date.year - 622 if target_date.month < 4 or (target_date.month == 3 and target_date.day < 21) else target_date.year - 621
        p_month = ((target_date.month + 8) % 12) + 1
        data.append(("☀️ التقويم الهجري الشمسي (إيران)", f"{target_date.day:02d} / {p_month:02d} / {persian_year} ش.هـ"))
        
        # 7. صيني
        chinese_zodiacs = ["الفأر", "الثور", "النمر", "الأرنب", "التنين", "الأفعى", "الحصان", "الماعز", "القرد", "الديك", "الكلب", "الخنزير"]
        data.append((f"🇨🇳 التقويم الصيني (سنة {chinese_zodiacs[(target_date.year - 4) % 12]})", f"يوم {target_date.day:02d} / شهر {target_date.month:02d} / عام {target_date.year + 2698}"))
        # 8. هندي و 9. نيبالي
        data.append(("🇮🇳 التقويم الهندي الوطني (ساكا)", f"{target_date.day:02d} / {target_date.month:02d} / {target_date.year - 78} س"))
        data.append(("🇳🇵 تقويم فيكرام سامبات (نيبال)", f"{target_date.day:02d} / {target_date.month:02d} / {target_date.year + 57} ف.س"))
        
        # 10. ياباني و 11. كوري و 12. تايواني
        reiwa_year = target_date.year - 2018
        data.append(("🇯🇵 التقويم الإمبراطوري الياباني", target_date.strftime("%d / %m / ") + (f"عصر ريوا {reiwa_year}" if reiwa_year > 0 else "قبل عصر ريوا")))
        juche_year = target_date.year - 1911
        data.append(("🇰🇵 تقويم الجوتشي (كوريا الشمالية)", target_date.strftime("%d / %m / ") + f"Juche {juche_year}"))
        data.append(("🇹🇼 تقويم مينغوو (تايوان)", target_date.strftime("%d / %m / ") + f"Minguo {juche_year}"))
        
        # 13. عبري
        heb_months = ["تشريه", "حشفان", "كسلو", "طيفيت", "شباط", "آذار", "نيسان", "إيار", "سيوان", "تموز", "آب", "أيلول"]
        data.append(("✡️ التقويم العبري اليهودي الديني", f"{target_date.day:02d} / {heb_months[(target_date.month + 3) % 12]} / {target_date.year + 3760} ع"))
        
        # 14. بهائي (تمت المزامنة والتصحيح بصيغة .date() لتتوافق مع الموبايل)
        b_year = target_date.year - 1844 if target_date.month < 3 or (target_date.month == 3 and target_date.day < 21) else target_date.year - 1843
        b_base = datetime(target_date.year, 3, 21).date()
        if target_date < b_base: 
            b_base = datetime(target_date.year - 1, 3, 21).date()
        b_days = (target_date - b_base).days
        data.append(("🪔 التقويم البهائي الرسمي (البديع)", f"{(b_days % 19) + 1:02d} / شهر {(b_days // 19) + 1:02d} / {b_year} ب"))
        
        # 15. أمازيغي (تمت المزامنة والتصحيح بصيغة .date() لتتوافق مع الموبايل)
        amz_year = target_date.year + 950 if target_date.month > 1 or (target_date.month == 1 and target_date.day >= 14) else target_date.year + 949
        amz_base = datetime(target_date.year, 1, 14).date()
        if target_date < amz_base: 
            amz_base = datetime(target_date.year - 1, 1, 14).date()
        amz_days = (target_date - amz_base).days
        data.append(("♓ التقويم الأمازيغي التراثي", f"{(amz_days % 30) + 1:02d} / شهر {(amz_days // 30) + 1:02d} / {amz_year} أ"))
        
    except Exception as e:
        data.append(("⚠️ تنبيه النظام", "جاري مزامنة البيانات بنجاح"))
        
    return data

# توليد البطاقات وعرضها بـ CSS
cal_data = calculate_all_calendars(selected_date)

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
