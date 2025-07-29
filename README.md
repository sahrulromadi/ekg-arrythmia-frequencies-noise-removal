
# Utilization of a Denoising Convolutional Autoencoder Model Based on Conv1D for Noise Removal in Electrocardiogram (ECG) Signals

This study focuses on the application of a Denoising Convolutional Autoencoder (DCAE) using one-dimensional convolutional layers (Conv1D) to effectively remove noise from electrocardiogram (ECG) signals.
ECG signals, which are critical for diagnosing heart conditions, are often contaminated by various types of noise such as baseline wander(bw), muscle artifacts(ma), and electrode motion(em) interference. 
These disturbances can hinder accurate interpretation and analysis.

This research explores the use of a Conv1D-based Denoising Convolutional Autoencoder (DCAE) for noise removal in electrocardiogram (ECG) signals, focusing on signal reconstruction in the time domain. The model is designed to learn the mapping between noisy ECG signals and their clean counterparts, enabling effective denoising with minimal reconstruction error.
In addition to time-domain approaches like the DCAE, hybrid models such as Wavelet-MLP, which operate in the wavelet coefficient domain, are also considered. These models extract key features from decomposed signals and use machine learning to reconstruct the clean signal.
Both methods—DCAE and Wavelet-MLP—aim to accurately recover the original ECG waveform from signals contaminated by noise such as baseline wander(bw), muscle artifacts(ma), and electrode motion(em).
By comparing the performance of time-domain and coefficient-domain denoising techniques, this study contributes to the development of reliable and efficient signal processing methods that improve the quality of ECG signals, ultimately supporting better clinical interpretation and diagnosis.



