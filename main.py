import argh
from pydub import AudioSegment
from pathlib import Path


def split_audio(time_between_samples: int, original_audio):
    time_between_samples = int(time_between_samples)
    folder = original_audio + ".dir\\"
    Path(folder).mkdir(parents=True, exist_ok=True)

    segment = AudioSegment.from_wav(original_audio)
    counter = 0

    while counter + time_between_samples < len(segment):
        new_segment = segment[counter:counter + time_between_samples]
        new_segment.export(folder + f"sample{counter}.wav", format='wav')
        counter += time_between_samples


if __name__ == "__main__":
    argh.dispatch_command(split_audio)
