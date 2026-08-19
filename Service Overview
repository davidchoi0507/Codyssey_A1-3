<!-----



Conversion time: 4.432 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs™ to Markdown version 2.0β2
* Tue Aug 18 2026 21:14:28 GMT-0700 (미 태평양 하계 표준시)
* Source doc: A1-3 moodwave 서비스 기획서
* Tables are currently converted to HTML tables.
----->



# moodwave (감정 기반 맞춤형 음악 큐레이션 웹 서비스) 서비스 기획서

**문서 버전:** v1.0

**작성자:** 코디세이 AI 네이티브 과정 참가자

**프로젝트명:** moodwave (Codyssey_A1-3)

**기획 분야:** 풀스택 생성형 AI 웹 서비스


## 1. 서비스 개요 및 기획 배경


### 1.1. 서비스 정의

**moodwave**는 사용자가 겪고 있는 일상적인 상황이나 내면의 감정을 자연어 텍스트로 자유롭게 표현하면, 대규모 언어 모델(LLM)이 텍스트 이면의 정서를 분석하여 마음을 어루만지는 **‘공감과 위로의 한마디’**와 그 감정의 파동에 어울리는 **‘맞춤형 음악 1곡(곡명 및 아티스트)’**을 즉각 추천해 주는 반응형 웹 애플리케이션입니다.


### 1.2. 기획 배경 및 문제 정의



* **감정의 과부하와 피로감:** 현대 사회의 복잡한 인간관계와 학업·업무 스트레스 속에서 많은 사람들은 자신의 감정을 온전히 털어놓고 위로받을 공간이 부족합니다.
* **음악 탐색 비용의 증가:** 스트리밍 플랫폼의 방대한 음악 라이브러리 속에서 '지금 내 기분에 딱 맞는 노래'를 검색하고 고르는 일조차 선택의 피로(Choice Fatigue)를 유발합니다.
* **텍스트 기반 정서 교감의 필요성:** 긴 대화형 챗봇의 부담감 없이, 한두 줄의 솔직한 고백만으로 즉각적인 정서적 지지와 큐레이션을 받을 수 있는 직관적인 마이크로 인터랙션 서비스가 요구됩니다.


## 2. 서비스 목적 및 핵심 가치


### 2.1. 서비스 목적



* **정서적 환기와 심리적 안정 제공:** 텍스트 작성을 통한 감정 배출(Catharsis)과 AI의 따뜻한 공감 피드백을 통해 사용자의 일상에 작은 위로를 전달합니다.
* **직관적이고 매끄러운 음악 발견 경험:** 알고리즘 기반 차트 순위가 아닌, 사용자의 고유한 순간과 정서적 맥락에 기반한 딥 리스닝(Deep Listening) 음악을 제안합니다.
* **경량화된 웹 표준 구현:** 무거운 프레임워크 없이 웹 표준 기술(Vanilla HTML/CSS/JS)과 서버리스 아키텍처를 결합하여 빠르고 안전하며 누구나 쉽게 접근할 수 있는 웹 환경을 구축합니다.


### 2.2. 핵심 가치 (Core Values)


<table>
  <tr>
   <td>핵심 가치
   </td>
   <td>정의 및 구현 방향
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>Empathy (공감)</strong>
   </td>
   <td>단순 키워드 매칭이 아닌 문맥과 감정의 결을 읽어내는 페르소나 기반 위로 메시지 제공
   </td>
  </tr>
  <tr>
   <td><strong>Simplicity (단순성)</strong>
   </td>
   <td>별도의 회원가입이나 복잡한 설정 없이 한 줄 입력으로 완성되는 단일 루프 UX
   </td>
  </tr>
  <tr>
   <td><strong>Responsiveness (접근성)</strong>
   </td>
   <td>PC 브라우저부터 모바일 화면까지 깨짐 없는 미디어 쿼리 기반 반응형 레이아웃 구현
   </td>
  </tr>
  <tr>
   <td><strong>Security (보안성)</strong>
   </td>
   <td>Vercel 환경 변수 격리를 통해 민감한 API 인증 키의 노출을 원천 차단하는 안전한 아키텍처
   </td>
  </tr>
