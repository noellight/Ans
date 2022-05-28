def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in array]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    print("len:{}".format(len(array)))
    if len(array) == 1:
        return array
    # 配列の先頭を基準値とする
    pivot = array[0]
    # ここから記述
    left = 0
    right = len(array)-1
    temp = array[0]
    array[0] = array[len(array)//2]
    array[len(array)//2] = temp
    while True:
        while True:
            if left >= right:
                break
            elif array[left] > pivot:
                break
            else:
                left += 1
        while True:
            if left >= right:
                break
            elif array[right] < pivot:
                break
            else:
                right -= 1
        if left >= right:
            break
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    print("current:",end="")
    for element in array:
        print(element,end=",")
    print()
    sort(array[0:left])
    sort(array[left:len(array)])
    # ここまで記述

if __name__ == '__main__':
    main()