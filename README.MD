# PortNinja: Open Ports Finder

## Description & Usage
A fast multithreaded ports scanner that scans for all open listening ports on the specified target server in the ports range 0 – 65535.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/PortNinja-Open-Ports-Finder/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, for security research purposes.

## Optimization
Multithreading was implemented in this program to create a dedicated software thread for each socket to connect to a dedicated port of the specified target (i.e. 65,536 threads/sockets are briefly created). All these created sockets/threads connect to their individual dedicated ports concurrently; maximizing an optimal scan rate.

## Dependencies to PIP-Install
- **requests** (for automatic update checks)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
