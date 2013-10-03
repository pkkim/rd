filename=$1
to_replace=$2

while [ $# -gt 2 ]
do
		sed -ie "0,/${to_replace}/{s/${to_replace}/${3}/}" $filename
		shift
done