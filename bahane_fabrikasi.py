#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bürokratik Gecikme Bahanesi Fabrikası
Türkiye Cumhuriyeti Devleti'nin en önemli ve anlamsız yazılım projesidir.
Bu program, işe geç kalmanız için son derece resmi, anlamsız ve inandırıcı bahaneler üretir.
"""

import random
import time

def bahane_uret():
    kisiler = [
        "Devlet Daireleri Arası Koordinasyon Kurulu",
        "Bürokratik İşlemler Üst Komitesi",
        "Gecikme İnceleme ve Onay Birimi",
        "Resmi Olmayan Resmi Mazeret Komisyonu",
        "Vatandaşın Geç Kalma Hakkını Koruma Derneği"
    ]
    
    eylemler = [
        "dosyanızın yanlış çekmeceye konulması nedeniyle",
        "mühürün mürekkebinin kurumaması sebebiyle",
        "imza yetkilisinin çay molasında olması hasebiyle",
        "evrakların fotokopi makinesinde sıkışması neticesinde",
        "sistemin güncellenmesi adına geçici olarak kapatılması yüzünden",
        "ilgili birimin toplantıda olması dolayısıyla",
        "mühürün kaybolması ve bulunması sürecinin devam etmesi nedeniyle"
    ]
    
    sonuclar = [
        "işleminiz 3-5 iş günü içinde sonuçlanacaktır.",
        "konuyla ilgili detaylı inceleme başlatılmıştır.",
        "başvurunuz kayıtlara alınmış olup sıraya konulmuştur.",
        "durumunuz üst makamlara arz edilmiştir.",
        "işleminiz öncelikli olarak değerlendirilecektir (belki)."
    ]
    
    kisi = random.choice(kisiler)
    eylem = random.choice(eylemler)
    sonuc = random.choice(sonuclar)
    
    bahane = f"Sayın yetkili, {kisi} tarafından bildirilen şu nedenle işe geç kalınmıştır: {eylem} {sonuc}"
    
    # Bürokratik bekletme efekti
    print("Bahaneniz üretiliyor...")
    for i in range(3):
        time.sleep(1)
        print("." * (i+1))
    
    return bahane

if __name__ == "__main__":
    print("=" * 60)
    print("BÜROKRATİK GECİKME BAHANESİ FABRİKASI v1.0")
    print("Resmi Onay: 2026/10/28 - Kayyum Grok")
    print("=" * 60)
    print()
    print(bahane_uret())
    print()
    print("Not: Bu bahane %100 gerçekçi değildir ama %200 bürokratiktir.")
    print()
    print("Damga: [RESMİ OLMAYAN RESMİ MÜHÜR]")
    print("İmza: Kayyum Grok (Tentivory)")
    print("Tarih: 28 Ekim 2026")
    print("Yer: Türkiye - Devlet Daireleri Arası Koordinasyon Boşluğu")
