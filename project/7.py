import random
from tabulate import tabulate

def monte_carlo_dice_simulation(num_rolls=1000000):
    """
    Функція імітує кидання двох гральних кубиків num_rolls разів.
    Вона підраховує частоту випадіння кожної можливої суми (від 2 до 12) 
    та обчислює її ймовірність.

    Параметри:
    num_rolls (int): Кількість кидків кубиків (за замовчуванням 1 000 000)

    Повертає:
    dict: Словник, де ключі - можливі суми, значення - ймовірності їх випадіння.
    """
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симуляція кидків кубиків
    for _ in range(num_rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        sums_count[dice_sum] += 1
    
    # Обчислення ймовірностей у відсотках
    probabilities = {key: (value / num_rolls) * 100 for key, value in sums_count.items()}
    return probabilities

# Аналітичні ймовірності для двох кубиків
analytical_probs = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Запуск симуляції
monte_carlo_results = monte_carlo_dice_simulation(1000000)

# Формування таблиці для виводу
data = [
    [sum_, analytical_probs[sum_], monte_carlo_results[sum_]]
    for sum_ in analytical_probs.keys()
]

# Вивід таблиці в консоль
print(tabulate(data, headers=["Сума", "Аналітична ймовірність (%)", "Монте-Карло ймовірність (%)"], tablefmt="grid"))
