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