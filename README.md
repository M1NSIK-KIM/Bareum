# 바름 - 사용자 맞춤 건강기능 식품 관리 및 추천 서비스  

<div align="center">
  <img src="https://github.com/Now-Hyeok/Bareum/assets/84857521/51bcc669-f565-49d0-89ac-24aac876ac08" style="width:350px; height:350px">
</div>

## 개발환경
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/Microsoft Azure-0078D4?style=for-the-badge&logo=Microsoft Azure&logoColor=white"> <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white"> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white"> <img src="https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=PWA&logoColor=white">

## 프로젝트 개요

### 프로젝트 설명

KT Aivle School 빅프로젝트 프로젝트

### 프로젝트 기간 및 참여인원

- 2023.05.22 ~ 2023.07.03

- 7명

### 프로젝트 목표

인공지능 기반 사용자 맞춤 건강기능식품 관리 및 추천 서비스

## 화면 구성

| 로그인 | 제품 등록 | 영양소 및 제품 확인 | 제품 추천 | 정기배송&쇼핑 | 복용알림 | 커뮤니티 |
| --- | --- | --- | --- | --- | --- | --- |
| <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/cdaa1b0f-2813-482c-9b57-5d9e07f35fa7" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/01714d4c-02f6-4e43-a480-b0a46e1c90c0" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/e7f21e94-d34b-4fa3-8dd7-74678ad05bd3" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/e7a29a71-6603-4750-bc0b-e380df064efd" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/4381c290-071c-4f35-b9b2-7877fc2b3960" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/a5a75065-6198-4bb3-aa4c-2025716a6fae" width="300px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/8baafbd6-2b39-432e-8293-3fadbe44d73e" width="300px"> |  


| 결과 영상 |
|:-:|
|![결과 영상](https://github.com/M1NSIK-KIM/Bareum/assets/76109508/e3803d66-9d52-4fd7-849a-a9f36d918e16)|


## 주요 기능 및 기대효과
<img src="https://github.com/Now-Hyeok/Bareum/assets/84857521/33cbfba2-77eb-428c-ac1b-07f7576e5c7f">



## AI
### OCR
- Clova AI 팀의 CRAFT와 deep-text-recognition-benchmark 논문을 참조하여 OCR모델
- OCR 기능의 성능을 개선하기 위해 코사인 유사도 검증을 사용하여 데이터베이스와 직접적으로 유사도를 확인하여 정확도를 높임

#### 학습 데이터



- 한글 데이터 "AI Hub 다양한 형태의 한글 문자 OCR"
- 영문 데이터 "Text OCR"
  
| 한글 데이터 | 영문 데이터 |
|---| --- |
| https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=91 | https://www.kaggle.com/datasets/robikscube/textocr-text-extraction-from-images-dataset |

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/ff52ee5c-7073-4221-bb16-fd9da67d958e" width="640px"> |

### 추천 
- Pycaret을 활용하여 데이터에 적합한 모델 XGBoost 사용
- Optuna를 활용하여 XGBoost Fine-Tuning
  
#### 학습 데이터
- 식품의약품안전처 기반으로 만들어진 랜덤 50만개 데이터

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/4411ff63-fe10-4861-9437-922ae0251b29" width="320px"> |

### 감정 분석
- KoBert 토크나이저 활용
- 2 Layers Bi-LSTM + Conv1D 구조

  
#### 학습 데이터
- 네이버 쇼핑 크롤링 리뷰 데이터 29,063

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/ce25c988-ae32-49af-be9d-a73d068e70a4" width="320px"> |


| 워드클라우드 결과 긍정  | 워드클라우드 결과 부정 | 
| --- | --- |
| <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/d4091b3a-66e5-45a8-91bf-6dac13fd7e08" width="320px"> | <img src="https://github.com/M1NSIK-KIM/Bareum/assets/76109508/26e3526f-434c-4097-a691-047924008b70" width="320px"> |


