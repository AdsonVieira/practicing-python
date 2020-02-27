<?php
function fat($n){
    return ($n > 0) ? $n * fat($n - 1) :1 ;
}
echo fat(170)."\n";