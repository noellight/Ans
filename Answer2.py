def search_index(sorted_array, target_number):
    # ここから記述
    current_left = 0
    current_right = len(sorted_array)
    current_middle = (current_right + current_left) // 2
    # 探索対象が存在しない場合、-1を返却
    while True:
        if (sorted_array[current_middle] == target_number):
            return current_middle
        elif (sorted_array[current_middle + 1] == target_number):
            return current_middle + 1
        elif (current_left + 1 == current_right):
            return -1
        elif (sorted_array[current_middle] > target_number):
            current_right = current_middle
            current_middle = (current_right + current_left) // 2
        else:
            current_left = current_middle
            current_middle = (current_right + current_left) // 2
    # ここまで記述
def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = search_index(sorted_array, target_number)
    # 結果出力
    print(target_index)
if __name__ == '__main__':
    main()