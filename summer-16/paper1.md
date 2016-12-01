## Bistatic STAP: application to airborne radar
Space-time Adaptive Processing (STAP) enables minimizing SINR loss for airborne radar surveillance applications by estimating the interference covariance matrix and adaptively filtering the data.  Straightforward implementation of STAP assumes Gaussian independently and identically distributed data. In a bistatic radar application, the inherent diversified geometry leads to clutter that is non-stationary in range and varying in angle and doppler. This causes significant challenges in characterizing the clutter covariance. My interest in this paper is an ongoing effort to learn statistical signal processing and particularly STAP in bistatic applications.

The paper utilizes numerical simulations to first demonstrate the effects of clutter that varies significantly over range bins and then tries a handful of algorithms to compare performance. The metric used in the paper is the product of two loss factors, $\mathrm{L}_{s,2}(\theta,\phi,f_d)$ and $\mathrm{L}_{s,1}(\theta,\phi,f_d)$ the clairvoyant SINR loss and the SINR loss due to covariance estimate errors, respectively.

![SINR Loss](old-papers/png/c1.png)

The figure reprinted from the paper shows SINR loss across doppler bins for two different range bins or space-time snapshots. One note is how different the characteristics are for each, demonstrating the non-stationary effect of the bistatic geometry. Second, various strategies are compared against the Joint Domain Optimum (JDO) case.

The strategies center around two approaches - reduced-dimension STAP localized to space-time snapshots, where the effects of clutter heterogeneity are assumed minimal, and time-varying adaptive weights. The contribution of this paper is to merge the strengths of these two techniques and validate the improvement in performance. Joint Domain Localization (JDL) using a 5x5 window in Angle Doppler space outperforms the other algorithms in both the near (range bin 25) and the far (range bin 150) cases.

Applications of this paper would be to further develop strategies for dealing with interference in heterogeneous environments. The application specifically called out is bistatic radar applications, where the receiver is located on a separate platform, usually unmanned, than the transmitter. To develop and field a bistatic radar that successfully mitigates interference from ground clutter returns, the detection processing system would need strategies for addressing the non-stationary effect of radar data in a bistatic geometry.

This paper suggests a promising strategy in the form of JDL 5x5 processing. Future work might test this against more cases, further explore a mathematical foundation for assessing various strategies and which parameters, for a given algorithm, will produce optimal results.

## Citation
W. L. Melvin, M. J. Callahan and M. C. Wicks, "Bistatic STAP: application to airborne radar," Radar Conference, 2002. Proceedings of the IEEE, 2002, pp. 1-7.


