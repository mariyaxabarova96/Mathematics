n = (100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150)
m = len(n)

#рассчитаем среднее арифмитическое

sred_arifm = sum(n)/m

#рассчитаем СКО

kvadrat = 0
for i in n:
    j = (i - sred_arifm)**2
    kvadrat = kvadrat + j
sko = (kvadrat/m)**(0.5)

#рассчитаем смещенную оценку дисперсии

smesh_dispers = sko**2

#рассчитаем несмещенную оценку дисперсии

kvadrat = 0
for i in n:
    j = (i - sred_arifm)**2
    kvadrat = kvadrat + j
nesmesh_dispers = (kvadrat/(m-1))
print('Среднее арифмитическое значение: ', sred_arifm)
print('СКО: ', round(sko,4))
print('Смещенная оценка дисперсии: ', round(smesh_dispers, 4))
print('Несмещенная оценка дисперсии: ', round(nesmesh_dispers, 4))