# FastAPI 연습 프로젝트

## 소개
이 프로젝트는 **FastAPI** 프레임워크를 학습하고 실습하기 위해 만들어졌습니다.  
할 일(Task)을 관리하는 간단한 REST API 서버로, 기본적인 CRUD 동작과 API 문서화 기능을 포함하고 있습니다.

## 주요 기능
- **할 일(Task) 관리**:
  - 할 일 목록 조회
  - 할 일 생성
  - 할 일 수정
  - 할 일 삭제
- **완료 상태 관리**:
  - 할 일 완료 처리 및 완료 취소

## 기술 스택 (Tech Stack)
- **Language**: Python 3.10+
- **Web Framework**: FastAPI
- **Server**: Uvicorn
- **Database ORM**: SQLAlchemy (Synchronous)
- **DB Driver**: PyMySQL
- **Other Tools**: 
  - Playwright (E2E 테스팅 또는 브라우저 자동화 용도)
  - Docker & Docker Compose
  - uv (Python Package Manager)

## 실행 방법

### 1. 로컬 환경에서 실행 (권장)
이 프로젝트는 `uv`를 사용하여 의존성을 관리합니다.

#### 사전 준비
- Python 3.10 이상 설치
- 로컬 MySQL 데이터베이스 실행 필요 (`3306` 포트)
  - Database 이름: `todo`
  - 접속 정보가 `api/db.py`에 하드코딩 되어 있으니 본인 환경에 맞게 수정이 필요할 수 있습니다.

#### 설치 및 실행
```bash
# 의존성 설치
uv sync

# 서버 실행
uv run uvicorn api.main:app --reload
```

### 2. Docker Compose 실행
Docker 환경에서 서버를 실행할 수 있습니다. (현재 DB 컨테이너 설정은 포함되어 있지 않으므로, 외부 DB 연결 설정이 필요할 수 있습니다.)

```bash
docker-compose up --build
```

## API 문서 확인
서버가 실행된 후, 아래 주소에서 Swagger UI를 통해 API를 직접 테스트해볼 수 있습니다.

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
