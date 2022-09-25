# TodoApp

### AWS + Docker + Nginx + FastAPI + MySQL

> 실행 방법
> * AWS EC2 인스턴스 생성
> * ssh 접속 후 docker 설치
>
> * /app/.env 파일 생성
> * /config/mysql/.env 파일 생성
> 
> ```
> # /app/.env
> 
> ```
  
```bash
git clone https://github.com/sihyeong671/Simple-TodoAPP-Server.git
cd Simple-TodoAPP-Server
sudo docker compose up -d

# 동작 확인
sudo docker compose ps
```
