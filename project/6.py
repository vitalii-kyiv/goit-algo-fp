def greedy_algorithm(items, budget):
    # Сортуємо їжу за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_calories = 0
    total_cost = 0
    
    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(name)
            total_calories += info['calories']
            total_cost += info['cost']
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(items)
    
    # DP таблиця
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення вибраних страв
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]
    
    return selected_items, dp[n][budget]


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 60

print("Жадібний алгоритм:", greedy_algorithm(items, budget))
print("Динамічне програмування:", dynamic_programming(items, budget))
