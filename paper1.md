## Experimental Study of Uncooperative Radar Signals as Illuminators for Passive Bistatic Radar Applications
In this first review of the Fall colloquium series, I will return to the general topic of radar and particularly multi-static radar technology.

Multi-static radars are those which generalize the location of the illuminating system, the transmitter, and the surveillance system, the receiver. Moreover, the number of transmitters and receivers can be generalized to numbers greater than one. The vast majority of fielded radar systems over the last century have been of the monostatic variety, where the transmitter and receiver are co-located in a single system.

A critical milestone to generalized multi-static systems is the bistatic case. Here, we have a single illuminating system and a single receiving system. The receiver may be categorized by it's relationship to the transmitter. When there is a null relationship we can say the transmitter is uncooperative and label the receiver as passive.

The focus of the subject paper is Passive Bistatic Radar (PBR) applications as they
relate to radar illuminators. This distinguishes from PBR systems which opportunistically hitchhike off of
non-radar electromagnetic emissions, such as HDTV, LTE, digital FM, WiFi. These non-radar systems have the
advantage of being ubiquitous and, in the case of large area broadcasters, powerful. They have the disadvantage of possessing waveforms that are effectively random, from a radar perspective. The consequence is that the ambiguity function response of these random waveforms possesses undesirable sibelobes in both
time and frequency. This is unsurprising as the signals were designed to carry digital payloads and not radar impulses. Much of the open-literature work in the field has focused on advanced signal processing methods to mitigate the effects of PBR as applied to opportunistic digital broadcast signals.

This paper however, focuses instead on using actual surveillance radar systems as the transmitters of opportunity, particularly civilian airport surveillance radars. The advantage of using surveillance radars is that their ambiguity function more closely resembles the desired impulse, which leads to improved time and frequency resolution of detected signals. The disadvantage is that, outside of a national defense context, these radars are few and far between.

There are two algorithmic challenges which the paper addresses: extracting the waveform parameters from the reference channels and extracting the target parameters from the surveillance channel. The aim of both is to provide geolocation measurements of a moving airborne target over time. The paper discusses the results of two experiments that solve the two challenges using the spatial discrimination of a dedicated reference antenna pointing at the known location of the stationary
transmitter and a dedicated surveillance array of antennas focused on the scattered signals. By using digital phased array processing techniques, the direction of arrival may be measured, while the bistatic range comes from the traditional signal detection techniques. With these two target parameters and knowledge of the receiver and transmitter locations, the target parameters can be transformed using trigonometric relations and coordinate transforms to common geolocation coordinate
systems.

The paper provides successful results from the two experiments to demonstrate the feasibility of the application. Further work could mature the existing system to something that was able to work in real-time
without _a priori_ crutches.

## Citation
Yasen Wang, Qinglong Bao and Zengping Chen, "Experimental study of uncooperative radar signals as illuminators for passive bistatic radar applications," 2016 Progress in Electromagnetic Research Symposium (PIERS), Shanghai, China, 2016, pp. 1345-1349.
