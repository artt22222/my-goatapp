import joblib
import os
import traceback
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Diseases, GoatStatistics

# โหลดโมเดลและ label encoder
model = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'RF_model.pkl'))
label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'label_encoder.pkl'))

# ฟังก์ชันวินิจฉัยโรค
def diagnosis(request):
    if request.method == 'POST':
        try:
            symptoms = request.POST.getlist('symptoms[]')
            print("อาการที่รับจากผู้ใช้:", symptoms)

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
                return render(request, 'error.html', {'error': 'กรุณาเลือกอาการอย่างน้อย 1 อาการ'})

            # แปลงอาการเป็นเวกเตอร์
            symptoms_vector = [1 if symptom in symptoms else 0 for symptom in all_possible_symptoms]
            print("เวกเตอร์ที่ส่งเข้าโมเดล:", symptoms_vector)

            # คำนวณความน่าจะเป็น
            proba = model.predict_proba([symptoms_vector])[0]
            class_labels = label_encoder.inverse_transform(range(len(proba)))

            # zip + sort
            zipped = sorted(zip(class_labels, proba * 100), key=lambda x: x[1], reverse=True)

            # เอา top3
            top3 = zipped[:3]
            other_list = zipped[3:]

            # รวมเปอร์เซ็นต์ที่เหลือทั้งหมด
            other_sum = sum(p for _, p in other_list)
            final_result = top3 + [("อื่นๆ", other_sum)]

            # normalize รวม 100%
            total_sum = sum(p for _, p in final_result)
            final_result = [(label, round(p / total_sum * 100, 2)) for label, p in final_result]

            # แผนที่ชื่อโรค
            disease_name_map = {
                'meli': 'โรคเมลิออยด์',
                'Anth': 'โรคแอนแทรกซ์',
                'bp': 'โรคปอดบวมจากแบคทีเรีย',
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

            # สร้างผลลัพธ์สำหรับการแสดงผล
            prediction_with_proba = []
            for disease_code, prob in final_result:
                disease_name = disease_name_map.get(disease_code, disease_code)

                if disease_name == "อื่นๆ":
                    prediction_with_proba.append((None, "อื่นๆ", prob, "disease/default.png"))
                else:
                    try:
                        disease_obj = Diseases.objects.get(title=disease_name)
                        prediction_with_proba.append((
                            disease_obj.pk,
                            disease_obj.title,
                            prob,
                            disease_obj.image.url if disease_obj.image else "disease/default.png"
                        ))
                    except Diseases.DoesNotExist:
                        prediction_with_proba.append((None, disease_name, prob, "disease/default.png"))

            # เก็บ session
            request.session['last_prediction'] = prediction_with_proba
            request.session['last_symptoms'] = symptoms
            request.session['other_diseases'] = [(code, round(p, 2)) for code, p in other_list]

            return redirect(reverse('result'))

        except Exception as e:
            print("❌ Error:", str(e))
            traceback.print_exc()
            return render(request, 'error.html', {'error': str(e)})

    else:
        if 'last_prediction' in request.session:
            return render(request, 'result.html', {
                'prediction_with_proba': request.session['last_prediction'],
                'symptoms': request.session.get('last_symptoms', [])
            })
        else:
            return render(request, 'form.html')


# ฟังก์ชันอื่น ๆ
# ------------------------
def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

def list(request):
    diseases = Diseases.objects.all()
    context = {'diseases': diseases}
    return render(request, 'list.html', context)

def detail(request, pk):
    disease = get_object_or_404(Diseases, pk=pk)
    context = {'disease': disease}
    return render(request, 'detail.html', context)

def home(request):
    stats = GoatStatistics.objects.last()
    # reset การวินิจฉัยเก่า
    if 'last_prediction' in request.session:
        del request.session['last_prediction']
        del request.session['last_symptoms']
        del request.session['other_diseases']
    return render(request, 'home.html', {'stats': stats})


def result(request):
    return render(request, 'result.html', {
        'prediction_with_proba': request.session.get('last_prediction', []),
        'symptoms': request.session.get('last_symptoms', []),
    })

# ------------------------
# ฟังก์ชันสำหรับโรค "อื่นๆ"
# ------------------------
def other_diseases(request):
    other_diseases = request.session.get('other_diseases', [])
    disease_name_map = {
        'meli': 'โรคเมลิออยด์',
        'Anth': 'โรคแอนแทรกซ์',
        'bp': 'โรคปอดบวมจากแบคทีเรีย',
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

    mapped_diseases = []
    for code, prob in other_diseases:
        disease_name = disease_name_map.get(code, code)
        try:
            disease_obj = Diseases.objects.get(title=disease_name)
            mapped_diseases.append({
                'pk': disease_obj.pk,
                'title': disease_obj.title,
                'prob': prob,
                'image': disease_obj.image.url if disease_obj.image else "disease/default.png"
            })
        except Diseases.DoesNotExist:
            mapped_diseases.append({
                'pk': None,
                'title': disease_name,
                'prob': prob,
                'image': "disease/default.png"
            })

    return render(request, 'other.html', {'other_diseases': mapped_diseases})
