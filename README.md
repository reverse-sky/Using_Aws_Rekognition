# Using_Aws_Rekognition
------
# cloud_computing_final_project 

## 목차
>### 1. [s3 bucket생성](#1.bucket생성)
>### 2. [EC2-생성-nginx설치](#2.EC2-생성-nginx설치)
>### 3. [웹페이지에 접속해서 s3에 사진 업로드](#3.웹페이지에-접속해서-s3에-사진-업로드)
>### 4. [s3와 rekognition을 연동, 사진을 labeling가능한지 확인 ](#4.s3와-rekognition을-연동,-사진을-labeling가능한지-확인)



## 1.bucket생성
### [브라우저에서 바로 AWS S3에 파일 업로드하기](https://medium.com/@hozacho/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90%EC%84%9C-%EB%B0%94%EB%A1%9C-aws-s3%EC%97%90-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0-637dde104bcc) 다음 블로그를 참고하여 bucket을 생성했다.
>+ aws의 s3를 검색  ![image](https://user-images.githubusercontent.com/45085563/142380067-48a85f6a-9d37-4ad0-973b-51769bef8710.png)
>+ bucket 생성![image](https://user-images.githubusercontent.com/45085563/142380154-c6e8da05-9db6-42ec-94b8-bcd536b31c4c.png)
>+ 엑세스 차단 설정 해체 ![image](https://user-images.githubusercontent.com/45085563/142380605-5c121ffd-2a7b-4c12-ae2b-633bb512db3f.png)
>+ s3_bucket이 생성되었습니다. ![image](https://user-images.githubusercontent.com/45085563/142380723-6cbce5e4-26b1-4998-8cc6-9c5d7685d479.png)
>+ bucket에 들어가서 권한 버튼을 클릭한다.![image](https://user-images.githubusercontent.com/45085563/142381014-3a0ba03f-ff26-4b19-ae94-f633a0e57f0f.png)
>+ 권한에서 밑으로 내려가면 CORS가 있다. ![image](https://user-images.githubusercontent.com/45085563/142381269-456edf44-4035-4d79-8d81-b6d9e031f4ad.png)

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "HEAD",
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ]
    }
]
```
>다음의 코드를 편집에 입력![image](https://user-images.githubusercontent.com/45085563/142382540-8aed584e-a0bf-4312-a06d-3249c7b0030c.png)
> *주의! 새로 생성한 s3 bucket은 xml이 아닌 json를 입력해야 한다고 한다. [aws_cors설정](https://docs.aws.amazon.com/ko_kr/sdk-for-javascript/v2/developer-guide/cors.html)*
>+ Cognito를 검색 ![image](https://user-images.githubusercontent.com/45085563/142383053-3dcd4c39-42b7-41f2-a551-f959f0c5fde5.png)
>+ 자격 증명 풀 관리 버튼 클릭 ![image](https://user-images.githubusercontent.com/45085563/142384751-229e8664-5339-417a-b503-e91a49f19ac0.png)
>+ *시작하기 자격증명 풀 관리를 하기 전에 리전을 선택해야합니다.(생성한 s3와 같은 리전을 선택)*![image](https://user-images.githubusercontent.com/45085563/142385406-0bf0099d-3b0b-4e13-9146-2b1683495956.png)

>+ 자격 증명 풀 이름 입력, 인증되지 않은 자격 증명 버튼 클릭 ![image](https://user-images.githubusercontent.com/45085563/142384860-830da217-a098-4426-9723-6d19fac31490.png)
>+ 풀 생성 버튼을 누르면 나오는 세부 정보 숨기기 버튼을 클릭합니다. ![image](https://user-images.githubusercontent.com/45085563/142385523-534c4c67-4d3e-462d-ba4b-cf9d4474c447.png)
>+ 역활 요약에서 정책 문서를 클릭한 다음, 다음 코드를 입력합니다. 이때 코드의 BUCKET_NAME에 아까 생성한 bucketname인 kwonsoon을 입력해주겠습니다.
```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "s3:*"
         ],
         "Resource": [
            "arn:aws:s3:::BUCKET_NAME/*",
            "arn:aws:s3:::BUCKET_NAME"
         ]
      }
   ]
}
``` 
>+ 그 후 확인 버튼을 누르면 다음과 같은 화면이 나타나는데, 플랫폼을 JavaScript로 변경한 다음 AWS 자격 증명 얻기의 코드를 notepad에 복사해둡시다. ![image](https://user-images.githubusercontent.com/45085563/142386206-ee948edd-bdc4-4f1c-99f3-479a1bf9935e.png)
## 2.EC2 생성 nginx설치
>+ 이제 EC2를 생성해서, 웹페이지를 만들어보겠습니다. 우선 인스턴스를 생성합니다. ![image](https://user-images.githubusercontent.com/45085563/142398285-57ebaa3a-7803-4d39-a605-f99f44cf7037.png)![image]
>+ ec2에서 인스턴스 시작 버튼을 클릭합니다. (https://user-images.githubusercontent.com/45085563/142398420-7573ccf3-1584-40b5-97b1-b471197b2d02.png)

>+ 시작버튼을 누르면 다음과 같은 os image를 선택하는 창이 나옵니다. 
>+ 밑으로 내려서 Ubuntu Server 18.04 LTS (HVM)를 선택해줍니다.![image](https://user-images.githubusercontent.com/45085563/142399174-eebb7805-de72-401e-b34f-f06ab66012e2.png)
>+ 그리 큰 자원이 필요하지 않으므로, t2.micro를 사용하겠습니다.![image](https://user-images.githubusercontent.com/45085563/142398923-d8e70792-aab3-4ad8-b510-521ba14258d8.png)
>+ 



## 3.웹페이지에 접속해서 s3에 사진 업로드
## 4.s3와 rekognition을 연동, 사진을 labeling가능한지 확인
