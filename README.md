# 🎵 Sound

Python으로 **소리를 분석하고 시각화**해 보는 실습 프로젝트입니다.

## 내용

- **사인파 생성** – 도(261.63Hz), 미(329.63Hz), 솔(392.00Hz) 음을 직접 만들어 화음 실험
- **STFT(단시간 푸리에 변환)** – 시간에 따른 주파수 성분 계산
- **크로마그램(Chromagram)** – 소리가 어떤 음계(C, D, E …)로 이루어졌는지 시각화
- 두 녹음 파일의 차이를 크로마그램으로 비교

## 파일 구조

```
├── Sound.py                           # 분석 코드
└── flute.wav / guitar.wav / piano.wav # 악기별 샘플 음원
```

## 사용 기술

`Python` `librosa` `NumPy` `Matplotlib`

## 실행 방법

```bash
pip install librosa numpy matplotlib
python Sound.py
```

> 코드에 불러올 음원 경로(`C:/Users/.../Downloads/...wav`)가 고정되어 있습니다. 저장소에 있는 `piano.wav` 등으로 바꿔서 실행하세요.

---
📅 2022년 8월
