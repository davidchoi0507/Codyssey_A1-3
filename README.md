# moodwave - 감정 기반 음악 추천 웹 서비스

사용자의 현재 감정과 상황을 분석하여 위로의 한 줄과 어울리는 음악을 추천해 주는 웹 애플리케이션입니다.

## 🔗 배포 및 저장소 링크
- **서비스 배포 URL:** https://codyssey-a1-3-8s2fcs9u5-david-choi1.vercel.app
- **GitHub 저장소 URL:** https://github.com/davidchoi0507/Codyssey_A1-3

## 🛠️ 기술 스택
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (반응형 웹 UI)
- **Backend:** Python (Vercel Serverless Functions)
- **AI / LLM:** Google Gemini API (`gemini-3.5-flash-lite`)
- **Deployment:** Vercel

## 프로젝트 구조
```
├── api/
│   └── recommend.py    # Gemini API 연동 백엔드 서버리스 함수 및 알림 연동
├── index.html          # 메인 웹페이지 (Hero, AI 추천 섹션, FAQ)
├── style.css           # 반응형 스타일시트 및 다크모드 테마
├── script.js           # 프론트엔드 비동기 통신, UX 예외 처리, 다크모드 토글
└── README.md           # 프로젝트 문서
```

## 환경 변수 설정
Vercel 대시보드의 **Settings > Environment Variables**에 아래 키를 등록해야 정상 작동합니다.
- `GEMINI_API_KEY`
