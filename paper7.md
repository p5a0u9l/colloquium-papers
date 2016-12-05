## Modified JDL with Doppler compensation for airborne bistatic radar

In this seventh review of the Fall colloquium series, I will review a paper which approaches the problem discussed in paper six from a signal processing perspective. The subject concerns the field of radar signal processing known as Space-Time Adaptive Processing (STAP) which uses the signal distribution to produce a clutter covariance matrix. Inversion of this matrix and forming an outer product of the data with a vector representing a target doppler/angle frequency mode is known to produce an adaptive, data-derived filter which maximizes signal to interference plus noise (SINR) and thus maximize probability of detection.

STAP can produce orders of magnitude gain, but only in the presence of range homogeneous data. This is the case for the traditional monostatic radars, where the transmitter and receiver are collocated. It is very different for bistatic receivers where, as mentioned in the previous review, the clutter ridge varies by range gate, creating a heterogeneous covariance sampling matrix.

This paper discusses one method of mitigating this effect by applying a range-dependent frequency shift to the data. The algorithm is easy to conceptualize if one thinks of clutter as a ridge of high amplitude in a range and doppler image, where range denotes a time delay corresponding to distance and doppler denotes a phase shift induced on the scattered signal due the Doppler effect. In bistatic geometries, this ridge is typically "tilted" with respect to range. The Doppler compensation applies a phaser rotation transform to the range-Doppler image that straightens the ridge, attempting to make the datas artificially homogeneous over range.

In addition, there is a technique known as Joint-Domain Localized (JDL) STAP, which attempts to address both the computational intractability of traditional STAP as well as the effects of heterogeneous clutter distributions by localizing the sample covariance training to a small region surrounding the data under test. Further, the paper refers to a modification to the JDL algorithm which varies the sampling of of the range-Doppler image to non-integer values, resulting in an interpolation applied to the data response.

The authors conduct a simulation to test the validity of the combined modified-JDL plus Doppler-compensated strategy for improving STAP performance in bistatic airborne sensors. A figure of merit known as SINR-Loss plots the reduction in SINR over the Doppler spectrum. Typically this results in a notch near the clutter Doppler center and the various algorithms attempt to raise the trough of the notch, as well as narrow it's width, which leads directly to improving the
minimum-detectable-velocity (MDV) metric. The authors demonstrate promising results in this respect against their simulated data.

Further work would prove the algorithm against experimental data. It is hard to estimate the efficacy of an algorithm tested against simulated data in this field for the reasons mentioned in the previous review. Bistatic clutter phenomenology is not well characterized by existing open literature sources, therefore simulations produced to replicate the phenomenology are not as impactful as those exercise against actual sensor data.

## Citation
1. Chin Heng, B. Lim, E. Aboutanios and B. Mulgrew, "Modified JDL with Doppler compensation for airborne bistatic radar," IEEE International Radar Conference, 2005., 2005, pp. 854-858.