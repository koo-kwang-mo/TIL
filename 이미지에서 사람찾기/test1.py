import cv2
import numpy as np

# MobileNet SSD 사전 학습된 모델과 구성 파일 경로
prototxt_path = "deploy.prototxt"
model_path = "mobilenet_iter_73000.caffemodel"

# 클래스 라벨 파일 경로
class_labels = "class_labels.txt"

# 모델 로드
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# 클래스 라벨 로드
with open(class_labels, 'r') as f:
    classes = f.read().strip().split('\n')

# 'person' 클래스 인덱스 찾기
person_class_id = classes.index('person')

def detect_people(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]

    # 이미지 전처리
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # 모델에 입력으로 블롭 설정
    net.setInput(blob)

    # 객체 탐지
    detections = net.forward()

    # 사람 객체 필터링
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # 신뢰도 임계값 설정
        if confidence > 0.2:
            class_id = int(detections[0, 0, i, 1])
            
            if class_id == person_class_id:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                label = f"Person: {confidence:.2f}"
                
                # 탐지된 객체 경계 상자와 라벨 그리기
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 결과 이미지 출력
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 예제 실행
# detect_people("path_to_your_image.jpg")