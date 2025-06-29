import pandas as pd
import numpy as np
import sys 
sys.stdout.reconfigure(encoding='utf-8')

features = {
    "ซึม": 0.8,
    "เบื่ออาหาร": 0.8,
    "ไข้": 0.9,
    "ผอมลง": 0.6,
    "ตัวสั่น": 0.2,
    "ตายเฉียบพลัน": 0.4,
    "ขนร่วง": 0.1,
    "คอตก": 0.3,
    "เดินวน/เดินมึน": 0.1,
    "ยืนลำบาก/เดินไม่ได้": 0.4,
    "ไอ": 0.3,
    "หายใจลำบาก": 0.3,
    "มีน้ำมูก": 0.2,
    "ถ่ายเหลวผิดปกติ": 0.2,
    "ถ่ายเป็นเลือด": 0.1,
    "ขี้สีดำ/เขียวผิดปกติ": 0.1,
    "กลิ่นปากแรง": 0.2,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.4,
    "แผลบริเวณผิวหนัง": 0.5,
    "ผิวหนังตกสะเก็ด": 0.4,
    "แผลบริเวณปาก/ลิ้น": 0.3,
    "น้ำลายไหลผิดปกติ": 0.3,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.4,
    "เต้านมอักเสบ": 0.2,
    "ต่อมน้ำเหลืองโต": 0.6,
    "บวมใต้คาง": 0.3,
    "ข้อบวม": 0.3,
    "แผลบริเวณขา/กีบ": 0.5,
}

def generate_data(disease_name, feature_prob, n_sample=100):
    data= []
    for _ in range(n_sample):
        sample= {}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand()< prob else 0
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

data = generate_data("meli", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/meli.csv", index=False, encoding='utf-8-sig')