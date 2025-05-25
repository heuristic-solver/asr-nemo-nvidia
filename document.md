# Project Overview
This project implements a Hindi Automatic Speech Recognition (ASR) system using NVIDIA's NeMo ASR model and ONNX Runtime for fast inference. The NeMo model is responsible for audio preprocessing and vocabulary handling, while the exported ONNX model ensures lightweight and efficient inference in production environments. The goal was to create a pipeline that performs speech-to-text conversion on audio files, using ONNX for deployment optimization and NeMo for high-accuracy preprocessing and decoding.

# Features Implemented 
1. Conversion of the NeMo .nemo model into an optimized .onnx model for optimized inference.

2. Audio preprocessing using NeMo’s built-in Mel Spectrogram preprocessor which was manually applied post-export due to input errors to model.

3. Resampling of input audio files to match the expected 16kHz sample rate.

4. Use of a virtual environment to resolve dependency and build issues.
5. FastAPI was used to make a web API of the application.

#Issues Encountered 
1. NumPy Compatibility Error with NeMo:
    Version mismatch between numpy and the compiled NeMo modules occured. I refered the original github repo for nemo and updated numpy version to fix the issue.
2. 
