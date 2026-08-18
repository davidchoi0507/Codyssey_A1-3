import json
import os
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, body):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode("utf-8"))

    def do_OPTIONS(self):
        self._send_json(204, {})

    def do_POST(self):
        try:
            # 1. 프론트엔드에서 보낸 데이터 읽기
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length)
            request_data = json.loads(raw_body.decode("utf-8"))
            mood = str(request_data.get("mood", "")).strip()

            if not mood:
                self._send_json(400, {"error": "기분을 입력해주세요."})
                return

            # 2. Vercel 환경 변수에서 API 키 가져오기
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                self._send_json(500, {"error": "서버에 API 키가 설정되지 않았습니다."})
                return

            # 3. OpenAI API로 보낼 편지(데이터) 작성
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            
            system_prompt = """당신은 따뜻하고 감각적인 음악 큐레이터입니다.
사용자의 현재 기분을 읽고 한국어로 짧은 위로와 음악을 추천하세요.
답변은 반드시 아래 JSON 형식으로만 해주세요:
{
  "comfort_message": "위로의 한 줄",
  "recommended_music": "곡명 - 아티스트"
}"""

            data = {
                "model": "gpt-3.5-turbo", # 빠르고 안정적인 3.5 모델 사용
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"사용자의 기분: {mood}"}
                ],
                "temperature": 0.7
            }

            # 4. 순수 파이썬 기능으로 우체국(API)에 편지 접수
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
            
            try:
                # 5. 우체국에서 답장 받기
                with urllib.request.urlopen(req) as response:
                    response_body = response.read().decode("utf-8")
                    result_json = json.loads(response_body)
                    
                    # AI가 준 텍스트(문자열)를 다시 JSON으로 변환
                    ai_content = result_json["choices"][0]["message"]["content"]
                    recommendation = json.loads(ai_content)
                    
                    self._send_json(200, recommendation)
                    
            except urllib.error.HTTPError as e:
                error_info = e.read().decode()
                print(f"OpenAI API Error: {error_info}")
                self._send_json(500, {"error": "OpenAI 서버와 통신하는 중 문제가 발생했습니다."})

        except Exception as error:
            print(f"General Server Error: {error}")
            self._send_json(500, {"error": "추천을 생성하는 중 서버 내부 오류가 발생했습니다."})

    def do_GET(self):
        self._send_json(405, {"error": "POST 요청만 지원합니다."})