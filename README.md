# Using_Aws_Rekognition
------
# cloud_computing_final_project 

## 목차
>### 1.[s3 bucket생성](#1.bucket생성)
>### 2.[웹페이지에 접속해서 s3에 사진 업로드](#2.웹페이지에-접속해서-s3에-사진-업로드)
>### 3.[s3와 rekognition을 연동, 사진을 labeling가능한지 확인 ](#3.s3와-rekognition을-연동,-사진을-labeling가능한지-확인)



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
> 주의! 새로 생성한 s3 bucket은 xml이 아닌 json를 입력해야 한다고 한다. [aws_cors설정](https://docs.aws.amazon.com/ko_kr/sdk-for-javascript/v2/developer-guide/cors.html)



## 2.웹페이지에 접속해서 s3에 사진 업로드
## 3.s3와 rekognition을 연동, 사진을 labeling가능한지 확인
