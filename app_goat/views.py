import joblib
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Diseases, GoatStatistics

# โหลดโมเดล
model = joblib.load('path/to/your/trained_model.pkl')  

# ฟังก์ชันการวินิจฉัยโรค
def diagnosis(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms[]')  # รับข้อมูลอาการจากฟอร์ม
        
        # กำหนดอาการทั้งหมดที่ใช้ในการฝึกโมเดล (ตัวอย่าง)
        all_possible_symptoms = ["ซึม", "เบื่ออาหาร", "ไข้", "ผอมลง", "ตัวสั่น",
                                 "ตายเฉียบพลัน", "ขนร่วง", "คอตก", "เดินวน/เดินมึน", "ยืนลำบาก/เดินไม่ได้"
                                 "ไอ", "หายใจลำบาก", "มีน้ำมูก", "ถ่ายเหลวผิดปกติ", "ถ่ายเป็นเลือด"
                                 "ขี้สีดำ/เขียวผิดปกติ", "กลิ่นปากแรง", "ตุ่มใส/ตุ่มหนองผิวหนัง", "แผลบริเวณผิวหนัง", "ตัวสั่น"
                                 "ผิวหนังตกสะเก็ด", "แผลบริเวณปาก/ลิ้น", "น้ำลายผิดปกติ", "ตาแดง", ""
                                 "น้ำตาไหลผิดปกติ", "ขี้ตาเยอะ/ตาแฉะ", "เดินกะเผลก", "เต้านมอักเสบ", "ต่อมน้ำเหลืองโต",
                                 "บวมใต้คาง","ข้อบวม","แผลบริเวณขา/กีบ",]  # อาจต้องเพิ่มข้อมูลตามที่ใช้ฝึกโมเดล
        
        # แปลงข้อมูลที่รับเข้ามาเป็น feature vector
        symptoms_vector = [1 if symptom in symptoms else 0 for symptom in all_possible_symptoms]
        
        # ทำนายโรคโดยใช้โมเดล
        prediction = model.predict([symptoms_vector])

        # ส่งผลลัพธ์กลับไป
        return JsonResponse({'prediction': prediction[0]})

    return render(request, 'diagnosis.html')

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
