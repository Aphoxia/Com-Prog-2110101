import math

def mosteller(w,h):
    result = math.sqrt(w * h) / 60
    return result

def du_bois (w,h):
    result = 0.007184 * (w ** 0.425) * (h ** 0.725)
    return result

def fujimoto (w,h):
    result = 0.008883 * ( w ** 0.444) * (h ** 0.663)
    return result

def main():
    w = float(input()) # body Weight
    h = float(input()) # Height
    Mosteller = mosteller(w,h)
    Du_Bois = du_bois(w,h)
    Fujimoto = fujimoto(w,h)
    print(f"""Mosteller = {Mosteller:.5f}
Du_Bois = {Du_Bois:.5f}
Fujimoto = {Fujimoto:.5f}""")
    
exec(input())
