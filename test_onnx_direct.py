import onnxruntime
import cv2
import numpy as np 
ort_session = onnxruntime.InferenceSession("/content/drive/MyDrive/face_recognition/models_onnx/InceptionResnetV1_v2.onnx")
#InceptionResnetV1ONNX = onnxruntime.InferenceSession("/content/arcfaceresnet100-8.onnx")

# Entrada dummy
img=cv2.imread('/content/face220502_200626.jpg')
img=cv2.resize(img,(160,160))
img=img.astype(np.float32)
img=(img-127.5)/128
img=np.expand_dims(img,0)
img=np.transpose(img,(0,3,1,2))
print(img.shape)

ort_inputs = {ort_session.get_inputs()[0].name: img}



ort_outs = ort_session.run(None, ort_inputs)
print("Salida InceptionResnetV1ONNX", type(ort_outs), type(ort_outs[0]), type(ort_outs[0][0]), ort_outs[0].shape)