# 선택 정렬 알고리즘 함수로 구현하기
# 시간 복잡도를 측정하기 위해 time 라이브러리 임포트
import time

# 선택 정렬 함수
def selection_sort(arr: list):
    # 리스트의 길이를 변수에 담는다.
    n = len(arr)

    # 정렬 시작 전 타임 스탬프 변수에 현재 시간 저장
    start = time.time()

    # 정렬 시작
    # 리스트의 전체 길이만큼 외부 반복
    for i in range(n):
        # 현재 외부 반복의 인덱스를 내부반복의 시작인덱스로 설정
        min_idx = i
        # i+1부터 n번째까지 i번째 값과 비교를 하여
        # 가장 작은 값을 가진 인덱스를 찾아오는 내부 반복문
        for j in range(i+1, n):
            # j번째 요소가 min_idx번째 요소보다 작으면
            if arr[j] < arr[min_idx]:
                # j를 min_idx로 설정
                min_idx = j
        # 가장 작은 값을 가진 인덱스 요소를 찾았으므로
        # min_idx의 값을 i번째 요소와 그 위치를 교환
        # 그 결과 i번째의 값은 i부터 n번째 요소들 중
        # 가장 작은 값이 될 것이다.
        # 교환하는 코드
        # 1. 실시간 맞교환이 안 되는 경우의 코드
        # min_value = arr[min_idx]
        # arr_i = arr[i]
        # arr[i] = min_value
        # arr[min_idx] = arr_i
        # 2. 실시간 맞교환을 하는 코드
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # 정렬 끝, 현재시간 저장
    end = time.time()

    # 정렬하는 데 걸린 시간 출력
    print(f"걸린 시간: {end - start}")

    # 전달받은 리스트 객체를 직접 수정해서
    # 반환한다.
    return arr

if __name__ == "__main__":
    # 데이터를 섞기 위한 랜덤 라이브러리 임포트
    import random
    # 데이터 생성
    data = [e for e in range(20000)]
    # 데이터 셔플
    random.shuffle(data)
    # print(data) # 데이터 확인
    result = selection_sort(data) # 걸린 시간 확인
    # print(result) # 결과 확인