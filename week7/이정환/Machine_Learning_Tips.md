# Machine Learning Tips

- Gradient descent방법 에서는 learning rate(alias : eta)(학습률)을 잘 조정해야한다.
  - 너무 작은 학습률은 local minimum에서 멈추게 될 수 있다.
  - 너무 큰 학습률은 overshooting 될 수 있다.
  - 결국 global minimum까지 잘 찾아갈 수 있게 적당한 학습률로 조정 하는 것이 중요하다.
  - 정답은 없다. 찾아가는 것이다.

---

- 전처리(preprocessing)
  - 변수마다 가지고 있는 데이터 값의 범위가 매우 다르다면 learning rate도 적당한데 cost가 막 발산하고 그런 경우가 생긴다.
  - 이럴 때는 정규화(표준화)를 해주어야 한다.
  - 데이터들을 어떤 범위 내에서만 있게 하는 것이다.
    - Standradization, Min Max scale, Normalization 등 여러 방법이 있다.

---

- 과대적합(Overfitting) ★
  - 학습 데이터에 너무 딱 맞는 모델 (새로운 데이터가 들어오면 잘 예측하지 못 한다.)

![overfitting](https://user-images.githubusercontent.com/49020354/75676630-fc0cc300-5ccc-11ea-9253-5731ca54cf04.PNG)

- 오른쪽 처럼 너무 딱 맞게 만든 모델을 과적합 되었다라고 한다.
  - 즉 왼쪽이 더 일반화가 잘 되었다고 할 수 있다.
- Overfitting을 줄이는 방법
  - 더 많은 학습 데이터
  - 변수 개수를 줄인다
  - 일반화 시킨다
    - 일반화의 방법은
    - weight을 너무 크게 하지 않는다
    - (cost에 Regularization strength를 곱해준 서메이션w^2를 더해주어서 일반화를 시키는 방법)
    - (일부러 학습 데이터의 cost를 높인다.)

---

- 검증 데이터(validation set) 이용
  - 중간고사 문제와 기말고사 문제가 똑같다면 기말고사는 제대로 된 점수라고 할 수 없다.
  - 학습 데이터 중에서 학습에 사용할 데이터와 아닌 데이터(검증 데이터)로 나눈다.
  - 그 후 학습에 사용할 데이터로만 학습 시킨 후, 검증 데이터로 예측 해보고 성능을 측정해본다.
  - 즉, 학습 데이터가 교과서라면 검증 데이터는 모의고사 정도?

![validation](https://user-images.githubusercontent.com/49020354/75677817-a4238b80-5ccf-11ea-9f5a-cd4fdba559aa.PNG)

---

- Online learing
  - 학습 데이터를 몇 부분으로 쪼개서 순차적으로 학습 시키는 방법
  - 이전의 학습을 기억하고 그대로 다음 데이터를 학습한다.
  - 요즘 시대에는 방대한 양의 데이터가 계속 쌓이기 때문에, 새로운 데이터가 들어왔을 때 이미 갖고있는 데이터로 학습된 모델에 새롭게 들어온 데이터를 추가 학습 시켜주면 되는 것이다.

![online learning](https://user-images.githubusercontent.com/49020354/75678213-78ed6c00-5cd0-11ea-8708-b0702d5cbfb8.PNG)

---

### Training epoch/batch

- epoch(에폭)
  - 전체 학습 데이터를 한 번 학습시켰을 때 1 epoch
- iteration
  - 학습 데이터를 몇 번에 걸쳐서 학습할 지 정하는 수 (20번 나눠서 한다면 20 iteration)
  - 한 번에 다 학습 시키려면 메모리가 매우 많이 소모되기 때문에 이를 해결하는 방법이다.
- batch size
  - 한 번의 iteration에 몇 개의 데이터씩 학습할 지 정하는 수 (한번의 iteration에 24개 씩 넣는다면 24 batch size)
  - 그런데 학습 데이터의 개수가 있으므로 batch size를 정해주면 iteration은 저절로 계산될 듯.

