const form = document.querySelector('#recommend-form');
const moodInput = document.querySelector('#mood-input');
const result = document.querySelector('#result');
const submitButton = form.querySelector('button[type="submit"]');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const mood = moodInput.value.trim();
  if (!mood) {
    alert('기분을 입력해주세요');
    moodInput.focus();
    return;
  }

  submitButton.disabled = true;
  submitButton.textContent = '로딩 중...';
  result.hidden = false;
  result.textContent = '당신의 기분에 맞는 음악을 찾고 있어요...';

  try {
    const response = await fetch('/api/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mood })
    });

    const data = await response.json();

    // 서버 응답이 실패(500 등)인 경우 서버가 전달한 error 메시지를 화면에 출력
    if (!response.ok) {
      throw new Error(data.error || '추천을 가져오지 못했습니다.');
    }

    result.innerHTML = `
      <p><strong>위로의 한마디:</strong> ${escapeHtml(data.comfort_message)}</p>
      <p><strong>추천 음악:</strong> ${escapeHtml(data.recommended_music)}</p>
    `;

  } catch (error) {
    result.textContent = error.message || '추천을 불러오는 중 문제가 발생했어요. 잠시 후 다시 시도해주세요.';
    console.error(error);
  } finally {
    submitButton.disabled = false;
    submitButton.innerHTML = '추천받기 <span aria-hidden="true">→</span>';
  }
});

function escapeHtml(value) {
  const element = document.createElement('div');
  element.textContent = String(value);
  return element.innerHTML;
}

const themeToggle = document.getElementById('theme-toggle');

if (themeToggle) {
  // 로컬스토리지에서 기존 테마 설정 불러오기
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeToggle.textContent = '☀️';
  }

  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    
    // 버튼 아이콘 변경 및 사용자의 선택 저장
    themeToggle.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
}