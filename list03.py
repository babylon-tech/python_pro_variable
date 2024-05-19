# 2. 「変数の有効範囲を狭くして、簡単な変数名にできないか」を考える
def show_target_income(name_data, income_data, target=10000, top=2):
    # リスト内包表記を使って書き換え
    name_and_income_tuples = [(name, income) for name, income in zip(name_data, income_data) if income >= target]
    tmp_name_data = [t[0] for t in name_and_income_tuples]
    tmp_income_data = [t[1] for t in name_and_income_tuples]

    total_income = sum(sorted(tmp_income_data, reverse=True)[:top])

    print(tmp_name_data)
    print(total_income)

name_data = ['A', 'B', 'C', 'D']
income_data = [100000, 100000, 80000, 3600]
show_target_income(name_data, income_data)
