import pandas as pd 
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

features = {
    "ซึม": 0.9,
    "เบื่ออาหาร": 0.8,
    "ไข้": 0.95,
    "ผอมลง": 0.3,
    "ตัวสั่น": 0.4,
    "ตายเฉียบพลัน": 0.95,
    "ขนร่วง": 0.05,
    "คอตก": 0.3,
    "เดินวน/เดินมึน": 0.1,
    "ยืนลำบาก/เดินไม่ได้": 0.4,
    "ไอ": 0.1,
    "หายใจลำบาก": 0.2,
    "มีน้ำมูก": 0.05,
    "ถ่ายเหลวผิดปกติ": 0.2,
    "ถ่ายเป็นเลือด": 0.6,
    "ขี้สีดำ/เขียวผิดปกติ": 0.5,
    "กลิ่นปากแรง": 0.2,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.01,
    "แผลบริเวณผิวหนัง": 0.1,
    "ผิวหนังตกสะเก็ด": 0.05,
    "แผลบริเวณปาก/ลิ้น": 0.05,
    "น้ำลายไหลผิดปกติ": 0.1,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.05,
    "ขี้ตาเยอะ/ตาแฉะ": 0.05,
    "เดินกะเผลก": 0.1,
    "เต้านมอักเสบ": 0.05,
    "ต่อมน้ำเหลืองโต": 0.4,
    "บวมใต้คาง": 0.5,
    "ข้อบวม": 0.1,
    "แผลบริเวณขา/กีบ": 0.1,
}

def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample= {}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand()< prob else 0
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

data = generate_data("Anth", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/anthrax.csv", index=False, encoding='utf-8-sig')