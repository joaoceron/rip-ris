usage: rip-ris.py [options]

<pre>
optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print version and exit
  -d, --debug           print debug info
  -p [PREFIX], --prefix [PREFIX]
                        prefix to be searched on the system. Ex.:
                        194.0.28.53/24
  -t [TIMESTAMP], --timestamp [TIMESTAMP]
                        timestamp used in the search. Ex.: 1579686913
  --csv                 print output in CSV format

</pre>

## Examples:
<pre>
  # get the last prefix visibility on the system
  ./rip-ris.py -p 194.0.28.53/24  
  # get prefix visibility in that particular timestamp
  ./rip-ris.py -p 194.0.28.53/24 -t 1579686913 
  </pre>
  Output:
         peer      collector                                        as_path                                                                                                                                                                                                                                                             community
0    328474       AMS-RIPE                   [328474, 6939, 55195, 48283]                                                                                                                                                                                                                                                                    []
1    131477       AMS-RIPE                         [131477, 55195, 48283]                                                                                                                                                                                                                                                         [19996:19996]
2     55720       AMS-RIPE                    [55720, 4637, 55195, 48283]                                                                                                                                                                                                                                                                    []
3     34854       AMS-RIPE                    [34854, 6939, 55195, 48283]                                                                                                                                                                                                                                            [34854:11000, 34854:11010]
4      7018       AMS-RIPE                     [7018, 6939, 55195, 48283]                                                                                                                                                                                                                                               [7018:5000, 7018:37232]
5       174       AMS-RIPE          [174, 1299, 6939, 6939, 55195, 48283]                                                                                                                                                                                                                                                                    []
