import cv2 as ocv
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 2, 1, 0.5, 0.5)
mpDrawings = mp.solutions.drawing_utils
frames = ocv.VideoCapture(0)

fingerTips = [8, 12, 16, 20]
handColor = (255, 0, 0)
isRight = True

while True:

    status, images = frames.read()
    images = ocv.flip(images, 1)
    height, width, channel = images.shape
    handsDetection = hands.process(images)

    if handsDetection.multi_hand_landmarks:
        myHands = []
        handsType = []
        for hand in handsDetection.multi_handedness:
            handType = hand.classification[0].label
            handsType.append(handType)

        for handType in handsType:
            if handType == "Right":
                handColor = (0, 0, 255)
                isRight = True
            if handType == "Left":
                handColor = (0, 255, 0)
                isRight = False

        for handLandmarks in handsDetection.multi_hand_landmarks:
            landmarkList = []

            for id, lm in enumerate(handLandmarks.landmark):
                landmarkList.append(lm)

            fingerFoldingStatus = []

            for tip in fingerTips:
                x, y = int(landmarkList[tip].x * width), int(
                    landmarkList[tip].y * height
                )
                # ocv.circle(images, (x, y), 15, (0, 255, 0), ocv.FILLED)

                if not ((landmarkList[tip].x > landmarkList[tip - 2].x) ^ isRight):
                    # ocv.circle(images, (x, y), 15, (0, 255, 255), ocv.FILLED)
                    fingerFoldingStatus.append(True)
                else:
                    fingerFoldingStatus.append(False)

            if (
                (landmarkList[4].y < landmarkList[3].y < landmarkList[2].y)
                and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                and (landmarkList[16].y < landmarkList[15].y < landmarkList[14].y)
                and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "STOP",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not (landmarkList[4].x < landmarkList[3].x < landmarkList[2].x) ^ isRight)
                and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "I LOVE YOU",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                and (landmarkList[16].y > landmarkList[14].y)
                and (landmarkList[20].y > landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "VICTORY",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x < landmarkList[2].x) ^ isRight))
                and (landmarkList[8].y > landmarkList[6].y)
                and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                and (landmarkList[16].y < landmarkList[15].y < landmarkList[14].y)
                and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "OKAY",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (landmarkList[4].y < landmarkList[3].y < landmarkList[2].y)
                and (landmarkList[8].y > landmarkList[7].y > landmarkList[5].y > landmarkList[6].y)
                and (landmarkList[12].y > landmarkList[11].y > landmarkList[9].y > landmarkList[10].y)
                and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "A",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "D",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x < landmarkList[3].x < landmarkList[2].x) ^ isRight))
                and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                ):
                ocv.putText(
                    images,
                    "L",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                and (landmarkList[4].y < landmarkList[2].y)
                and ((landmarkList[6].y < landmarkList[5].y) and (landmarkList[6].y < landmarkList[8].y))
                and ((landmarkList[10].y < landmarkList[9].y) and (landmarkList[10].y < landmarkList[12].y))
                and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
            ):
                ocv.putText(
                    images,
                    "S",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if (
                (not ((landmarkList[4].x < landmarkList[2].x) ^ isRight))
                and (not ((landmarkList[8].x < landmarkList[7].x < landmarkList[6].x) ^ isRight))
                and (not ((landmarkList[12].x < landmarkList[11].x < landmarkList[10].x) ^ isRight))
                and (not ((landmarkList[16].x < landmarkList[15].x < landmarkList[14].x) ^ isRight))
                and (not ((landmarkList[20].x < landmarkList[19].x < landmarkList[18].x) ^ isRight))
                ):
                ocv.putText(
                    images,
                    "C",
                    (20, 60),
                    ocv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    6,
                )

            if all(fingerFoldingStatus):
                if landmarkList[4].y < landmarkList[3].y < landmarkList[2].y:
                    ocv.putText(
                        images,
                        "LIKE",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                if landmarkList[4].y > landmarkList[3].y > landmarkList[2].y:
                    ocv.putText(
                        images,
                        "DISLIKE",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )

            mpDrawings.draw_landmarks(
                images,
                handLandmarks,
                mpHands.HAND_CONNECTIONS,
                mpDrawings.DrawingSpec(handColor, 5, 2),
                mpDrawings.DrawingSpec((255, 0, 0), 3, 2),
            )

    ocv.imshow("Hand Gesture Detection", images)
    k = ocv.waitKey(1)
    if k == 27:
        ocv.destroyAllWindows()
        break
