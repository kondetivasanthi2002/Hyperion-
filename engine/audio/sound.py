"""
Audio Engine - Sound Buffer and Synthesizer
Provides WebAudio/Software SoundBuffer, Oscillator synth, and sound effect generators.
"""

import math
import random
from typing import List, Tuple

class SoundBuffer:
    """Stores audio PCM samples and channel information."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.samples: List[float] = []

    def duration(self) -> float:
        return len(self.samples) / float(self.sample_rate)


class AudioSynthesizer:
    """Software audio synthesizer supporting Sine, Square, Sawtooth, and Noise waveforms with ADSR envelope."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate_tone(self, frequency: float, duration: float, waveform: str = "sine") -> SoundBuffer:
        buf = SoundBuffer(self.sample_rate)
        total_samples = int(self.sample_rate * duration)
        for i in range(total_samples):
            t = i / float(self.sample_rate)
            phase = 2.0 * math.pi * frequency * t
            if waveform == "sine":
                val = math.sin(phase)
            elif waveform == "square":
                val = 1.0 if math.sin(phase) >= 0 else -1.0
            elif waveform == "sawtooth":
                val = 2.0 * (t * frequency - math.floor(0.5 + t * frequency))
            elif waveform == "noise":
                val = random.uniform(-1.0, 1.0)
            else:
                val = math.sin(phase)
            buf.samples.append(val)
        return buf
