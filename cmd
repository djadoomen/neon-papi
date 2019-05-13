#!/bin/sh

if [[ $# == 0 ]] || [[ "$1" != -?* ]]; then
  echo -e "usage: ./run {<OPTION> | (OPTIONS)}\n\t- requires at least one option.\n\n\
example: ./run -bp\n\n\
OPTIONS:\n-b\tdocker build\n-p\tdocker push\n-q\tdocker pull\n\n";
	exit 1;
fi

for char in "${1:1}"; do
  case "$char" in
    b)
      docker build --force-rm -t valentinorban/neon:papi .;;
    p)
      docker push valentinorban/neon:papi;;
    q)
      docker pull valentinorban/neon:papi;;
  esac
done
