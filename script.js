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

    if (!response.ok) throw new Error('추천을 가져오지 못했습니다.');

    const data = await response.json();
    // API는 { recommendation: '...' } 또는 { message: '...' } 형식을 지원합니다.
    const recommendation = data.recommendation ?? data.message ?? '추천 결과를 받았습니다.';
    result.innerHTML = `<strong>오늘의 추천</strong><br>${escapeHtml(recommendation)}`;
  } catch (error) {
    result.textContent = '추천을 불러오는 중 문제가 발생했어요. 잠시 후 다시 시도해주세요.';
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