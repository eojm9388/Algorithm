## 1206 View

조망권이 확보되기 위해서는 양쪽의 거리가 2인 부분에 빌딩이 가리지 않아야한다.

빌딩을 하나씩 순회하면서 양쪽 거리 2만큼의 숫자가 작은지를 확인해야한다.

만약 하나라도 자신보다 높은 빌딩이 있다면 조망권은 확보되지 않는다.

그 후 자신의 빌딩중에서 조망권이 확보된 세대의 수는 양쪽 거리 2만큼의 빌딩 중 제일 높은 빌딩을
자신의 빌딩 높이에서 뺀 만큼이다.

모든 빌딩을 순회하면서 조망권이 있는 세대수의 총합을 구한다.

## 4828 min max

숫자 리스트를 받아와 `max`와 `min` 메서드를 사용하여 최댓값과 최솟값을 구한다.

## 4835 구간합

M개의 이웃한 숫자의 합들 중 제일 작은 값과 큰 값을 구하는 문제

맨 처음에 비교할 값을 인덱스의 첫번째 값부터 시작했다.

리스트 슬라이싱을 하면서 이웃한 숫자들의 합을 구하고 최대, 최소값과 비교한다.

## 1208 Flatten

주어진 덤프 수만큼 가장 높은 박스의 박스를 가장 낮은 박스에 옮긴 후 높이차를 구하는 문제

먼저 박스의 높이별로 카운트를 한 리스트를 만들었다.

먼저 낮은 높이의 박스에 덤프를 하여 높이를 높여주고 다시 덤프를 수행해 높은 높이의 박스의 높이를 감소시켰다.

덤프가 마무리 된 후 가장 높은 높이의 박스와 낮은 박스의 차이를 구했다.

## 4834 숫자카드

카드가 나올 수 있는 제일 큰 수가 9이기 때문에 0부터 9까지 나온 카드의 개수를 셀 수 있는 리스트를 만든다.

나온 카드를 순회하면서 나온 카드를 카드 개수 리스트를 증가시킨다.

나온 카드의 최대 개수가 같다면 그 중 높은 카드의 숫자를 얻어야하기 때문에

카드 개수 리스트를 `reverse`하고 `index`로 찾아주었다.

나온 `index`를 9에 빼주면 가장 많이 나온 카드 중 제일 큰 수를 얻을 수 있다.

## 9490 풍선팡

풍선 배열의 모든 값을 비교해봐야하기 때문에 함수로 만들었다.

가로방향과 세로방향의 반복문을 따로 순회하여 꽃가루의 총합을 구했다.

만약 배열의 벗어나는 범위하면 `continue`로 스킵한다.

가운데 중앙값은 중복되므로 결과값에서 한번 빼주었다.

모든 풍선배열을 순회하면서 최대 꽃가루 총합을 구한다.

## 4831 전기버스

전기버스가 최소로 몇번 충전소를 거쳐야 도착지점에 가는지 문제

먼저 이동가능여부를 확인하는 코드를 함수로 만드는 것이 좋겠다고 생각하였다.

함수에서 확인해보아야할 것

- 전기버스가 도착지점에 도달했는가
- 전기버스의 이동거리내에 충전소가 있는가
- 만약 2개 이상이라면 제일 나중에 있는 충전소에서 충전하는것이 최소한으로 충전소를 간다.

함수에서 이동가능여부와 이동한 거리를 반환해주면 좋겠다고 생각함

반환값을 튜플로 맞춰주기 위해서 이동 불가에도 이동거리를 0으로 해서 줌

반복문을 돌면서 조건을 확인하며 이동거리를 다시 함수에 할당한다.

> 이동거리의 범위들과 횟수가 헷갈린다.

## 1979 어디에 단어가 들어갈 수 있을까

원하는 길이의 단어가 낱말풀이에 몇 개 들어갈 수 있는지 구하는 문제

세로와 가로를 구분해서 개수를 구하고 싶어 함수를 만들었다.

처음에는 원하는 길이를 제한조건으로 함수를 정의하였다.

- 제한범위를 설정하는데 너무 복잡함
- 조건이 계속 추가됨

다음으로 모든 빈칸의 개수를 세는 함수를 만들었다.

- 중복이 생긴다.

따라서 한줄에 찾을 수 있는 빈칸을 찾는 함수를 만듬

