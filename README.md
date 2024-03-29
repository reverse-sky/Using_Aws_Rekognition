# Using_Aws_Rekognition
# A.프로젝트 명:
>웹페이지를 이용한 사진내의 텍스트 인식 및 음성 파일 생성 프로그램
------

# B.프로젝트 멤버 이름 및 멤버 별로 담당한 파트에 대한 소개
> 20185141:용권순 (1인팀)
# C.프로젝트 소개 및 개발 내용 소개
>ec2의 ip를 통해서 웹페이지에 접속하여 s3에 사진을 업로드 할 수 있다. 업로드한 사진에 text가 있을 경우 aws rekognition을 이용해서 text를 읽어서 문장을 저장한뒤, 저장한 문장을 aws polly를 사용하여 mp3파일로 생성한다. 

# D.	프로젝트 개발 결과물 소개 (+ 다이어그램)
>웹페이지에 접속해서 폴더를 생성해서 파일을 업로드 하고 삭제할 수 있습니다. 업로드한 파일을 rekognition을 이용해서 텍스트를 읽고, 읽은 문장을 
>polly로 만들어서 mp3파일을 생성합니다.
<img width="751" alt="image" src="https://user-images.githubusercontent.com/45085563/144748105-b3c80428-fd46-4174-8767-df816b0b12fc.png">

# E.	개발 결과물을 사용하는 방법 소개 (+ 프로그램 구동 화면 스크린 샷 첨부)
>![image](https://user-images.githubusercontent.com/45085563/142407419-6076abca-ce17-4ebe-b8a6-1ecc204ff14a.png)   
>+ ec2에 공인 ip를 이용해서 접속할 시 nginx로 구성된 idnex.html홈페이지가 보여지게 된다.    
>+ Create New Album버튼을 클릭하면 s3에 우리가 생성한 이름으로 폴더가 생성된다.    
>![image](https://user-images.githubusercontent.com/45085563/142408671-11f8265d-514f-4b34-b81a-85a823934512.png)   
컴퓨터뿐만 아니라 핸드폰으로도 업로드 할 수 있습니다.    
>>![image](https://user-images.githubusercontent.com/45085563/142409594-f8666e30-7618-466d-8ec3-55b4e3dd2e7e.png)     
>+ text이미지를 올렸을 때, rekognition을 사용해서 file을 text로 변경한 다음, polly를 사용하여 음성 mp3파일을 생성한 다음 s3버킷에 올립니다.
>![image](https://user-images.githubusercontent.com/45085563/144748515-4d2de4fb-cd92-4b33-81d1-2b91bab0752e.png)
>+ test.png파일을 올림 
>![test](https://user-images.githubusercontent.com/45085563/144748502-a7ca9c7b-5df4-47c9-aab5-3285699ef62b.png)
>+ test.png파일    
>![image](https://user-images.githubusercontent.com/45085563/144748475-3dec83dd-06e9-4f7d-a905-eaa6ed7693a2.png)
>+ mp3파일 생성 및 업로드   
>![image](https://user-images.githubusercontent.com/45085563/144746396-766a7819-c982-4282-b8cf-874b688bb0e5.png)   
>mp3파일이 생성된 것을 확인할 수 있습니다. 

# F.	개발 결과물의 필요성 및 활용방안
>전세계의 전체적인 고령화로 디지털 문화를 이용하는 사람들의 평균 연령대가 증가하고 있다. 그러나 고령 사용자의 경우 노화로 인한 여러가지 문제가 존재하는데, 다음 결과물은 고령 사용자의 노화, 특히 노안에 대한 솔루션을 제공할 수 있다. 또한 스마트폰 및 전자기계 사용량의 증가로 인해 청년 노안의 비율도 꾸준히 증가하고 있다. 청년 노안을 발생시키는 가장 큰 원인은 작은 글씨를 밝은 빛으로 읽다 보니 눈에 피로가 쌓이게 되는것. 이에 개발 결과물은 다음 솔루션을 제공한다.  
  카카오톡이나 메세지를 통해 이미지를 받더라도, 화질의 문제, 혹은 노안의 문제로 text를 읽는데 어려움이 있는 사용자가 있을 수 있는데, 다음 방식은 별도의 어플리케이션을 설치할 필요 없이 인터넷만 있다면 웹페이지에 접속하여 사진을 업로드 하기만 하면 mp3로 변환하여 사진에 존재하는 text를 읽어주는 방식으로 고령 사용자의 디지털 문화 사용의 편의성을 향상시킬 수 있을 것이다.
