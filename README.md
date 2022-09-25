# TodoApp

### AWS + Docker + Nginx + FastAPI + MySQL

> 실행 방법
> * AWS EC2 인스턴스 생성
> * ssh 접속 후 docker 설치
> * 아래 명령어 실행
>
> ```bash
> git clone https://github.com/sihyeong671/Simple-TodoAPP-Server.git
> cd Simple-TodoAPP-Server
>
> ```
> 
>
> * /app/.env 파일 생성
> * /config/mysql/.env 파일 생성
> 
> ```
> # /app/.env
> MYSQL_USER=root
> MYSQL_PASSWORD=#your root password
> MYSQL_HOST=db # same as docker container name
> MYSQL_PORT=8008
> MYSQL_DB_NAEM=TODOS
>
> # /config/mysql/.env
> MYSQL_ROOT_PASSWORD=#your root password
> MYSQL_USER=#custom user name
> MYSQL_PASSWORD=#custom user password
> ```
>
> sudo명령어는 AWS에서 사용
> ```
> 도커 컨테이너 올리기
> sudo docker compose up -d
> # 동작 확인
> sudo docker compose ps
> ```
  

<img width="1438" alt="스크린샷 2022-09-25 오후 10 11 25" src="https://user-images.githubusercontent.com/77565951/192145537-6ccdd4b0-3a2c-4616-846d-61144a95d60d.png">