- 한줄의 빈칸의 개수가 여러개 있을 수 있음 `ex) [1, 3, 2]`
- 반환값을 리스트로 받았다.

한줄씩 보면서 빈칸을 찾으면 빈칸의 개수를 세면서 진행하고, 만약 빈칸이 아닌지점에 도달하면 빈칸 리스트에 추가한뒤, 빈칸의 개수를 초기화하고 다시 진행하였다.

> `while`문을 사용하였는데 마지막 순회에서 빈칸을 찾게되면 빈칸 리스트에 추가되지 못하는 문제 발생
>
> -> 빈칸의 개수를 추가는 코드를 마지막에 한번 더 넣어줌 (0은 한번 더 넣어줘도 상관없다.)

가로, 세로 한줄씩 N까지 반복하여 모든 빈칸의 개수 (연속된 빈칸의 길이)를 구한 뒤, 원하는 길이의 빈칸의 개수를 출력한다.

## 2001 파리퇴치

M범위를 파리채로 잡을 수 있는 최대 파리 수를 구하는 문제

각 좌표에 따라 잡을 수 있는 모기의 수를 구하는 함수를 만듬

M 크기만큼 중첩반복문을 사용하여 파리의 수를 구한다.

이 문제에선 범위가 중요한 듯

함수에서 따로 조건문을 사용하지 않고, 전체 좌표를 순회하는 반복문에서 범위를 제한하면 된다.

## 5789 현주의상자바꾸기

현주가 가지고 있는 숫자상자를 Q번 L에서 R까지 숫자를 바꾸는 문제

문제 그대로 풀면 풀린다.

## 1961 숫자 배열 회전

주어진 행렬을 90, 180, 270도 회전한 행렬을 출력하는 문제

3번 회전함으로 한 줄씩 출력하는 코드를 작성

회전한 후 출력되는 문자의 규칙을 찾아냄

3번의 회전을 하나의 반복문에 넣어 만들었다.

`end=' '`를 사용하여 각 회전 사이에 공백을 넣었다.

> 범위를 잘 계산해보자


## 1209 Sum

100X100 2차원 배열의 숫자를 각 행, 열, 대각선의 합 중 최댓값을 구하는 문제

100X100이 정해져있기 때문에 하나의 반복문안에 모든 합을 구하였음

각 행과 열의 움직임에 따라 위치를 잘 잡아줘야한다.


## 4836 색칠하기

빨간색과 파란색을 색깔을 각 영역에 칠할 때 보라색 칸의 개수를 구하는 문제

먼저 아무것도 칠해지지 않은 10X10 영역을 만듬

입력 받은 좌표값, 색깔을 변수에 저장하고 해당 영역에 따라 할당해준다.

전에 칠해져 있는 색깔에 따라 다르게 칠해줘야한다.
- 전에 아무것도 칠해져 있지 않다면 현재 색깔
- 전에 칠해진 색깔이 현재 색깔과 다르다면 보라색

전체를 순회하면서 보라색 칸의 개수를 구했다.


## 4837 부분집합의 합

1부터 12까지 숫자들의 부분집합 중 원하는 크기와 합을 가진 부분집합의 개수를 구하는 문제

1부터 12까지 모든 부분집합을 구한 뒤 개수와 합을 비교하여 결과값을 구한다.


## 16268 풍선팡2
풍선의 상하좌우와 본인의 꽃가루 더한 값중 최댓값을 구하는 문제

이 문제는 풍선팡에서 현재 좌표의 풍선의 꽃가루가 아닌 상하좌우만을 보면 된다.

풍선팡1을 참고하자


## 1945 간단한 소인수 분해

입력받은 수를 2, 3, 5, 7, 11로 소인수분해하여 각 지수의 값을 구하는 문제

지수를 카운트해줄 리스트를 만들었다.

`while`문을 사용하여 각 수별로 조건을 걸어 나눗셈을 진행하였다.

나머지가 0이라면 해당 숫자의 지수를 증가시켜 결과를 구했다.


## 6485 삼성시의 버스 노선
 
버스의 노선을 입력받고 정류장의 위치를 입력받아 각 정류소에 버스가 몇 대 지나가는지 구하는 문제

A(출발점)와 B(도착점)를 따로 구분하여 리스트에 받았다.
- 쉽게 버스 노선의 범위를 구할 수 있다.

C(정류장)에 노선이 몇개 겹치는지를 반복문을 통해 구했다.


