import cv2 as cv

# Video-Capture-Objekt erstellen
cap = cv.VideoCapture(0)

def gesichterkennung(frame):
    # Lade den vortrainierten Gesichts-Kaskadenclassifier von OpenCV
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Konvertiere das Bild in Graustufen
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Wende die Gesichtserkennung an
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Zeichne einen Rahmen um das erkannte Gesicht
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return frame

while True:
    # Einzelbild erfassen
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    # Ergebnisbild anzeigen
    frame_with_face = gesichterkennung(frame)
    cv.imshow('Drücke ESC zum Schließen', frame_with_face)

    # Überprüfen, ob ESC-Taste gedrückt wurde
    if cv.waitKey(1) & 0xFF == 27:
        break

# Video-Capture freigeben
cap.release()
cv.destroyAllWindows()