## A new method of generating multivariate Weibull distributed data

In this sixth review of the Fall colloquium series, I will review a paper which continues the theme of simulating radar phenomena, but approaches it from a perspective theoretical clutter models. The paper is by notable contributors from the Air Force Research Labs (AFRL) Sensors Directorate in Dayton, OH, teamed with researchers from Georgia Tech Research Institute (GTRI).

As noted by the authors, reflections from the earth, collectively referred to as clutter, continue to form the greatest challenge to radar detection theory. The simplest model of a received signal is that of the signal corrupted by additive white Gaussian noise. However, this case is never practical, as in all terrestrial radar the earth asserts itself as the largest scatterer. Variations in surface roughness, shape, and material make modeling the ground reflections a challenge.

For this reason, much research has focused on identifying random distributions suitable for modeling clutter. These distributions are typically "heavy-tailed" with a large shape parameter and an excess of outlier datas relative to Gaussians. The Weibull distribution has been validated as an appropriate model against experimental data, and has been characterized by radar researchers since it's introduction in the late 1960s. The Weibull is characterized by a random variable that
modulates the amplitude of a complex normal distribution.

The ultimate goal of clutter distribution characterization is a library of clutter models that can be queried in real time on a deployed sensor, perhaps aided by prior knowledge of the scene, to generate a vector of likelihood hypotheses against the data under test using the library. This method then provides a maximum likelihood choice for forming the null detection hypothesis. Data coordinates whose power exceed the threshold set by this hypothesis are tagged as detections under a probability of false alarm design constraint.

Though not addressed in the paper, bistatic geometries introduce additional challenges to the problem as the locus of clutter at any time, assuming an airborne transmitter and receiver pair, is summation of the velocity projections of each leg of the bistatic triangle.

The contribution of the subject paper introduces a new method of computing multivariate Weibull distributions which is more computationally tractable than the traditional Method of Norms. The Transform Method sacrifices cdf accuracy for a significant reduction in number of samples generated. This work may be furthered by validating the modeling strategy against experimental data.

## Citation
1. J. G. Metcalf, K. J. Sangston, M. Rangaswamy, S. D. Blunt and B. Himed, "A new method of generating multivariate Weibull distributed data," 2016 IEEE Radar Conference (RadarConf), Philadelphia, PA, 2016, pp. 1-6.

