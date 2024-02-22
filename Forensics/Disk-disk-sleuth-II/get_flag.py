instr="( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )( 3 ) ( _ ) ( 0 ) ( b ) ( a ) ( 8 ) ( d ) ( 0 ) ( 2 ) ( d ) ( } )"
outstr=""
for i in instr: 
    if i not in " ()": 
        outstr+=i
print(outstr)