</table>



## 3. 타겟 사용자 정의 및 페르소나


### 3.1. 주 타겟 및 부 타겟



* **주 타겟 (Primary):** 일상, 학업, 직장에서 스트레스를 받고 즉각적인 감정 해소 및 따뜻한 위로가 필요한 2030 직장인 및 취업준비생/학생
* **부 타겟 (Secondary):** 정형화된 인기 차트 중심의 음악에서 벗어나 상황 맞춤형 명곡을 추천받고 싶은 인디/감성 음악 리스너


### 3.2. 대표 페르소나 (Persona)


<table>
  <tr>
   <td>구분
   </td>
   <td>페르소나 A (직장인 이지은, 28세)
   </td>
   <td>페르소나 B (대학생 최준혁, 23세)
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>상황 및 Pain Point</strong>
   </td>
   <td>퇴근길 지하철에서 업무 스트레스로 우울하며, 누구에게도 하소연하기 어려운 상태
   </td>
   <td>시험 기간 늦은 밤 도서관에서 집중이 안 되고 공허함을 느끼며 분위기 전환이 필요함
   </td>
  </tr>
  <tr>
   <td><strong>서비스 니즈</strong>
   </td>
   <td>짧게 감정을 털어놓고 바로 나를 다독여주는 말과 차분한 음악을 추천받고 싶음
   </td>
   <td>현재의 고독하고 몽환적인 감성에 어울리는 새로운 앰비언트/인디 음악을 탐색하고 싶음
   </td>
  </tr>
  <tr>
   <td><strong>사용 시나리오</strong>
   </td>
   <td>모바일 웹으로 접속하여 "오늘 회사에서 크게 혼나서 자존감이 바닥이야" 입력 후 위로와 음악 확인
   </td>
   <td>노트북으로 접속하여 "비 오는 밤 홀로 집중할 수 있는 차분한 음악이 필요해" 입력 후 추천곡 감상
   </td>
  </tr>
</table>



## 4. 정보 구조도(IA) 및 페이지/섹션 구성


### 4.1. 전체 페이지 레이아웃 구조

사용자 편의성과 단일 페이지 웹(SPA)의 직관성을 살려, 상단 고정 네비게이션과 스무스 스크롤로 연결되는 **3단 핵심 섹션** 및 **헤더/푸터**로 구성합니다.


<table>
  <tr>
   <td>섹션명 (HTML ID)
   </td>
   <td>구성 요소
   </td>
   <td>기능 및 UI 역할
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>Header / Navbar</strong>
   </td>
   <td>
<ul>

<li>브랜드 로고 (moodwave)</li>

<li>섹션 바로가기 네비게이션 링크 (소개, 추천받기, FAQ)</li>

