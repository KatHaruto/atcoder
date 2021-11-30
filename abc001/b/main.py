m_km = float(input()) / 1000
if m_km < 0.1:
    print("00")
elif m_km <= 5:
    print(int(m_km * 10) if m_km * 10 >= 10 else "0" + str(int(m_km * 10)))
elif 6 <= m_km <= 30:
    print(int(m_km) + 50)
elif 35 <= m_km <= 70:
    print(int((m_km - 30) / 5 + 80))
elif m_km >= 70:
    print(89)
