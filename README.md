# re-engineered_Quant-Based_Tool (Python Version)

This tool can be used to achieve likelihood ratio for suspect(s) and/or victim(s) in a DNA mixture using probabilistic genotyping

## Getting Started

Use these instructions to get started with reQBT (Python)

### Prerequisities

Python 2.7.11

```
https://www.python.org/downloads/
```

### Installing

Clone/download this repository

```
https://github.com/mramdass/re-engineered_Quant-Based_Tool_Python
```

## Running the tests

Open case.csv and enter mixture information in the following format:

```
Case Name,Locus,Contributors,Deducible,Quant,Known Pn 1,Replicate 1,Replicate 2,Replicate 3
John Butler,D8,3,D,60,12;14,8;12;13;14;15,8;10;12;13;14;15,8;13;14
John Butler,D21,3,D,60,28;30,28;29;30;30.2,28;29;29.2;30;30.2;31,29;30;30.2;31
John Butler,D7,3,D,60,9;9,8;9;10;11,8;9;11,8;9
John Butler,CSF,3,D,60,10;10,9;10;12,10;12,9;10;12
John Butler,D3,3,D,60,16;17,14;15;16;17;18,14;15;16;17;18;19,14;15;16;17;18;19
John Butler,TH01,3,D,60,6;6,6;8;9;9.3,6;8;9;9.3,6;8;9.3
John Butler,D13,3,D,60,11;14,8;9;14,8;9;11;12,8;9;11;13
John Butler,D16,3,D,60,11;13,9;10;11;12;13,10;11;12;13,10;12;13
John Butler,D2,3,D,60,22;23,19;20;22,19;20;22;25,19;27
John Butler,D19,3,D,60,12;14,12;13;13.2;14;15.2,12;13;13.2;14;15.2,12;13;13.2;14;15.2
John Butler,vWA,3,D,60,17;18,16;17;18,16;17;18,16;17
John Butler,TPOX,3,D,60,8;8,6;8;9;11,8;9,8;9
John Butler,D18,3,D,60,14;16,12;13;14;17;18,12;14;17;18,12;13;14;16;17;18
John Butler,D5,3,D,60,12;13,11;13,11;13,10;11;12;13;14
John Butler,FGA,3,D,60,21;22,19;21;22;23;24;25;26,19;21;22;23;25,19;21;22;23;25;26
```

OR

```
Case Name,Locus,Contributors Pn,Contributors Pd,Deducible,Quant,Known Pn 1,Replicate 1,Replicate 2,Replicate 3
John Butler,D8,3,3,D,60,12;14,8;12;13;14;15,8;10;12;13;14;15,8;13;14
John Butler,D21,3,3,D,60,28;30,28;29;30;30.2,28;29;29.2;30;30.2;31,29;30;30.2;31
John Butler,D7,3,3,D,60,9;9,8;9;10;11,8;9;11,8;9
John Butler,CSF,3,3,D,60,10;10,9;10;12,10;12,9;10;12
John Butler,D3,3,3,D,60,16;17,14;15;16;17;18,14;15;16;17;18;19,14;15;16;17;18;19
John Butler,TH01,3,3,D,60,6;6,6;8;9;9.3,6;8;9;9.3,6;8;9.3
John Butler,D13,3,3,D,60,11;14,8;9;14,8;9;11;12,8;9;11;13
John Butler,D16,3,3,D,60,11;13,9;10;11;12;13,10;11;12;13,10;12;13
John Butler,D2,3,3,D,60,22;23,19;20;22,19;20;22;25,19;27
John Butler,D19,3,3,D,60,12;14,12;13;13.2;14;15.2,12;13;13.2;14;15.2,12;13;13.2;14;15.2
John Butler,vWA,3,3,D,60,17;18,16;17;18,16;17;18,16;17
John Butler,TPOX,3,3,D,60,8;8,6;8;9;11,8;9,8;9
John Butler,D18,3,3,D,60,14;16,12;13;14;17;18,12;14;17;18,12;13;14;16;17;18
John Butler,D5,3,3,D,60,12;13,11;13,11;13,10;11;12;13;14
John Butler,FGA,3,3,D,60,21;22,19;21;22;23;24;25;26,19;21;22;23;25,19;21;22;23;25;26
```

OR

```
Case Name,Locus,Deducible,Quant,Known Pn 1,Unknowns Pn,Unknowns Pd,Replicate 1,Replicate 2,Replicate 3
John Butler,D8,D,60,12;14,2,3,8;12;13;14;15,8;10;12;13;14;15,8;13;14
John Butler,D21,D,60,28;30,2,3,28;29;30;30.2,28;29;29.2;30;30.2;31,29;30;30.2;31
John Butler,D7,D,60,9;9,2,3,8;9;10;11,8;9;11,8;9
John Butler,CSF,D,60,10;10,2,3,9;10;12,10;12,9;10;12
John Butler,D3,D,60,16;17,2,3,14;15;16;17;18,14;15;16;17;18;19,14;15;16;17;18;19
John Butler,TH01,D,60,6;6,2,3,6;8;9;9.3,6;8;9;9.3,6;8;9.3
John Butler,D13,D,60,11;14,2,3,8;9;14,8;9;11;12,8;9;11;13
John Butler,D16,D,60,11;13,2,3,9;10;11;12;13,10;11;12;13,10;12;13
John Butler,D2,D,60,22;23,2,3,19;20;22,19;20;22;25,19;27
John Butler,D19,D,60,12;14,2,3,12;13;13.2;14;15.2,12;13;13.2;14;15.2,12;13;13.2;14;15.2
John Butler,vWA,D,60,17;18,2,3,16;17;18,16;17;18,16;17
John Butler,TPOX,D,60,8;8,2,3,6;8;9;11,8;9,8;9
John Butler,D18,D,60,14;16,2,3,12;13;14;17;18,12;14;17;18,12;13;14;16;17;18
John Butler,D5,D,60,12;13,2,3,11;13,11;13,10;11;12;13;14
John Butler,FGA,D,60,21;22,2,3,19;21;22;23;24;25;26,19;21;22;23;25,19;21;22;23;25;26
```

To Run, double click on reQBT_Python_vX.X.py (where Xs represent version digits) or via command line:

```
python reQBT_Python_vX.X.py
```

Notes:

```
NEG - in place of a replicate if you wish to imply that all alleles dropped out; drop-in and drop-out rates will be applied
INC - in place of a replicate if you wish to ignore that replicate
```

## Author

* **Munieshwar Ramdass** - *Initial* - [re-engineered Quant-Based Tool](https://github.com/mramdass/re-engineered_Quant-Based_Tool)

## License


re-engineered Quant-Based Tool Copyright (C) 2016 Munieshwar Ramdass

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
