# Benchmarks

This repository benchmarks Gramex vs FastAPI on MongoDB querying.

Summary:

- Gramex: 77 requests/second
- FastAPI: 39 requests/second

Test setup

1. Create a MongoDB database called `testdatabase` with a collection `testcollection`
2. Upload [admission.csv](admission.csv) into it
3. Install Apache Benchmark

## Gramex benchmarks

Install and run `gramex`. Then run Apache Benchmark

```bash
ab -n 1000 -c 10 http://127.0.0.1:9988/mongo
```

Results: **77 requests/second** (Gramex 1.70)

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


Server Software:        Gramex/1.70.0
Server Hostname:        127.0.0.1
Server Port:            9988

Document Path:          /mongo
Document Length:        88040 bytes

Concurrency Level:      10
Time taken for tests:   12.980 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      88247000 bytes
HTML transferred:       88040000 bytes
Requests per second:    77.04 [#/sec] (mean)
Time per request:       129.803 [ms] (mean)
Time per request:       12.980 [ms] (mean, across all concurrent requests)
Transfer rate:          6639.21 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       1
Processing:    14  129  18.6    126     227
Waiting:       13  129  18.8    125     226
Total:         14  129  18.6    126     227

Percentage of the requests served within a certain time (ms)
  50%    126
  66%    130
  75%    135
  80%    140
  90%    154
  95%    162
  98%    179
  99%    193
 100%    227 (longest request)
```


## FastAPI benchmarks

Install and run FastAPI:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then run Apache Benchmark:

```bash
ab -n 1000 -c 10 http://127.0.0.1:9988/mongo
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

Document Path:          /mongo
Document Length:        88040 bytes

Concurrency Level:      10
Time taken for tests:   25.924 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      88187000 bytes
HTML transferred:       88040000 bytes
Requests per second:    38.57 [#/sec] (mean)
Time per request:       259.241 [ms] (mean)
Time per request:       25.924 [ms] (mean, across all concurrent requests)
Transfer rate:          3322.01 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       1
Processing:    31  258  16.4    256     303
Waiting:       29  214  45.0    228     303
Total:         31  258  16.4    256     303

Percentage of the requests served within a certain time (ms)
  50%    256
  66%    260
  75%    263
  80%    265
  90%    274
  95%    279
  98%    283
  99%    285
 100%    303 (longest request)
```
