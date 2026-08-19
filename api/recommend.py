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
            # 1. 프론트엔드 데이터 읽기
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length)
            request_data = json.loads(raw_body.decode("utf-8"))
            mood = str(request_data.get("mood", "")).strip()

            if not mood:
                self._send_json(400, {"error": "기분을 입력해주세요."})
                return

            # 2. Vercel 환경 변수에서 Gemini API 키 가져오기
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                self._send_json(500, {"error": "서버에 API 키가 설정되지 않았습니다."})
                return

            # 3. Gemini API 주소 및 데이터 작성 (선생님이 쓰시던 gemini-3.5-flash-lite 유지)
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            
            prompt = f"""당신은 따뜻하고 감각적인 음악 큐레이터입니다.
사용자의 현재 기분을 읽고 한국어로 짧은 위로와 음악을 추천하세요.
사용자의 기분: {mood}

답변은 반드시 아래 JSON 형식으로만 작성하세요:
{{
  "comfort_message": "위로의 한 줄",
  "recommended_music": "곡명 - 아티스트"
}}"""

            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "response_mime_type": "application/json"
                }
            }

            # 4. Gemini에게 요청 보내기
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
            
            try:
                # 5. Gemini의 답장 받기
                with urllib.request.urlopen(req) as response:
                    response_body = response.read().decode("utf-8")
                    result_json = json.loads(response_body)
                    
                    # Gemini의 응답 구조에서 텍스트 뽑아내기
                    ai_content = result_json["candidates"][0]["content"]["parts"][0]["text"]
                    recommendation = json.loads(ai_content)
                    
                    # ==================== [보너스 과제] 운영 자동화 (Discord 연동) ====================
                    discord_webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
                    if discord_webhook_url:
                        try:
                            webhook_data = {
                                "content": f"🎵 **[Moodwave 신규 추천 발생]**\n- **사용자 기분**: {mood}\n- **위로 문구**: {recommendation.get('comfort_message')}\n- **추천 음악**: {recommendation.get('recommended_music')}"
                            }
                            
                            wb_req = urllib.request.Request(
                                discord_webhook_url, 
                                data=json.dumps(webhook_data).encode("utf-8"), 
                                headers={
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                }
                            )
                            urllib.request.urlopen(wb_req, timeout=2)
                        except Exception as wb_err:
                            print(f"Webhook 전송 오류: {wb_err}")
                    # =========================================================================================

                    self._send_json(200, recommendation)
                    
            except urllib.error.HTTPError as e:
                error_info = e.read().decode()
                print(f"Gemini API Error: {error_info}")
                self._send_json(500, {"error": "Gemini 서버와 통신하는 중 문제가 발생했습니다."})

        except Exception as error:
            print(f"General Server Error: {error}")
            self._send_json(500, {"error": "추천을 생성하는 중 서버 내부 오류가 발생했습니다."})

    def do_GET(self):
        self._send_json(405, {"error": "POST 요청만 지원합니다."})
