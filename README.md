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
>+ 이제 EC2를 생성해서, 웹페이지를 만들어보겠습니다. 우선 인스턴스를 생성합니다. ![image](https://user-images.githubusercontent.com/45085563/142398285-57ebaa3a-7803-4d39-a605-f99f44cf7037.png)![image](https://user-images.githubusercontent.com/45085563/142398420-7573ccf3-1584-40b5-97b1-b471197b2d02.png)
>+ ec2에서 인스턴스 시작 버튼을 클릭합니다. 

>+ 시작버튼을 누르면 os image를 선택하는 창이 나옵니다.
 
>+ 밑으로 내려서 Ubuntu Server 18.04 LTS (HVM)를 선택해줍니다. ![image](https://user-images.githubusercontent.com/45085563/142399460-a7b5319a-e972-4b40-b890-10c7e6d13c67.png)
>+ 그리 큰 자원이 필요하지 않으므로, t2.micro를 사용하겠습니다.![image](https://user-images.githubusercontent.com/45085563/142398923-d8e70792-aab3-4ad8-b510-521ba14258d8.png)
>+ 나머지 설정은 그대로 둔체, 보안 그룹 구성을 설정합니다. ![image](https://user-images.githubusercontent.com/45085563/142399574-0b9a89db-fe1f-4ad7-8a5e-b448ad0ad136.png)
>+ http로 웹페이지에 접근하기 위해서 80포트를 열어준 것입니다. 검토 및 시작 버튼을 클릭합니다.
>+ 시작하기 버튼을 클릭하면 키 페어 생성 창이 뜹니다. 가상머신에 ssh로 접근하기 위한 설정이므로, 새로운 키를 생성해보겠습니다.
>![image](https://user-images.githubusercontent.com/45085563/142399896-86e3e764-026f-4fad-83b0-3c3767578f32.png) 키 페어 다운로드 버튼을 누릅니다.
>+ puttygen을 사용하여 다운로드한 pen파일을 이용해봅시다. load버튼을 클릭합니다. 파일 확장자를 all files로 바꾼 다음 ![image](https://user-images.githubusercontent.com/45085563/142401446-bc278c62-4573-4e6c-b604-9d509f0fd929.png) 다운로드한 pem파일을 클릭합니다. 
>+ Save private key버튼이 활성화 된 것을 볼 수 있습니다. Save private key를 클릭후, y를 클릭합니다. ![image](https://user-images.githubusercontent.com/45085563/142401662-a6850406-4579-4346-a303-5223cc16da27.png) 원하는 경로와 이름으로 key를 생성한다음, putty를 실행합니다.
>+ 우선 접속할 instance의 ip를 입력합니다. ![image](https://user-images.githubusercontent.com/45085563/142402344-cc183fd6-ee97-47fd-9f9a-209e8ac613aa.png)

>+ Category에서 SSH Auto를 클릭한 다음 Browse버튼을 클릭합니다. ![image](https://user-images.githubusercontent.com/45085563/142401936-1fcc7562-0c47-4c88-9c5a-20ea5fcb258d.png)
>+ 저장한 경로에서 생성한 키를 클릭합니다.![image](https://user-images.githubusercontent.com/45085563/142402199-92ee25e4-8911-4dd7-8607-65ed9ed47c22.png)![image](https://user-images.githubusercontent.com/45085563/142402230-45901850-9be9-4917-8718-8ca1f289d2a4.png)
>+ open 버튼을 클릭하면 다음과 같은 화면이 뜨는데,![image](https://user-images.githubusercontent.com/45085563/142402547-eecf6c41-b8b7-41b3-8c31-e1c9794ff34a.png)  Accept버튼을 클릭하면 연결이 된 것을 확인할 수 있습니다.(초기 로그인은 ubuntu입니다.)![image](https://user-images.githubusercontent.com/45085563/142402595-8c7ee7e3-3af9-4a02-8901-61c32c674701.png)

>다음 명령어를 차례대로 입력해서 nginx가 설치 되었는지를 확인합니다. 
```
$sudo apt update
$sudo apt install nginx -y
$systemctl status nginx
```
>![image](https://user-images.githubusercontent.com/45085563/142403092-207a93ae-4db2-4ad4-bf98-208cd5be8aa6.png)
> directory를 이동합니다. 
```cd /var/www/html ```
>![image](https://user-images.githubusercontent.com/45085563/142403503-13d4b6b5-565f-4424-b2bd-e74b086e9e45.png)
>다음 명령어를 입력하여 index.html을 삭제하고, 새롭게 생성합니다. 
```
sudo rm index.nginx-debian.html
sudo vi index.html
```

```xml
<!DOCTYPE html>
<html>

<head>
  <script src="https://sdk.amazonaws.com/js/aws-sdk-2.283.1.min.js"></script>
  <script src="./app.js"></script>
  <script>
    function getHtml(template) {
      return template.join('\n');
    }
    listAlbums();
  </script>
</head>

<body>
  <h1>My Photo Albums App</h1>
  <div id="app"></div>
</body>

</html>
```
index.html파일에 다음과 같이 입력합니다.![image](https://user-images.githubusercontent.com/45085563/142405482-812075f7-e86b-4ba4-96e6-7ef9a796e704.png)

>+ 마찬가지로 app.js파일을 생성합니다. ```sudo vi app.js```
```
var albumBucketName = 'kwonsoon';
var bucketRegion = 'us-east-1';
var IdentityPoolId = 'us-east-1:18bc5a31-916b-4241-844c-3328758e6a8e';

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IdentityPoolId
  })
});

var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {
    Bucket: albumBucketName
  }
});

function listAlbums() {
  s3.listObjects({
    Delimiter: '/'
  }, function (err, data) {
    if (err) {
      return alert('There was an error listing your albums: ' + err.message);
    } else {
      console.log('앨범', data.CommonPrefixes)
      var albums = data.CommonPrefixes.map(function (commonPrefix) {
        var prefix = commonPrefix.Prefix;
        var albumName = decodeURIComponent(prefix.replace('/', ''));
        return getHtml([
          '<li>',
          '<span onclick="deleteAlbum(\'' + albumName + '\')">X</span>',
          '<span onclick="viewAlbum(\'' + albumName + '\')">',
          albumName,
          '</span>',
          '</li>'
        ]);
      });
      var message = albums.length ?
        getHtml([
          '<p>Click on an album name to view it.</p>',
          '<p>Click on the X to delete the album.</p>'
        ]) :
        '<p>You do not have any albums. Please Create album.';
      var htmlTemplate = [
        '<h2>Albums</h2>',
        message,
        '<ul>',
        getHtml(albums),
        '</ul>',
        '<button onclick="createAlbum(prompt(\'Enter Album Name:\'))">',
        'Create New Album',
        '</button>'
      ]
      document.getElementById('app').innerHTML = getHtml(htmlTemplate);
    }
  });
}

function createAlbum(albumName) {
  albumName = albumName.trim();
  if (!albumName) {
    return alert('Album names must contain at least one non-space character.');
  }
  if (albumName.indexOf('/') !== -1) {
    return alert('Album names cannot contain slashes.');
  }
  var albumKey = encodeURIComponent(albumName) + '/';
  s3.headObject({
    Key: albumKey
  }, function (err, data) {
    if (!err) {
      return alert('Album already exists.');
    }
    if (err.code !== 'NotFound') {
      return alert('There was an error creating your album: ' + err.message);
    }
    s3.putObject({
      Key: albumKey
    }, function (err, data) {
      if (err) {
        return alert('There was an error creating your album: ' + err.message);
      }
      alert('Successfully created album.');
      viewAlbum(albumName);
    });
  });
}

function viewAlbum(albumName) {
  var albumPhotosKey = encodeURIComponent(albumName) + '//';
  s3.listObjects({
    Prefix: albumPhotosKey
  }, function (err, data) {
    if (err) {
      return alert('There was an error viewing your album: ' + err.message);
    }
    // 'this' references the AWS.Response instance that represents the response
    var href = this.request.httpRequest.endpoint.href;
    var bucketUrl = href + albumBucketName + '/';
    console.log('앨범', data.Contents)

    var photos = data.Contents.map(function (photo) {
      var photoKey = photo.Key;
      var photoUrl = bucketUrl + encodeURIComponent(photoKey);
      return getHtml([
        '<span>',
        '<div>',
        '<img style="width:128px;height:128px;" src="' + photoUrl + '"/>',
        '</div>',
        '<div>',
        '<span onclick="deletePhoto(\'' + albumName + "','" + photoKey + '\')">',
        'X',
        '</span>',
        '<span>',
        photoKey.replace(albumPhotosKey, ''),
        '</span>',
        '</div>',
        '</span>',
      ]);
    });
    var message = photos.length ?
      '<p>Click on the X to delete the photo</p>' :
      '<p>You do not have any photos in this album. Please add photos.</p>';
    var htmlTemplate = [
      '<h2>',
      'Album: ' + albumName,
      '</h2>',
      message,
      '<div>',
      getHtml(photos),
      '</div>',
      '<input id="photoupload" type="file" accept="image/*">',
      '<button id="addphoto" onclick="addPhoto(\'' + albumName + '\')">',
      'Add Photo',
      '</button>',
      '<button onclick="listAlbums()">',
      'Back To Albums',
      '</button>',
    ]
    document.getElementById('app').innerHTML = getHtml(htmlTemplate);
  });
}

function addPhoto(albumName) {
  var files = document.getElementById('photoupload').files;
  if (!files.length) {
    return alert('Please choose a file to upload first.');
  }
  var file = files[0];
  var fileName = file.name;
  var albumPhotosKey = encodeURIComponent(albumName) + '//';

  var photoKey = albumPhotosKey + fileName;
  s3.upload({
    Key: photoKey,
    Body: file,
    ACL: 'public-read'
  }, function (err, data) {
    if (err) {
      console.log(err)
      return alert('There was an error uploading your photo: ', err.message);
    }
    alert('Successfully uploaded photo.');
    viewAlbum(albumName);
  });
}

function deletePhoto(albumName, photoKey) {
  s3.deleteObject({
    Key: photoKey
  }, function (err, data) {
    if (err) {
      return alert('There was an error deleting your photo: ', err.message);
    }
    alert('Successfully deleted photo.');
    viewAlbum(albumName);
  });
}

function deleteAlbum(albumName) {
  var albumKey = encodeURIComponent(albumName) + '/';
  s3.listObjects({
    Prefix: albumKey
  }, function (err, data) {
    if (err) {
      return alert('There was an error deleting your album: ', err.message);
    }
    var objects = data.Contents.map(function (object) {
      return {
        Key: object.Key
      };
    });
    s3.deleteObjects({
      Delete: {
        Objects: objects,
        Quiet: true
      }
    }, function (err, data) {
      if (err) {
        return alert('There was an error deleting your album: ', err.message);
      }
      alert('Successfully deleted album.');
      listAlbums();
    });
  });
}
``` 

>+ 다음 코드를 app.js에 입력합니다. 여기서 
```json
var albumBucketName = 'kwonsoon';
var bucketRegion = 'us-east-1';
```부분은 자신의 bucket이름과 region을 입력합니다. 

## 3.웹페이지에 접속해서 s3에 사진 업로드
> + 생성한 vm의 ip로 접속하면 다음과 같은 화면을 얻을 수 있습니다.
![image](https://user-images.githubusercontent.com/45085563/142407419-6076abca-ce17-4ebe-b8a6-1ecc204ff14a.png)

## 4.s3와 rekognition을 연동, 사진을 labeling가능한지 확인
