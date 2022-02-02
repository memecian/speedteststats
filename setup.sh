#!/bin/sh
# TODO: finish and test on linux!!!!!
shopt -s extglob
# script to setup speedteststats as a cron job
echo "Setting up SpeedtestStats."
ARCH=`lscpu | head -n 1`
echo $ARCH
case $ARCH in
	@(x86_64))
		ARCHDL="x86_64"
		;;
	@(i386))
		ARCHDL="i386"
		;;
	@(armel))
		ARCHDL="armel"
		;;
	@(armhf))
		ARCHDL="armhf"
		;;
	@(aarch))
		ARCHDL="aarch"
		;;
	*)
esac
# remove after completion
echo $ARCHDL

# add CPU Architecture as an environment variable

# download speedtest according to architecture
printf "https://install.speedtest.net/app/cli/ookla-speedtest-1.1.1-linux-%s.tgz" $ARCHDL

