#!/bin/bash #03/02/2022/alejandroperezm
grep -v '>' sequence.fasta |wc| awk '{print $3-$1}'


