# Test on Python3.7
# Code Formatter : Black
def profile(
    name: str, address: str, hobbies: list, is_married: bool, school: dict, skills: list
):
    data = {
        "name": name,
        "address": address,
        "hobbies": hobbies,
        "is_married": is_married,
        "school": school,
        "skills": skills,
    }
    return data


biodata = profile(
    name="Ahmad Syaifudin",
    address="Jln. Tirtowening Tanjungkenongo, Kec. Pacet, Kab. Mojokerto",
    hobbies=["Membaca", "Nonton Anime", "Mendengarkan Music"],
    is_married=False,
    school={"highSchool": "MA Hikmatul Amanah", "university": None},
    skills=[
        {"name": "Python3", "score": 8},
        {"name": "Go", "score": 6},
        {"name": "Web Dev", "score": 7},
    ],
)

print(biodata)
