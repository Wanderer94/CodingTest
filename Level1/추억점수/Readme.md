#### 두 개의 리스트를 묶기

zip은 두 개의 리스트를 서로 묶어줄 때 사용합니다.

```python
name = ['merona', 'gugucon']
price = [500, 1000]

z = zip(name, price)
print(list(z))
```

name 리스트에 아이스크림 이름이 price 리스트에 아이스크림의 가격이 순서대로 있을 때 두 리스트의 0번을 묶어주고, 1번을 묶어주는 겁니다. zip의 결과는 zip 타입의 객체이므로 우리가 알고 있는 리스트 타입으로 변환해서 값을 확인해볼 수 있습니다.

```py
[('merona', 500), ('gugucon', 1000)]
```

zip을 사용하면 다음과 같이 두 리스트에 대해서 하나의 for 문으로 싶게 사용할 수 있습니다.

```py
name = ['merona', 'gugucon']
price = [500, 1000]

for n, p in zip(name, price):
    print(n, p)
```
