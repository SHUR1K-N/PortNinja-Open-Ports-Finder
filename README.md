# PortNinja: Open Ports Finder

## Description & Usage
A super fast multithreaded ports scanner that scans for open listening ports on the specified target server with the following methods:

1. All ports in existence (1 – 65,535)
2. Top 1,000 common ports only [(reference)](https://nullsec.us/top-1-000-tcp-and-udp-ports-nmap-default/)
3. User-specified range of ports
4. User-specified individual ports

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/PortNinja-Open-Ports-Finder/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for research purposes.

## Scan Speeds
The user can select one of four scan speed options for use case-specific executions, ranging from slowest (most accurate) to fastest (may miss ports), as shown below:

<div align="center">

|Option   |Speed    |Accuracy                                   |Scan Time    |
|---------|---------|-------------------------------------------|-------------|
|1.	      |Slowest  |Most accurate (zero / minimum missed ports)|~3+ hours    |
|2.	      |Slower   |Very accurate (minimum missed ports)       |~2 hours     |
|3.	      |Faster   |Accurate (missed ports not *impossible*)   |~15+ minutes |
|4.	      |Fastest  |Accurate-ish (may miss ports)              |A few seconds|

</div>

The default scan speed is option #3, and provides a fairly accurate result while being fast. However, for specific use cases, a slower or faster scan could be required.

## Optimization
Multithreading was implemented in this program to create a dedicated software thread for each socket to connect to a dedicated port of the specified target. All these sockets/threads are briefly created, then connected to their individual dedicated ports concurrently to maximize the scan rate, and then correctly terminated upon completion of execution.

## Note
PortNinja does *not* perform a stealthy scan, that is, it works on the basis of establishing the *complete* three-way handshake instead of just sending a SYN flagged packet followed by the RST flagged packet (as it would in a SYN scan). PortNinja terminates each connection with its individual port properly by the time that individual port has been scanned; but this in itself does not by any means dictate that the target will not be aware of all these sudden connection attempts through all of its ports that are being "scanned" by PortNinja.

## Dependencies to PIP-Install
- **requests** (for automatic update checks)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
