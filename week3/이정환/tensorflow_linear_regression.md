# Tensorflow

> Tensorflow란 구글에서 만든 딥러닝 프로그램을 쉽게 구현할 수 있도록 다양한 기능을 제공해주는 라이브러리이다.

### 1. Tensor

- **Tensor**란 array를 말한다.

- **Tensor**에서 *rank*는 차원, *shape*은 2차원 이라면 행과 열 개수(차원이 늘어나도 같은 개념), *type*은 data type을 말한다(보통 int32나 float32).

---

### 2. Tensorflow로 linear regression하기

- 오차의 제곱을 cost function이라 한다. => (y*hat* - y)^2
- 그리고 회귀식이 `H(x) = Wx + b` 라 했을 때

  - cost function은 cost(W, b)가 되고



- 모델 학습의 목표는 cost(W, b)를 최소로 하는 것이므로
  - 이를 최소로 하는 W와 b를 찾는 것이 목표이다.



- cost function의 식은 다음과 같다.

![soosic1](https://user-images.githubusercontent.com/49020354/72874040-7f351380-3d34-11ea-9923-e7282c20bce5.PNG)



- 이 식을 후에 미분할 때 편리 성을 위해 다음 식으로 바꿔준다.

![soosic2](https://user-images.githubusercontent.com/49020354/72874049-83f9c780-3d34-11ea-8854-bc6222dd6261.PNG)



- (회귀에서 W(베타, 회귀계수)를 찾는 방법에는 최소제곱법 같은 방법도 있지만, 이 강의에서는 경사하강법으로 설명했다.)



- cost function이 최소가 되는 값을 찾을 때 Gradient decent algorithm을 이용한다.



- b가 0이라 할 때, cost function은 *cost(W)*
  - x축을 W로 놓고 y축을 cost function으로 놓고 그래프를 그린다.



- 그 후 경사도(기울기)가 가장 작은 지점을 찾는다.
  - cost(W, b)라면 3차원 그래프



- 그래서 위 식을 W의 변화에 대한 식으로 정리하면 이렇게 된다.
  - 여기서 alpha는 학습률이다.

![soosic3](https://user-images.githubusercontent.com/49020354/72874062-86f4b800-3d34-11ea-8561-b7c266d41390.PNG)



- 위 식을 미분하면 이렇게 된다.

![soosic4](https://user-images.githubusercontent.com/49020354/72874069-8a883f00-3d34-11ea-924d-53b1bfb1101b.PNG)



- 이 식을 이용해 W가 가장 작은 지점을 찾아가는 것이다.
- 그래프는 꼭 Convex function의 모양이 되는지 확인해야 한다.(볼록한(밥그릇) 모양)
- x(변수)가 많아지면 수식도 길어지고 불편하기 때문에 matrix를 이용한다. (다항 회귀)

  - 식 표현이 간단해진다.

  - Tensor에선 matrix 이용.

---

- 현재 김성훈 교수님의 모두의 딥러닝 강의를 듣고 있는데, 내 컴퓨터에는 Tensorflow 2.0.0버전이 깔려있고 강의에선 Tensorflow 1.0.0버전이라 코드가 맞지 않아서 당장 실습은 못 하고있다..ㅠㅠ
- 개념부터 정리하고 실습은 추후에 2.0.0버전에 맞춰서 공부할 예정이다!