"""Build eunnamahn.github.io (KO + EN) from the data in this file.

Run from the repo root:  python3 _tools/build_site.py
Writes index.html, projects/*.html, en/index.html, en/projects/*.html.
Jekyll skips folders that start with "_", so this script is not published.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "baduk89@hanmail.net"
GITHUB = "https://github.com/eunnamahn"
LINKEDIN = "https://www.linkedin.com/in/eunnamahn/"
SITE = "https://eunnamahn.github.io"

ICON = {
    "bell": '<svg viewBox="0 0 24 24" fill="none" stroke="#e4572e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16V11a6 6 0 0112 0v5l2 2H4z"/><path d="M10 21h4"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="#0e7c7b" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>',
    "talk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 10h8M8 13h5"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="#2f55d4" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="#2f55d4" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="M16 16l5 5"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "gh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
    "back": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M15 6l-6 6 6 6"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="8" height="7" rx="2"/><rect x="13" y="4" width="8" height="7" rx="2"/><rect x="3" y="13" width="8" height="7" rx="2"/><rect x="13" y="13" width="8" height="7" rx="2"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h6a2 2 0 012 2v12a2 2 0 00-2-2H4zM20 5h-6a2 2 0 00-2 2v12a2 2 0 012-2h6z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M5 19l1.4-1.4M17.6 6.4L19 5"/></svg>',
}

# ---------------------------------------------------------------- shared project facts
LINKS = {
    "savers": [("gh", "https://github.com/eunnamahn/savers-project"), ("play", "https://youtube.com/shorts/yv6POI7o4R8")],
    "bidmate": [("gh", "https://github.com/eunnamahn/bidmate-rfp-rag"), ("play", "https://youtu.be/vdpqzdG4k2I")],
    "adstudio": [("gh", "https://github.com/eunnamahn/ad-creative-studio"), ("play", "https://youtu.be/dgjC8w8YQi8"), ("play", "https://youtu.be/k3lqPzKlClQ", "video2")],
    "pillscope": [("gh", "https://github.com/eunnamahn/OralMedicineImageDetection")],
    "scibert": [],
}
TAGS = {
    "savers": ["FastAPI", "Docker Compose", "AWS EC2", "Vercel", "FCM", "pytest"],
    "bidmate": ["LangChain", "FAISS", "KURE-v1", "EXAONE 3.5", "Ollama", "RAGAS", "FastAPI"],
    "adstudio": {"ko": ["CLIP 유사도 평가 기준"], "en": ["CLIP similarity evaluation"]},  # only tech from my own role
    "pillscope": ["YOLOv11", "RT-DETRv2", "RF-DETR", "COCO", "WBF"],
    "scibert": ["TensorFlow", "BiLSTM-CRF", "BERT", "SciBERT"],
}
# card thumbnail: ("img", file, style) or ("flow", None, None)
THUMB = {
    "savers": ("img", "proj_savers_screens.jpg", "phones"),
    "bidmate": ("flow", None, None),
    "adstudio": ("img", "proj_ad-studio_screen.jpg", "phones"),
    "pillscope": ("img", "proj_pillscope_pred.jpg", "fit"),
}
SHOT = {"savers": "proj_savers_screens.jpg", "bidmate": "proj_bidmate_screen.jpg", "adstudio": "proj_ad-studio_screen.jpg",
        "pillscope": "proj_pillscope.jpg", "scibert": "proj_scibert.jpg"}
ARCH = {"savers": "arch_savers.jpg", "bidmate": "arch_bidmate.jpg", "adstudio": "arch_adstudio.jpg", "pillscope": "arch_pillscope.jpg"}
CODE = {  # (KO label, EN label, url) — same links as the GitHub profile README
    "savers": [("평가 코드 (apps/ai-engine/eval)", "Evaluation code (apps/ai-engine/eval)", "https://github.com/eunnamahn/savers-project/tree/main/apps/ai-engine/eval"),
               ("FCM 실발송 PR #214", "Real FCM sending PR #214", "https://github.com/team-savers/savers-project/pull/214"),
               ("#215", "#215", "https://github.com/team-savers/savers-project/pull/215")],
    "bidmate": [("골든셋·전처리 실험 (experiments/)", "Golden set and preprocessing experiments (experiments/)", "https://github.com/eunnamahn/bidmate-rfp-rag/tree/main/experiments"),
                ("공고 추천 API (src/recommender.py)", "Recommendation API (src/recommender.py)", "https://github.com/eunnamahn/bidmate-rfp-rag/blob/main/src/recommender.py")],
    "adstudio": [("평가 기준 문서 (eval/eval_criteria.md)", "Evaluation criteria (eval/eval_criteria.md)", "https://github.com/eunnamahn/ad-creative-studio/blob/main/eval/eval_criteria.md")],
    "pillscope": [("COCO → YOLO 파이프라인, EDA·전처리·증강 노트북 (members/eunnam)", "COCO → YOLO pipeline, EDA, preprocessing and augmentation notebooks (members/eunnam)", "https://github.com/eunnamahn/OralMedicineImageDetection/tree/main/members/eunnam")],
}
ORDER = ["savers", "bidmate", "pillscope", "adstudio", "scibert"]

# ---------------------------------------------------------------- Korean
KO = {
    "lang": "ko", "title": "안은남 · AI 엔지니어",
    "desc": "수학적 모델링 연구 역량으로 LLM·RAG의 성능 문제를 측정하고 원인을 찾아 고치는 AI 엔지니어 안은남입니다.",
    "skip": "본문으로 건너뛰기",
    "hello": "안녕하세요, 안은남입니다",
    "tagline": "수학적 모델링 연구 역량으로 LLM·RAG의 성능 문제를 측정하고 원인을 찾아 고치는 AI 엔지니어",
    "resume": ("이력서", "resume.pdf"), "other_lang": ("English", "en/"), "other_code": "EN",
    "photo_alt": "안은남 프로필 사진",
    "about_h": "소개",
    "about": [
        "미국 대학원에서 석유공학을 연구하며 해석해, 인공신경망 대리 모델, 시계열 예측 모델을 만들고 검증했고, 지금은 <b>LLM과 RAG의 답을 측정하는 평가 코드</b>를 만듭니다.",
        "SAVERS에서는 챗봇이 거절해야 할 질문에 답하는 결함을 찾아 검색 단계까지 추적했고, 입찰메이트에서는 점수를 막던 골든셋 오류와 근거 잘림을 찾아 고쳤습니다. 영어 발표와 문서 작성이 자유롭습니다 (TOEIC 985).",
    ],
    "proj_tag": "프로젝트", "proj_h": "만들고 검증한 것들",
    "proj_p": "수상한 해커톤 프로젝트와 부트캠프 팀 프로젝트입니다. 카드를 누르면 문제와 결정, 결과를 정리한 글로 이어집니다.",
    "others_h": "그 밖의 프로젝트",
    "paper_tag": "논문", "paper_h": "제1저자로 발표한 논문",
    "papers": [
        ("재난 취약계층을 위한 근거 기반 대피 안내 서비스의 설계 및 구현", "한국정보처리학회 학술대회(ACK 2026) · 제1저자, 구두발표(2026.11.06) · KIPS_C2026B0142", None, "2026"),
        ("Multi-Well Analytical Solution for Coning Under Simultaneous Steady-State Flow of Three Phases", "SPE Improved Oil Recovery Conference · 제1저자, 구두발표 · doi.org/10.2118/190182-MS", "https://doi.org/10.2118/190182-MS", "2018"),
    ],
    "res_tag": "연구", "res_h": "대학원 연구",
    "res_p": "The Pennsylvania State University · 2015.08 – 2024.12 · 석유·에너지 분야 수학적 모델링",
    "research": [
        ("시공간 저류층 데이터와 딥러닝을 활용한 원유 생산량 예측", "박사 연구 · Seq2Seq-LSTM과 유전 알고리즘으로 운영 조건 변화에 따른 생산량 예측, 테스트 R² 0.81 이상", "2021 – 2024"),
        ("실험계획법(DOE)을 결합한 인공신경망 대리 모델", "박사 연구 · 실험계획법으로 시뮬레이션 수를 줄여 학습, 저류층 시뮬레이터 대신 쓸 수 있는 평균 오차 2% 미만", "2019 – 2020"),
        ("원유와 함께 물·가스가 딸려 나오는 현상의 해석해 유도", "석사 논문 · 물과 가스가 함께 유입되기 전 최대 생산량을 시뮬레이션 없이 계산, 6가지 유정 배치로 확장 · SPE 2018", "2015 – 2018"),
        ("원유·물·가스 흐름 시뮬레이터 개발", "수업 프로젝트(PNG 512) · 60×30 격자에서 원유·물·가스 흐름을 계산하는 MATLAB 약 1,000줄, Newton-Raphson과 GMRES", "2016"),
    ],
    "edu_h": "학력",
    "edu": [
        ("Penn State 박사과정 수료", "2018.08 – 2024.12", "Energy and Mineral Engineering · 지도교수 Gregory R. King · 부전공 통계학, 계산과학 · GPA 3.81 / 4.00"),
        ("Penn State 석사", "2015.08 – 2018.08", "Energy and Mineral Engineering (석유천연가스공학) · 지도교수 Russell T. Johns · GPA 3.71 / 4.00"),
        ("한양대학교 자원환경공학과 학사", "2009.03 – 2015.02", "학과 수석(33명 중 1위), 제2공과대학 차석 졸업 · GPA 4.28 / 4.50"),
    ],
    "misc": [
        ("강의·활동", [
            ("대학원 학생회 공동회장", "2019 – 2024", "College of Earth and Mineral Sciences, Penn State"),
            ("대학원 강의조교", "2016.11 – 2024.12", "Penn State 학부 수업을 영어로 강의·지도"),
            ("한국석유공사 베트남 사무소 해외 인턴십", "2013.06 – 2013.08", "8주 · 산업통상자원부 자원개발특성화대학 사업 선발"),
        ]),
        ("교육·자격", [
            ("코드잇 스프린트 AI 엔지니어 10기 수료", "2026.02 – 2026.08", "팀 프로젝트 3회(객체 탐지, RAG, 생성형 AI)와 해커톤 1회, 팀장 3회 역임"),
            ("데이터분석 준전문가(ADsP)", "2026.06", "한국데이터산업진흥원(제49회)"),
            ("TOEIC 985", "2026.03", ""),
            ("Engineer in Training (EIT)", "2017.03", "미국 NCEES FE 시험 합격(펜실베이니아주) · 등록번호 ET 023429"),
        ]),
        ("수상·병역", [
            ("고용노동부장관상(장려상)", "2026.09", "제8회 K-디지털 트레이닝 해커톤 · 326팀 중 공동 3위"),
            ("EME 올해의 대학원 조교상", "2017", "Penn State · 학과 조교 약 60명 중 1명"),
            ("대학생 논문 공모전 3회 입상", "2013 – 2014", "GS에너지 3위, 한국광해관리공단·한국환경산업기술원 2위"),
            ("국가 이공계 장학금", "2013 – 2014", "4학기 전액"),
            ("육군 병장", "2010.01 – 2011.11", "만기제대"),
        ]),
    ],
    "skills_h": "기술",
    "skills": [("AI · LLM", ["LangChain", "RAG (FAISS, BM25)", "KURE-v1", "EXAONE 3.5 (Ollama)", "OpenAI API"]),
               ("평가", ["골든셋 설계", "Hit@k", "MRR", "거절 정확도", "RAGAS", "mAP", "pytest", "GitHub Actions CI"]),
               ("ML · 비전", ["PyTorch", "TensorFlow", "Scikit-learn", "YOLO", "RT-DETR", "실험계획법(DOE)", "MATLAB"]),
               ("백엔드 · 인프라", ["Python", "FastAPI", "Docker Compose", "AWS EC2", "Vercel", "GCP", "FCM", "Git"])],
    "contact_tag": "연락", "contact_h": "연락하기",
    "contact": f'채용이나 협업 제안은 <a href="mailto:{EMAIL}">{EMAIL}</a>으로 편하게 메일 주세요. 코드는 <a href="{GITHUB}">GitHub</a>, 경력은 <a href="{LINKEDIN}">LinkedIn</a>에서 볼 수 있습니다.',
    "footer": "© 2026 안은남 · 최종 업데이트 2026년 11월",
    "dock": {"home": "홈", "projects": "프로젝트", "papers": "논문", "email": "이메일", "theme": "밝기 전환", "lang": "English"},
    "link_label": {"gh": "GitHub", "play": "시연 영상"},
    "back": "프로젝트 목록", "code_h": "직접 작성한 코드", "prev": "이전", "next": "다음",
    "h_work": "내가 맡은 일", "h_mets": "성과", "h_shot": "화면", "h_arch": "시스템 구조", "h_decs": "구조 결정", "h_limit": "한계",
    "kv": ("역할", "기간", "팀"), "dec_k": ("왜:", "바꾼 구조:", "결과:"),
    "arch_note": "버건디 라벨이 제가 맡은 부분입니다. 이미지를 누르면 크게 볼 수 있습니다.",
    "arch_alt": "시스템 아키텍처. 버건디 라벨은 내가 맡은 일",
    "P": {
        "savers": dict(title="SAVERS", sub="재난 취약계층 맞춤 대피 안내", when="2026.07 – 2026.09", org="K-디지털 트레이닝 해커톤 2026", team="4인 팀", role="팀장 · PM · 평가와 인프라",
            award="고용노동부장관상 · 326팀 중 공동 3위 · ACK 2026 제1저자",
            desc="호우·홍수 특보 때 위치와 이동 능력에 맞는 대피소와 도보 경로를 알려 주는 웹 앱입니다. 대피소와 경로는 규칙 코드가 정하고 LLM은 설명만 하게 나눴고, 그 경계가 지켜지는지 재는 평가 코드를 만들었습니다.",
            lead="재난문자는 지역 전체에 같은 내용으로 갑니다. 혼자 판단하고 움직이기 어려운 주민에게 앱 설치나 상시 위치 추적 없이 맞춤 대피 안내를 보내고, 보호자에게는 가족이 대피했는지 알려 주는 PWA입니다.",
            flow=[("bell", "공식 특보", "기상청·홍수통제소"), ("code", "규칙 코드", "대피소·경로 계산"), ("talk", "LLM", "결과 설명만")], flow_tag="판단은 코드<i>·</i>설명은 LLM",
            video="시연 영상 46초",
            shot="서비스 화면: 알림 링크 진입 → 대피소 안내 → 경로와 도착 확인", arch_title="규칙 코드가 판단하고 LLM은 설명하는 구조",
            work=[("팀 운영", "중도 하차한 팀원의 QA와 인프라를 이어받아 역할과 일정을 다시 정하고, 설계 확정 대신 짧은 주기 개발로 전환"),
                  ("평가 코드", "보호자 응답 골든셋 40건(답변 35, 거절 5), 적대 회귀 12건, 거절 프로브 34건과 자동 채점 스크립트"),
                  ("인프라 코드", "FCM 웹푸시 실발송 연결(PR #214, #215), Vercel과 AWS EC2 배포, 자동 품질 검사 CI"),
                  ("기록과 논문", "설계 결정 기록(ADR) 관리, ACK 2026 논문 제1저자 집필과 구두발표")],
            mets=[dict(v="3.2 → 8.3", l="행동 지침 명확성 (10점 만점)", bars=[("재난문자", 32, "3.2"), ("SAVERS", 83, "8.3")], s="지인 52명에게 재난문자와 SAVERS 화면을 차례로 보여 준 설문 · Wilcoxon p<0.001 · \"5분 안에 집을 나서겠다\" 13% → 60%", full=True),
                  dict(v="6/6", l="찾아낸 과소거절", s="거절해야 할 대조군 6건 모두에 엉뚱한 근거로 답함. 불필요한 거절은 1/28(3.6%)"),
                  dict(v="12/12", l="막아 낸 오답 유도 문장", s="처음 채점기는 8/12만 걸러 놓친 4건을 분석하고 채점기를 보강. 정답 문장 35/35는 잘못 막지 않음")],
            decs=[("판단은 규칙 코드, LLM은 설명만", "LLM이 대피소나 경로를 만들면 환각이 곧 안전 사고가 됩니다.", "위험 판정은 기상청과 홍수통제소의 공식 판정을 그대로 쓰고, 대피소와 침수 회피 경로는 OSMnx·NetworkX 규칙 코드가 정합니다. LLM은 정해진 결과를 설명만 하고, 보호자 응답은 이벤트 기록만 근거로 씁니다.", "팀원이 만든 검증기는 답변을 주장 단위로 쪼개 기록과 대조합니다. 저는 이 검증기를 검증하는 평가셋을 만들었고, 통과 기준은 기록에 없는 내용 0건입니다."),
                  ("답할 때와 거절할 때를 모두 잰다", "근거 일치 지표만 보면 엉뚱한 근거로 답하는 실패가 드러나지 않습니다.", "답해야 할 질문 28건과 거절해야 할 대조군 6건으로 거절 프로브를 만들어 양쪽을 따로 쟀습니다.", "불필요한 거절은 1/28로 낮았지만 대조군 6건에는 모두 답했습니다. 원인이 검증기가 아니라 앞단 검색에 있음을 추적하고 재현 방법과 함께 문서로 남겼습니다."),
                  ("팀원이 빠진 뒤 최소 기능부터", "개발 도중 팀원이 중도 하차해, 남은 4명이 맡은 일을 다시 나눠야 했습니다.", "웹푸시 실발송, 침수 회피 경로, 보호자 확인을 먼저 만들고 공공 API 실시간 수집은 대회 이후 과제로 미뤘습니다.", "리뷰를 거친 코드 변경 240여 건을 합쳐 기간 안에 완성했고, 326팀 중 공동 3위로 고용노동부장관상을 받았습니다.")],
            limit="35/35와 12/12는 미리 쓴 정답·오답 문장을 채점에 직접 넣어 잰 값입니다. 거절 프로브를 잴 때 생성기는 근거 문장을 그대로 옮기는 오프라인 스텁이었으므로, 실제 생성 모델을 붙인 뒤 다시 재야 합니다."),
        "bidmate": dict(title="입찰메이트", sub="공공 RFP 문서 RAG 질의응답", when="2026.06 – 2026.07", org="코드잇 스프린트 팀 프로젝트", team="5인 팀", role="평가 담당",
            desc="공공기관 제안요청서 100건에서 근거를 달아 답하고 문서에 없는 질문은 거절하는 RAG 챗봇입니다. 95문항 골든셋과 채점기를 만들고, 점수를 막던 골든셋 오류와 근거 잘림을 찾아 고쳤습니다.",
            lead="수십 쪽짜리 HWP와 PDF가 섞인 공공 RFP에서 입찰 담당자가 답의 근거를 바로 확인할 수 있게, 출처를 달아 답하고 문서로 답할 수 없는 질문은 거절하는 챗봇입니다. 외부 API 없이 로컬 모델로만 동작합니다.",
            flow=[("doc", "RFP 100건", "HWP·PDF 전처리"), ("search", "검색", "KURE-v1 · k=4"), ("check", "근거 달린 답", "없으면 거절")], flow_tag="",
            video="시연 영상 2분",
            shot="서비스 화면: RFP 핵심 요약 답변과 근거 출처 (가운데 일부 생략)", arch_title="인덱싱, 서빙, 평가 루프로 나눈 구조",
            work=[("골든셋", "K-means로 대표 문서를 골라 50건을 만들고, 5개 유형 95문항(19개 RFP)으로 확장"),
                  ("전처리 실험", "표와 서식이 뒤섞인 HWP·PDF의 파싱과 청킹 48개 조합을 비교하는 실험 코드"),
                  ("평가", "RAGAS 평가 설계, 문항 유형별 자동 채점기, 임베딩 비교와 KURE-v1 전환"),
                  ("추천 API", "회사 프로필에 맞는 공고를 고르는 규칙 기반 추천 API(FastAPI, src/recommender.py)")],
            mets=[dict(v="0.3 → 1.0", l="정답 문서 검색 비율 Hit@k", bars=[("수정 전", 30, "0.3"), ("수정 후", 100, "1.0")], s="모델이 아니라 골든셋의 정답 파일명이 틀려 있던 것을 찾아 고친 결과", full=True),
                  dict(v="0.977", l="최종 설정 MRR", s="검색·답변 설정 708개 조합을 95문항 개발셋으로 3단계 비교 · Hit@4 1.0"),
                  dict(v="3.6초", l="평균 응답, API 비용 0원", s="GCP VM의 Ollama로 KURE-v1 + EXAONE 3.5 로컬 실행 · 문서에 없는 질문 19/19 거절")],
            decs=[("점수가 멈추면 측정부터 의심한다", "Hit@k가 0.3에서 오래 멈춰 있었고, 모델과 설정만 바꿔서는 오르지 않았습니다.", "틀린 문항을 하나씩 열어 보니 검색은 맞는 문서를 가져오고 있었고, 제가 만든 골든셋의 정답 파일명이 잘못되어 있었습니다.", "골든셋을 바로잡자 1.0이 되었습니다. 이후로는 점수가 이상하면 틀린 문항부터 직접 엽니다."),
                  ("근거 수보다 입력 창", "근거를 4건에서 12건으로 늘리자 5개 유형 평균 점수가 81.9점에서 40.7점으로 떨어졌습니다.", "변수를 하나씩 바꿔 보니 근거가 모델 입력 창(4,096토큰)을 넘어 잘리고 있었습니다. 같은 설정에서 k=4, 8, 12가 81.9, 46.1, 40.7점이었습니다.", "근거 4건과 8,192토큰 입력 창으로 확정해 같은 조건 비교에서 82.8점을 얻었습니다."),
                  ("외부 API 없이 로컬 스택으로", "공공 문서를 다루는 만큼 외부 API 없이 돌아가야 했고, 비용도 줄여야 했습니다.", "OpenAI 대신 KURE-v1 임베딩과 EXAONE 3.5를 GCP VM의 Ollama로 돌렸습니다.", "평균 3.6초에 답하고 외부 API 비용은 0원입니다. 효과 없이 응답만 21초 늦추던 리랭커는 뺐습니다.")],
            limit="설정 선택과 평가에 같은 95문항 골든셋을 썼기 때문에, 처음 보는 질문에서는 점수가 더 낮을 수 있습니다. 독립 시험셋으로 다시 재는 것이 다음 과제입니다."),
        "adstudio": dict(title="AI 광고 스튜디오", sub="소상공인용 광고 이미지·문구 생성", when="2026.08", org="코드잇 스프린트 팀 프로젝트", team="5인 팀", role="팀장 · PM · 평가 기준 설계",
            desc="제품 사진 한 장으로 배경과 문구를 생성해 광고 이미지와 쇼츠를 만드는 서비스입니다. 사진 속 제품이 바뀌지 않았는지를 1순위 지표로 정하고 판정 기준을 설계했습니다.",
            lead="시간대와 채널마다 광고 이미지를 새로 만들기 어려운 소상공인을 위해, 제품 사진 한 장으로 배경과 문구를 만들고 사람이 승인한 결과만 쇼츠로 만들어 예약 게시하는 서비스입니다.",
            video="시연 영상 3분 38초", video2="생성 쇼츠 예시 13초",
            shot="서비스 화면: 원본 제품은 그대로 두고 배경만 바꾼 톤별 광고 시안과 문구 편집", arch_title="생성 파이프라인과 제품 보존 검사 구조",
            work=[("팀 운영", "팀장이자 PM으로 4주 스프린트 운영, 최종 보고서 총괄"), ("평가 기준", "제품 보존율을 1순위 지표로 정의하고 판정 기준(eval_criteria) 설계")],
            mets=[dict(v="4/4", l="제품 보존 판정 통과", s="제품 영역 CLIP 유사도 0.85 이상 + 사람 확인 · 대표 조합 4건 (대규모 평가는 미실시)"),
                  dict(v="17.47 → 1.72초", l="배경 생성 시간 (팀 성과)", s="LCM-LoRA 적용으로 약 10배 단축 · 이미지 한 장 전체 처리 5.97초")],
            decs=[("제품이 바뀌면 광고가 아니다", "생성 모델은 배경을 바꾸면서 제품 모양이나 라벨까지 바꿀 수 있습니다.", "원본 제품을 생성한 배경 위에 합성해 제품을 지키고, 제품 영역의 CLIP 유사도가 0.85 이상인지 검사한 뒤 사람이 다시 확인하게 했습니다.", "대표 조합 4건이 모두 통과했습니다."),
                  ("사람이 승인한 것만 게시", "자동으로 만든 결과를 그대로 올리면 잘못된 광고가 나갈 수 있습니다.", "사람이 승인한 이미지만 13초 쇼츠로 만들어 YouTube에 예약 게시하게 했습니다.", "팀 자동화 테스트 486건을 통과했습니다.")],
            limit="정밀 이미지 비교(SSIM)와 블라인드 사람 평가는 하지 못해, 다음 단계 과제로 보고서에 적었습니다."),
        "pillscope": dict(title="PillScope", sub="경구약제 이미지 객체 탐지", when="2026.04 – 2026.05", org="코드잇 스프린트 팀 프로젝트", team="5인 팀", role="팀장 · PM · 모델 실험",
            desc="생김새가 비슷한 알약 56종을 사진에서 찾아 구별하는 객체 탐지 모델입니다. 학습 이미지 186장과 51배 클래스 불균형을 증강과 누수 방지 split으로 풀었습니다.",
            lead="3~4개가 함께 찍힌 사진에서 각 알약의 위치를 찾고 56종 중 품목을 맞히는 모델입니다. 학습 이미지는 186장, 클래스 불균형은 51배(153장 대 3장)였습니다.",
            shot="왼쪽 정답, 오른쪽 모델 예측 · 희귀 클래스(큐시드정)까지 탐지", arch_title="학습 파이프라인과 서비스를 연결한 구조",
            work=[("팀 운영", "팀장이자 PM으로 7단계 실험 일정과 역할 관리"), ("파이프라인", "COCO → YOLO 공용 학습 파이프라인 구축, YOLOv11l 학습과 DETR 계열 실험"), ("데이터", "Crop & Paste 증강, 비슷한 사진을 같은 split으로 묶는 누수 방지")],
            mets=[dict(v="186 → 1,026장", l="증강으로 늘린 학습 이미지", s="mAP@0.5 0.886 → 0.964"),
                  dict(v="0.851 → 0.9355", l="Kaggle 점수", s="conf 임계값 조정과 3모델 WBF 앙상블"),
                  dict(v="0.936", l="YOLOv11l 검증 mAP@[0.75:0.95]", s="RF-DETR 0.882, RT-DETRv2 0.883보다 높음. 모델마다 학습 이미지 수가 달라 통제 비교는 아님", full=True)],
            decs=[("점수가 부풀지 않게 split부터", "촬영 옵션만 다른 비슷한 사진이 학습과 검증에 나뉘어 들어가면 점수가 실제보다 높게 나옵니다.", "비슷한 사진을 같은 split으로 묶었습니다.", "검증 점수를 믿고 모델을 비교할 수 있게 됐습니다."),
                  ("데이터가 적은 알약을 직접 늘린다", "한 번도 찾지 못하는 희귀 알약이 있었습니다.", "데이터가 적은 알약을 오려 붙이고, 인터넷 알약 이미지를 대회 배경에 합성했습니다.", "학습 이미지가 1,026장이 됐고 희귀 알약까지 탐지했습니다.")],
            limit="모델마다 학습 이미지 수가 달라(1,116 / 1,206 / 186장) 모델 비교는 통제된 비교가 아닙니다."),
        "scibert": dict(title="생의학 초록 문장 분류", sub="BERT·SciBERT 임베딩 비교", when="2019.09 – 2019.12", org="Penn State IST 597 딥러닝 수업", team="2인 팀(동일 기여)", role="임베딩 교체 실험", year="2019",
            desc="논문 초록 문장이 배경, 방법, 결과 중 무엇인지 분류하는 모델의 임베딩만 SciBERT로 바꿔, 어휘 수 1/175로 정확도를 유지했습니다.",
            short="BERT·SciBERT 임베딩으로 바꿔 어휘 수 1/175로 정확도 유지 (92.35% → 92.43%)",
            lead="생의학 논문 초록 대부분은 구조가 없어 연구자가 방법이나 결과만 골라 읽기 어렵습니다. 기존 문장 분류 모델(HSLN)은 그대로 두고 단어 임베딩만 Word2Vec에서 BERT·SciBERT로 바꿔 비교했습니다. 지도 C. Lee Giles 교수.",
            shot="HSLN 분류기와 데이터는 그대로 두고 임베딩만 교체한 비교",
            work=[("실험", "BERT·SciBERT에서 단어 임베딩을 추출해 Word2Vec을 대체하고, 기준선 재현을 포함한 5가지 조건 실험")],
            mets=[dict(v="1/175", l="임베딩 어휘 수", s="더 작은 임베딩으로 같은 수준의 정확도"), dict(v="92.35 → 92.43%", l="정확도", s="PubMed 20k RCT, 단일 실행")],
            decs=[("모델은 두고 임베딩만 바꾼다", "무엇이 성능을 바꿨는지 알려면 한 번에 한 변수만 바꿔야 합니다.", "분류기와 데이터는 그대로 두고 임베딩만 교체했습니다.", "데이터 토큰 중 사전학습 어휘에 있는 비율이 16%로 낮은 점(Word2Vec 68%)을 성능의 한계 요인으로 분석했습니다.")],
            limit="단일 실행 결과라 실행마다의 편차는 확인하지 못했습니다."),
    },
}

# ---------------------------------------------------------------- English
EN = {
    "lang": "en", "title": "Eunnam Ahn · AI Engineer",
    "desc": "AI engineer using mathematical modeling to measure LLM/RAG performance problems and fix their root causes.",
    "skip": "Skip to content",
    "hello": "Hi, I'm Eunnam Ahn",
    "tagline": "AI engineer using mathematical modeling to measure LLM/RAG performance problems and fix their root causes",
    "resume": ("Curriculum Vitae", "../resume_en.pdf"), "other_lang": ("한국어", "../"), "other_code": "KO",
    "photo_alt": "Photo of Eunnam Ahn",
    "about_h": "About",
    "about": [
        "In graduate research at Penn State I built and validated analytical solutions, neural-network surrogates and time-series forecasting models; now I write <b>evaluation code that measures whether LLM and RAG answers are right</b>.",
        "On SAVERS I traced a chatbot that answered questions it should refuse back to retrieval, and on BidMate I found and fixed the golden-set errors and evidence truncation holding scores down. Fluent in English presentation and writing (TOEIC 985).",
    ],
    "proj_tag": "Projects", "proj_h": "What I built and tested",
    "proj_p": "An award-winning hackathon project and bootcamp team projects. Each card opens a write-up of the problem, the decisions and the results.",
    "others_h": "Other projects",
    "paper_tag": "Publications", "paper_h": "First-author papers",
    "papers": [
        ("Design and Implementation of an Evidence-Grounded Evacuation Guidance Service for Disaster-Vulnerable Populations", "Proc. Annual Conference of KIPS (ACK 2026) · first author, oral presentation (Nov 6, 2026) · KIPS_C2026B0142", None, "2026"),
        ("Multi-Well Analytical Solution for Coning Under Simultaneous Steady-State Flow of Three Phases", "SPE Improved Oil Recovery Conference · first author, oral presentation · doi.org/10.2118/190182-MS", "https://doi.org/10.2118/190182-MS", "2018"),
    ],
    "res_tag": "Research", "res_h": "Graduate research",
    "res_p": "The Pennsylvania State University · Aug 2015 – Dec 2024 · mathematical modeling in petroleum and energy",
    "research": [
        ("Oil production forecasting with spatial-temporal reservoir data and deep learning", "Ph.D. research · Seq2Seq-LSTM tuned with a genetic algorithm to forecast output under changing operations, test R² above 0.81", "2021 – 2024"),
        ("Artificial neural network proxy model with design of experiments", "Ph.D. research · DOE kept simulation runs few; the proxy replaces the reservoir simulator with average test error under 2%", "2019 – 2020"),
        ("Exact formula for water and gas inflow into multiple oil wells", "M.S. thesis · critical oil rate before water or gas breaks through, computed with no simulation and extended to six well layouts · SPE 2018", "2015 – 2018"),
        ("Oil–water–gas flow simulator, built from scratch", "Course project (PNG 512) · ~1,000 lines of MATLAB on a 60×30 grid with Newton-Raphson and GMRES", "2016"),
    ],
    "edu_h": "Education",
    "edu": [
        ("Ph.D. Coursework Completed (ABD), Penn State", "Aug 2018 – Dec 2024", "Energy and Mineral Engineering · advised by Prof. Gregory R. King · double minor in Statistics and Computational Science · GPA 3.81 / 4.00"),
        ("M.S., Penn State", "Aug 2015 – Aug 2018", "Energy and Mineral Engineering (Petroleum and Natural Gas Engineering option) · advised by Prof. Russell T. Johns · GPA 3.71 / 4.00"),
        ("B.S., Hanyang University", "Mar 2009 – Feb 2015", "Natural Resources and Environmental Engineering · 1st of 33 in the department, 2nd in the College of Engineering II · GPA 4.28 / 4.50"),
    ],
    "misc": [
        ("Teaching &amp; activities", [
            ("Co-chair, EMS Graduate Student Council", "2019 – 2024", "College of Earth and Mineral Sciences, Penn State"),
            ("Graduate Teaching Assistant", "Nov 2016 – Dec 2024", "Taught Penn State undergraduate courses in English"),
            ("Overseas internship, KNOC Vietnam Office", "Jun – Aug 2013", "8 weeks · selected through the Ministry of Trade, Industry and Energy resource-development university program"),
        ]),
        ("Training &amp; certifications", [
            ("Codeit Sprint AI Engineer Bootcamp (10th cohort)", "Feb – Aug 2026", "3 team projects (detection, RAG, generative AI) and a hackathon, team lead on 3"),
            ("Advanced Data Analytics Semi-Professional (ADsP)", "Jun 2026", "Korea Data Agency (49th exam)"),
            ("TOEIC 985", "Mar 2026", "out of 990"),
            ("Engineer in Training (EIT)", "Mar 2017", "NCEES FE exam, Pennsylvania · ET 023429"),
        ]),
        ("Honors &amp; service", [
            ("Minister of Employment and Labor Award", "Sep 2026", "8th K-Digital Training Hackathon · joint 3rd of 326 teams"),
            ("EME Graduate Teaching Assistant of the Year", "2017", "Penn State · 1 of ~60 TAs"),
            ("Student paper competitions, 3 awards", "2013 – 2014", "GS Energy 3rd; Mine Reclamation Corporation and Korea Environmental Industry &amp; Technology Institute 2nd"),
            ("National Science &amp; Engineering Scholarship", "2013 – 2014", "Full tuition, 4 semesters"),
            ("Sergeant, Republic of Korea Army", "Jan 2010 – Nov 2011", "Honorable discharge"),
        ]),
    ],
    "skills_h": "Skills",
    "skills": [("AI · LLM", ["LangChain", "RAG (FAISS, BM25)", "KURE-v1", "EXAONE 3.5 (Ollama)", "OpenAI API"]),
               ("Evaluation", ["Golden-set design", "Hit@k", "MRR", "Refusal accuracy", "RAGAS", "mAP", "pytest", "GitHub Actions CI"]),
               ("ML · Vision", ["PyTorch", "TensorFlow", "Scikit-learn", "YOLO", "RT-DETR", "Design of experiments", "MATLAB"]),
               ("Backend · Infra", ["Python", "FastAPI", "Docker Compose", "AWS EC2", "Vercel", "GCP", "FCM", "Git"])],
    "contact_tag": "Contact", "contact_h": "Get in touch",
    "contact": f'For roles or collaboration, email me at <a href="mailto:{EMAIL}">{EMAIL}</a>. My code is on <a href="{GITHUB}">GitHub</a> and my profile is on <a href="{LINKEDIN}">LinkedIn</a>.',
    "footer": "© 2026 Eunnam Ahn · Last updated November 2026",
    "dock": {"home": "Home", "projects": "Projects", "papers": "Publications", "email": "Email", "theme": "Toggle theme", "lang": "한국어"},
    "link_label": {"gh": "GitHub", "play": "Demo video"},
    "back": "All projects", "code_h": "Code I wrote", "prev": "Previous", "next": "Next",
    "h_work": "What I did", "h_mets": "Results", "h_shot": "Screens", "h_arch": "System architecture", "h_decs": "Key decisions", "h_limit": "Limitations",
    "kv": ("Role", "Period", "Team"), "dec_k": ("Why:", "What changed:", "Result:"),
    "arch_note": "Burgundy labels mark the parts I owned. Click the image to enlarge it. (Diagram in Korean.)",
    "arch_alt": "system architecture; Burgundy labels mark the parts I owned",
    "P": {
        "savers": dict(title="SAVERS", sub="Evacuation guidance for disaster-vulnerable residents", when="Jul – Sep 2026", org="K-Digital Training Hackathon 2026", team="Team of 4", role="Team lead · PM · Evaluation & infra",
            award="Minister of Employment and Labor Award · joint 3rd of 326 teams · first author, ACK 2026",
            desc="A web app that sends shelter and walking-route guidance fitted to each resident's location and mobility during heavy-rain and flood alerts. Rule-based code picks shelters and routes and the LLM only explains them; I wrote the evaluation code that checks this boundary holds.",
            lead="Official disaster texts send the same message to everyone in an area. SAVERS is a PWA that gives residents who cannot judge or evacuate alone personal guidance, with no app install and no constant location tracking, and tells guardians whether their family member has evacuated.",
            flow=[("bell", "Official alert", "KMA · flood control"), ("code", "Rule-based code", "Shelter and route"), ("talk", "LLM", "Explains only")], flow_tag="Code decides<i>·</i>LLM explains",
            video="Demo video (46 s)",
            shot="Service screens: alert link → shelter guidance → route and arrival check (UI in Korean)", arch_title="Rule-based code decides, the LLM explains",
            work=[("Team", "Took over QA and infrastructure from a teammate who left mid-project, re-planned roles and schedule, and switched from fixing the design up front to short iterations"),
                  ("Evaluation code", "A 40-case guardian golden set (35 answer, 5 refusal), 12 adversarial regressions, a 34-case refusal probe and automated scoring scripts"),
                  ("Infrastructure code", "Real FCM web-push sending (PR #214, #215), Vercel and AWS EC2 deployment, CI quality checks"),
                  ("Records and paper", "Kept the decision records (ADRs); first-authored and presented the ACK 2026 paper")],
            mets=[dict(v="3.2 → 8.3", l="Action clarity (out of 10)", bars=[("Disaster text", 32, "3.2"), ("SAVERS", 83, "8.3")], s="Within-subject survey of 52 acquaintances shown the disaster text and then SAVERS · Wilcoxon p<0.001 · \"would leave within 5 minutes\" 13% → 60%", full=True),
                  dict(v="6/6", l="Under-refusals found", s="All 6 out-of-scope controls were answered from unrelated evidence; wrong refusals were only 1/28 (3.6%)"),
                  dict(v="12/12", l="Adversarial answers blocked", s="The first scorer caught only 8/12; I analyzed the 4 misses and extended it. 0 of 35 correct answers wrongly blocked")],
            decs=[("Rule-based code decides, the LLM only explains", "If an LLM produced shelters or routes, a hallucination would become a safety incident.", "Risk levels come straight from the official KMA and flood-control alerts; shelters and flood-avoiding routes come from OSMnx / NetworkX rule-based code. The LLM only explains fixed results, and guardian replies use the event log as their only evidence.", "A teammate's verifier splits each answer into claims and checks them against the log. I built the evaluation set that tests the verifier, with a pass bar of zero unsupported claims."),
                  ("Measure both answering and refusing", "Grounding scores alone miss answers built on unrelated evidence.", "A refusal probe with 28 questions that should be answered and 6 controls that should be refused measured both directions separately.", "Wrong refusals were low at 1/28, but all 6 controls were answered. I traced the cause to retrieval rather than the verifier and documented it with steps to reproduce."),
                  ("After teammates left, ship the minimum first", "Teammates left mid-development, and the remaining four had to split the work again.", "Real web-push sending, flood-avoiding routes and guardian check-in came first; real-time public-API ingestion was moved to after the competition.", "We merged about 240 reviewed code changes, finished on time and won the Minister of Employment and Labor Award, joint 3rd of 326 teams.")],
            limit="35/35 and 12/12 come from feeding pre-written correct and adversarial answers straight into scoring. During the refusal probe the generator was an offline stub that copies evidence sentences, so the numbers must be re-measured with a real model."),
        "bidmate": dict(title="BidMate", sub="RAG Q&amp;A for public RFP documents", when="Jun – Jul 2026", org="Codeit Sprint team project", team="Team of 5", role="Evaluation",
            desc="A RAG chatbot that answers questions about 100 public RFPs with cited evidence and refuses what the documents cannot answer. I built the 95-question golden set and scorers, and found and fixed the golden-set errors and evidence truncation holding scores down.",
            lead="Public RFPs mix long HWP and PDF files. BidMate lets bid managers see where each answer comes from: it cites the source and refuses questions the documents cannot answer, running only on local models with no external API.",
            flow=[("doc", "100 RFPs", "HWP · PDF parsing"), ("search", "Retrieval", "KURE-v1 · k=4"), ("check", "Cited answer", "or refusal")], flow_tag="",
            video="Demo video (2 min)",
            shot="Service screen: RFP summary with the cited source (middle trimmed; UI in Korean)", arch_title="Indexing, serving and an evaluation loop",
            work=[("Golden set", "Picked representative documents with K-means for 50 questions, then grew it to 95 questions of 5 types over 19 RFPs"),
                  ("Preprocessing experiments", "Experiment code comparing 48 parsing and chunking combinations for HWP and PDF files full of tables"),
                  ("Evaluation", "RAGAS evaluation design, type-specific automated scorers, embedding comparison and the switch to KURE-v1"),
                  ("Recommendation API", "Rule-based bid recommendation API matched to a company profile (FastAPI, src/recommender.py)")],
            mets=[dict(v="0.3 → 1.0", l="Hit@k, correct document retrieved", bars=[("Before", 30, "0.3"), ("After", 100, "1.0")], s="Fixing wrong answer file names in the golden set, not changing the model", full=True),
                  dict(v="0.977", l="MRR of the final setup", s="708 retrieval and generation configurations compared in 3 stages on the 95-question dev set · Hit@4 1.0"),
                  dict(v="3.6 s", l="Mean latency, $0 API cost", s="KURE-v1 + EXAONE 3.5 on Ollama on a GCP VM · refused 19/19 out-of-scope questions")],
            decs=[("When a score stalls, check the measurement first", "Hit@k sat at 0.3 for a long time and changing models and settings did not move it.", "Opening the failed questions one by one showed retrieval was finding the right documents; the answer file names in my golden set were wrong.", "Fixing the golden set took it to 1.0. Since then, when a score looks wrong I open the failed cases first."),
                  ("The context window matters more than the evidence count", "Raising evidence from 4 to 12 chunks dropped the 5-type average from 81.9 to 40.7.", "Changing one variable at a time showed evidence was being cut off past the 4,096-token context; with the same settings, k=4, 8 and 12 scored 81.9, 46.1 and 40.7.", "Settling on 4 chunks and an 8,192-token context scored 82.8 in a like-for-like comparison."),
                  ("A local stack with no external API", "Public documents called for no external API, and costs had to come down.", "Replaced OpenAI with KURE-v1 embeddings and EXAONE 3.5 on Ollama on a GCP VM.", "Mean latency 3.6 s with no external API cost. A reranker that added 21 s for no gain was removed.")],
            limit="The same 95-question golden set was used to choose and to evaluate the configuration, so scores on unseen questions may be lower. Re-measuring on an independent test set is the next step."),
        "adstudio": dict(title="AI Ad Studio", sub="Ad images and copy for small businesses", when="Aug 2026", org="Codeit Sprint team project", team="Team of 5", role="Team lead · PM · Evaluation criteria",
            desc="A service that turns one product photo into ad images and Shorts with generated backgrounds and copy. I made product preservation the top metric and designed the pass criteria.",
            lead="Small businesses cannot remake ad images for every time slot and channel. AI Ad Studio generates backgrounds and copy from one product photo, and only human-approved results become Shorts scheduled to YouTube.",
            video="Demo video (3:38)", video2="Generated Short (13 s)",
            shot="Service screen: tone-specific drafts that keep the original product and change only the background, with copy editing (UI in Korean)", arch_title="Generation pipeline with a product-preservation check",
            work=[("Team", "Ran a 4-week sprint as team lead and PM; owned the final report"), ("Evaluation criteria", "Defined product preservation as the top metric and designed the pass criteria (eval_criteria)")],
            mets=[dict(v="4/4", l="Passed the preservation check", s="Masked-region CLIP similarity ≥ 0.85 plus human review · 4 representative cases (no large-scale evaluation)"),
                  dict(v="17.47 → 1.72 s", l="Background generation (team result)", s="About 10× faster with LCM-LoRA · 5.97 s per image end to end")],
            decs=[("If the product changes, it is not an ad", "Generative models can alter a product's shape or label while changing the background.", "The original product is composited onto the generated background, checked for masked-region CLIP similarity ≥ 0.85, then reviewed by a person.", "All 4 representative cases passed."),
                  ("Publish only what a person approved", "Posting generated results automatically could put out a wrong ad.", "Only human-approved images become 13-second Shorts scheduled to YouTube.", "The team's 486 automated tests passed.")],
            limit="No pixel-level comparison (SSIM) or blind human evaluation yet; both are listed as next steps in the report."),
        "pillscope": dict(title="PillScope", sub="Object detection for oral medication images", when="Apr – May 2026", org="Codeit Sprint team project", team="Team of 5", role="Team lead · PM · Model experiments",
            desc="An object detector that finds and tells apart 56 look-alike pills in photos. Augmentation and leakage-proof splits handled only 186 training images and a 51× class imbalance.",
            lead="The model locates each pill in photos of 3–4 pills and names it among 56 classes. There were 186 training images and a 51× class imbalance (153 vs. 3).",
            shot="Ground truth (left) vs. model prediction (right); the rare class is detected too", arch_title="Training pipeline connected to the service",
            work=[("Team", "Managed a 7-stage experiment plan and roles as team lead and PM"), ("Pipeline", "Built the shared COCO → YOLO training pipeline, trained YOLOv11l and ran DETR experiments"), ("Data", "Crop-and-paste augmentation; grouped near-duplicate shots into the same split to prevent leakage")],
            mets=[dict(v="186 → 1,026", l="Training images after augmentation", s="mAP@0.5 0.886 → 0.964"),
                  dict(v="0.851 → 0.9355", l="Kaggle score", s="Confidence tuning and a 3-model WBF ensemble"),
                  dict(v="0.936", l="YOLOv11l validation mAP@[0.75:0.95]", s="Ahead of RF-DETR 0.882 and RT-DETRv2 0.883; training-set sizes differed, so this is not a controlled comparison", full=True)],
            decs=[("Fix the split before trusting the score", "Near-duplicate shots split across training and validation inflate the score.", "Grouped near-duplicate shots into the same split.", "Validation scores became trustworthy enough to compare models."),
                  ("Grow the rare pills directly", "Some rare pills were never detected.", "Cropped and pasted under-represented pills and composited web pill images onto the competition background.", "The training set grew to 1,026 images and the rare pills became detectable.")],
            limit="Training-set sizes differed by model (1,116 / 1,206 / 186 images), so the model comparison is not controlled."),
        "scibert": dict(title="Biomedical abstract sentence classification", sub="BERT vs. SciBERT embeddings", when="Sep – Dec 2019", org="Penn State IST 597 Foundations of Deep Learning", team="Team of 2 (equal contribution)", role="Embedding experiments", year="2019",
            desc="Swapped only the embeddings of a classifier that labels abstract sentences as background, methods or results, keeping accuracy with a 175× smaller vocabulary.",
            short="Swapped Word2Vec for BERT / SciBERT embeddings and kept accuracy with 1/175 of the vocabulary (92.35% → 92.43%)",
            lead="Most biomedical abstracts are unstructured, so readers cannot jump to the methods or results they need. Keeping the HSLN sentence classifier as is, we replaced only the word embeddings, from Word2Vec to BERT and SciBERT. Advised by Dr. C. Lee Giles.",
            shot="Same HSLN classifier and data; only the embedding changes (labels in Korean)",
            work=[("Experiments", "Extracted BERT / SciBERT token embeddings to replace Word2Vec and ran five conditions, including a baseline re-run")],
            mets=[dict(v="1/175", l="Embedding vocabulary size", s="A much smaller embedding at the same accuracy"), dict(v="92.35 → 92.43%", l="Test accuracy", s="PubMed 20k RCT, single run")],
            decs=[("Keep the model, change only the embedding", "To know what changed the score, change one variable at a time.", "The classifier and data stayed fixed; only the embedding was swapped.", "Low vocabulary coverage (16% of dataset tokens vs. 68% for Word2Vec) was identified as the bottleneck.")],
            limit="Single-run results; run-to-run variance was not measured."),
    },
}


# ---------------------------------------------------------------- rendering
def head(L, title, desc, depth, canon, alt):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{canon}">
<link rel="alternate" hreflang="{'en' if L['lang']=='ko' else 'ko'}" href="{SITE}/{alt}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{canon}">
<meta property="og:image" content="{SITE}/profile.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Inter:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">{L['skip']}</a>
<div class="dots"></div>
"""


