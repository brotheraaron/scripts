#!/bin/bash

# Set variables for Azure resources
rgName=
vnetName=
subnetName=
subnetCidr=$(az network vnet subnet show -g $rgName -n $subnetName --vnet-name $vnetName | jq -r '.addressPrefix')

# Get starting IP, ending IP and total number of IPs in subnet IP range
firstHost=$(curl -Ss subnet.im/$subnetCidr | jq -r .firsthost)
lastHost=$(curl -Ss subnet.im/$subnetCidr | jq -r .lasthost)
totalHost=$(curl -Ss subnet.im/$subnetCidr | jq -r .totalhosts)

# initialize iterator to zero
i=0

# Hacky way to get IPs in variables so the for loop can iterate over them
a1=$(echo $firstHost | tr '.' '\t' | awk '{print $1}')
b1=$(echo $firstHost | tr '.' '\t' | awk '{print $2}')
c1=$(echo $firstHost | tr '.' '\t' | awk '{print $3}')
d1=$(echo $firstHost | tr '.' '\t' | awk '{print $4}')
a2=$(echo $lastHost | tr '.' '\t' | awk '{print $1}')
b2=$(echo $lastHost | tr '.' '\t' | awk '{print $2}')
c2=$(echo $lastHost | tr '.' '\t' | awk '{print $3}')
d2=$(echo $lastHost | tr '.' '\t' | awk '{print $4}')

# For loop will print n of total <tab> IP <tab> what owns the IP for all the IPs in the subnet range
for ip in $(eval echo "$a1.{$b1..$b2}.{$c1..$c2}.{$d1..$d2}"); do ((i = i + 1)); printf "$i of $totalHost \t $ip \t"; az network vnet check-ip-address --resource-group $RgName --name $vnetName --ip-address $ip | jq -r '.inUseWithResource'; done

# TODO
# Validate nulls are true nulls
# Count nulls to report total number of free IPs
# Prompt user for RgName and vnetName so they don't have to edit script by hand
# Maybe put some error checking and failure outputs. For example if you do something crazy like run this loop against a /8 it will crash the cloud shell.
# Maybe output to a file

# This code is best effort and does not come with any warranty explicit or implied.
