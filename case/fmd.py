import pandas as pd
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')


#feature อาการ
features = {
    "ซึม": 0.9,
    "เบื่ออาหาร": 0.9,
    "ไข้": 0.95,
    "ผอมลง": 0.4,
    "ตัวสั่น": 0.2,
    "ตายเฉียบพลัน": 0.1,
    "ขนร่วง": 0.1,
    "คอตก": 0.3,
    "เดินวน/เดินมึน": 0.05,
    "ยืนลำบาก/เดินไม่ได้": 0.3,
    "ไอ": 0.05,
    "หายใจลำบาก": 0.05,
    "มีน้ำมูก": 0.2,
    "ถ่ายเหลวผิดปกติ": 0.2,
    "ถ่ายเป็นเลือด": 0.01,
    "ขี้สีดำ/เขียวผิดปกติ": 0.05,
    "กลิ่นปากแรง": 0.2,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.4,
    "แผลบริเวณผิวหนัง": 0.1,
    "ผิวหนังตกสะเก็ด": 0.05,
    "แผลในปาก/ลิ้น": 0.98,
    "น้ำลายไหลผิดปกติ": 0.95,
    "ตาแดง": 0.05,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.95,
    "เต้านมอักเสบ": 0.05,
    "ต่อมน้ำเหลืองโต": 0.1,
    "บวมใต้คาง": 0.05,
    "ข้อบวม": 0.01,
    "แผลบริเวณขา/กีบ": 0.98,
}


def generate_data(disease_name, feature_prob, n_sample=100):
    data = []
    for _ in range(n_sample):
        sample={}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand() < prob else 0
        sample["disease"] = disease_name
        data.append(sample)
    return pd.DataFrame(data)

df_disease = generate_data("FMD", features, n_sample=100)

print(df_disease.head())

print(df_disease.drop(columns="disease").mean()*100)

df_disease.to_csv("case/FMD.csv", index=False, encoding='utf-8-sig')