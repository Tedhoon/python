# 그래도 시험인데 정리를 해볼까나


__getitem__(self, key): 객체에서 [] 연산자를 사용하여 조회할때 동작을 정의합니다. 예를들어 _list[10]은 _list.__getitem__(10)으로 동작합니다. 키의 타입이 적절하지 않다면 TypeError에러를, 키가 인덱스를 벗어났을 경우는 IndexError를 던져야 합니다.

__setitem__(self, key, value): 객체에서 [] 연산자를 사용해서 변수를 지정할때 동작을 정의합니다. 예를들어 _list[10] = 1은 _list.__setitme__(10, 1)으로 동작합니다.