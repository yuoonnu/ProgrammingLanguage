def celsius_to_fahrenheit(celsius):
    """섭씨(C) 온도를 화씨(F) 온도로 변환합니다."""
    # 공식: (C × 9/5) + 32
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """화씨(F) 온도를 섭씨(C) 온도로 변환합니다."""
    # 공식: (F - 32) × 5/9
    return (fahrenheit - 32) * 5/9

def km_to_miles(kilometers):
    """킬로미터(km)를 마일(mi)로 변환합니다."""
    # 1 km ≈ 0.621371 miles
    return kilometers * 0.621371

def miles_to_km(miles):
    """마일(mi)을 킬로미터(km)로 변환합니다."""
    # 1 mile ≈ 1.60934 kilometers
    return miles * 1.60934
