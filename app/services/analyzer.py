import numpy as np
import librosa

def analyze_audio(y, sr):
    max_seconds = 60
    max_samples = sr * max_seconds
    if len(y) > max_samples:
        y = y[:max_samples]

    spec = np.abs(librosa.stft(y, n_fft=1024, hop_length=1024))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=1024)

    def band(f1, f2):
        idx = (freqs >= f1) & (freqs < f2)
        if not np.any(idx):
            return 0.0
        return float(np.mean(spec[idx]))

    low = band(20, 120)
    low_mid = band(120, 500)
    mid = band(500, 4000)
    high = band(4000, 10000)
    air = band(10000, 20000)

    peak = float(np.max(np.abs(y)))
    rms = float(np.mean(np.abs(y)))
    crest = float(peak / (rms + 1e-6))
    centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    rolloff = float(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)))

    issues = []
    if low_mid > max(mid * 2.6, 0.1):
        issues.append("mud")
    if air < max(high * 0.20, 0.05):
        issues.append("lack_of_air")
    if high > max(mid * 1.5, 0.3):
        issues.append("harsh")
    if crest < 4.8:
        issues.append("weak_transients")
    if low > max(mid * 4.0, 0.2):
        issues.append("loose_low_end")

    return {
        "low": low,
        "low_mid": low_mid,
        "mid": mid,
        "high": high,
        "air": air,
        "peak": peak,
        "rms": rms,
        "crest": crest,
        "centroid": centroid,
        "rolloff": rolloff,
        "phase_corr": 1.0,
        "stereo_width": 0.0,
        "issues": issues,
    }