# 9386 연속한 1의 개수
주어진 수열에서 연속한 1의 개수의 최댓값을 구하는 문제

수열을 문자열로 받아와 전체를 순회하여 구했다.

1의 개수를 세어주는 변수를 따로 선언하여 구했다.

마지막이 1로 끝날때에도 최댓값 갱신은 해주어야한다.


# 1210 Ladder_1
사다리타기 - 당첨된 사다리의 번호를 구하는 문제

한칸 사다리를 내려가면서 좌우 연결다리가 있는지 확인하며 내려간다.
- 맨왼쪽과 맨오른쪽일때를 생각해줘야한다.

방향 변수를 사용하여 연결다리가 있다면 움직이는 방향을 바꿔준다.

> 사다리의 출발지점을 알면 좌우 이동을 한번에 할수도 있다.


## 이진탐색
A와 B중 먼저 책페이지를 찾는 사람을 구하는 문제

문제의 이진탐색 조건을 잘 봐야한다.

> 조건문의 부등호를 잘 보자.


## 4843 특별한 정렬
수열을 큰 수, 작은 수, 다음 큰 수, 다음 작은 수.... 10개를 출력하는 문제

버블, 카운팅, 선택 정렬를 구현하여 오름차순 내림차순을 한개씩 구했다.

내림차순 하나, 오름차순 하나씩 5번 출력한다.


## 1221 GNS
숫자를 문자열로 표현한 리스트를 정렬하여 문자열로 다시 출력하는 문제

먼저 문자열의 숫자 순서대로 담은 리스트를 만든다.

모든 문자열을 순회하면서 각 문자열을 문자열 숫자 리스트에서 찾아 리스트로 다시 만든다 -> 정수형 리스트

만들어진 리스트는 정수형이라 정렬이 가능하다. -> 정렬

정렬된 정수 리스트를 다시 순회하면서 문자열로 바꿔준다.


## 4861 문자열 비교
문자열1이 문자열2에 포함되어있는지 확인하는 문제


## 4864 회문
가로열과 세로열에 길이가 M만큼인 문자열이 뒤집어도 같은 문자열을 찾는 문제

길이가 M인 문자열을 만들고 그 문자열을 슬라이싱을 통해 반대로 뒤집어주었다.


## 1989 초심자의 회문 검사
입력받은 문자열이 뒤집어도 똑같은지 확인하는 문제

입력받은 문자열을 슬라이싱으로 뒤집어 비교한 결과를 구한다.


## 1215 회문1
글자판에서 회문의 개수가 몇개인지 구하는 문제

회문 문제처럼 입력값 K만큼 리스트로 받아 리스트를 뒤집어 일치하는지 검사하며 개수를 구한다.


## 3143 가장 빠른 문자열 타이핑
문자열 A와 B가 있다. B가 A에 포함되어있다면 타이핑 횟수를 줄일 수 있다. 최소 타이핑 횟수를 구하는 문제

완전탐색으로 A문자열에 B가 몇개 있는지 개수를 구한다.

구한 개수를 적절히 빼주어 타이핑 횟수를 구한다.


## 4865 글자수
str1의 단어들이 str2에 몇개 들어있는지, 최대 개수를 구하는 문제

str1의 각 단어들을 딕셔너리로 만들어서 글자와 개수를 구했다

다시 딕셔너리를 순회하면서 최대 개수를 구했다.


## 1974 스도쿠 검증
주어진 스도쿠가 맞는지 아닌지 확인하는 문제

스도쿠의 숫자들을 행 방향, 열 방향, 3X3 부분 모두 하나씩 검사해본다.

전부다 탐색하는 방법을 사용하여 인덱스 범위를 지정하는 것이 중요하다

다른 방법을 사용할 수 있을거 같다.


## 2005 파스칼의 삼각형
입력받은 숫자크기의 파스칼의 삼각형을 출력하는 문제

위에 줄의 앞에 숫자와 위에 숫자를 더한 규칙이 있다.

현재 줄의 맨 앞 숫자와 맨 뒤 숫자가 1로 고정되고 그 후에는 규칙대로 만들면 된다.

현재 줄을 다 출력하면 현재줄을 위에 줄로 갱신해준다.


## 반복문자 지우기
주어진 문자열에서 중복되는 문자열이 있다면 지우는 문제

스택을 사용하여 구하였다.

