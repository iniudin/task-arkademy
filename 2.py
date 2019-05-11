import re

# use regex for validation.
# Test on Python3.7
# Code Formatter : Black


def check_username(username: str):
    # ^[a-z.]{8,8}$, ^ mulai dari, a-z . kombinasi huruf kecil dan titik, panjang 8
    result = re.match(r"^[a-z.]{8,8}$", username)
    if result:
        return True
    else:
        return False


def check_email(email: str):
    # (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$){,4})
    # (user    +         @  + domain    + . com, net, co.id etc.) minimal 4
    result = re.match(
        r"((^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$){,4})", email
    )
    if result:
        return True
    else:
        return False


username = check_username("h.lohalo")
print(username)
email = check_email("sysfdn@gmail.com")
print(email)
