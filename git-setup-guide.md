
# Git 전역 설정 및 로컬 저장소 생성 가이드

## ✅ 1. 개행 문자 설정

운영 체제에 따라 자동 개행 문자 변환 설정:

### ▶ Windows:
```
git config --global core.autocrlf true
```

### ▶ macOS (또는 Linux):
```
git config --global core.autocrlf input
```

---

## ✅ 2. 사용자 이름과 이메일 주소 설정

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## ✅ 3. 기본 브랜치 이름을 `main`으로 설정

```
git config --global init.defaultBranch main
```

---

## ✅ 4. Git 전역 설정 목록 확인

```
git config --global --list
```

---

## ✅ 5. Git 전역 설정을 에디터로 열기

```
git config --global --edit
```

---

## ✅ 6. Git 기본 에디터를 Visual Studio Code로 설정

```
git config --global core.editor "code --wait"
```

> `code --wait`는 설정 파일을 열고 닫을 때까지 Git이 기다리게 합니다.

---

## ✅ 7. 작업 디렉토리에서 Git 저장소 생성

`app.py`가 있는 디렉토리로 이동 후 저장소를 초기화합니다:

```
cd /path/to/your/project  # app.py가 있는 디렉토리로 이동
git init
```

> 경로는 실제 파일 위치에 맞게 변경하세요.
