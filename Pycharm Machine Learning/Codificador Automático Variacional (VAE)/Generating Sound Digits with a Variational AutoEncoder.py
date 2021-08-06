import librosa

from preprocess import MinMaxNormaliser

class SoundGenerator:
    """SoundGenerator is responsible for generating audios
    from spectrograms."""

    def __init__(self, vae, hop_length):
        self.vae = vae
        self.hop_length = hop_length
        self._min_max_normaliser = MinMaxNormaliser(0, 1)

    def generate(self, spectrograms, min_max_values):
        generated_spectrograms, latent_representations = self.vae.reconstruct(spectrograms)
        signals = self.convert_spectrograms_to_audio(generated_spectrograms, min_max_values)
        return signals, latent_representations

    def convert_spectrograms_to_audio(self, spectrograms, min_max_values):
        signals = []
        for spectrogram, min_max_value in zip(spectrograms, min_max_values):
            # reshape the log spectrogram
            log_spectrogram = spectrogram[:, :, 0]  # we are coping the first and secound dimension, and discarding the third
            # apply denormalization
            denorm_log_spec =
            # log spectrogram -> spectrogram
            # apply Griffin-Lim
            # append signal to "signals"
