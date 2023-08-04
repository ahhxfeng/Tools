#!/bin/sh

# script for start arweave localnet
# use think to start service 
# start the arweave localnet with supervisor which can auto
# restart arweave when it crash

#for test 
now=$(date +"%T")



cd /home/think
echo "this script has exec at $now" >> start_with_supervisor.log
cd /home/think/work/arlocalnet/_build/localnet/rel/arweave
./bin/start config_file config.json storage_module 0,dWL9LfeZ747JF_WDOMDsgStia_gwhgjpr3fsLCXhGgE 2>&1 >/dev/null  &

exit 0