스택의 0번째는 무조건 `push` 그 외 top이 중복이라면 `pop`, 아니라면 `push`

마지막으로 스택의 길이를 구하면 된다.


## 4866 괄호검사
`{}`와 `()`가 잘 사용되었는지 확인하는 문제

스택을 사용하여 괄호를 확인한다.

`pop`을 할 때 `top`의 괄호를 보고 조건을 결정한다.


## 1234 비밀번호
입력된 비밀번호에서 중복을 제거해 만든 비밀번호를 구하는 문제

`Stack클래스`를 만들어 푼다.

`get`메서드를 통해서 스택의 제일 위의 요소와 현재 숫자를 비교하여 중복여부를 파악한다.


## 4871 그래프 경로
노드를 간선으로 연결한 그래프의 정보를 준다. 출발노드에서 도착노드에 도달할 수 있는지 구하는 문제

`Stack`을 이용하여 `DFS`를 구현하여 문제를 풀었다.

출발노드부터 시작하여 인접한 노드를 탐색하면서, 도착노드를 방문했다면 성공, 전부 탐색했는데 못 방문했다면 실패

`DFS`에서 방문기록을 저장하는 리스트를 생성하는 것이 중요하다.


## 1219 길찾기
노드를 간선으로 연결한 그래프의 정보를 준다. 출발노드에서 도착노드에 도달할 수 있는지 구하는 문제

4871 그래프검사 문제와 똑같다.


## 4874 Forth
후위계산식의 결과값을 구하는 문제

스택을 사용하였다.

사칙연산을 구현하는 부분이 중요하다.

`/`는 분모로 `0`을 사용할 수 없다.

정수를 `/`연산하면 실수가 나온다.


## 1221 계산식1
입력받은 계산식을 후위표현식으로 바꾼뒤 결과값을 출력하는 문제

스택을 사용하였다.

연산자 우선순위를 정해 스택에 넣는 순서를 정해주었다.

그 후 후위표현식을 `Forth`문제와 같은 방법으로 계산해주었다


## 4875 미로
미로가 주어질 때, 출발점에서 도착점까지 도달할 수 있는지를 구하는 문제

DFS의 델타탐색을 사용하여 문제를 풀었다.

방문 가능한 지점에 대한 조건에 대해 고려할게 많다.


## 4881 배열 최소합
NxN 배열의 숫자에서 N개의 숫자를 골라 합의 최소를 구하는 문제

순열을 사용하여 문제를 풀었다

순열의 이해가 좀 더 필요함


## 1223 계산기2
주어진 계산식을 후위표현식으로 바꾼뒤 계산 결과를 구하는 문제

스택을 사용하여 후위표현식으로 바꿔주는 함수를 만들었다

바꿔준 후위표현식을 스택을 사용하여 계산해주었다. 


## 1859 백만장자 프로젝트
매매가를 보며 낼 수 있는 최대 이익을 구하는 문제

재귀로 만들었지만 런타임에러가 발생함
> 답은 다 맞음

뒤에서부터 시작하면 쉽다.


## 4869 종이붙이기
주어진 가로 길이의 종이를 붙일 수 있는 경우의 수는 구하는 문제

- 점화식
`f(n) = f(n-1) + 2*f(n-2)`


## 1225 암호생성기
일정한 규칙으로 변경되는 암호문을 생성하는 문제

8개의 숫자를 5번을 바꾸면 1사이클이 된다.

1사이클 동안 암호문을 변경하는 함수를 만들었다.

한 숫자가 0이 될때 까지 반복하여 암호문을 만들었다.

일정한 규칙을 찾아 사이클을 도는 횟수를 줄였다.


## 1860 진기의 최고급 붕어빵
M초동안 K개의 붕어빵을 만드는데 N명의 손님이 기다리지 않고 붕어빵을 받을 수 있을 지 구하는 문제

손님의 대기시간을 정렬했다.

반복하면서 K개의 붕어빵을 만들때마다 대기시간과 비교하면서 가능여부를 보았다.

`for-else문`을 사용하였다.

`return`을 사용하기위해 함수로 만들었다.


## 5099 피자굽기
피자를 구울 때 마지막에 꺼내는 피자의 번호를 구하는 문제

피자의 치즈양이 입력될 때 순서와 치즈양을 리스트로 가지는 리스트를 다시 만들어줌

화덕은 원형으로 이루어짐으로 `deque`을 사용해서 구현해주었다.

