# 3. 最後に、「良い名前」を考える
def show_target_income(names, incomes, income_threshold=10000, top_income_count_for_sum=2):
    selected_name_and_income_tuples = [(name, income) for name, income in zip(names, incomes) if income >= income_threshold]
    selected_names = [t[0] for t in selected_name_and_income_tuples]
    selected_incomes = [t[1] for t in selected_name_and_income_tuples]

    top_total_income = sum(sorted(selected_incomes, reverse=True)[:top_income_count_for_sum])

    print(selected_names)
    print(top_total_income)

name_data = ['A', 'B', 'C', 'D']
income_data = [100000, 100000, 80000, 3600]
show_target_income(name_data, income_data)
