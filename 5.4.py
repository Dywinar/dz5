resh_algebra = set(input("Кто решил задачу по алгебре: ").split(" "))
resh_geom   = set(input("Кто решил задачу по геометрии: ").split(" "))
resh_trigon = set(input("Кто решил задачу по тригонометрии").split(" "))
resh_2olimp = resh_algebra.intersection(resh_geom)
resh_3olimp = resh_2olimp.intersection(resh_trigon)
if len(resh_3olimp) != 0:
  print(" ".join(sorted(resh_3olimp)))
else:
  print("Все три задачи никто не решил")
