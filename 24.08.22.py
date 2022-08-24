from statistics import mean
import numpy as np


# Задание 1

# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением,
# равным 16. Найти доверительный интервал для оценки математического ожидания а с надежностью 0.95, если выборочная средняя М = 80,
# а объем выборки n = 256

sigma1 = 16
p1 = 0.95
M1 = 80
n1 = 256
alpha1 = 1 - p1
# так как известно СКО, то будем пользоваться критерием Лапласа

# найдем стандартную ошибку среднего
sr_oshibka = sigma1/(n1)**0.5

# так как мы имеем нормальное распределение, то можно использовать половину значений, поэтому рассчитаем z по таблице
# Лапласа для значения alpha/2 = 0.025

z1 = -1.96

#  Теперь рассчитаем доверительный интервал

p_granica1 = M1 - z1 * sr_oshibka
l_granica1 = M1 + z1 * sr_oshibka

print(f"Ответ задачи 1: [{l_granica1}, {p_granica1}] - интервал, который с вероятностью 95% покрывает истинное M(x) = a генеральной совокупности")

# Задание 2

# В результате 10 независимых измерений некоторой величины Х, выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение
# величины Х при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0.95.

list2 = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
p2 = 0.95
alpha2 = 1 - p2
n2 = 10
M2 = mean(list2)

# Независимые испытания выполнены с одинаковой точностю => это нормальное распределение
# Так как СКО неизвестно, следовательно будем пользоваться критерием Стьюдента
# Для начала найдем несмещенную дисперсию

dispersia2 = np.std(list2, ddof=1)
sigma2 = dispersia2**0.5


# Найдем необходимыe параметры для критерия Стьюдента

k2 = n2 - 1
p2 = 1 - alpha2/2

SE2 = sigma2/n2**0.5

# Запишем полученное значение

t2 = 2.262

# Найдем границы интервала

l_granica_2 = M2 - t2*SE2
p_granica_2 = M2 + t2*SE2

print(f"Ответ задачи 2: [{round(l_granica_2, 4)}, {round(p_granica_2, 4)}] - интервал, который с вероятностью 95% покрывает истинное M(x) = a значение величины Х")


# Задача 3
# Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм
# Используя одностронний критерий с alpha = 0.05, проверить эту гипотезу, если в выборке из n = 100 шариков
# средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм

# Примем значение 17 мм за нулевую гипотезу.

mu_0_3 = 17

# А значение 17.5 мм за альтернативную гипотезу.

mu_3 = 17.5

alpha3 = 0.05
n3 = 100
d3 = 4
sigma3 = 2

# Найдем стандартную ошибку среднего

sr_oshibka_3 = sigma3/n3**0.5

# Так как нам известно СКО, то работаем по стандартной таблице
# Найдем расчетное значение

z_rasch_3 = (mu_3 - mu_0_3)/ sr_oshibka_3
z_tabl_3 = 1.65

if z_rasch_3 > z_tabl_3:
    print(f"Ответ задачи 3 : Отвергаем гипотезу Н0, принимаем альтернативную Н1, среднее значение {mu_3}")
else:
    print(f"Ответ задачи 3 : Верна гипотеза Н0, среднее значение {mu_0_3}")

# Задача 4
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190
# Известно, что их веса распределены нормально
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?

# Примем значение 200 г за нулевую гипотезу.
mu_0_4 = 200

n4 = 10
list4 = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

M = mean(list4)
dispersia4 = np.std(list4, ddof=1)
sigma4 = dispersia4**0.5

# Так как неизвестно СКО, будем использовать критерий Стьюдента

z_tabl_4 = 2.821

# Найдем стандартную ошибку среднего

sr_oshibka_4 = sigma4/n4**0.5

z_rasch_4 = (M - mu_0_4)/sr_oshibka_4

if z_rasch_4 > z_tabl_4:
    print(f"Ответ задачи 4 : Отвергаем гипотезу Н0, принимаем альтернативную Н1, среднее значение {M}")
else:
    print(f"Ответ задачи 4 : Верна гипотеза Н0, среднее значение {mu_0_4}")


