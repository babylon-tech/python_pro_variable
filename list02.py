# 1. 「変数を使わずに書けないか」を考える
def show_target_income(name_data, income_data, target=10000, top=2):
    tmp_name_data = []
    tmp_income_data = []
    # 組み込み関数のzip関数を使って書き換え
    for tmp_name, tmp_income in zip(name_data, income_data):
        if tmp_income >= target:
            tmp_income_data.append(tmp_income)
            tmp_name_data.append(tmp_name)

    # Pythonのスライス機能とメソッドチェーンを使って書き換え
    total_income = sum(sorted(tmp_income_data, reverse=True)[:top])

    print(tmp_name_data)
    print(total_income)

name_data = ['A', 'B', 'C', 'D']
income_data = [100000, 100000, 80000, 3600]
show_target_income(name_data, income_data)
