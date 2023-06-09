

<h1 style="font-family: cursive;" align="center">BlueJamm ⚡ </h1>  <a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/e92d3b4c5675f9defea3d4a4e14aad8a9002a4a887ea2fa3d93d87ea8d4cc4fe/68747470733a2f2f6672657368696465612e636f6d2f6a6f6e61682f6170702f73696d706c652d766965772d636f756e746572"><img title="repo views" src="https://camo.githubusercontent.com/e92d3b4c5675f9defea3d4a4e14aad8a9002a4a887ea2fa3d93d87ea8d4cc4fe/68747470733a2f2f6672657368696465612e636f6d2f6a6f6e61682f6170702f73696d706c652d766965772d636f756e746572" data-canonical-src="https://freshidea.com/jonah/app/simple-view-counter" style="max-width: 100%;"></a>

<p align="center">Script for quick and easy DOS-attacks on bluetooth devices for pentest purposes</p>

<b>BlueJamm</b> is a powerful tool designed to disrupt Bluetooth device connections by flooding them with ping packets. By leveraging this tool, users can effectively jam Bluetooth connections and prevent devices from establishing successful connections in their vicinity.

BlueJamm operates by continuously sending a high volume of ping packets to the target Bluetooth device. This flood of packets overwhelms the device's resources and prevents it from effectively processing legitimate connection requests. As a result, the Bluetooth device experiences difficulties in establishing connections, effectively rendering it inaccessible or unresponsive.

The tool's ability to flood Bluetooth devices with ping packets makes it an efficient means of disrupting Bluetooth connections in various scenarios. It can be utilized for security testing, network diagnostics, or as a means of temporary disruption in specific environments. However, it's important to note that BlueJamm should be used responsibly and with proper authorization, as it may violate regulations or cause interference with legitimate Bluetooth operations.

Please note that intentionally disrupting or interfering with Bluetooth connections without proper authorization may be illegal in some jurisdictions. It is essential to familiarize yourself with local laws and regulations before using tools like BlueJamm.



## Disclaimer
<p align="center">This project was created only for good purposes and personal use.</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

# ⚙️How To Use

#  >_     

```
$ sudo apt update
$ sudo apt install python3
$ sudo git clone https://github.com/root-cyborg127/Bluejammer
$ cd Bluejammer
$ python3 bluejamm.py
```
### Note
<p>The script works only with Linux systems.</p>
<p>YOU MUST RUN THIS SCRIPT IN SU MODE~[ROOT]</p>
<p>You must have "l2ping" util on your linux machine (it installed as default on Kali Linux).</p>
<p>YOU MUST SCAN AND ATTACK BEFORE SOMEONE CONNECT TO THE TARGET!!!</p>


## It tested on
Kali Linux as attacker, and ARTIS Bluetooth Speaker as target

## Using
<p>First of all, you must scan network for Bluetooth devises. For example, you can use "hcitool".</p>

```
$ sudo apt update
$ apt install hcitool
$ sudo service bluetooth start
$ hcitool scan
```
<p>Output will be like:</p>

```
A1:B2:C3:D6:E7      ARTIS Bluetooth Speaker
B1:C2:D3:E4:F5      iPhone(Vishwa)
C1:D2:E3:F4:G5      Some Bluetooth device
```
<p>Then copy target addres (for example "A1:B2:C3:D6:E7") and paste it in "Target addr".</p>

## Manual

1. "Target addr" - addres of your target (Check info above).
2. "Packages size" - size of the packages, that will be sent to the target. 600 is optimal.
3. "Threads count" - number of threads, that will send packages to the target at the same time. I used 500 threads, and that was enough. Check the table below, to find optimal value.

|  Packages size | Threads count| Ping, ms  | Distance, meters | Time waited, sec  | Device |
|:--------------:|:-----: |:------------:|:--------------------:|:----------------:|:------:|
|  600           | 1       | 9           |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 10      | 38          |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 20      | 78          |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 50      | 229         |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 100     | 413         |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 200     | 806         |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 500     | 1961        |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 1000    | 6621        |0,3                   |           5      |ARTIS Bluetooth Speaker|
|  600           | 1000+   | Couldn't calculate  |0,3           |           5      |ARTIS Bluetooth Speaker|


![screenshot](https://github.com/root-cyborg127/Bluejammer/blob/main/screenshots/screenshot.JPG )

## ⚠ What happens to the target device

<p>I can't say about all devices, but device I tested just turned off.</p>