하나씩 피자를 꺼내며 다 구워졌으면 다음 피자를 넣어서 구워주었다

마지막에 나온 피자의 인덱스 번호를 출력해준다.


## 5907 회전
N개의 숫자열을 M번 회전시켰을 때 첫번 째 숫자를 출력하는 문제

나머지 연산으로 구함

`queue`로 구할수도 있다


## 5102 노드의 거리
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 구하는 문제

`BFS`를 사용하여 문제를 풀었다.

거리문제를 `BFS`로 풀면 잘 풀린다.


## 5105 미로의 거리
미로의 시작지점에서 도착지점까지 몇칸만에 갈 수 있는지를 구하는 문제

`BFS`와 `델타탐색`을 사용하여 구하였다.

현재 좌표와 다음 좌표로 가기 위헤 사용한 조건문의 순서가 중요하다.

도착지점을 사용하지 않고, 대신 `visited[ni][nj] == 3`을 사용할 때 이동거리가 3이 된 좌표를 도착지점으로 잘못 인식하기 때문에 도착지점의 좌표를 사용해야한다.


## 1216 미로1
미로의 출발점에서 도착점까지 갈 수 있는지를 구하는 문제

5105 미로의 거리 문제와 풀이법이 동일하다.


## 1231 중위순회
트리에서 중위순회하여 해당 문자열을 출력하는 문제

노드의 번호와 해당 노드의 알파벳, 자식노드들이 주어진다.

자식이 부족할 때 어떻게 처리해줄지, 해당 노드의 알파벳은 어떻게 할지가 중요하다.

해당 노드의 번호가 주어지기 때문에 알파벳을 담아줄 리스트를 따로 하나 더 만들어 처리해줌


## 5176 이진탐색
완전이진트리를 중위순회하여 원하는 노드를 출력하는 문제

`tree`를 2개 만들어 먼저 완전이진트리를 만들어주고 그 트리를 중위순회하면서 새로운 트리를 만들어준다.

원하는 노드를 출력한다.


## 5174 서브 트리
원하는 노드를 루트로 하는 서브 트리의 노드 개수를 구하는 문제

순회를 진행하면 상위 노드로는 순회하지 않기 때문에 전위 순회로 개수를 구함
> 런타임 에러 : 함수 호출 제한

왼쪽 자식 노드와 오른쪽 자식 노드에 값이 있다면 함수를 진행


## 5178 노드의 합
부모 노드는 자식 노드의 합으로 이루어진 완전 이진 트리에서 원하는 노드의 숫자를 구하는 문제 

완전 이진 노드는 부모와 자식의 노드 번호를 `//2` 나 `*2`로 구할 수 있다.

숫자가 입력되지 않은 부모 노드부터 채우며 완전 이진 트리를 완성하였다.


## 5177 이진 힙
최소힙을 만들고, 마지막 노드의 조상 노드의 합을 구하는 문제

최소힙은 자식 노드들이 부모 노드보다 작은 숫자로 구성된 트리이다.

최소힙을 만들고 조상 노드들의 합을 구해주었다.


## 1232 사칙연산
이진트리로 표현한 사친연산식의 값을 구하는 문제

트리의 노드 정보를 [값, 왼쪽 자식 번호, 오른쪽 자식 번호]로 만들어서 풀었다.

후위표현식으로 바꾸고 계산을 할려고 했지만 실패하여 재귀함수로 문제를 품


## 5688 세제곱근을 찾아라
입력받은 정수의 세제곱근을 찾는 문제

1부터 1씩 증가시키며 세제곱근을 찾는다.


## 5185 이진수
입력받은 16진수를 2진수로 출력하는 문제

16진수 문자열을 `int(Hex, 16)`으로 16진수 정수로 바꿀 수 있다

`format(val, 'b':2진수 'o':8진수 'h':16진수 'd':10진수)`로 바꿀 수 있다

`문자열.zfill(N)`: 문자열의 길이가 N이 될때까지 앞에 0을 채워준다


## 1240 단순 2진 암호코드
암호코드를 해독하여 결과를 출력하는 문제

암호코드가 아닌 부분은 0이기 때문에 `문자열.strip('0')`을 사용해서 문자열 양쪽의 0을 제거해줌

한 줄의 코드만 있으면 암호코드를 해석할 수 있기 때문에 숫자를 출력할 수 있다.

