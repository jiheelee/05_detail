# READ ME

### 목표

- 영화 추천 사이트의 세부 페이지 구성
- Template Variable을 활용한 Template 제작



### 환경

- Django Web Framework
- C9.io
- html / css
- Bootstrap v.4.2.1



#### 1. Django Setting

- movie 프로젝트를 생성하고 detail 이라는 앱을 생성
- setting에 언어와 allowed_host를 설정해줌

#### 2. base.html 구성

- Bootstrap을 적용시킴
- MySite, Q&A, Mypage, SignUp 메뉴를 구성
- 메뉴 위치는 d-flex justify-content-between 옵션으로 지정
- favicon 추가

#### 3. 페이지 구성

- 페이지들은 base.html을 extends 시켜서 구성
- /
  - header 와 footer 를 사용하여 페이지 구성
  - Header
    - 높이는 350px, 너비는 브라우저 전체 영역
    - header 에 배경 이미지 적용
    - header 영역의 수직/수평 가운데 정렬 위치에 h1 태그를 이용하여 글 작성
  - Footer
    - 브라우저 최하단에 고정
    - 높이는 50px 이상, 너비는 브라우저 전체 영역
    - 좌측에는 이름, 우측에는 브라우저 최상단으로 이동하는 링크
- signup
  - Form 태그를 이용하여 email, text, password * 2 총 4개의 input 생성
  - Grid System 을 이용하여 좌측에는 이미지 우측에는 Form 을 생성
- mypage
  - 화면의 좌측에는 사용자의 정보, 우측에는 사용자가 작성한 글 목록을 보여주는 영역 생성
  - Card를 이용해서 좌측 사용자의 정보란을 구성
    - 이미지는 rounded-circle 클래스를 이용하여 원형으로 구성
    - 이미지는 static 폴더 안에 있는 이미지를 사용
    - position-fixed 클래스를 이용하여 스크롤이 내려가도 좌측에 계속 유지하도록 구성
  - Jumbotron과 Card를 이용해서 우측 사용자가 작성한 글 목록을 구성
- qna
  - Form 태그를 이용하여 제목, 이메일, 내용을 입력하는 input 생성
  - col 클래스를 이용하여 제목과 이메일 부분은 Grid System 적용
- str:not_found
  - 위의 경로가 아닌 다른 요청이 들어올 경우 보여지는 404 페이지 구성
  - variable routing을 이용하여 사용자가 잘못 입력한 경로를 띄워줌