## CRLB performance for bistatic MIMO radar

In this final review of the Fall colloquium series, I will review a paper that derives the performance bounds for bistatic MIMO radars. The Cramer-Rao Lower Bound is used as a design figure of merit in that enables predicting the very best case given the system constraints. A radar system is parameterized by the illuminating waveform characteristics. Additionally, a key performance metric of any radar system is localization error. Given an estimate of a target's angular/Doppler frequency and its range, what is the error when the estimate is geolocated? Additionally, bistatic systems are very sensitive to the Tx/Rx/Target triangle geometry. Geolocation accuracy will vary with target location, not only due to distance, as is the case with monostatic radars, but with respect to the angle formed by the Target/Tx pair and the Target/Rx pair.

The authors consider the problem under the multiple-input, multiple-output (MIMO) system concept. In addition to the Receiver Angle of Arrival, measured by computing the phase progression of planar waves incident on a linear array of antenna elements, in MIMO, it is assumed that the receiver has access to an Angle of Departure measurement from the transmitter. For solving a target's position, this additional piece of information provides an over-solved system. This enables the ability to censor noisy measurements or exercise additional discrimination with respect to false alarms.

The CRLB presented is formulated assuming a prior distribution of target Doppler. The use-case presented by the authors seemed to indicate tracking humans. This allows some convenient bounds on target motion as opposed to targets of interest such as airborne platforms. First, the velocity distribution is very narrow with respect to the airborne receiver array. Second, humans are typically limited to movement in two dimensions, on the ground. With these assumptions, the contribution of the target velocity to the angle/Doppler frequency estimation is smaller.

Additionally, the CRLB formulation requires knowledge of the Tx/Rx pair positions and velocities and the illuminating waveform parameters. These include, the number of elements on each array, the pulse repetition interval, the signal bandwidth. Given these, the CRLB analysis provides a valuable source of best-case system performance as a function of target location.

This work is focused on a somewhat narrow use-case that assumes well-bounded target velocity distributions and a stationary transmitter. Future work might evaluate the CRLB analysis when the target velocity distributions are wider than that of the receiver and transmitter platforms, as is often the case when the target is a fighter jet.

## Citation
1. Li Li and J. L. Krolik, "CRLB performance for bistatic MIMO radar," 2015 IEEE Radar Conference (RadarCon), Arlington, VA, 2015, pp. 1468-1472.


