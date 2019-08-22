![Funken logo](https://github.com/ar0551/GhFunken/blob/master/graphics/funkenLogo.png)

# GhFunken
Grasshopper interface (GPL) to the [Funken](https://github.com/astefas/Funken) Serial Protocol Toolkit.

GhFunken is a Grasshopper plug-in that interfaces to the Funken Serial Protocol Toolkit. It offers classes to initiate communication with Funken-Enabled Arduino devices, send commands and handle responses. On a more general level, it allows to fully remote control an Arduino-based device running Funken from Grasshopper, without need to access directly the Arduino code.

Funken is a [Arduino](https://www.arduino.cc) [library](https://www.arduino.cc/en/Reference/Libraries) that enables [callbacks](https://en.wikipedia.org/wiki/Callback_(computer_programming)) on an arduino. It is part of a workflow that simplifies communication between your Arduino and any host, that is able to speak to it via serial messages.
For more info on Funken, see the [Funken Repository](https://github.com/astefas/Funken).

GhFunken is build on top of [PyFunken](https://github.com/ar0551/PyFunken) and [PySerial](https://github.com/pyserial/pyserial).


## How to use GhFunken
GhFunken acts as an interface to send commands to an Arduino devices running a Funken implementation. Hence, to work properly, GhFunken assumes you kwow what protocol is defined in the Funken implementation running on the Arduino. For more details on how to define your own protocol using Funken, see [here](https://github.com/astefas/Funken#how-to-use-funken). For basic Arduino protocols which are shipped with Funken, see [here](https://github.com/astefas/Funken/blob/master/README.md#quickstart).

### How to install GhFunken
See the Setup and Quickstart instructions in the release files. Installation instructions COMING SOON!

### Examples
[Go to the examples folder in this repository and see a more detailed explanation of what is going on inside these examples.](https://github.com/ar0551/GhFunken/tree/master/exampleFiles)


## License
GhFunken: Grasshopper interface (GPL) to the [Funken](https://github.com/astefas/Funken) Serial Protocol Toolkit.

Copyright (c) 2019, Andrea Rossi

GhFunken is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3.0 as published by the Free Software Foundation.

GhFunken is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GhFunken; If not, see http://www.gnu.org/licenses/.

@license GPL-3.0 https://www.gnu.org/licenses/gpl.html


![DDU logo](https://github.com/ar0551/PyFunken/blob/master/materials/DDU-logo_BLACK_RGB.png)

Significant parts of GhFunken have been developed by Andrea Rossi and Alexander Stefas at [DDU Digital Design Unit - Prof. Oliver Tessmann - Technische Universität Darmstadt](http://www.dg.architektur.tu-darmstadt.de/dg/startseite_3/index.de.jsp).

## References
[Stefas, A, Rossi, A and Tessmann, O. 2018. Funken: Serial Protocol Toolkit for Interactive Prototyping, In Proceedings of ECAADE 2018, Lodz. Poland](http://papers.cumincad.org/data/works/att/ecaade2018_388.pdf)

