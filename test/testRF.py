import joblib as jb 
import numpy as np

model = jb.load("test/RF_model.pkl")
le = jb.load("test/label_encoder.pkl")

thai_questions = [
    "แพะซึมหรือไม่?", "แพะเบื่ออาหารหรือไม่?", "มีไข้หรือไม่?", "ผอมลงรวดเร็วหรือไม่?",
    "ตัวสั่นหรือไม่?", "ตายเฉียบพลันหรือไม่?", "ขนร่วงผิดปกติหรือไม่?", "คอตกหรือไม่?",
    "เดินวน/เดินมึนหรือไม่?", "ยืนลำบาก/ล้มง่ายหรือไม่?", "ไอหรือไม่?", "หายใจลำบากหรือไม่?",
    "มีน้ำมูกผิดปกติหรือไม่?", "ถ่ายเหลวผิดปกติหรือไม่?", "ถ่ายเป็นเลือดหรือไม่?",
    "ขี้สีดำหรือเขียวผิดปกติหรือไม่?", "มีกลิ่นปากแรงหรือไม่?", "มีตุ่มหนอง/ตุ่มใสที่ผิวหนังหรือไม่?",
    "มีแผลตามลำตัวหรือไม่?", "ผิวหนังตกสะเก็ดหรือไม่?", "มีแผลบริเวณปาก/ลิ้นหรือไม่?",
    "น้ำลายไหลผิดปกติหรือไม่?", "ตาแดงหรือไม่?", "น้ำตาไหลมากผิดปกติหรือไม่?",
    "ขี้ตาเยอะ/ตาแฉะหรือไม่?", "เดินกะเผลกหรือไม่?", "เต้านมอักเสบ/แข็งหรือไม่?",
    "ต่อมน้ำเหลืองโตหรือไม่?", "บวมใต้คางหรือไม่?", "ข้อบวมหรือไม่?", "มีแผลบริเวณขา/กีบหรือไม่?"
]

print("Please answer question")
input_user = []
for q in thai_questions:
    while True:
        val = input(f"{q} (0/1): ")
        if val in['0', '1'] :
            input_user.append(int(val))
            break
        else :
            print("Please answer 0 or 1")

input_user = np.array([input_user])
input_user_2d= input_user.reshape(1, -1)
pred_index = model.predict(input_user_2d) [0]
pred_label = le.inverse_transform([pred_index]) [0]
probs = model.predict_proba(input_user_2d)[0]
pred_prob= probs[pred_index]*100    

print(f"\n โรคืั้คาดว่าเป็นมากที่สุด : **{pred_label}** ({pred_prob:.2f}%)")
print(f"\n โอกาสแต่ละโรค:")
for i,p  in enumerate(probs):
    print(f"- {le.classes_[i]} : {p*100:.2f}%")