## Adaptive Clutter Cancellation in Bistatic Radar
In Paper 1, I reviewed similar research related to bistatic radar and clutter cancellation. The focus of that work was a numerical simulation comparing various strategies using a metric known as SINR Loss. This paper preceded that one and presents more of the mathematical framework for the problem. As mentioned before, I have an ongoing interest in Space-Time Adaptive Processing (STAP) methods for radar applications.

STAP is a broad term that is used to capture the processing techniques associated with maximizing SINR in sensors by characterizing the covariance of interferers. This results in a well-known result involving sample matrix inversion (SMI) and used frequently in both RF communications and radar. Namely, the optimal weight set for the $k$th range realization is denoted as

\begin{align}
    w_k = \mathbf{R}_k^{-1} v_{st}
\end{align}

When the sensor data is filtered with $w_k$ the SINR is maximized, which in turn maximizes probability of detection, $P_D$. $\mathbf{R}$ is the ideal (also known as _clairvoyant_) interference covariance and $v_{st}$ is the space-time steering vector.

In space-time radar, the environment is sensed by a number of antenna array elements, spatial samples, and a number of pulses, temporal samples. In the presence of zero-mean, unity-variance Gaussian noise, the covariance reduces to an identity matrix and the optimal filter for each range snapshot is the space-time steering vector itself. Apart from physical mapping scalars such as element spacing, carrier frequency, _et al_, the steering vector is comprised of a Kronecker product of two matched filters which can be implemented as a two-dimensional discrete Fourier transform. Pulse samples are transformed to Doppler frequency responses, and element samples are transformed to spatial frequency, or direction of arrival, responses.

In real-world applications, the covariance is not known and must be estimated. The SMI estimator is known to be maximum-likelihood in the presence of i.i.d Gaussian noise. In most radars however, the strongest, most persistent, interferer is ground clutter, and samples are often coupled in various ways. This results in SINR loss, the minimization of which has been studied extensively for monostatic radar platforms. In bistatic radars, where the receiver is physically separated from the transmitter, the problem is compounded further. The triangular geometry induces non-symmetry in clutter scatter paths which leads to responses in angle and doppler that are not range independent, as they are in monostatic applications. This non-stationarity makes SMI training using adjacent range cells a less effective estimator. For airborne platforms, the triangle defined by the transmitter, receiver, and the ground is also continually changing.

The primary ameliorating strategy investigated in this paper is known as Joint-Domain Localized (JDL). Joint in the sense of Angle and Doppler (or similarly, Element and Pulse) and Localized in the sense of reducing the number of training data to a region centered on the range cell under test. This reduction has the added benefit of reducing the computational throughput required, which can be prohibitive in many cases. However, the reduced sampling requires a reduction in clutter rank in order to satisfy the lower training bound known as the Reed-Mallet-Brennan (RMB) Rule. There is a transformation $T$ associated with JDL processing to reduce the problem to a subspace of dimensionality $Q$, where $Q << NM$. $NM$ is the product of the number of temporal pulses and spatial elements and represents the space in which theoretical STAP is applied.

The contributions of this paper can be summarized as a numerical confirmation of the hypothesis that bistatic clutter cancellation suffers from challenges more general, and intractable, than monostatic radars, as well as validation of the JDL-STAP method as a successful means of reducing a large portion of the loss induced by bistatic geometries.

Applications of this research involve developing bistatic radar systems, which can have many practical advantages. In the context of defensive surveillance, bistatics enables a forward-deployed passive sensor cooperating with a larger transmitter, such as an early warning system. This can increase the effective area surveilled while maintaining a low-visibility profile to aggressors.

As of the writing of this paper, the field was very nascent. Many of the more exotic algorithms developed to address bistatic clutter cancellation remained computationally intractable for most platforms until recently. There is now renewed academic interest in the subject of bistatic and multi-static sensor networks and strategies for reducing the impact of diverse geometries on the signal processing. This and other papers have addressed radars with a lower PRF, future work could
investigate the more complicated case of high-PRF radars, where there is inevitable range aliasing, such that a given cell may contain the response of one or more clutter returns folded onto one cell.

## Citation
W. L. Melvin, M. J. Callahan and M. C. Wicks, "Adaptive clutter cancellation in bistatic radar," Signals, Systems and Computers, 2000. Conference Record of the Thirty-Fourth Asilomar Conference on, Pacific Grove, CA, USA, 2000, pp. 1125-1130 vol.2.