def dock(L, depth, lang_href):
    up = "../" * depth
    home = up or "./"
    d = L["dock"]
    return f"""<footer>{L['footer']}</footer>
<nav class="dock" aria-label="Navigation">
  <a href="{home}" title="{d['home']}" aria-label="{d['home']}">{ICON['home']}</a>
  <a href="{home}#projects" title="{d['projects']}" aria-label="{d['projects']}">{ICON['grid']}</a>
  <span class="sep"></span>
  <a href="{GITHUB}" title="GitHub" aria-label="GitHub">{ICON['gh']}</a>
  <a href="{home}#papers" title="{d['papers']}" aria-label="{d['papers']}">{ICON['book']}</a>
  <a href="mailto:{EMAIL}" title="{d['email']}" aria-label="{d['email']}">{ICON['mail']}</a>
  <span class="sep"></span>
  <a class="lang" href="{lang_href}" title="{d['lang']}" aria-label="{d['lang']}" lang="{'en' if L['lang']=='ko' else 'ko'}">{L['other_code']}</a>
  <button type="button" id="theme" title="{d['theme']}" aria-label="{d['theme']}">{ICON['sun']}</button>
</nav>
<script>
(function(){{
  var b=document.getElementById('theme');
  b.addEventListener('click',function(){{var r=document.documentElement,dark=r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches,n=dark?'light':'dark';r.dataset.theme=n;try{{localStorage.setItem('theme',n)}}catch(e){{}}}});
  document.addEventListener('click',function(e){{var box=e.target.closest('.arch');if(!box)return;var lb=document.createElement('div');lb.className='lb';lb.innerHTML=box.innerHTML;lb.addEventListener('click',function(){{lb.remove()}});document.body.appendChild(lb)}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{var lb=document.querySelector('.lb');if(lb)lb.remove()}}}});
}})();
</script>
</body>
</html>
"""


