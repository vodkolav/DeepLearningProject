<div style="display: flex; justify-content: center;">

## AUDIOSR – VAE
</div>


Niv Aharon Cohen, Michael Berger



### ABSTRACT

In this project, we explored audio super-resolution by recreating and enhancing the model proposed in AUDIOSR: Versatile Audio Super-Resolution at Scale. Audio super-resolution aims to reconstruct high-resolution audio from lower-resolution inputs, with applications in areas such as music restoration, audio compression, and telecommunication. The AUDIOSR model employs a diffusion-based generative approach to upscale audio bandwidth from 2 kHz to 16 kHz, generating high-resolution audio output at 24 kHz bandwidth with a 48 kHz sampling rate. Our work involved replicating the AUDIOSR architecture and training process, while introducing some modifications to further improve performance and versatility. We extended the model by integrating additional features to filter different noises and distortions. The performance of both the original and modified models was evaluated on standard datasets, demonstrating competitive results in terms of audio quality and bandwidth restoration. Our findings provide insights into the adaptability of diffusion models in audio super-resolution and open avenues for further research in this domain.
Our code demo is avaliable on Github on this link:
PUT LINK????????????????????????????


### 1.	INTRODUCTION

Audio super-resolution (ASR) is the task of converting low-resolution audio signals to high-resolution, enhancing their fidelity, bandwidth, and perceptual quality. This problem is crucial in various fields, including music production, audio restoration, and telecommunication, where audio data often suffers from bandwidth limitations. As deep learning techniques advance, several generative models have emerged, offering new possibilities for tackling ASR with greater accuracy and scalability.

One such model is AUDIOSR: Versatile Audio Super-Resolution at Scale[????], which leverages a diffusion-based generative framework to reconstruct high-resolution audio from low-resolution inputs.
The model upscales audio bandwidth from 2 kHz to 16 kHz and generates high-fidelity output with a bandwidth of 24 kHz and a sampling rate of 48 kHz. This approach marks a significant step forward in the domain of ASR by effectively capturing the complex temporal and spectral characteristics of audio signals.
The AUDIOSR model builds upon earlier work by Haohe Liu, particularly the AudioLDM[???????] framework. AudioLDM was initially designed to convert text to audio by conditioning audio generation on text during the training process. It introduces a novel combination of Variational Autoencoders (VAE), Contrastive Language-Audio Pretraining (CLAP), latent diffusion models, and audio vocoders to synthesize high-quality audio. While AudioLDM focuses on text-conditioned audio generation, AUDIOSR extends these ideas specifically to bandwidth extension and high-resolution audio reconstruction, focusing on the audio domain, but now with audio-conditioning instead of text-conditioning.
In this project, we aimed to recreate the AUDIOSR model and extend its capabilities. Our work introduces several modifications to improve the versatility and performance of the model, including adjustments to the training process, to train on different distortions and noises. This paper presents the details of our implementation, the enhancements we introduced, and a comprehensive evaluation of the model's performance.



### 2.	LITERATURE REVIEW
One notable approach in the field of audio enhancement is presented by Mostafa Sadeghi in "Audio-visual Speech Enhancement Using Conditional Variational Auto-Encoders" [????] This study introduces a novel method leveraging Conditional Variational Auto-Encoders (CVAEs) for improving audio quality through the integration of visual information. The method employs a dual VAE architecture, with one VAE dedicated to processing audio and another to analyzing the visual representation of the speaker's lips.

The core innovation of this approach lies in the conditioning of the audio VAE on the visual VAE. By using lip movement data as a conditional input, the model enhances the audio signal more effectively on the additional contextual information provided by the visual data. This approach mirrors the concepts explored in our project on audio super resolution (AudioSR), where high-resolution audio is learned conditionally based on low-resolution audio, with both signals encoded using VAEs. The integration of visual data for audio enhancement highlights the potential of using multi-modal information to improve audio quality.

Another significant contribution to the field is presented by Huajian Fang in "Variational Autoencoder for Speech Enhancement with a Noise-Aware Encoder" [??????]. This study addresses the challenge of noise reduction in speech enhancement through a sophisticated VAE-based approach. Fang’s method involves training two distinct VAEs: one for clean audio and another for noisy audio. The purpose of this dual VAE system is to encode both clean and noisy audio into separate latent spaces.

A key aspect of this approach is the use of Kullback-Leibler (KL) divergence to align the latent representations of noisy audio with those of clean audio. By minimizing the divergence between these latent spaces, the model effectively reduces the influence of noise, resulting in enhanced speech quality. This noise-aware encoding technique demonstrates a robust method for improving audio clarity by refining the latent space representations. The concept of aligning noisy and clean latent spaces shares similarities with our exploration of conditional learning in AudioSR, underscoring the relevance of advanced VAE techniques for effective audio enhancement.

### 3. PROBLEM FORMULATION ANMETHOD
Given an analog signal that has been discretely sampled at a rate of l samples per second, resulting in a low-resolution sequence of values. The goal of audio super resolution (SR) is to estimate a higher resolution signal sampled at a rate of h samples per second, where h > l and T is the total duration in seconds. According to Nyquist’s theory, the low resolution signal have maximum frequency
bandwidths of l/2 Hz and the high resolution signal have h/2 Hz. Therefore, the
information contained between frequencies of h/2 − l/2 Hz is missing from the low resolution signal. Estimating the “missing” frequency data is the core objective of the SR task.






### 4. PREPROCESSING
In our study, we first apply a low-pass filter to the audio signal, following the procedure outlined in AUDIOSR. The cutoff frequency for the low-pass filter is randomly selected from a uniform distribution between 2 kHz and 16 kHz. To ensure the robustness and generalization of the filtering process, the type of low-pass filter is also chosen randomly from four different filter designs: Chebyshev, Elliptic, Butterworth, and Boxcar. The order of the filter is selected randomly from an integer range between 2 and 10. This variability in the filter selection is crucial to replicate the diverse conditions observed in the referenced work and to address the filter generalization problem.

After filtering, we introduce noise into the waveform. The noise type is selected randomly between single-tone noise and Gaussian noise. For both noise types, the amplitude is chosen from a uniform distribution within the range of 0.001 to 0.2, and the center frequency is uniformly sampled between 100 Hz and 15 kHz. In the case of Gaussian noise, we further introduce variability by randomly sampling the standard deviation from a uniform distribution between 50 Hz and 800 Hz, ensuring a broad spectrum of noise characteristics.


### EXPERIMENT


### RESULT

### CONCLUSION

### REFERENCES

