# Tensorflow로 logistic regression 하기

> 거창하게 Tensorflow로 한다고 쓰긴 했지만 logistic regression의 개념만 정리하려 한다. logistic regression은 classification 문제에 쓰인다. logistic regression이 만들어지는 과정(logit함수, Odds, Odds ratio 등의 개념)은 건너뛰겠다.

- **logistic regression**의 hypothesis는 다음과 같다.
  - 이 식은 항상 0 ~ 1 사이의 값을 갖는다.

![soosic5](https://user-images.githubusercontent.com/49020354/72875011-b6a4bf80-3d36-11ea-971e-2bcfafe1c246.PNG)



- 일단 hypothesis가 linear regression과 다르기 때문에 다른 cost function을 써야한다.
- linear regression의 cost function에는 제곱하는 식이 있어서 선형식인 linear regression식을 넣으면 딱 좋게 밥그릇 모양의 그래프가 나오지만, **logistic regression**식을 넣으면 울퉁불퉁한 모양의 그래프가 나와서 출발점에 따라 cost가 낮은 지점이 달라질 수 있다.(cost가 가장 낮은 지점을 제대로 찾기 힘들다)



- 그래서 **logistic regression**에 어울리는 cost function 식이 있다.

![soosic6](https://user-images.githubusercontent.com/49020354/72875018-b99fb000-3d36-11ea-9ab6-3c782138149e.PNG)



- 바로 이 식이다.
  - y가 1일 때와 0일 때의 cost 식이 달라진다.
  - 그래야 울퉁불퉁하지 않은 그래프를 그릴 수 있다.
- **logistic regression**의 hypothesis에는 e가 있어서 그래프가 울퉁불퉁해 지는 것이다.
  - 그래서 exp와 상극인 log를 이용해서 그래프를 울퉁불퉁하지 않게 만들어 주는 것이다.

---

- 위 식을 한 줄로 풀어 놓은 식이 있다.

![soosic7](https://user-images.githubusercontent.com/49020354/72875024-bc9aa080-3d36-11ea-8066-aed4a49be466.PNG)



- 바로 이 식이다.
  - y가 1이면 + 뒤에 식이 0이 되며 사라진다.
  - y가 0이면 + 앞의 식이 0이 되며 사라진다.
  - 그래서 위 식과 같아진다!

- 위 식에 의하면 실제 y가 1일 때, 1에 가까운 확률 값으로 예측한다면 cost(W)는 0에 가까운 값이 되고, 0에 가까운 확률 값으로 예측한다면 cost(W)는 매우 큰 값으로 발산한다.

- 반대로 실제 y가 0일 때, 0에 가까운 확율 값으로 예측한다면 cost(W)는 0에 가까운 값이 되고, 1에 가까운 확률 값으로 예측한다면 cost(W)는 매우 큰 값으로 발산한다.

- **정리하자면 정답과 같게 예측하면 cost는 작아지고, 다르게 예측하면 cost는 커진다는 것이다.** ~~너무 당연한가~~



- 그 후 W를 찾아갈 때는 linear regression과 동일하게 Gradient decent algorithm을 이용한다.

![soosic3](https://user-images.githubusercontent.com/49020354/72874062-86f4b800-3d34-11ea-8561-b7c266d41390.PNG)



---

- logistic regression 식이 만들어지는 과정이나 계수의 의미는 이미 공부했고, 자료가 있기 때문에 정리하지 않았다.
- 모두의 딥러닝 강의에서 다룬 내용만 정리했다!

