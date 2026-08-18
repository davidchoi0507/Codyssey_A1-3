# moodwave - 감정 기반 음악 추천 웹 서비스

사용자의 현재 감정과 상황을 분석하여 위로의 한 줄과 어울리는 음악을 추천해 주는 웹 애플리케이션입니다.

## 🔗 배포 및 저장소 링크
- **서비스 배포 URL:** [여기에 Vercel 배포 URL 붙여넣기]
- **GitHub 저장소 URL:** https://github.com/davidchoi0507/Codyssey_A1-3

## 🛠️ 기술 스택
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (반응형 UI)
- **Backend:** Python (Vercel Serverless Functions)
- **AI / LLM:** OpenAI API (`gpt-3.5-turbo`)
- **Deployment:** Vercel

## 📂 프로젝트 구조
├── api/
│   └── recommend.py    # OpenAI API 연동 백엔드 서버리스 함수
├── index.html          # 메인 웹페이지 (Hero, 추천 섹션, FAQ)
├── style.css           # 반응형 스타일시트
├── script.js           # 프론트엔드 비동기 통신 및 UI 렌더링
└── README.md


## ⚙️ 환경 변수 설정
Vercel 대시보드의 **Settings > Environment Variables**에 아래 키를 등록해야 정상 작동합니다.
- `OPENAI_API_KEY`: OpenAI API Secret Key
