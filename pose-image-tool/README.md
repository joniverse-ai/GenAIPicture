# Pose Image Tool

SDXL-Turbo + ControlNet OpenPose로 참조 이미지의 자세를 유지한 채 다른 인물/장면을 생성합니다.

## 구조

```
pose-image-tool/
├── pose_tool.ipynb     # Colab 노트북 (핵심)
├── prompts.md          # 테스트 프롬프트 모음
└── samples/            # 생성 결과 예시
```

## 사용법

1. `pose_tool.ipynb`를 [Google Colab](https://colab.research.google.com)에 업로드
2. 순서대로 셀 실행
3. 프롬프트를 원하는 대로 수정하여 재생성

## 모델

| 항목 | 값 |
|------|-----|
| Base model | `stabilityai/sdxl-turbo` |
| ControlNet | `thibaud/controlnet-openpose-sdxl-1.0` |
| VAE | `madebyollin/sdxl-vae-fp16-fix` |
| Steps | 4 |
| Guidance | 0.0 |
