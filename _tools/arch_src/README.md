# 아키텍처 그림 원본

`assets/arch_*.jpg`를 만든 원본 HTML입니다. 아이콘(Tabler, MIT)은 SVG로 파일 안에 들어 있어서 인터넷 없이 열립니다.
Jekyll은 `_`로 시작하는 폴더를 게시하지 않으므로 이 폴더는 사이트에 나타나지 않습니다.

## 고치는 법
1. HTML을 브라우저로 열어 확인하며 글자·위치를 고칩니다 (캔버스 2000×1091, 위치는 `left/top` px).
2. 아래 명령으로 2400×1309 PNG를 만듭니다.

```bash
google-chrome --headless=new --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=1.2 --window-size=2000,1091 \
  --screenshot=arch_savers.png file://$PWD/arch_savers.html
```

3. JPG로 바꿔 `assets/arch_<프로젝트>.jpg`에 덮어쓰고, 포트폴리오 덱의 같은 그림도 교체합니다.

## 규칙
- 내가 맡은 일: 진한 버건디 라벨만 사용 (칸 채우기·테두리로 표시하지 않음)
- 팀이 만든 부분: 남색 테두리, 외부 서비스: 회색
- 단일 항목 상자는 가운데 정렬, 목록 상자는 왼쪽 정렬 + 세로 가운데
- 화살표 라벨은 두 상자 사이 정가운데
- 회사 로고 대신 일반 아이콘(종, 비구름, 스마트폰, 번개 등)