def flow_html(p, tag=True):
    nodes = "".join(
        (('<span class="arw">→</span>' if i else "") + f'<div class="node">{ICON[ic]}<b>{a}</b><span>{b}</span></div>')
        for i, (ic, a, b) in enumerate(p["flow"])
    )
    t = f"<h4>{p['flow_tag']}</h4>" if tag and p.get("flow_tag") else ""
    return f'<div class="flow"><div class="st">{nodes}</div>{t}</div>'


def link_label(L, pid, link):
    p = L["P"][pid]
    if len(link) > 2:
        return p[link[2]]
    return p.get("video", L["link_label"]["play"]) if link[0] == "play" else L["link_label"]["gh"]


def card(L, pid, depth):
    p = L["P"][pid]
    up = "../" * depth
    mode, img, style = THUMB[pid]
    if mode == "flow":
        vis = flow_html(p, tag=False)
    else:
        vis = f'<div class="vis img {style}" style="position:absolute;inset:0;height:auto"><img src="{up}assets/{img}" alt="{p["title"]}" loading="lazy"></div>'
    kinds = list(dict.fromkeys(l[0] for l in LINKS[pid]))
    minis = "".join(f'<span class="mini">{ICON[k]}{"GitHub" if k=="gh" else ("시연" if L["lang"]=="ko" else "Demo")}</span>' for k in kinds)
    award = f'<span class="award">{p["award"]}</span>' if p.get("award") else ""
    tags = "".join(f'<span class="chip">{t}</span>' for t in tags_for(pid, L))
    return f"""<a class="card" href="projects/{pid}.html">
 <div class="vis"><div class="top"><small>{p['org']}</small><span class="acts">{minis}</span></div>{vis}</div>
 <div class="body"><h3><span>{p['title']} <em>· {p['sub']}</em></span><span aria-hidden="true">↗</span></h3>
 <div class="meta"><span class="num">{p['when']}</span> · {p['team']}, {p['role']}</div>
 {award}
 <p class="desc">{p['desc']}</p>
 <div class="chips out">{tags}</div></div></a>"""


