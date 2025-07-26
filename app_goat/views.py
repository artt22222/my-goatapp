import joblib
import os
import traceback
from django.conf import settings
from django.shortcuts import render
from .models import Diseases, GoatStatistics
from django.shortcuts import get_object_or_404

# โหลดโมเดลและ label encoder
model = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'RF_model.pkl'))
label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'label_encoder.pkl')) 

def diagnosis(request):
    if request.method == 'POST':
        try:
            symptoms = request.POST.getlist('symptoms[]')
            print("📥 อาการที่รับจากผู้ใช้:", symptoms)  

            all_possible_symptoms = [
                                    'ซึม','เบื่ออาหาร','ไข้','ผอมลง','ตัวสั่น',
                                    'ตายเฉียบพลัน','ขนร่วง','คอตก','เดินวน/เดินมึน','ยืนลำบาก/เดินไม่ได้',
                                    'ไอ','หายใจลำบาก','มีน้ำมูก','ถ่ายเหลวผิดปกติ','ถ่ายเป็นเลือด',
                                    'ขี้สีดำ/เขียวผิดปกติ','กลิ่นปากแรง','ตุ่มใส/ตุ่มหนองที่ผิวหนัง','แผลบริเวณผิวหนัง','ผิวหนังตกสะเก็ด',
                                    'แผลในปาก/ลิ้น','น้ำลายไหลผิดปกติ','ตาแดง','น้ำตาไหลผิดปกติ','ขี้ตาเยอะ/ตาแฉะ',
                                    'เดินกะเผลก','เต้านมอักเสบ','ต่อมน้ำเหลืองโต','บวมใต้คาง','ข้อบวม/ข้ออักเสบ',
                                    'แผลบริเวณขา/กีบ'
            ]

            if not symptoms:
                return render(request, 'app_goat/error.html', {'error': 'กรุณาเลือกอาการอย่างน้อย 1 รายการ'})

            # แปลงอาการเป็นเวกเตอร์
            symptoms_vector = [1 if symptom in symptoms else 0 for symptom in all_possible_symptoms]
            print("🧠 เวกเตอร์ที่ส่งเข้าโมเดล:", symptoms_vector)  

            # คำนวณความน่าจะเป็น
            proba = model.predict_proba([symptoms_vector])[0]   
            class_labels = label_encoder.inverse_transform(range(len(proba)))  

            #  zip + sort
            zipped = sorted(zip(class_labels, proba * 100), key=lambda x: x[1], reverse=True)

            #  แยก top 3
            top3 = zipped[:3]

            # หารวมของ "เปอร์เซ็นต์ทั้งหมด"
            total_percent = sum([p for _, p in zipped])  

            #  คำนวณเปอร์เซ็นต์ส่วนเกินจาก top3
            top3_sum = sum([p for _, p in top3])
            other_sum = total_percent - top3_sum

            #  รวม other_sum เข้ากับอันดับที่ 1
            top1_label, top1_prob = top3[0]
            top3[0] = (top1_label, top1_prob + other_sum)

            # ✅ Prediction with adjusted probability
            prediction_with_proba_raw = top3


            # แปลงชื่อย่อโรค → ภาษาไทย
            disease_name_map = {
                'meli': 'โรคเมลิออยด์',
                'Anth': 'โรคแอนแทรกซ์',
                'bp': 'โรคปอดปวมจากแบคทีเรีย',
                'FMD': 'โรคปากและเท้าเปื่อย',
                'arth': 'โรคข้ออักเสบ',
                'cae': 'โรคข้อและสมองอักเสบ',
                'conj': 'โรคตาอักเสบ',
                'orf': 'โรคปากเปื่อยพุพอง',
                'para': 'โรคพยาธิภายใน',
                'ppr': 'โรคพีพีอาร์',
                'skin': 'โรคผิวหนัง',
                'tb': 'โรควัณโรค',
            }

            # path รูปภาพ
            base_path = 'app_goat/disease/'
            image_map = {
                'โรคปากและเท้าเปื่อย': f'{base_path}f_m.jpg',
                'โรคปากเปื่อยพุพอง': f'{base_path}m.png',
                'โรคแอนแทรกซ์': f'{base_path}antrax.png',
                'โรคข้ออักเสบ': f'{base_path}arth.jpg',
                'โรคข้อและสมองอักเสบ': f'{base_path}brain_arth.png',
                'โรคปอดปวมจากแบคทีเรีย': f'{base_path}bac.png',
                'โรคเมลิออยด์': f'{base_path}meli.jpg',
                'โรควัณโรค': f'{base_path}tub.png',
                'โรคตาอักเสบ': f'{base_path}eye.png',
                'โรคผิวหนัง': f'{base_path}skin.png',
                'โรคพีพีอาร์': f'{base_path}ppr.jpg',
                'โรคพยาธิภายใน': f'{base_path}internal.jpg',
            }

            
            # สร้าง map สำหรับ lookup pk จากชื่อโรคไทย
            disease_thai_name_to_pk = {
            d.title: d.pk for d in Diseases.objects.all()
}

            # ✅ รวมชื่อภาษาไทย + ความน่าจะเป็น + รูปภาพ
            prediction_with_proba = [
                (
                disease_thai_name_to_pk.get(disease_name_map.get(disease_code, disease_code), None),  # pk
                disease_name_map.get(disease_code, disease_code),  # title (ชื่อโรค)
                prob,
                image_map.get(disease_name_map.get(disease_code, disease_code), f'{base_path}default.png')  # รูป
                )
                for disease_code, prob in prediction_with_proba_raw
            ]


            return render(request, 'app_goat/result.html', {
                'prediction_with_proba': prediction_with_proba,
                'symptoms': symptoms,
            })

        except Exception as e:
            print("❌ Error:", str(e))
            traceback.print_exc()
            return render(request, 'app_goat/error.html', {'error': str(e)})

    return render(request, 'app_goat/form.html')



# ฟังก์ชันที่ใช้แสดงข้อมูลเกี่ยวกับโรค
def about(request):
    return render(request, 'app_goat/about.html')

# ฟังก์ชันที่ใช้แสดงข้อมูลในฟอร์ม
def form(request):
    return render(request, 'app_goat/form.html')

# ฟังก์ชันที่แสดงรายชื่อโรคทั้งหมด
def list(request):
    diseases = Diseases.objects.all()  # ดึงข้อมูลโรคทั้งหมดจากฐานข้อมูล
    context = {'diseases': diseases}
    return render(request, 'app_goat/list.html', context)

# ฟังก์ชันที่แสดงรายละเอียดของโรค
def detail(request, pk):
    disease = get_object_or_404(Diseases, pk=pk)  # ดึงข้อมูลโรคที่ต้องการแสดง
    context = {'disease': disease}
    return render(request, 'app_goat/detail.html', context)

# ฟังก์ชันที่ใช้แสดงข้อมูลสถิติ
def home(request):
    stats = GoatStatistics.objects.last()  # ดึงข้อมูลสถิติล่าสุด
    return render(request, 'app_goat/home.html', {'stats': stats})

# ฟังก์ชันที่แสดงผลลัพธ์หลังจากการวินิจฉัย
def result(request):
    return render(request, 'app_goat/result.html')
