def show_target_income(name_data, income_data, target=10000, top=2):
    tmp_name_data = []
    tmp_income_data = []
    for income_idx in range(len(income_data)):
        tmp_income = income_data[income_idx]
        if tmp_income >= target:
            tmp_income_data.append(income_data[income_idx])
            tmp_name = name_data[income_idx]
            tmp_name_data.append(tmp_name)

    tmp_income_data2 = sorted(tmp_income_data, reverse=True)
    top_income_data = []
    for income_idx in range(len(tmp_income_data2)):
        if income_idx < top:
            tmp_income = tmp_income_data2[income_idx]
            top_income_data.append(tmp_income)
    total_income = sum(top_income_data)

    print(tmp_name_data)
    print(total_income)

name_data = ['A', 'B', 'C', 'D']
income_data = [100000, 100000, 80000, 3600]
show_target_income(name_data, income_data)