<li>다크모드 테마 토글 버튼 (🌙 / ☀️)</li>
</ul>
   </td>
   <td>상단 상시 고정(Sticky Header), 블러 백그라운드 적용, 원클릭 섹션 스크롤 이동 및 테마 전환
   </td>
  </tr>
  <tr>
   <td><strong>1. Hero 섹션 (#home)</strong>
   </td>
   <td>
<ul>

<li>서브 타이포 (EYEBROW)</li>

<li>메인 카피라이팅 (H1 헤드라인)</li>

<li>서비스 소개 서술문 및 시각 오브제 (Glow Orb)</li>

<li>'지금 시작하기' CTA 버튼</li>
</ul>
   </td>
   <td>서비스의 핵심 컨셉 전달, 시각적 몰입감 제공, 음악 추천 입력 폼으로의 빠른 유도
   </td>
  </tr>
  <tr>
   <td><strong>2. AI 음악 추천 섹션 (#recommend)</strong>
   </td>
   <td>
<ul>

<li>섹션 헤드라인 및 안내 문구</li>

<li>감정 입력 폼 (&lt;input type="text">)</li>

<li>'추천받기' 액션 버튼</li>

<li>입력 가이드 힌트 텍스트</li>

<li>AI 추천 결과 렌더링 카드 (.result)</li>
</ul>
   </td>
   <td>사용자 감정 텍스트 수집, 비동기 통신(fetch), 로딩 인디케이터 처리, 위로 문구 및 추천 음악 카드 출력
   </td>
  </tr>
  <tr>
   <td><strong>3. FAQ 섹션 (#faq)</strong>
   </td>
   <td>
<ul>

<li>섹션 소개 타이틀</li>

<li>아코디언 형태의 질의응답 리스트 (&lt;details>, &lt;summary>)</li>
</ul>
   </td>
   <td>AI 음악 추천 원리, 데이터 보안 및 처리 방식, 추천 실패 시 대처법 등 사용자 가이드 제공
   </td>
  </tr>
  <tr>
   <td><strong>Footer</strong>
   </td>
   <td>
<ul>

<li>저작권 표기 (© 2026 moodwave)</li>

<li>프로젝트 메타데이터 정보</li>
</ul>
   </td>
   <td>웹 서비스 마무리 영역 및 브랜딩 정체성 유지
   </td>
  </tr>
</table>



## 5. 핵심 기능 명세 (Feature Specifications)


### 5.1. 프론트엔드 기능 명세



* **순수 웹 표준 구현 (Vanilla Web):** React, Vue 등의 무거운 라이브러리 없이 순수 HTML5 시맨틱 태그, CSS3 Flex/Grid, Vanilla JavaScript를 활용하여 브라우저 로딩 속도 최적화.
* **반응형 웹 디자인 (Responsive Design):** 미디어 쿼리(@media (max-width: 720px))를 적용하여 데스크톱(1120px 기준), 태블릿, 모바일 기기 등 모든 해상도에서 레이아웃 깨짐 없이 100% 최적화된 뷰 제공.
* **비동기 통신 및 UX 상태 제어:** 자바스크립트 fetch API를 활용하여 페이지 새로고침 없이 백엔드(/api/recommend)와 통신하며, 응답 대기 중 버튼 비활성화(disabled) 및 "로딩 중..." 텍스트 피드백 제공.


### 5.2. 백엔드 및 AI 연동 명세



* **서버리스 아키텍처 (Serverless Function):** Vercel 플랫폼 기반의 api/recommend.py를 통해 서버 인프라 관리 없이 온디맨드로 실행되는 경량 백엔드 파이프라인 구축.
* **무의존성 직통 통신 (Zero-Dependency Architecture):** 외부 중량 패키지 없이 파이썬 내장 라이브러리인 urllib.request를 사용하여 LLM API 엔드포인트와 HTTP POST 직통 통신을 수행, 콜드 스타트 및 빌드 의존성 에러 원천 차단.
* **정형화된 JSON 데이터 파싱:** LLM의 자연어 응답 중 구조화된 JSON 데이터만을 안전하게 파싱하여 클라이언트에 200 OK 상태 코드와 함께 전달.


### 5.3. 보너스 고도화 기능 명세



* **UX 고도화 (다크 모드 & LocalStorage):**
    * 사용자 브라우저의 로컬 스토리지에 테마 설정을 저장하여 재방문 시에도 설정 유지.
    * 부드러운 CSS transition (0.4s ease)을 통해 시각적 피로도를 최소화하는 전환 효과 적용.
* **운영 자동화 (Discord Webhook 연동):**
    * 사용자가 추천을 생성할 때마다 백엔드에서 운영자 모니터링 채널(Discord Webhook)로 사용자 입력 감정, 위로 문구, 추천 곡명을 실시간 자동 알림 전송.
    * 타임아웃(2초) 및 예외 격리(try-except) 처리를 통해 알림 서버의 장애가 메인 서비스에 영향을 주지 않도록 결함 격리 설계.


## 6. AI 기능 입·출력 및 실패/예외 처리 기준


### 6.1. AI 시스템 프롬프트 및 페르소나 설계


<table>
  <tr>
   <td><strong>AI 페르소나</strong>
   </td>
   <td>사용자의 지친 마음을 따뜻하게 안아주고 감각적인 음악을 골라주는 전문 감성 음악 큐레이터
   </td>
  </tr>
  <tr>
   <td><strong>지시문 (System Prompt)</strong>
   </td>
   <td>
    당신은 따뜻하고 감각적인 음악 큐레이터입니다. \
사용자의 현재 기분을 읽고 한국어로 짧은 위로와 음악을 추천하세요. \
답변은 반드시 아래 JSON 형식으로만 해주세요: \
{ \
  "comfort_message": "사용자에게 전하는 따뜻한 위로의 한 줄", \
  "recommended_music": "곡명 - 아티스트" \
}
   </td>
  </tr>
  <tr>
   <td><strong>LLM 모델 및 파라미터</strong>
   </td>
   <td>Google Gemini API / OpenAI API, Temperature: 0.7 (자연스럽고 감성적인 표현 유도)
   </td>
  </tr>
</table>



### 6.2. 데이터 입·출력 인터페이스 규격


<table>
  <tr>
   <td>구분
   </td>
   <td>필드명
   </td>
   <td>타입
   </td>
   <td>설명 및 예시
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>입력 (Request)</strong>
   </td>
   <td>mood
   </td>
   <td>String (필수)
   </td>
   <td>사용자가 입력한 자연어 감정 텍스트
<p>
<em>예: "오늘 시험을 망쳐서 너무 우울하고 기운이 없어"</em>
   </td>
  </tr>
  <tr>
   <td rowspan="2" ><strong>출력 (Response)</strong>
   </td>
   <td>comfort_message
   </td>
   <td>String
   </td>
   <td>감정에 공감하는 따뜻한 위로의 문구 (1~2문장)
<p>
<em>예: "노력했던 만큼 아쉬움이 크겠지만, 오늘 하루만큼은 푹 쉬며 자신을 다독여주세요."</em>
   </td>
  </tr>
  <tr>
   <td>recommended_music
   </td>
   <td>String
   </td>
   <td>정서적 맥락에 어울리는 추천 곡명 및 가수
<p>
<em>예: "옥상달빛 - 수고했어, 오늘도"</em>
   </td>
  </tr>
</table>



### 6.3. 단계별 실패 및 예외 처리 기준 (Exception Handling)

서비스의 신뢰성과 사용자 경험을 보호하기 위해 클라이언트, 통신 계층, 서버리스 백엔드, AI 응답의 4단계 예외 처리 기준을 정의합니다.


<table>
  <tr>
   <td>발생 단계
   </td>
   <td>예외 시나리오
   </td>
   <td>시스템 처리 기준
   </td>
   <td>사용자 피드백 (UX)
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>1. 클라이언트 입력 검증</strong>
   </td>
   <td>사용자가 입력창에 아무것도 입력하지 않거나 공백만 입력 후 '추천받기' 클릭
   </td>
   <td>JavaScript 레벨에서 !mood.trim() 검증 수행, API 통신 차단
   </td>
   <td>브라우저 경고창 출력:
<p>
"기분을 입력해주세요!"
   </td>
  </tr>
  <tr>
   <td><strong>2. 비동기 통신 오류</strong>
   </td>
   <td>인터넷 연결 끊김, Vercel 네트워크 지연 또는 타임아웃 발생
   </td>
   <td>fetch().catch() 블록에서 에러 감지, 버튼 상태 원복 (disabled = false)
   </td>
   <td>결과 영역 안내 문구:
<p>
"추천을 불러오는 중 문제가 발생했어요. 잠시 후 다시 시도해주세요."
   </td>
  </tr>
  <tr>
   <td><strong>3. 백엔드 인증/설정 오류</strong>
   </td>
   <td>Vercel 환경 변수(API 키) 미설정 또는 잘못된 키 입력
   </td>
   <td>HTTP 500 에러 반환 및 서버 로그에 OPENAI_API_KEY / GEMINI_API_KEY 누락 기록
   </td>
   <td>클라이언트에 에러 코드 전달 및 UI에 재시도 안내 메시지 표시
   </td>
  </tr>
  <tr>
   <td><strong>4. AI 응답 파싱 오류</strong>
   </td>
   <td>LLM이 지정된 JSON 규격 외에 부가적인 마크다운이나 텍스트를 반환한 경우
   </td>
   <td>파이썬 json.JSONDecodeError 예외를 try-except로 포획하여 결함 격리
   </td>
   <td>안전한 Fallback 응답 반환 또는 HTTP 500 에러 처리 후 클라이언트에 친절한 재시도 유도
   </td>
  </tr>
  <tr>
   <td><strong>5. 허용되지 않은 HTTP 메서드</strong>
   </td>
   <td>브라우저 주소창 직접 입력(GET 요청) 등 지원하지 않는 메서드로 접근
   </td>
   <td>do_GET() 메서드에서 HTTP 405 Method Not Allowed 반환
   </td>
   <td>{"error": "POST 요청만 지원합니다."} JSON 반환으로 엔드포인트 오용 방지
   </td>
  </tr>
</table>



## 7. 기술 스택 및 보안 아키텍처


### 7.1. 기술 스택 요약


<table>
  <tr>
   <td>계층 (Layer)
   </td>
   <td>사용 기술
   </td>
   <td>선정 이유 및 역할
<p>
 
   </td>
  </tr>
  <tr>
   <td><strong>Frontend</strong>
   </td>
   <td>HTML5, CSS3, Vanilla JavaScript
   </td>
   <td>순수 웹 표준 기술로 경량화 및 브라우저 호환성 확보, 반응형 UI 제공
   </td>
  </tr>
  <tr>
   <td><strong>Backend (Serverless)</strong>
   </td>
   <td>Python 3.12 (Vercel Serverless Functions)
   </td>
   <td>서버리스 경량 엔드포인트 구현, API 키 보안 유지, 비즈니스 로직 처리
   </td>
  </tr>
  <tr>
   <td><strong>AI Engine</strong>
   </td>
   <td>Google Gemini API / OpenAI API
   </td>
   <td>감정 분석 및 위로 문구/음악 추천 생성용 생성형 AI 모델
   </td>
  </tr>
  <tr>
   <td><strong>Deployment / Hosting</strong>
   </td>
   <td>Vercel (CI/CD 연동)
   </td>
   <td>GitHub 연동 자동 배포 및 전 세계 CDN 기반 빠른 로딩 속도 보장
   </td>
  </tr>
  <tr>
   <td><strong>Version Control</strong>
   </td>
   <td>Git, GitHub
   </td>
   <td>소스 코드 형상 관리 및 과제 제출용 리포지토리 운용
   </td>
  </tr>
</table>



### 7.2. 보안 및 환경 변수 관리 원칙



* **API 키 유출 방지:** AI 서비스 호출에 사용되는 API Secret Key는 프론트엔드 코드나 깃허브 저장소(GitHub Repo)에 절대 하드코딩하지 않습니다.
* **Vercel 환경 변수 격리:** Vercel 대시보드의 Settings > Environment Variables에 환경 변수로 안전하게 등록하여 서버 사이드(백엔드)에서만 os.environ.get()을 통해 접근하도록 격리합니다.
* **CORS 보안 헤더 설정:** 백엔드 응답 시 정형화된 HTTP 헤더(Content-Type: application/json; charset=utf-8, Access-Control-Allow-Origin: *)를 명시하여 웹 표준 통신 규격을 준수합니다.
