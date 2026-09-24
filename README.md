# 송보경 | Performance Marketing Portfolio

타깃이 반응하는 콘텐츠를 만들고, 데이터로 성과를 증명하는 퍼포먼스 마케터 송보경의 웹 포트폴리오입니다.

**웹 포트폴리오 → https://urgr1111.github.io/performance-marketing-portfolio/**

---

## 1. 메인 프로젝트: 달칩샌드 일본 진출 Meta 광고

(주)네이처오다 · 제1기 KITA 글로벌마케팅마스터 마케팅 프로젝트 최우수상

**문제:** 쌀과자의 본고장 일본에서, 생소한 한국 쌀과자가 살아남을 방법은 무엇일까?

도쿄·오사카 30~40대 아이엄마를 타깃으로 세팅하고, 직접 기획·제작한 AI 광고 영상으로 Meta 광고를 집행했습니다. 광고 클릭이 곧바로 Amazon.co.jp 상품 페이지로 이어지는 트래픽 캠페인입니다.

| 항목 | 내용 |
|---|---|
| 캠페인 | Meta(페이스북·인스타그램·스레드) → Amazon.co.jp 상품 페이지 직행 · 링크 클릭 목적 · 2주 |
| 예산 | 캠페인 전체 ₩469,201 · 내 담당 세트(아이엄마 타깃) ₩338,026 |
| 내 역할 | 일본 시장 분석 · 아이엄마 타깃 소재 기획 및 제작(100%) · Meta 광고 집행 및 성과 데이터 분석 · 프로젝트 전체 기여도 40% |

> KITA 과정 연계 기업 프로젝트 참여이며, 수행 범위는 기획·광고·홍보·데이터 분석입니다. 실제 수출·납품·판매는 수행하지 않았습니다.

### 핵심 성과 (아이엄마 타깃 세트, 링크 클릭 기준)

| 지표 | 값 | 비교 |
|---|---|---|
| 링크 클릭 | 2,339 | 캠페인 전체 3,149의 74% |
| 링크 CTR | 3.50% | 캠페인 평균 2.51%의 1.4배 |
| 이긴 소재의 CPC | ₩143 | 코미디 소재 ₩200 대비 −28% |
| 캐릭터 소재 CPC | ₩143 → ₩138 | 지출을 2.6배(₩84,150 → ₩221,065) 늘려도 하락 |

### 데이터로 내린 판단

| 데이터 | 판단 |
|---|---|
| 1주차 캐릭터편 CTR 4.70% vs 코미디편 3.00% (p<0.001) | 코미디 중단, 광고 세트 일예산 ₩14,300 → ₩70,000 |
| 코미디편은 끝까지 본 비율이 더 높음 (7.35% vs 2.60%) | 캠페인 KPI가 링크 클릭이므로 클릭 효율이 앞선 캐릭터편에 예산 집중 |
| 2주차 보완판: 25% 지점까지 본 비율 8.6% → 25.6%, 링크 CTR 3.38% → 1.69% (p<0.001) | 시청은 늘었지만 클릭은 절반 → 보완판을 멈추고 원본 유지 |
| 링크 클릭의 87%가 여성, 55세 이상 링크 CTR 4.54% vs 25~54세 3.08% | 메인 메시지 유지 · 5060 전용 세트 분리 테스트 제안 |
| 2주차 링크 클릭의 76%가 릴스 지면 | 9:16 세로형 포맷 우선 · 릴스 지면 분리 테스트 |

- Meta가 소재별 노출을 자동으로 분배하기 때문에 무작위 A/B 테스트는 아닙니다. CTR 차이가 우연인지 두 비율 z검정으로 확인했습니다.
- 지면별 비용 데이터는 없어 지면별 비용 효율은 비교하지 않았습니다.

### 한계와 다음 설계

