# Project Overview
This project implements a Hindi ASR system using NVIDIA's NeMo ASR model and ONNX Runtime for fast inference. The NeMo model is responsible for audio preprocessing and vocabulary handling, while the exported ONNX model ensures lightweight and efficient inference in production environments. 

# Features Implemented 
1. Conversion of the NeMo .nemo model into a .onnx model for optimized inference.

2. Audio preprocessing using NeMo’s built-in Mel Spectrogram preprocessor which was manually applied post export due to input errors to model.

3. Resampling of input audio files to match the expected 16kHz sample rate.

4. Use of a virtual environment to resolve dependency and build issues.
5. FastAPI was used to make a web API of the application.

# Issues Encountered 
1. NumPy Compatibility Error with NeMo:
    Version mismatch between numpy and the compiled NeMo modules occured. I refered the original github repo for nemo and updated numpy version to fix the issue.
   
2. Preprocessing Not Included in ONNX Export: To fix this I used Nemo's preprocessor module manually before sending input into the onnx model for inference.
   
4. Output from ONNX Model: The onnx model output was simply probabilities which had to be decoded into text for which the vocabulary used for training the model had to be retrieved manually
   from the library.
   
6. Build Errors:  Created and isolated the project in a virtual environment (venv) to manage dependencies safely and avoid conflicts with system wide packages. This however was not an issue
   after using docker.

# Limitations
I had considered quantization for further optimization but did not have enough time to do so. Given a few more days, the model could have been optimized better for memory and cpu usage. 

