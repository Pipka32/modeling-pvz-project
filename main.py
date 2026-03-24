import random

# Часть 2. Математическая формализация 
# Определяем факторы (переменные) 
CLIENTS = 40          # Интенсивность (сколько человек придет) 
STAFF_CAPACITY = 10   # Среднее время обслуживания одного человека 
def run_simulation(n_staff):
    # N — количество сотрудников (управляющий параметр) 
    total_wait = 0
    for _ in range(CLIENTS):
        # Имитируем случайное время ожидания
        wait = random.uniform(1, STAFF_CAPACITY) / n_staff
        total_wait += wait
    
    # Выходная метрика: среднее время ожидания 
    return round(total_wait / CLIENTS, 2)

print("Результаты эксперимента для проекта:")
# Запускаем симуляцию для разного количества сотрудников 
for n in [1, 2, 3]:
    avg_wait = run_simulation(n)
    print(f"При {n} сотр. среднее время ожидания: {avg_wait} мин.")