def tags_for(pid, L):
    t = TAGS[pid]
    return t[L["lang"]] if isinstance(t, dict) else t


def rows(items):
    return "".join(f'<div class="row"><b>{a}</b><span class="d num">{b}</span></div><div class="role">{c}</div>' for a, b, c in items)


def oi(i, title, sub, year, href=None):
    inner = f'<span class="n">0{i}.</span><div><b>{title}</b><span>{sub}</span></div><span class="y num">{year}</span>'
    return f'<a class="oi" href="{href}">{inner}</a>' if href else f'<div class="oi">{inner}</div>'


def home(L, prefix):
    depth = 1 if L["lang"] == "en" else 0
    up = "../" * depth
    canon = "en/" if L["lang"] == "en" else ""
    alt = "" if L["lang"] == "en" else "en/"
    lang_href = L["other_lang"][1]
    cards = "\n".join(card(L, pid, depth) for pid in ORDER[:4])
    sp = L["P"]["scibert"]
    others = oi(1, sp["title"], sp["short"], sp["year"], f"projects/scibert.html")
    papers = "".join(oi(i + 1, *p[:2], p[3], p[2]) for i, p in enumerate(L["papers"]))
    research = "".join(oi(i + 1, *r) for i, r in enumerate(L["research"]))
    misc = "".join(f'  <section class="blk"><h2>{h}</h2><div>{rows(items)}</div></section>\n' for h, items in L["misc"])
    skills = "".join(f'<div class="skrow"><b>{g}</b><div class="chips">' + "".join(f'<span class="chip">{s}</span>' for s in items) + "</div></div>" for g, items in L["skills"])
    about = "".join(f"<p>{x}</p>" for x in L["about"])
    rname, rhref = L["resume"]
    # only show the CV button when the PDF exists (resume_en.pdf is not uploaded yet)
    pdf = os.path.normpath(os.path.join(ROOT, "en" if L["lang"] == "en" else "", rhref))
    resume_pill = f'        <a class="pill dark" href="{rhref}">{rname}</a>\n' if os.path.exists(pdf) else ""
    return head(L, L["title"], L["desc"], depth, canon, alt) + f"""<main id="main">
<div class="wrap">
  <header class="hero" id="top">
    <div>
      <h1>{L['hello']} <span class="wave" aria-hidden="true">👋</span></h1>
      <p>{L['tagline']}</p>
      <div class="links">
{resume_pill}        <a class="pill" href="{GITHUB}">GitHub</a>
        <a class="pill" href="{LINKEDIN}">LinkedIn</a>
        <a class="pill" href="mailto:{EMAIL}">{EMAIL}</a>
        <a class="pill" href="{lang_href}">{L['other_lang'][0]}</a>
      </div>
    </div>
    <img class="avatar" src="{up}profile.jpg" alt="{L['photo_alt']}">
  </header>
  <section class="blk"><h2>{L['about_h']}</h2><div>{about}</div></section>
</div>

<section class="sec" id="projects">
  <div class="wide">
    <span class="tag">{L['proj_tag']}</span>
    <h2>{L['proj_h']}</h2>
    <p>{L['proj_p']}</p>
    <div class="grid">
{cards}
    </div>
    <div class="others"><h3>{L['others_h']}</h3>{others}</div>
  </div>
</section>

<section class="sec" id="papers">
  <div class="wide">
    <span class="tag">{L['paper_tag']}</span>
    <h2>{L['paper_h']}</h2>
    <div class="others" style="margin-top:30px">{papers}</div>
  </div>
</section>

<section class="sec" id="research">
  <div class="wide">
    <span class="tag">{L['res_tag']}</span>
    <h2>{L['res_h']}</h2>
    <p>{L['res_p']}</p>
    <div class="others" style="margin-top:30px">{research}</div>
  </div>
</section>

<div class="wrap" style="margin-top:70px">
  <section class="blk" id="education"><h2>{L['edu_h']}</h2><div>{rows(L['edu'])}</div></section>
{misc}  <section class="blk" id="skills"><h2>{L['skills_h']}</h2><div>{skills}</div></section>
</div>

<section class="sec" id="contact">
  <div class="wide">
    <span class="tag">{L['contact_tag']}</span>
    <h2>{L['contact_h']}</h2>
    <p class="contact">{L['contact']}</p>
  </div>
</section>
</main>
""" + dock(L, depth, lang_href)


