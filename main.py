import cv2
import time
from pyzbar.pyzbar import decode

# Abre a webcam
# cap representa a webcam 
cap = cv2.VideoCapture(0)

while True:
    #time.sleep(0.3)
    # o metodo cap.read() retorna dois valores 
    # ret ---> indica que a captura foi bem sucedida 
    #          quando retornar false ele sai do laço 
    # frame -> retorna uma matriz numpy com o frame capturado 
    ret, frame = cap.read()
    
    # Decodifica o QR Code
    decoded = decode(frame)
    
    # Desenha o retângulo em volta do QR Code
    for obj in decoded:
        cv2.rectangle(
            frame,       # representa o desenho total da tela capturada 
            obj.rect,    # Coordenadas o objeto decodificado
            (0, 255, 0), # Define a cor da linha 
            2)           # largura da linha 
        
        # Mostra o conteúdo do QR Code
        data = obj.data.decode('utf-8')

        # adiciona texto a uma imagem 
        cv2.putText(
            frame,      # representa o desenho  
            data,       # texto que será desenhado 
            (           # identifica onde o texto será desenhado 
                obj.rect[0], 
                obj.rect[1] - 10
            ),
            cv2.FONT_HERSHEY_SIMPLEX, # Define a fonte do texto
            0.5,         # Tamanho do texto 
            (0, 255, 0), # define a cor do texto
            2)           # define a largura do contorno do texto 
        
    # Mostra o frame com o QR Code identificado
    cv2.imshow('frame', frame)
    
    # Encerra o programa se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
