# asr-nemo-nvidia
This project exposes a speech-to-text transcription API using a pre-trained NeMo ASR model exported to ONNX for fast and efficient inference.

# Instructions to Build and Run the Container

### 1. Clone the repository
```bash
git clone https://github.com/heuristic-solver/asr-nemo-nvidia
cd <directory name>
```

### 2. Download the .nemo model file

```bash
curl -L 'https://api.ngc.nvidia.com/v2/models/org/nvidia/team/nemo/stt_hi_conformer_ctc_medium/1.6.0/files?redirect=true&path=stt_hi_conformer_ctc_medium.nemo' -o 'stt_hi_conformer_ctc_medium.nemo'
```

### 3. Build the Docker image 
```bash
docker build -t asr-api .
```
or 

```bash
docker build --no-cache -t asr-app .
```

### 4. Run the container 
```bash
docker run -p 8000:8000 asr-api
```

Sample Testing can be done by using the following command 
```bash
curl -X POST "http://localhost:8000/transcribe" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@speech_hi.wav"
```
or if you are on windows powershell you can try 
```bash
curl.exe -X POST "http://localhost:8000/transcribe" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@speech_hi.wav"
```

Additionally you can go to http://localhost:8000/docs to manually upload the .wav speech file to test it out. 
