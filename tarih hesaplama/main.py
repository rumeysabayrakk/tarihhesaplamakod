from datetime import datetime

# İlk tarih aralığı
start1 = datetime(2001, 5, 9)
end1 = datetime(2023, 6, 16)

# İkinci tarih aralığı
start2 = datetime(2001, 5, 9)
end2 = datetime(2023, 6, 16)

# İki aralığın kesişimi
intersection_start = max(start1, start2)
intersection_end = min(end1, end2)

# Kesişimin kontrolü ve kesişim aralığı
if intersection_start <= intersection_end:
    intersection_duration = intersection_end - intersection_start
    print("İki aralık kesişmektedir.")
    print("Kesişim Aralığı:", intersection_start, "-", intersection_end)
    print("Kesişim Süresi:", intersection_duration)
else:
    print("İki aralık kesişmemektedir.")
