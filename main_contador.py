import cv2
from pyzbar.pyzbar import decode

# Abre a webcam
cap = cv2.VideoCapture(0)

# Define a posição da linha vertical
linha_posicao = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)

# Define o contador de QR Code que cruzam a linha
contador_qr_code = 0

while True:
    # Captura um frame da webcam
    ret, frame = cap.read()
    
    # Desenha a linha vertical no frame
    cv2.line(frame, (linha_posicao, 0), (linha_posicao, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), (0, 0, 255), 5)
    
    # Decodifica o QR Code
    decoded = decode(frame)
    
    # Desenha o retângulo em volta do QR Code
    for obj in decoded:
        cv2.rectangle(frame, obj.rect, (0, 255, 0), 2)
            
        # Mostra o conteúdo do QR Code
        data = obj.data.decode('utf-8')
        cv2.putText(frame, data, (obj.rect[0], obj.rect[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Verifica se o QR Code está do lado direito da linha
        if obj.rect[0] > linha_posicao:
            # Incrementa o contador
            contador_qr_code += 1
            # Mostra a mensagem na tela
            cv2.putText(frame, "QR Code do lado direito: " + str(contador_qr_code), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    # Desenha o contador de QR Code que cruzam a linha
    cv2.putText(frame, f"QR Codes na linha: {contador_qr_code}", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Mostra o frame com o QR Code identificado
    cv2.imshow('frame', frame)
    
    # Encerra o programa se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