def met(m):
    bars = ""
    if m.get("bars"):
        bars = '<div class="bars">' + "".join(
            f'<div class="bar{" now" if i else ""}"><span>{a}</span><i style="width:{w}%"></i><em>{v}</em></div>' for i, (a, w, v) in enumerate(m["bars"])
        ) + "</div>"
    return f'<div class="met{" full" if m.get("full") else ""}"><div class="v num">{m["v"]}</div><div class="l">{m["l"]}</div>{bars}<div class="s">{m["s"]}</div></div>'


def detail(L, pid):
    p = L["P"][pid]
    en = L["lang"] == "en"
    depth = 2 if en else 1
    up = "../" * depth
    canon = f"{'en/' if en else ''}projects/{pid}.html"
    alt = f"{'' if en else 'en/'}projects/{pid}.html"
    lang_href = f"../../projects/{pid}.html" if en else f"../en/projects/{pid}.html"
    i = ORDER.index(pid)
    pv = ORDER[i - 1] if i > 0 else None
    nx = ORDER[i + 1] if i + 1 < len(ORDER) else None
    links = "".join(f'<a class="pill{" dark" if l[0]=="gh" else ""}" href="{l[1]}">{ICON[l[0]]}{link_label(L, pid, l)}</a>' for l in LINKS[pid])
    code = ""
    if pid in CODE:
        i_lab = 0 if L["lang"] == "ko" else 1
        code = f'<h3>{L["code_h"]}</h3><p>' + ", ".join(f'<a href="{c[2]}">{c[i_lab]}</a>' for c in CODE[pid]) + "</p>"
    award = f'<span class="award">{p["award"]}</span>' if p.get("award") else ""
    vis = f'<div class="dvis">{flow_html(p)}</div>' if p.get("flow") else ""
    work = "".join(f"<h3>{a}</h3><p>{b}</p>" for a, b in p["work"])
    mets = "".join(met(m) for m in p["mets"])
    k1, k2, k3 = L["kv"]
    w1, w2, w3 = L["dec_k"]
    decs = "".join(f'<div class="dec"><h3>{n+1}. {d[0]}</h3><p><b>{w1}</b> {d[1]}</p><p><b>{w2}</b> {d[2]}</p><p><b>{w3}</b> {d[3]}</p></div>' for n, d in enumerate(p["decs"]))
    arch = ""
    if pid in ARCH:
        arch = f"""<h2>{L['h_arch']}</h2><p class="archcap">{p['arch_title']}</p>
 <div class="arch"><img src="{up}assets/{ARCH[pid]}" alt="{p['title']} {L['arch_alt']}" loading="lazy"></div>
 <p class="archnote">{L['arch_note']}</p>"""
    tags = "".join(f'<span class="chip">{t}</span>' for t in tags_for(pid, L))
    pn = ""
    if pv:
        pn += f'<a href="{pv}.html"><small>{L["prev"]}</small><b>{L["P"][pv]["title"]}</b></a>'
    if nx:
        pn += f'<a class="nx" href="{nx}.html"><small>{L["next"]}</small><b>{L["P"][nx]["title"]}</b></a>'
    title = f"{p['title']} · {p['sub']} | {'Eunnam Ahn' if en else '안은남'}"
    home_href = up or "./"
    return head(L, title, p["desc"], depth, canon, alt) + f"""<main id="main"><div class="wrap dt">
 <div class="back"><a class="pill" href="{home_href}#projects">{ICON['back']}{L['back']}</a></div>
 <h1>{p['title']} · {p['sub']}</h1>
 <div class="meta"><span class="num">{p['when']}</span> · {p['org']}</div>
 {award}
 <p class="lead">{p['lead']}</p>
 <div class="links">{links}</div>
 <div class="hr"></div>
 {vis}
 <h2>{L['h_work']}</h2>
 <dl class="kv"><dt>{k1}</dt><dd>{p['role']}</dd><dt>{k2}</dt><dd class="num">{p['when']}</dd><dt>{k3}</dt><dd>{p['team']} · {p['org']}</dd></dl>
 {work}
 {code}
 <h2>{L['h_mets']}</h2>
 <div class="mets">{mets}</div>
 <h2>{L['h_shot']}</h2>
 <figure class="shot"><img src="{up}assets/{SHOT[pid]}" alt="{p['shot']}" loading="lazy"><figcaption>{p['shot']}</figcaption></figure>
 {arch}
 <h2>{L['h_decs']}</h2>
 {decs}
 <h2>{L['h_limit']}</h2>
 <p class="limit">{p['limit']}</p>
 <div class="chips out" style="margin-top:28px">{tags}</div>
 <div class="pn">{pn}</div>
</div></main>
""" + dock(L, depth, lang_href)


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    write("index.html", home(KO, ""))
    write("en/index.html", home(EN, "en/"))
    for pid in ORDER:
        write(f"projects/{pid}.html", detail(KO, pid))
        write(f"en/projects/{pid}.html", detail(EN, pid))
    print("built", 2 + 2 * len(ORDER), "pages")
