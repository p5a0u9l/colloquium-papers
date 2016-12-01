## Cognitive Radar for Target Tracking
I work in radar technology and enjoy keeping current with the research literature on the subject. Cognitive radar is particularly interesting as it holds promise of merging the results of fields like control theory and machine learning with radar.

In a cognitive radar, the target state estimate and associated covariance is passed to a Perception block which uses a model to predict which mode parameter changes would optimize the state estimate. These parameter updates are sent to a control block that activates the new transmitter parameters. In this way, errors in target detection are reduced and surveillance focus is easily redirected with reduced settling time.

Dr. Kristine Bell, along with colleagues from the Ohio State University, and funding from the Air Force Research Labs in Dayton, Ohio, have built upon previous work with software-defined platforms and cognitive radar experiments. In the paper, the Perception block is implemented with a State Estimator, known in radar parlance as a tracker, using a Maximum a Posteriori with Penalty Function (MAP-PF) algorithm. A key characteristic of MAP-PF is constraining future detections to the region predicted by the tracker.

Bell _et al_ constructed a controlled experiment wherein a single moving target, in the form of a human body, was tracked at close range over time. Additionally, a single transmitter parameter was chosen for optimization - that of the pulse repetition frequency. The goal of varying the PRF was to optimize tracking performance while avoiding Doppler aliasing and avoiding effects of zero-Doppler clutter.

One of the most challenging aspects of any radar system is dealing with the signal returns from stationary objects. These returns typically dominate the power envelope of Doppler filters around 0 Hz. Tracking objects whose Doppler is varying and transitioning through clutter is a universal radar challenge. In the experiment, a person is moving at a constant rate in a circular fashion, such that their one-dimensional distance from the sensor is varying as a sine wave. Of course, the range rate, being the time derivative of range, varies as a cosine, symmetrically about zero Doppler.

A positive result of the experiment demonstrated adaptation when the target Doppler is approaching a zero-crossing. According to the cost function implemented, the PRF dropped in the region of zero Doppler and then returned to the higher PRF. For tracker performance to be optimized, a higher PRF minimizes range error due to the more frequent sampling of the space. This is true when the target velocity separates it from zero Doppler. However, as the target approaches zero Doppler, reducing the PRF becomes advantageous in order to increase the frequency resolution, which in turn increases the minimal detectable velocity. In this way, the experiment demonstrated adaptation to the details of the scene, which in turn, improved performance.

Future extensions to this work could involve demonstrating real-time implementation, as the current research performed the processing offline.

Applications involve any future radar or sensor systems where performance requirements and environmental dynamics dictate advanced methods of adapting waveforms to optimize sensed parameters.

## Citation
K. L. Bell, J. T. Johnson, G. E. Smith, C. J. Baker and M. Rangaswamy, "Cognitive radar for target tracking using a software defined radar system," 2015 IEEE Radar Conference (RadarCon), Arlington, VA, 2015, pp. 1394-1399.
