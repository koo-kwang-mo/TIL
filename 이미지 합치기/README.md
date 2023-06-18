# 이미지에서 사람을 확인하고 포즈를 바꾸는 코드를 만들어보자.


### 6.14
 No module named 'object_detection'으로 텐서플로우의 모델을 찾지 못했다.
 -> 텐서플로우의 models\research 로 위치를 옮긴다.(cd models\research)
 -> set PYTHONPATH=%PYTHONPATH%;%cd%;%cd%\slim 로 환경변수 재설정.
 -> 파이썬에서 모델을 확인했다.
 -> 해결