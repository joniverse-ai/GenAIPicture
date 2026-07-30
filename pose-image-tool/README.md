# 원하는 포즈로 이미지 만드는 도구

## 도구 설명
- 이 도구는 ControlNet의 포즈(Pose) 조건을 써서 "이 자세로 한 장 만들어 줘"라는 도구를 직접 만드는 것

## 사용법
1. 오픈코드를 통해 Colab mcp를 연결하여 노트를 열었습니다.
2. 설치 - 컨트롤넷 참조 업로드 - 포즈 추출 - 모델 로드 - 프롬프트를 통해 생성 - 비교
3. https://github.com/joniverse-ai/GenAIPicture/tree/main/pose-image-tool/samples

## 테스트 결과
- 포즈 1: a man wearing a spider-man costume, standing with confident pose, urban background, cinematic lighting, photorealistic
 → 결과: 실패. 프롬프트 한국어 성능이 낮아서 AI가 영문 프롬프트 권장함. 한국어 프롬프트는 시간이 오래 걸림./ 초기 이미지는 컨트롤넷의 포즈가 적용이 안됨


## 한계
- 컨트롤넷 로딩에 문제가 있었음. - 모델 변경 thibaud -> diffusers
- 한국어 프롬프트는 SDXL에서 처리 성능이 매우 낮아서 영어로 변경을 권장함.
- CLIP 최대 77토큰을 넘어서 프롬프트 일부가 잘림. 
- 한국어 프롬프트로 인해 세션 다시 시작함.
- 오픈코드를 통해 안내받고 세션을 진행한 구간까지 재실행 해줌.
- enable_model_cpu_offload()가 ControlNet 파이프라인과 충돌하거나 첫 추론에 과도하게 오래 걸리는 것으로 보입니다. 
- 중단하고 enable_model_cpu_offload()를 제거하는 게 빠릅니다. Colab에서 정지(⏹) 버튼을 누른 후 알려주세요. 수정해서 다시 실행하겠습니다.
- 재실행만 10여차례,,,,
- 모델이 문제있어보여서 모델을 바꿔보자고 했으나 묵인당함..
- 모델을 qkRna. SD 1.5
- 또 모델을 바꿔야 한다고 해서 오늘은... 이대로 마무리...
