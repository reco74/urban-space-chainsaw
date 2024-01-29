import cv2 as cv

# Video-Capture-Objekt erstellen
cap = cv.VideoCapture(0)

while True:
    # Einzelbild erfassen
    ret, frame = cap.read()

    # Ergebnisbild anzeigen
    cv.imshow('Drücke ESC zum Schließen', frame)

    # Überprüfen, ob ESC-Taste gedrückt wurde
    if cv.waitKey(1) & 0xFF == 27:
        break

# Video-Capture freigeben
cap.release()
cv.destroyAllWindows()