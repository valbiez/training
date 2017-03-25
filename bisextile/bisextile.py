

def is_bisextile(annee):
    est_divisible_par_4 = (annee % 4 == 0)
    est_divisible_par_100 = (annee % 100 == 0)
    est_divisible_par_400 = (annee % 400 == 0)

    if est_divisible_par_4:
        if est_divisible_par_100:
            if est_divisible_par_400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    annee = int(input("annee: "))
    if is_bisextile(annee):
        print("bistextile")
    else:
        print("pas bistextile")
