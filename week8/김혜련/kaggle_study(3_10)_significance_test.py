# -*- coding: utf-8 -*-
"""KAGGLE_STUDY(3.10)_significance test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14QU1xtIvxGRW9Ac6a0d104D2IjvTbTR0

# 제 18장 유의성 검정(significance test)

<br>
<br>
<br>

> 1. 가설검정의 원리

> 2. 귀무가설과 대립가설

> 3. 검정통계량과 유의수준

> 4. 제1종 오류와 제2종 오류

> 5. 유의성 검정절차

> 6. t-검정

<br>
<br>
<br>

> ## 1. 가설검정의 원리

 : 주장이 타당할까? 어떤 차이에 대해, 우연에 의한 차이? or 실질적인 차이? 
 <br>
 : 귀무가설에 대한 반증을 찾아 이를 기각하는 것
 <br>
 : 모순에 의한 논증법(argument by contradiction) 
 <br>
> 하나의 통계량 값이 그 기대값으로부터 그 통계량의 표준오차 단위로 2단위 이상 떨어져있으면 우연으로 보기 힘들다. 

<br>
<br>

> ## 2. 귀무가설과 대립가설


> 관측된 차이는 '우연의 의한 결과다' ? 귀무가설(null hypothesis) H0 
<br>
> <-> 관측된 차이는 '실질적이다' ? 대립가설(alternative hypothesis) H1

> ※ 유의성 검정 시, 귀무가설을 '상자 모형에 대한 진술'의 형태로 표현해야함
<br>
> 즉, 표본 추출상의 우연이 아니라 논쟁은 상자에 든 전체에 관한 것임 
<br>
> *** [O / X QUIZ]
<br>
> [O / X] 귀무가설을 채택한다 or 대립가설을 채택한다
<br>

> 통계학에선, 더 나은 이론이 나오기 전까지만,
<br>
> 즉, 데이터가 쌓여서 새로운 쪽으로 갈아타기 전까지만 귀무가설을 기각 X 
<br>
> (기존 패러다임으로는.. ) 귀무가설을 기각하지 못한다
 

<br> 
<br>

> ## 3. 검정통계량과 유의수준

> ### 검정통계량이란?
> 자료에서 얻은 통계치와 귀무가설 하에서 기대되는 값 사이의 차이를 측정하는 것 
<br>
> z-통계량 또는 t-통계량이 널리 사용됨
<br>
> 표본이 크기가 크면 상자의 내용물에 관계없이 z-검정을 사용
<br> 
> <-> 표본의 크기 작고, 질적인 자료도 아니면? t-검정(t-test) by 고셋 
<br>
"""

from IPython.display import Image
Image('./sample_data/h1.PNG')

"""> z or t = 실제(관측치)와 이론의 표준화된 차이 
> 통계량(관측치) - 기대값(귀무가설 하 기대값 / 상자의 평균) 
<br>
> / 통계량의 표준오차(표준단위로 나타냄 /표준오차 단위로 얼마나 떨어져있나) 
<br>
<br>
> 위 값을오부터 표준정규분포곡선에서 해당하는 면적에 어디에 해당하는지 알 수 있음 

<br>
<br>

> ### 어떤 기준으로 귀무가설을 기각할 것인지? 유의수준 !

> (significance level, 'a', 검정의 크기(size of test))   

> 귀무가설에 대한 반증의 강도에 대해 미리 기준을 정해 놓고 이를 근거로 p-값을 판단 
<br>

> ### => 가설검정? (z-값 또는 t-값으로부터) p-값을 계산하고 (유의수준에 비추어) 최종적으로 p-값의 크고 작음을 판단하여, 귀무가설에 대한 반증을 찾아 이를 기각하는 절차<br>

> p-value / p-값 / 관측된 유의수준
> : p-값은 귀무가설이 맞을 확률? X 
<br>
> 귀무가설이 옳다는 가정하에 실제의 관측치 또는 극단적인 관측치의 값을 얻을 확률 
<br>
> 이 확률(p-값)이 작아질수록 귀무가설에 대립되는 반대의 근거(대립가설)는 강해진다. 


<br>
<br>

> ### (그 외) 양측검정? 단측검정? 1종오류? 2종오류? 검정력? 기각역?
"""

from IPython.display import Image
Image('./sample_data/h2.PNG')
Image('./sample_data/h3.PNG')

"""> ## 5 ~ 6. 유의성 검정절차(t-test)

> ### [유의성 검정 절차] 

> 1. 유의수준 a를 정한다

> 2. 일단 귀무가설이 옳다고 가정한다

> 3. 자료(관측치)와 이론(귀무가설)의 차이를 측정한 검정통계량 값을 구한다

> 4. 관측된 유의수준인 p-값을 계산한다

> 5. 관측된 유의수준인 p-값과 미리 설정된 유의수준인 a를 비교한다


> 평균 검정(z-검정, t-검정, 분산분석/3개)의 하나로서, 
<br>
> 비교집단이 2개 이하일 경우 사용한다.  


> ※ z-검정의 경우, 정규성, 모분산을 알고 있을 경우에만 사용

> ※ t-검정에는 크게 3가지가 있는데, 단일표본 t-검정, 독립표본 t-검정, 쌍체표본 t-검정 

> ## scipy.stats module 이 위 세 가지 종류의 t-검정을 제공함 

> 참고_1 :  https://no17.tistory.com/189

> 참고_2 : https://iaingallagher.tumblr.com/post/50980987285/t-tests-in-python
"""

# 1.[단일표본 t-검정]

# 영국 남자 평균키 175.3cm - 어떤 설문조사를 통해 10명의 남성 키를 조사하였고, 표본의 평균이 모평균으로부터 차이가 큰 지 알고 싶음 ! 

# 1) 유의수준 a를 정한다 = 5% = 0.05
# 2) 일단 귀무가설이 옳다고 가정한다 => 영국 남자 평균키와 10명의 남성키는 같다
# 3) 자료(관측치)와 이론(귀무가설)의 차이를 측정한 검정통계량 값을 구한다 => 표본의 크기가 작아, t-test 
# 4) 관측된 유의수준인 p-값을 계산
# 5) 관측된 유의수준인 p-값과 미리 설정된 유의수준인 a (0.05)를 비교함 => p < 0.05


from scipy import stats

one_sample_data = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]

one_sample = stats.ttest_1samp(one_sample_data, 175.3) # tuple형 데이터(t-value + p-value) 포함 

print(one_sample)
print()
print("The t-statistic is %.3f and the p-value is %.3f." % one_sample)

# 2.[독립표본 t-검정(Unpaired t-test)] - 독립변인 2집단 비교
# 성별로 8명의 성인 남녀 몸무게 조사 

female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]

two_sample = stats.ttest_ind(male, female)
print(two_sample)
print()
print("The t-statistic is %.3f and the p-value is %.3f." % two_sample)
print()

# 분산이 불규칙하다고 가정한다면? 
two_sample_diff_var = stats.ttest_ind(male, female, equal_var = False)
print("if we assume variances than the t-statistic is %.3f and the p-value is %.3f" % two_sample_diff_var)

# 3.[쌍체표본 t-검정(Paired t-test)] - 종속변인 2집단 (repeated measures/다른 시간대, 조건 하에 ?)
# 수술 전 9명의 몸무게 -> 수술 후 모뭄게 

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]

follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

paired_sample = stats.ttest_rel(baseline, follow_up)
print("t-statistic is %.3f and the p-value is %.3f." % paired_sample)

