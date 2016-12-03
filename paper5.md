## Time and frequency synchronization of bistatic FMCW radar

In this fifth review of the Fall colloquium series, I will review a paper which aims to model and characterize phenomenon inherent to bistatic systems, synchronization to the illuminator waveform. Unlike a monostatic system which is able to leverage a single local oscillator to drive both the transmitter and receiver A/D (or D/A) clocks, a bistatic radar must sample the received signal and reconstruct the location of the signal both in time and frequency.

The particular type of radar in the subject paper is a frequency-modulated continuous-wave (FMCW) radar. Systems utilizing these waveforms are often cheaper to field than their pulse-doppler counterparts and provide good range accuracy over short ranges. As such, they are increasingly used in vehicles leveraging sensors for self-driving cars. The simplicity of design derives chiefly from the ability to mix the received RF signal directly using the transmit channel's signal. Of course, a bistatic system fundamentally breaks the physical proximity which allows this convenience. As such, it imposes a challenge in synchronizing. The author notes that errors in deriving the time and frequency offset of the received signal manifest in reduced SNR, which affects probability of detect, and range measurement error, which affects geolocation accuracy.

The obstacle can be overcome by implementing a reference channel on the bistatic receiver which is dedicated to receiving the direct-path of the illuminator. Synchronizing the waveform contained in this direct-path signal then can serve as the reference clock for signals arriving from various other angles which hopefully contain target reflections. However, the received direct-path signal contains non-idealities not present in monostatic systems. Firstly, the signal has traveled through the air and picked up additive Gaussian noise at the receiver front-end.

Secondly, at typical RF frequencies, say, X-band, which is the carrier frequency of the simulation in the paper, a cycle of the complex exponential completes a revolution in a fraction of a nanosecond. At these levels, phase noise can contribute significantly to accuracy. All clocks will differ in their accounting of time, even those disciplined by GPS pulse-per-second signals and driven by crystal oscillators. In this case, a difference on the order of a part-per-trillion between the transmit clock and the receiver clock will induce an additional non-trivial error term.

The authors conducted a simulation modeling the phase noise using Leeson's equation [2] as complex gain terms on the received signal, in addition to the conventional Gaussian noise term. The contribution derived a curve demonstrating the nanosecond delta plus 95% confidence interval as a function of received SNR.

Future work for the authors should include the effects of platform motion, which are absent in this paper as the transmit and receive platforms are apparently stationary. Platform motion will induce a direct-path doppler term in the frequency offset that represents the projection of the transmitter velocity and receiver velocity vectors onto the line connecting the two (i.e., the direct-path).

## Citation
1. J. Kim, J. Chun and I. Choi, "Time and frequency synchronization of bistatic FMCW radar," IET International Radar Conference 2015, Hangzhou, 2015, pp. 1-4.

2. Leeson, D. B. (February 1966), "A Simple Model of Feedback Oscillator Noise Spectrum", Proceedings of the IEEE, 54 (2): 329–330