- **한계:** 광고 링크가 아마존 상세페이지로 직행해 클릭 이후의 구매 전환(CVR)은 추적하지 못했습니다.
- **다음 설계(팀 공동):** UTM·GA4·Meta Pixel을 심은 일본어 브랜드 페이지를 경유하는 퍼널을 제안했습니다. 아마존 직행 80~90%, 경유 페이지 10~20%로 예산을 나눠 비교하는 구조입니다.
- **향후 개선:** Amazon Attribution 태그로 Meta 유입이 상세페이지 조회 → 장바구니 → 구매로 이어지는 전체 퍼널을 추적하겠습니다.

---

## 2. 근거 데이터 (Data Evidence)

포트폴리오의 모든 수치는 Meta 광고관리자 화면과 내보내기(Raw Data Report) 엑셀을 Python(pandas)으로 다시 집계해 검증했습니다.

| 번호 | 내용 | 파일 |
|---|---|---|
| E1 | Meta 광고관리자 · 아이엄마 타깃 세트 원본 화면 | `images/evidence/ev_adsmanager_t1.png` |
| E2 | Meta 광고관리자 · 건강 관심 여성 세트 원본 화면 (비교용 · 팀원 제작 소재) | `images/evidence/ev_adsmanager_t2.png` |
| E3 | 원본 엑셀 발췌 (일·성별·연령·소재별 691행 × 57열) | `images/evidence/ev_raw_sample.png` |
| E4 | 소재별 성과 재집계 + 비율 검정 | `images/evidence/ev_creative_table.png` |
| E5 | 성별·연령별 반응률 | `images/evidence/ev_age_gender.png` |
| E6 | 지면별 링크 클릭 (2주차) | `images/evidence/ev_placement.png` |
| E7 | 원본 vs 보완판 시청·클릭 비교 | `images/evidence/ev_v2_compare.png` |

세팅 오류로 잘못 올린 광고 1건은 모든 집계에서 제외했습니다.

### 근거 이미지 다시 만들기

원본 엑셀(광고 성과 데이터)은 저장소에 포함하지 않았습니다. 엑셀 두 개를 가진 경우에만 실행할 수 있습니다.

```bash
pip install -r analysis/requirements.txt
DALCHIP_DATA_DIR=/엑셀/파일이/있는/폴더 python analysis/make_evidence.py
```

필요한 파일: `달칩-메타-광고-데이터_성별-연령버전.xlsx`, `2주차-영상-참여-지표.xlsx`

---

## 3. 그 밖의 경험

- **글로벌 타깃 영문 콘텐츠:** 네이처오다 링크드인 영문 게시물 9건 단독 운영 · 누적 노출 2,270회, 반응 60건 · 반응률 1위(4.2%)는 친환경 원재료(우렁이 농법) 스토리. 표본이 작아 결론 대신 초기 가설로 사용
- **채널 운영:** 아이즈모바일 아이즈크루 2기, YBM, DSC 공유대학 서포터즈로 카드뉴스·영상·블로그 기획·제작·발행

---

## 4. 저장소 구조

```
index.html                  웹 포트폴리오 (HTML · CSS · JS 한 파일)
images/                     프로젝트 이미지, 영상 장면, 채널 캡처
images/evidence/            근거 데이터 이미지 E1~E7
analysis/make_evidence.py   원본 엑셀 → 근거 이미지 생성 스크립트
analysis/requirements.txt   스크립트 실행에 필요한 패키지
```

## 5. 사용 도구

**광고 · 데이터:** Meta 광고관리자 · Amplitude · Tableau · Python(pandas, matplotlib)
**콘텐츠 제작:** Google Flow/Veo · Higgsfield · Fish Audio · CapCut · 미리캔버스 · Lovable
**이 사이트:** HTML · CSS · JavaScript · GitHub Pages

---

## Contact

**송보경 (Bokyung Song)** · [khodu0616@gmail.com](mailto:khodu0616@gmail.com) · [LinkedIn](https://www.linkedin.com/in/jay-bokyung-song-457332276/) · [YouTube](https://www.youtube.com/@bokyung30) · [Instagram](https://instagram.com/s.bokyung98) · [Blog](https://blog.naver.com/urgr0226)
