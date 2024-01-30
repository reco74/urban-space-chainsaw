import cv2 as cv
import os

# Video-Capture-Objekt erstellen
cap = cv.VideoCapture(0)

# Zähler für aufgenommene Bilder
photo_count = 0

# Speicherort für die Bilder
photo_directory = 'C:/Users/User/Pictures/Bilder vom Python Code' #Dateipfad von meinem Laptop, muss also individuell angepasst werden


while True:
    # Einzelbild erfassen
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    # Ergebnisbild anzeigen
    cv.imshow('Drücke ESC zum Schließen', frame)

    # Überprüfen, ob ESC-Taste gedrückt wurde
    if cv.waitKey(1) & 0xFF == 27:
        break

    # Überprüfen, ob Leertaste gedrückt wurde
    elif cv.waitKey(1) & 0xFF == 32:  # 32 entspricht dem ASCII-Code für Leertaste
        # Foto aufnehmen und speichern
        photo_count += 1
        photo_filename = os.path.join(photo_directory, f'photo_{photo_count}.png')
        cv.imwrite(photo_filename, frame)
        print(f'Foto aufgenommen und als {photo_filename} gespeichert.')

# Video-Capture freigeben
cap.release()
cv.destroyAllWindows()