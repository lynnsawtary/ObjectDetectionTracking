import cv2
import time
import os
from collections import Counter
from ultralytics import YOLO


def process_video(video_source, output_path):
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    os.makedirs("outputs", exist_ok=True)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    input_fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        input_fps if input_fps > 0 else 20,
        (frame_width, frame_height)
    )

    prev_time = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video ended or frame could not be read.")
            break

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.4
        )

        detected_classes = []

        if results[0].boxes is not None:
            boxes = results[0].boxes

            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                detected_classes.append(class_name)

                confidence = float(box.conf[0])
                track_id = int(box.id[0]) if box.id is not None else -1

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                label = f"ID {track_id} | {class_name} | {confidence:.2f}"
                label_width = max(260, len(label) * 12)

                cv2.rectangle(
                    frame,
                    (x1, max(0, y1 - 30)),
                    (x1 + label_width, y1),
                    (0, 255, 0),
                    -1
                )

                cv2.putText(
                    frame,
                    label,
                    (x1 + 5, y1 - 8),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 0),
                    2
                )

        object_counts = Counter(detected_classes)

        panel_x = 20
        panel_y = 70
        panel_width = 260
        panel_height = 40 + (len(object_counts) * 30)

        cv2.rectangle(
            frame,
            (panel_x, panel_y),
            (panel_x + panel_width, panel_y + panel_height),
            (30, 30, 30),
            -1
        )

        cv2.putText(
            frame,
            "Detected Objects",
            (panel_x + 10, panel_y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        y_offset = panel_y + 55

        for object_name, count in object_counts.items():
            cv2.putText(
                frame,
                f"{object_name}: {count}",
                (panel_x + 10, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )
            y_offset += 30

        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        out.write(frame)
        cv2.imshow("Object Detection and Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Processed video saved at: {output_path}")


def main():
    while True:
        print("\n==============================")
        print(" Object Detection and Tracking")
        print("==============================")
        print("1. Webcam detection")
        print("2. Video file detection")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            process_video(0, "outputs/webcam_output.mp4")

        elif choice == "2":
            video_path = input("Enter video file path: ").strip().strip('"')
            process_video(video_path, "outputs/video_output.mp4")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()