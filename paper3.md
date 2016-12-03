## A signal and plot simulator for passive bistatic radar

In this third review of the Fall colloquium series, I will review a paper which describes a system for modeling and simulating passive bistatic radar (PBR) systems.

The first paper reviewed discussed using bistatics in conjunction with civilian radar surveillance systems, partly as an answer to the complexities associated with the random waveforms of traditional PBR systems. The second paper discussed an application exploiting ground scattering of GPS signals to improve water-content maps. This third paper addresses the development of systems seeking to exploit digital broadcast signals.

Modeling and simulation promises the ability to reduce the cost and risk associated with fielding a general system. This paper addresses implementing these types of software tools to PBR systems. There are two steps to a bistatic radar simulation. The forward problem addresses simulating the received signal as a summation of direct-path energy, ground, and other undesirable, reflections, commonly referred to as clutter, and the desired signal, which nominally represents scattering from an airborne target. The inverse problem addresses suppressing the unwanted elements and extracting the parameters of the desired target reflection.

The paper describes using XML as a format for specifying scenario generation, with parameters of one or more transmitters, one or more receivers, one or more target entities, and clutter reflectors. Given the relevant kinematic and electromagnetic parameters of each entity, the forward simulation problem becomes one of mapping the constituent signals into a bistatic radar range equation. This is a generalized version of the monostatic radar equation, which itself, is a variant of the well-known Friis' equation for free-space path loss.

The paper concludes by presenting results of a simulation that appear, graphically, to reproduce the results real-world data.

I find this paper not contributing significantly to the area of bistatic radar phenomenology simulation.

A significant consideration of any radar simulation is the Radar Cross-Section (RCS) of the scattering entities. This models the amount of power reflected toward the receiver and remains an area of active research. In general, an object in space will present a varying RCS that is a complicated function of the object's shape and materials. This paper simplifies by allowing users to specify one of two general target types, Airplane or Fighter.

A second area of active research for bistatic simulations is that of the ground clutter. This also is complicated function of surface type and shape. Sea clutter varies from tree clutter which varies from city clutter. This paper treats clutter as a set of objects, similar to targets, rather than a pervasive, heterogeneous effect.

I find the contributions of the subject paper to be in the area of developing software tools which can be used to provide a systems engineering analysis of PBR systems by varying illuminator waveform parameters and scenario elements.

## Citation
M. Zywek, M. Malanowski and M. K. Baczyk, "A signal and plot simulator for passive bistatic radar," 2016 17th International Radar Symposium (IRS), Krakow, 2016, pp. 1-4.
URL: http://ieeexplore.ieee.org.offcampus.lib.washington.edu/stamp/stamp.jsp?tp=&arnumber=7497373&isnumber=7497259
