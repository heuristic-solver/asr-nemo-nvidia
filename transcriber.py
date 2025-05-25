
import torchaudio
import numpy as np
import onnxruntime as ort
import torch
from nemo.collections.asr.models import ASRModel


nemo_model = ASRModel.restore_from("stt_hi_conformer_ctc_medium.nemo")
preprocessor = nemo_model.preprocessor.eval()
vocab = list(nemo_model.decoder.vocabulary)
nemo_model.export("stt_hi_conformer_ctc_medium.onnx")
# Load ONNX runtime session once
ort_sess = ort.InferenceSession("stt_hi_conformer_ctc_medium.onnx")
input_name_1 = ort_sess.get_inputs()[0].name
input_name_2 = ort_sess.get_inputs()[1].name

def transcribe_file(file_path: str) -> str:
    waveform, sample_rate = torchaudio.load(file_path)
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)

    audio_signal = waveform[0].unsqueeze(0)
    audio_signal_len = torch.tensor([audio_signal.shape[1]], dtype=torch.long)

    with torch.no_grad():
        features, features_len = preprocessor(input_signal=audio_signal, length=audio_signal_len)

    input_audio = features.cpu().numpy().astype(np.float32)
    length = features_len.cpu().numpy().astype(np.int64)

    outputs = ort_sess.run(None, {
        input_name_1: input_audio,
        input_name_2: length
    })

    logits = outputs[0]
    token_ids = np.argmax(logits, axis=-1)[0]

    # CTC decoding to obtain text from model output 
    blank_id = logits.shape[-1] - 1
    decoded_tokens = []
    previous_token = blank_id
    for token in token_ids:
        if token != blank_id and token != previous_token:
            decoded_tokens.append(token)
        previous_token = token

    decoded_text = "".join([vocab[int(t)] for t in decoded_tokens])
    return decoded_text
