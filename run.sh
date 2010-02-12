#!/bin/bash

mydir="$(dirname "$0")"

add_pypath()
{
    if [ -n "$PYTHONPATH" ];then
        PYTHONPATH="$1:$PYTHONPATH"
    else
        PYTHONPATH="$1"
    fi
}

add_pypath "$mydir"
export PYTHONPATH
"$mydir/bin/faketw-server" "$@"

