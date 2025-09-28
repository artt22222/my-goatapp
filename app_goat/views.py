import joblib
import os
import traceback
from django.conf import settings
from django.urls import reverse
from django.templatetags.static import static
from django.shortcuts import render, redirect, get_object_or_404
from .models import Diseases, GoatStatistics
from django.contrib import messages


# ฟังก์ชันวินิจฉัยโรค
def diagnosis(request):
    if request.method == 'POST':
        try:
            symptoms = request.POST.getlist('symptoms[]')
            print("อาการที่รับจากผู้ใช้:", symptoms)

            model = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'model_Rf5.pkl'))
            label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'label_encoder5.pkl'))
            feature_names = joblib.load(os.path.join(settings.BASE_DIR, 'test', 'feature_names5.pkl'))

            symptoms_vector = [1 if symptom in symptoms else 0 for symptom in feature_names]
            print("เวกเตอร์ที่ส่งเข้าโมเดล:", symptoms_vector)

            # คำนวณความน่าจะเป็น
            proba = model.predict_proba([symptoms_vector])[0]
            class_labels = label_encoder.inverse_transform(range(len(proba)))

            # zip + sort
            zipped = sorted(zip(class_labels, proba * 100), key=lambda x: x[1], reverse=True)

            # แยกตัวที่ >= 5% กับ < 5%
            kept = [(label, p) for label, p in zipped if p >= 7]
            removed = [(label, p) for label, p in zipped if p < 7]

            removed_sum = sum(p for _, p in removed)

            # เอา top3 จาก kept
            top3 = kept[:3]
            other_list = kept[3:]

            # ถ้ามี removed_sum ก็ redistribute เข้า top3
            if top3 and removed_sum > 0:
                total_top3 = sum(p for _, p in top3)
                redistributed = []
                for label, p in top3:
                    # คำนวณสัดส่วนใหม่
                    extra = (p / total_top3) * removed_sum
                    redistributed.append((label, p + extra))
                top3 = redistributed

            # รวมเปอร์เซ็นต์ที่เหลือทั้งหมด
            other_sum = sum(p for _, p in other_list)
            final_result = top3 + [("อื่นๆ", other_sum)]

            # normalize ให้รวม 100%
            total_sum = sum(p for _, p in final_result)
            final_result = [(label, round(p / total_sum * 100, 2)) for label, p in final_result]
            print("ผลลัพธ์สุดท้าย:", final_result)


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
            messages.error(request, f"เกิดข้อผิดพลาด: {str(e)}")
            return redirect('result')


    else:
        if 'last_prediction' in request.session:
            return render(request, 'result.html', {
                'prediction_with_proba': request.session['last_prediction'],
                'symptoms': request.session.get('last_symptoms', [])
            })
        else:
            return render(request, 'form.html')



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

    # ตรวจสอบ referrer
    referrer = request.META.get('HTTP_REFERER', '')
    if 'list' in referrer:
        request.session['back_from'] = 'list'
    else:
        request.session['back_from'] = 'result'  # fallback ถ้าเข้ามาโดยตรง

    context = {
        'disease': disease,
        'back_from': request.session['back_from'],  # ส่งไป template ด้วย
    }
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


