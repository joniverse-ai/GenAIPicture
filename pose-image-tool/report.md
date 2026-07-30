# 트러블 리포트

## 최종 시도: SD 1.5 + ControlNet OpenPose

### 시도한 구성

| 항목 | 값 |
|------|-----|
| Base model | `runwayml/stable-diffusion-v1-5` |
| ControlNet | `lllyasviel/sd-controlnet-openpose` |
| Steps | 20 |
| Guidance Scale | 7.5 |
| ControlNet Scale | 1.0 |
| Seed | 42 |
| Negative prompt | bad anatomy, ugly, disfigured, worst quality, low quality |
| Reference | https://cdn.sisajournal.com/news/photo/first/201707/img_170343_2.png |

### 진행 상황

1. Cell 0 (install) — 성공
2. Cell 1 (pose 추출) — 성공, `pose.png` 저장 완료 (640×512 skeleton)
3. Cell 2 (pipeline load) — **실패 (다운로드 중단)**

### 문제: ControlNet 모델 다운로드 지연

- `lllyasviel/sd-controlnet-openpose` (1.45GB) 다운로드가 0%에서 멈춤
- 이후 `runwayml/stable-diffusion-v1-5` (~5GB)도 추가 다운로드 필요
- Colab 무료 티어의 HuggingFace 다운로드 속도가 매우 느림
- OpenCode MCP 연결이 다운로드 완료 전에 타임아웃 발생

### 원인 분석

1. **모델 크기 과다**: ControlNet 1.45GB + SD 1.5 약 5GB = 총 ~6.5GB 다운로드 필요
2. **Colab 무료 티어 제한**: 다운로드 속도가 매우 느리고 세션 유지 시간에 제한이 있음
3. **MCP 타임아웃**: OpenCode의 Colab MCP 연결이 장시간 다운로드를 기다리지 못하고 타임아웃
4. **모델 변경 이슈**: SDXL-Turpo → SD 1.5로 변경 과정에서 반복된 재시도로 시간 소모

### 전체 전환 과정

| 단계 | 시도한 모델 | 결과 |
|------|------------|------|
| 1 | SDXL-Turbo + thibaud/controlnet-openpose-sdxl-1.0 | ControlNet 로딩 문제 |
| 2 | SDXL-Turbo + diffusers 기반 변경 | 포즈가 프롬프트를 따르지 않음 |
| 3 | SD 1.5 + lllyasviel/sd-controlnet-openpose | 다운로드 중단 (현재) |

### 권장 해결 방안

1. **용량이 작은 모델 시도**: `lllyasviel/sd-controlnet-openpose` 대신 경량 ControlNet 사용
2. **로컬 실행**: Colab 대신 로컬 환경에서 미리 모델을 다운로드 후 실행
3. **캐싱 활용**: HuggingFace 캐시가 있는 환경에서 재시도
4. **더 작은 base 모델**: `runwayml/stable-diffusion-v1-5` 대신 경량 파생 모델 사용
