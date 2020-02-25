# Multinomial classification (Softmax)

- `H(x) = WX`
  - 이 식의 값은 -무한대부터 +무한대까지의 실수 값이다.

- 이를 binary classification을 위해 식을 변형하여 적용한 것이 logistic regression이다.

- 그리고 이것을 어떻게 multinomial classification에 적용할까 고민하던 중 하나의 방법을 찾아낸다.

- 3개의 class (A, B, C)를 가진 y를 예측하고 싶다.

- 그랬을 때 binary classifier 3개가 있다면 해결가능하다.
  - A인지 아닌지 알 수 있는 binary classifier.

  - B인지 아닌지 알 수 있는 binary classifier.
  - C인지 아닌지 알 수 있는 binary classifier.

- 3개가 있으면 된다.

![class3](https://user-images.githubusercontent.com/49020354/74332365-e9dbeb00-4dd8-11ea-86aa-9b067203f9f1.PNG)

- 이렇게 말이다.

- 그렇다면 식으로 바꾸면 어떻게 될까.

- 변수가 3개가 있다는 가정하에 대수식으로 작성해보면

![cap2](https://user-images.githubusercontent.com/49020354/74332854-0e849280-4dda-11ea-9572-954f641e3f59.PNG)

- 이렇게 A, B, C 클래스를 분류하는 식 3개를 따로따로 계산하면 된다.
  - 하지만 이 방식은 class가 늘어난다면 class의 개수에 따라 식이 만들어 질 것이다.(복잡하다)
- 그래서 matrix의 이점을 이용해 식을 합치면 된다.

![cap3](https://user-images.githubusercontent.com/49020354/74332862-10e6ec80-4dda-11ea-8a4c-10f4df9e1e50.PNG)

- 이렇게 말이다.
- 하지만 이렇게 하면 결과 값도 3개가 나온다.

![cap4](https://user-images.githubusercontent.com/49020354/74333268-f3fee900-4dda-11ea-9e83-96c917e7551c.PNG)

- 이런식으로 나온다.

- 각각의 값은 ![](https://user-images.githubusercontent.com/49020354/74333586-90c18680-4ddb-11ea-9621-5f747856e9bd.PNG) 를 나타낸다.
- 하지만 여전히 각각의 값은 -무한대부터 +무한대까지의 실수 값이다.
  - 그래서 classification 결과값(0 ~ 1사이의 값(확률 값))으로 바꾸기 위해 Sigmoid함수를 적용한다.
  - Sigmoid함수의 종류는 꽤 많다.
- 그 중에 여기(multinomial)서는 Softmax를 사용한다.

![cap6](https://user-images.githubusercontent.com/49020354/74335289-362a2980-4ddf-11ea-9282-52c723ed7cf1.PNG)

- 이것이 바로 Softmax이다.
  - 그냥 실수 값을 확률 값으로 바꾸어준다.
  - 그 후 가장 확률 값이 높게 나온 class가 그 데이터의 class이다.
- 그렇다면 이제 cost를 구하는 방법이다.

![cap8](https://user-images.githubusercontent.com/49020354/74336406-8904e080-4de1-11ea-93b1-ce4c5f9d9af6.PNG)

- 강의에서 L을 one-hot encoding을 이용해 확률 값을 한 값만 1로 나머지는 0으로 만든다고 했다.
  - 1로 나온 class가 그 데이터의 class인 것이다.(가장 높게 나온 확률 값이 1로 된다.)
- S는 확률 값, L은 최종 class 결과 값.

![cap7](https://user-images.githubusercontent.com/49020354/74336037-e187ae00-4de0-11ea-9a38-66203e83b18a.PNG)

- 여기선 Cross-entropy를 이용한다.
- 맨위에 있는 식이고, 이 식에서 곱은 엘리먼트 곱이다.(원소끼리 곱해줌)
  - 밑에 그림에 동그라미 안에 동그라미 있는 것이 있는데 이것 또한 엘리먼트 곱을 나타낸 것이다.
  - 이게 무슨 말이냐면, 같은 인덱스에 있는 원소끼리 곱해준다는 것이다.
- 그렇게 계산 후 맨앞에 서매이션이 붙었으니 결과 값들을 더해주면 최종 결과 값이 나온다.

---

- 여기까지 잘 달려왔다.
- 강의에서 교수님께서 Cross-entropy cost식과 logistic cost식이 결국 같다고 하셨다.
- 그 이유는 알아서 생각하라고... ㅋㅋ
  - 내 생각엔 어차피 엘리먼트 곱이므로 한 값이 0이라면 그 결과 값은 0이 된다.
  - 그러므로 예측한 값이 1인 값만 살아남는다는 이야기이다.
  - 이런 점에서 logistic cost function과 똑같다.