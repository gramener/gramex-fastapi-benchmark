# Benchmarks

This repository benchmarks Gramex vs FastAPI on MongoDB querying.

Summary:

| Server  | <100 KB data        | 3 GB data             |
|---------|---------------------|-----------------------|
| Gramex  | 75 requests/second  | 0.08 requests/second  |
| FastAPI | 43 requests/second  | 0.08 requests/second  |

System specs:

- Processor: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
- RAM: 16GB
- Storage: 1TB
- Network adapter: Intel(R) Wireless-AC 9560 160MHz

Test setup

1. Create a MongoDB database called `testdatabase` with a collection `testcollection`
2. Upload [admission.csv](admission.csv) into it
3. Also create a MongoDB collection `imdbtitles`
4. Downlod the [IMDb dataset title.principals.tsv.gz](https://datasets.imdbws.com/title.principals.tsv.gz), unzip it, and upload it
5. Install Apache Benchmark

## Gramex benchmarks

Install and run `gramex`. Then run Apache Benchmark

```bash
ab -n 1000 -c 10 http://127.0.0.1:9988/admission
```

Results: **75 requests/second** (Gramex 1.71)

```text
This is ApacheBench, Version 2.3 <$Revision: 1874286 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Gramex/1.71.0
Server Hostname:        127.0.0.1
Server Port:            9988

Document Path:          /admission
Document Length:        88040 bytes

Concurrency Level:      10
Time taken for tests:   13.352 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      88247000 bytes
HTML transferred:       88040000 bytes
Requests per second:    74.90 [#/sec] (mean)
Time per request:       133.519 [ms] (mean)
Time per request:       13.352 [ms] (mean, across all concurrent requests)
Transfer rate:          6454.40 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       1
Processing:    14  133  25.0    130     268
Waiting:       11  132  25.4    130     267
Total:         14  133  25.0    130     268

Percentage of the requests served within a certain time (ms)
  50%    130
  66%    137
  75%    144
  80%    147
  90%    163
  95%    171
  98%    196
  99%    228
 100%    268 (longest request)
```

Next, run this:

```bash
ab -n 1 -c 1 http://127.0.0.1:9988/imdb?nconst=nm0068609
```

Results: **0.08 requests/second** (Gramex 1.71)

```text
This is ApacheBench, Version 2.3 <$Revision: 1874286 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Gramex/1.71.0
Server Hostname:        127.0.0.1
Server Port:            9988

Document Path:          /imdb?nconst=nm0068609
Document Length:        321 bytes

Concurrency Level:      1
Time taken for tests:   13.331 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      526 bytes
HTML transferred:       321 bytes
Requests per second:    0.08 [#/sec] (mean)
Time per request:       13331.325 [ms] (mean)
Time per request:       13331.325 [ms] (mean, across all concurrent requests)
Transfer rate:          0.04 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing: 13330 13330   0.0  13330   13330
Waiting:    13330 13330   0.0  13330   13330
Total:      13330 13330   0.0  13330   13330
```


## FastAPI benchmarks

Install and run FastAPI:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then run Apache Benchmark:

```bash
ab -n 1000 -c 10 http://127.0.0.1:8000/admission
```

Results: **39 requests/second** (fastapi: 0.66, uvicorn: 0.14)

```text
This is ApacheBench, Version 2.3 <$Revision: 1874286 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        uvicorn
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /admission
Document Length:        88040 bytes

Concurrency Level:      10
Time taken for tests:   23.240 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      88187000 bytes
HTML transferred:       88040000 bytes
Requests per second:    43.03 [#/sec] (mean)
Time per request:       232.400 [ms] (mean)
Time per request:       23.240 [ms] (mean, across all concurrent requests)
Transfer rate:          3705.68 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       1
Processing:    25  231  15.5    230     274
Waiting:       24  190  40.0    201     273
Total:         25  231  15.5    230     274

Percentage of the requests served within a certain time (ms)
  50%    230
  66%    234
  75%    236
  80%    238
  90%    244
  95%    248
  98%    252
  99%    260
 100%    274 (longest request)
```

Next, run this:

```bash
ab -n 1 -c 1 http://127.0.0.1:8000/imdb?nconst=nm0068609
```

Results: **0.08 requests/second** (fastapi: 0.66, uvicorn: 0.14)

```text
This is ApacheBench, Version 2.3 <$Revision: 1874286 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        uvicorn
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /imdb?nconst=nm0068609
Document Length:        321 bytes

Concurrency Level:      1
Time taken for tests:   13.280 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      466 bytes
HTML transferred:       321 bytes
Requests per second:    0.08 [#/sec] (mean)
Time per request:       13279.558 [ms] (mean)
Time per request:       13279.558 [ms] (mean, across all concurrent requests)
Transfer rate:          0.03 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing: 13279 13279   0.0  13279   13279
Waiting:    13279 13279   0.0  13279   13279
Total:      13279 13279   0.0  13279   13279
```
