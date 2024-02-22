#!/bin/bash

strings network-dump.flag.pcap | grep "p i c o"| tr -d ' '

