def solution(array):
    array.sort()  # 오름차순 정렬
    return array[len(array) // 2]

# len(): 객체의 길이(요소의 개수)를 반환