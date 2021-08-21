import sys
from collections import defaultdict, deque

sys.stdin = open("./baekjoon/testcase.txt")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 1단계: 각 부품 별로 필요한 하위 부품을 파악
# - 각 상위 부품을 만드는 데 필요한 하위 부품을 필요한 개수 만큼 배열에 저장
# - 가령, {상위: [(하위1, 2), (하위2, 3), (하위3, 1)]}
# - 이 때, adj에 key로 등록되지 않은 부품은 더 이상 분리될 수 없는 기본 부품을 의미
adj = defaultdict(list)
for _ in range(M):
    x, y, k = tuple(map(int, sys.stdin.readline().split()))
    # x를 만드는데 하위 부품 y가 필요한 개수만큼 인접 리스트에 추가
    adj[x].append((y, k))

# 2단계: 최종 제품을 만들기 위해 필요한 기본 부품 세기
# 누적된 기본 부품을 세는 dict 초기화
subitems = defaultdict(int)
# 최종 제품으로 frontier 초기화
s = N
frontier = deque([(s, 1)])
while frontier:
    # 부품 v1, 필요한 개수 k1
    v1, k1 = frontier.popleft()
    # v1의 각 하위 부품을 확인
    for v2, k2 in adj[v1]:
        # v2가 인접 리스트에 없는 경우, 기본 부품이므로 더 이상 분리 불가
        if v2 not in adj:
            # 기본 부품 개수에 누적 후 다음 부품으로 넘어감
            subitems[v2] += k1*k2
        # v2가 인접 리스트에 있는 경우, 추가 분리가 필요
        else:
            # 이 때, v1을 1개 만들기 위해 v2가 k2개 필요하므로,
            # v1을 k1개 만들기 위해서는 v2가 k1*k2개 필요
            frontier.append((v2, k1*k2))

# 누적된 기본 부품 개수 출력
for i in range(1, N+1):
    if i in subitems:
        print(i, subitems[i])

