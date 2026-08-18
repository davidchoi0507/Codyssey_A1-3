import json
import os
from http.server import BaseHTTPRequestHandler
from openai import OpenAI

SYSTEM_PROMPT = """당신은 따뜻하고 감각적인 음악 큐레이터입니다.
사용자의 현재 기분을 읽고 한국어로 짧은 위로와 음악을 추천하세요.
반드시 요청된 JSON 형식만 반환하며, 추천 음악에는 곡명과 아티스트를 포함하세요.
"""

# 최신 OpenAI 규격에 맞춘 JSON 스키마
RESPONSE_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "mood_music_recommendation",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "comfort_message": {
                    "type": "string",
                    "description": "사용자에게 전하는 따뜻한 위로의 한 줄",
                },
                "recommended_music": {
                    "type": "string",
                    "description": "추천 곡명과 아티스트",
                },
            },
            "required": ["comfort_message", "recommended_music"],
            "additionalProperties": False,
        }
    }
}

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
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length)
            request_data = json.loads(raw_body.decode("utf-8"))
            mood = str(request_data.get("mood", "")).strip()

            if not mood:
                self._send_json(400, {"error": "기분을 입력해주세요."})
                return

            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise RuntimeError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

            client = OpenAI(api_key=api_key)
            
            # 여기서 에러가 났었습니다! 존재하지 않는 responses 대신 올바른 chat.completions 사용
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"사용자의 기분: {mood}"}
                ],
                response_format=RESPONSE_SCHEMA
            )
            
            # AI가 준 JSON 텍스트를 파이썬 데이터로 변환
            recommendation = json.loads(completion.choices[0].message.content)

            self._send_json(200, recommendation)
            
        except json.JSONDecodeError:
            self._send_json(400, {"error": "요청 본문은 올바른 JSON이어야 합니다."})
        except Exception as error:
            print(f"recommend API error: {error}")
            self._send_json(500, {"error": "추천을 생성하는 중 서버 오류가 발생했습니다."})

    def do_GET(self):
        self._send_json(405, {"error": "POST 요청만 지원합니다."})