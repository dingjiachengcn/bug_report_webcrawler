# 将你的时间数据复制到这个长字符串中，每个时间数据占一行
data = """
2 days, 23:43:00
1 day, 13:26:00
1 day, 23:29:00
6 days, 14:35:00
1 day, 13:53:00
5 days, 9:11:00
4 days, 22:27:00
11 days, 10:51:00
3 days, 23:55:00
17 days, 4:20:00
31 days, 7:34:00
18 days, 6:35:00
12 days, 12:06:00
4 days, 23:35:00
63 days, 1:51:00
8 days, 2:42:00
25 days, 10:34:00
3 days, 1:47:00
11 days, 2:37:00
1 day, 8:29:00
4 days, 4:05:00
10 days, 9:24:00
3 days, 3:03:00
7 days, 5:20:00
8 days, 6:55:00
1 day, 20:14:00
6 days, 1:08:00
7 days, 8:30:00
7 days, 2:01:00
8 days, 2:42:00
16 days, 10:54:00
11 days, 0:04:00
11 days, 0:57:00
5 days, 11:41:00
5 days, 4:50:00
6 days, 3:32:00
5 days, 17:04:00
2 days, 18:07:00
12 days, 13:46:00
6 days, 14:27:00
15 days, 4:18:00
16 days, 16:52:00
26 days, 2:09:00
9 days, 11:40:00
4 days, 11:35:00
21 days, 17:21:00
27 days, 1:24:00
5 days, 7:31:00
3 days, 6:31:00
20 days, 9:12:00
18 days, 1:19:00
30 days, 3:11:00
22 days, 9:53:00
22 days, 9:41:00
4 days, 3:57:00
101 days, 9:43:00
27 days, 14:44:00
12 days, 1:56:00
16 days, 5:22:00
16 days, 1:34:00
1 day, 12:02:00
1068 days, 17:17:00
11 days, 15:13:00
1 day, 19:06:00
3 days, 6:04:00
6 days, 8:04:00
2 days, 19:20:00
13 days, 5:56:00
13 days, 6:09:00
13 days, 6:38:00
7 days, 19:52:00
17 days, 7:04:00
5 days, 2:19:00
9 days, 4:15:00
39 days, 11:45:00
9 days, 6:38:00
9 days, 13:07:00
18 days, 10:25:00
17 days, 11:32:00
3 days, 16:03:00
3 days, 19:44:00
4 days, 20:28:00
6 days, 5:05:00
0:20:00
16 days, 14:06:00
8 days, 8:36:00
8 days, 3:06:00
43 days, 10:11:00
25 days, 21:09:00
18 days, 2:52:00
6 days, 11:41:00
11 days, 19:00:00
14 days, 17:00:00
13 days, 17:00:00
15:16:00
46 days, 3:58:00
15 days, 7:30:00
8 days, 14:37:00
12 days, 9:11:00
4 days, 14:02:00
16 days, 14:38:00
27 days, 4:13:00
48 days, 5:46:00
17 days, 6:41:00
18 days, 1:36:00
11 days, 19:04:00
11 days, 10:07:00
33 days, 8:43:00
13 days, 2:46:00
50 days, 20:24:00
27 days, 1:53:00
9 days, 7:25:00
8 days, 4:10:00
29 days, 10:26:00
11 days, 13:05:00
89 days, 20:34:00
12 days, 3:18:00
10 days, 5:46:00
32 days, 23:52:00
12 days, 11:54:00
11 days, 6:12:00
28 days, 10:04:00
3 days, 21:32:00
15 days, 1:32:00
9 days, 2:02:00
1 day, 15:43:00
16 days, 8:42:00
17 days, 13:05:00
10 days, 18:49:00
8 days, 20:59:00
24 days, 1:22:00
10 days, 22:23:00
58 days, 8:02:00
3 days, 1:26:00
7 days, 10:08:00
4 days, 6:44:00
19 days, 11:53:00
1 day, 12:24:00
17 days, 12:57:00
2 days, 17:30:00
3 days, 5:08:00
10 days, 14:18:00
6 days, 3:04:00
6 days, 5:14:00
30 days, 6:49:00
4 days, 10:11:00
5 days, 4:29:00
6 days, 4:06:00
26 days, 9:38:00
19 days, 9:05:00
1 day, 12:28:00
22 days, 8:41:00
6 days, 19:49:00
36 days, 0:57:00
23 days, 19:48:00
66 days, 0:00:00
7 days, 8:24:00
7 days, 8:46:00
62 days, 13:49:00
29 days, 2:47:00
7 days, 8:31:00
8 days, 8:11:00
4 days, 12:43:00
5 days, 9:47:00
86 days, 13:04:00
53 days, 8:45:00
2 days, 18:03:00
32 days, 4:24:00
4 days, 8:58:00
1 day, 8:59:00
12 days, 3:35:00
1 day, 9:05:00
5 days, 15:00:00
2 days, 6:05:00
15 days, 13:03:00
90 days, 11:52:00
90 days, 11:53:00
29 days, 19:51:00
183 days, 19:01:00
4 days, 10:03:00
56 days, 3:55:00
5 days, 11:40:00
13 days, 13:27:00
20 days, 2:47:00
4 days, 11:10:00
121 days, 19:21:00
3 days, 5:23:00
3 days, 14:49:00
2 days, 19:18:00
8 days, 10:11:00
40 days, 13:26:00
5 days, 14:11:00
5 days, 12:16:00
4 days, 17:32:00
9 days, 7:08:00
1 day, 4:35:00
35 days, 4:08:00
2 days, 7:44:00
3 days, 19:28:00
11 days, 14:57:00
15 days, 15:05:00
60 days, 15:37:00
8 days, 16:06:00
3 days, 9:45:00
3 days, 10:20:00
3 days, 12:12:00
11 days, 14:21:00
21 days, 2:32:00
82 days, 4:59:00
4 days, 18:15:00
19 days, 15:08:00
20 days, 14:43:00
5 days, 14:15:00
20 days, 15:09:00
3 days, 7:16:00
36 days, 9:01:00
1 day, 15:30:00
2 days, 22:16:00
9 days, 6:13:00
2 days, 10:42:00
15 days, 19:29:00
121 days, 19:21:00
4 days, 6:31:00
10 days, 0:43:00
17 days, 15:52:00
6 days, 16:09:00
5 days, 12:16:00
112 days, 4:26:00
8 days, 15:47:00
19 days, 17:17:00
27 days, 2:22:00
20 days, 0:28:00
6 days, 2:43:00
4 days, 6:25:00
3 days, 7:01:00
3 days, 11:33:00
20 days, 18:50:00
10 days, 4:09:00
10 days, 7:48:00
19 days, 8:27:00
5 days, 8:48:00
1 day, 1:44:00
1 day, 8:44:00
35 days, 17:53:00
55 days, 19:27:00
77 days, 13:44:00
1 day, 10:00:00
7 days, 0:33:00
31 days, 2:36:00
28 days, 11:00:00
51 days, 5:57:00
10 days, 17:30:00
11 days, 7:22:00
4 days, 6:21:00
12 days, 18:01:00
4 days, 10:08:00
21 days, 21:16:00
64 days, 3:49:00
54 days, 21:31:00
19:59:00
12 days, 11:14:00
19 days, 7:18:00
5 days, 14:50:00
28 days, 16:49:00
59 days, 2:15:00
42 days, 3:52:00
8 days, 8:38:00
7 days, 9:28:00
86 days, 12:51:00
42 days, 14:00:00
126 days, 7:39:00
45 days, 5:36:00
4 days, 3:26:00
10 days, 4:41:00
20 days, 14:36:00
5 days, 16:47:00
18 days, 23:57:00
35 days, 15:00:00
37 days, 23:41:00
31 days, 4:45:00
50 days, 12:10:00
3 days, 18:16:00
17 days, 12:14:00
18 days, 22:38:00
2 days, 4:59:00
109 days, 21:49:00
45 days, 3:10:00
3 days, 4:57:00
4 days, 13:47:00
8 days, 4:02:00
70 days, 8:31:00
15 days, 14:17:00
21:40:00
56 days, 10:43:00
41 days, 13:09:00
41 days, 19:47:00
4 days, 8:29:00
7 days, 14:30:00
1 day, 22:56:00
5 days, 8:37:00
8 days, 7:48:00
73 days, 5:39:00
6 days, 18:46:00
13 days, 16:28:00
126 days, 11:23:00
3 days, 10:13:00
57 days, 14:28:00
121 days, 22:09:00
47 days, 12:34:00
20 days, 6:55:00
4 days, 15:12:00
12 days, 15:05:00
12 days, 19:44:00
14 days, 10:36:00
3 days, 9:30:00
89 days, 13:59:00
137 days, 22:31:00
78 days, 3:10:00
1 day, 13:09:00
1 day, 14:13:00
9 days, 20:43:00
52 days, 15:09:00
11 days, 21:53:00
10 days, 10:31:00
7 days, 13:58:00
33 days, 13:37:00
3 days, 18:18:00
112 days, 7:56:00
13 days, 11:06:00
2 days, 14:19:00
8 days, 15:56:00
9 days, 10:53:00
7 days, 15:35:00
3 days, 8:41:00
24 days, 11:49:00
30 days, 8:44:00
17 days, 9:30:00
13 days, 8:26:00
12 days, 10:34:00
12 days, 3:41:00
13 days, 15:31:00
124 days, 16:20:00
146 days, 0:46:00
6 days, 13:51:00
83 days, 6:24:00
6 days, 14:09:00
10 days, 12:48:00
26 days, 5:29:00
19 days, 0:20:00
12 days, 0:15:00
38 days, 15:45:00
6 days, 10:36:00
4 days, 1:27:00
11 days, 6:39:00
18 days, 15:28:00
49 days, 12:33:00
43 days, 12:35:00
49 days, 14:26:00
56 days, 14:29:00
138 days, 9:47:00
28 days, 16:08:00
113 days, 2:07:00
62 days, 9:34:00
28 days, 16:34:00
29 days, 9:08:00
23 days, 17:16:00
38 days, 13:29:00
3 days, 5:49:00
36 days, 14:05:00
5 days, 15:17:00
3 days, 12:18:00
80 days, 5:34:00
55 days, 11:27:00
5 days, 3:27:00
1 day, 14:12:00
1 day, 14:12:00
1 day, 23:40:00
167 days, 0:17:00
5 days, 7:28:00
13 days, 1:15:00
106 days, 0:17:00
92 days, 0:17:00
29 days, 21:27:00
11 days, 22:57:00
133 days, 0:17:00
166 days, 0:15:00
58 days, 2:44:00
45 days, 3:10:00
12:15:00
9:06:00
2 days, 12:01:00
3 days, 15:05:00
34 days, 4:20:00
33 days, 11:02:00
7 days, 12:49:00
4 days, 21:40:00
78 days, 3:17:00
1 day, 7:01:00
162 days, 3:31:00
68 days, 21:27:00
36 days, 0:58:00
64 days, 16:36:00
176 days, 15:35:00
38 days, 9:13:00
5 days, 13:22:00
4 days, 19:22:00
7 days, 6:17:00
14 days, 11:57:00
7 days, 4:00:00
7 days, 10:55:00
96 days, 16:12:00
1 day, 8:43:00
9 days, 3:09:00
10 days, 3:33:00
14 days, 7:24:00
7 days, 18:43:00
8 days, 6:36:00
5 days, 17:34:00
11 days, 4:05:00
11 days, 4:07:00
11 days, 4:08:00
5 days, 4:09:00
11 days, 4:10:00
62 days, 10:47:00
33 days, 4:46:00
14 days, 23:44:00
5 days, 0:45:00
111 days, 5:49:00
6 days, 7:18:00
5 days, 11:02:00
54 days, 21:31:00
18 days, 7:05:00
2 days, 9:35:00
18 days, 7:39:00
3 days, 11:10:00
1 day, 14:27:00
85 days, 16:38:00
15 days, 4:53:00
1 day, 9:54:00
2 days, 12:43:00
6 days, 19:04:00
8 days, 23:26:00
2 days, 5:46:00
7 days, 6:26:00
15 days, 6:04:00
18 days, 0:24:00
2 days, 7:33:00
57 days, 18:08:00
9 days, 22:37:00
172 days, 3:28:00
11 days, 4:22:00
5 days, 8:00:00
117 days, 11:27:00
5 days, 12:01:00
7 days, 21:04:00
20 days, 20:44:00
8 days, 4:28:00
1 day, 5:57:00
13 days, 13:09:00
27 days, 16:39:00
1 day, 9:06:00
2 days, 3:36:00
9 days, 1:47:00
10 days, 11:43:00
4 days, 0:14:00
1 day, 5:45:00
8 days, 2:09:00
5 days, 14:41:00
2 days, 4:19:00
21 days, 4:41:00
43 days, 9:17:00
9 days, 3:47:00
7 days, 12:51:00
2 days, 1:40:00
1 day, 22:11:00
1 day, 13:26:00
135 days, 3:09:00
4 days, 9:56:00
82 days, 19:50:00
20 days, 16:43:00
21 days, 0:02:00
78 days, 7:05:00
149 days, 16:46:00
15 days, 0:45:00
43 days, 2:31:00
3 days, 8:39:00
5 days, 23:31:00
5 days, 10:14:00
66 days, 18:24:00
23 days, 23:42:00
40 days, 2:20:00
13 days, 2:19:00
6 days, 22:55:00
3 days, 7:45:00
2 days, 21:21:00
17 days, 1:45:00
11 days, 3:15:00
9 days, 7:31:00
9 days, 14:16:00
5 days, 14:20:00
58 days, 3:43:00
21 days, 5:04:00
27 days, 1:24:00
217 days, 17:47:00
57 days, 0:37:00
13 days, 17:42:00
2 days, 14:27:00
1 day, 20:05:00
31 days, 0:43:00
6 days, 6:05:00
6 days, 5:16:00
23 days, 19:12:00
17 days, 9:50:00
230 days, 21:37:00
49 days, 22:20:00
5 days, 3:56:00
8 days, 0:53:00
17:05:00
44 days, 4:26:00
24 days, 13:55:00
3 days, 6:02:00
187 days, 16:21:00
11 days, 15:50:00
2 days, 3:08:00
7 days, 3:57:00
6 days, 3:34:00
16:04:00
15 days, 0:58:00
31 days, 3:02:00
14 days, 7:22:00
73 days, 2:47:00
2 days, 6:56:00
4 days, 4:01:00
131 days, 8:40:00
20 days, 22:24:00
18 days, 22:55:00
11 days, 2:39:00
6 days, 6:30:00
40 days, 14:23:00
119 days, 1:35:00
4 days, 7:21:00
20 days, 4:29:00
8 days, 1:26:00
14 days, 10:17:00
7 days, 10:32:00
19:51:00
43 days, 20:37:00
4 days, 12:13:00
125 days, 11:13:00
43 days, 19:36:00
194 days, 19:17:00
21 days, 9:56:00
243 days, 14:41:00
63 days, 18:38:00
13 days, 4:48:00
13 days, 6:01:00
68 days, 21:27:00
14 days, 13:57:00
68 days, 3:16:00
7 days, 14:45:00
16:14:00
1 day, 19:50:00
20 days, 6:15:00
5 days, 12:05:00
102 days, 5:49:00
3 days, 5:53:00
67 days, 3:30:00
14 days, 2:07:00
2 days, 3:07:00
7 days, 23:28:00
1 day, 8:44:00
56 days, 10:43:00
2 days, 20:01:00
36 days, 20:55:00
3 days, 20:54:00
16 days, 4:30:00
4 days, 19:26:00
2 days, 21:05:00
5 days, 3:20:00
53 days, 16:29:00
3 days, 7:57:00
50 days, 21:59:00
40 days, 0:24:00
47 days, 1:34:00
17 days, 2:50:00
9 days, 6:44:00
12 days, 5:25:00
8 days, 9:01:00
6 days, 14:19:00
30 days, 12:07:00
37 days, 19:28:00
2 days, 23:47:00
267 days, 5:12:00
6 days, 3:45:00
179 days, 4:19:00
3 days, 9:09:00
25 days, 19:17:00
42 days, 21:18:00
230 days, 22:29:00
18 days, 2:56:00
61 days, 4:22:00
115 days, 15:06:00
179 days, 15:29:00
34 days, 3:19:00
5 days, 8:41:00
5 days, 20:38:00
121 days, 19:21:00
1 day, 2:27:00
177 days, 1:47:00
5 days, 13:14:00
31 days, 6:46:00
7 days, 5:34:00
49 days, 9:33:00
7 days, 14:27:00
5 days, 11:34:00
14 days, 10:01:00
22 days, 6:36:00
4 days, 2:54:00
181 days, 1:16:00
10 days, 14:02:00
94 days, 12:25:00
22 days, 5:40:00
5 days, 6:33:00
14 days, 14:40:00
27 days, 20:29:00
2 days, 1:30:00
5 days, 5:15:00
2 days, 5:20:00
18 days, 10:36:00
34 days, 12:25:00
54 days, 0:09:00
4 days, 1:03:00
9 days, 5:16:00
8 days, 6:36:00
103 days, 1:20:00
12 days, 7:00:00
3 days, 18:18:00
54 days, 0:25:00
5 days, 5:15:00
89 days, 9:58:00
3 days, 0:36:00
77 days, 17:07:00
69 days, 1:48:00
1 day, 4:52:00
6 days, 3:51:00
134 days, 18:04:00
17 days, 0:39:00
74 days, 1:22:00
4 days, 4:34:00
198 days, 6:52:00
59 days, 7:33:00
13 days, 7:37:00
60 days, 16:48:00
20 days, 20:44:00
4 days, 5:54:00
3 days, 13:18:00
2 days, 1:26:00
63 days, 6:15:00
2 days, 10:30:00
348 days, 12:53:00
2 days, 8:10:00
7 days, 9:37:00
23 days, 9:40:00
6 days, 10:17:00
1 day, 16:13:00
4 days, 9:16:00
8 days, 11:08:00
3 days, 0:54:00
199 days, 12:25:00
26 days, 12:54:00
11 days, 6:30:00
230 days, 13:25:00
108 days, 12:27:00
78 days, 16:44:00
7 days, 13:19:00
88 days, 3:56:00
10 days, 8:21:00
3 days, 9:50:00
38 days, 12:34:00
58 days, 1:59:00
3 days, 11:29:00
20 days, 12:16:00
20 days, 16:28:00
21 days, 17:37:00
33 days, 22:17:00
8 days, 0:36:00
34 days, 3:23:00
26 days, 4:06:00
28 days, 12:34:00
36 days, 8:57:00
36 days, 5:13:00
15 days, 11:41:00
10 days, 17:18:00
62 days, 18:02:00
9 days, 2:40:00
16 days, 14:51:00
4 days, 9:21:00
49 days, 5:29:00
4 days, 22:07:00
21 days, 2:11:00
22 days, 15:38:00
32 days, 7:08:00
7 days, 6:14:00
22 days, 9:42:00
1 day, 7:24:00
21 days, 2:14:00
7 days, 3:26:00
7 days, 22:54:00
7 days, 2:20:00
8 days, 6:41:00
31 days, 10:57:00
24 days, 2:18:00
2 days, 4:27:00
15 days, 21:45:00
18 days, 22:48:00
19 days, 7:41:00
23:24:00
51 days, 21:29:00
53 days, 20:18:00
4 days, 10:47:00
1 day, 19:29:00
3 days, 2:13:00
95 days, 14:37:00
4 days, 18:19:00
33 days, 2:17:00
11 days, 14:42:00
2 days, 6:36:00
33 days, 21:58:00
21 days, 15:36:00
35 days, 7:50:00
1 day, 23:07:00
4 days, 10:49:00
11 days, 18:46:00
12 days, 13:48:00
67 days, 14:22:00
26 days, 23:43:00
13 days, 21:46:00
10 days, 0:19:00
45 days, 3:41:00
19 days, 23:52:00
28 days, 6:22:00
135 days, 15:10:00
2 days, 2:23:00
120 days, 8:16:00
6 days, 6:48:00
16 days, 8:18:00
18 days, 0:01:00
25 days, 13:19:00
98 days, 14:41:00
8 days, 2:31:00
10 days, 12:15:00
20 days, 18:09:00
170 days, 10:21:00
1 day, 3:58:00
28 days, 6:30:00
1 day, 1:29:00
3 days, 18:06:00
3 days, 0:52:00
2 days, 6:33:00
57 days, 7:19:00
2 days, 8:27:00
20:04:00
132 days, 8:29:00
2 days, 5:11:00
29 days, 14:30:00
11 days, 16:19:00
30 days, 2:18:00
2 days, 4:32:00
129 days, 0:42:00
54 days, 8:21:00
6 days, 3:49:00
3 days, 19:43:00
10 days, 14:31:00
40 days, 15:54:00
3 days, 23:47:00
14 days, 22:00:00
85 days, 7:17:00
110 days, 14:26:00
2 days, 13:07:00
55 days, 3:50:00
19 days, 12:58:00
17 days, 17:14:00
258 days, 2:03:00
13 days, 9:15:00
1 day, 13:53:00
27 days, 17:14:00
4 days, 23:59:00
14 days, 2:27:00
101 days, 7:25:00
16 days, 9:29:00
134 days, 12:14:00
25 days, 13:30:00
19 days, 15:46:00
12 days, 17:24:00
3 days, 4:44:00
4 days, 11:09:00
2 days, 12:40:00
137 days, 2:37:00
26 days, 13:06:00
87 days, 17:30:00
76 days, 9:48:00
2 days, 18:00:00
96 days, 5:45:00
57 days, 0:14:00
8 days, 9:13:00
40 days, 17:03:00
133 days, 14:14:00
2 days, 22:55:00
15 days, 21:00:00
43 days, 22:47:00
44 days, 0:29:00
6 days, 2:08:00
10 days, 12:05:00
87 days, 13:10:00
52 days, 1:46:00
12 days, 22:18:00
86 days, 0:23:00
15 days, 18:56:00
30 days, 13:07:00
11 days, 18:18:00
63 days, 21:29:00
7 days, 1:55:00
223 days, 5:08:00
65 days, 16:38:00
428 days, 8:07:00
22 days, 10:43:00
16 days, 3:47:00
2 days, 0:08:00
15 days, 9:12:00
11 days, 10:10:00
1 day, 13:43:00
19 days, 11:24:00
5 days, 5:59:00
97 days, 6:02:00
5 days, 11:05:00
5 days, 23:34:00
15 days, 2:21:00
15 days, 23:46:00
6 days, 3:47:00
12 days, 20:27:00
1 day, 5:12:00
7 days, 9:33:00
39 days, 13:21:00
11 days, 2:57:00
12 days, 14:59:00
35 days, 20:54:00
6 days, 11:48:00
299 days, 15:00:00
21 days, 17:20:00
20 days, 19:34:00
6 days, 0:39:00
29 days, 1:21:00
34 days, 19:24:00
52 days, 1:47:00
10 days, 18:13:00
3 days, 13:18:00
13 days, 0:35:00
324 days, 6:02:00
28 days, 19:39:00
93 days, 20:01:00
87 days, 1:26:00
108 days, 2:53:00
63 days, 7:24:00
9 days, 23:01:00
3 days, 2:50:00
149 days, 17:36:00
54 days, 18:15:00
87 days, 7:53:00
3 days, 3:34:00
10 days, 2:51:00
8 days, 0:13:00
323 days, 14:33:00
365 days, 23:10:00
29 days, 5:31:00
11 days, 1:33:00
8 days, 6:10:00
6 days, 5:36:00
8 days, 3:45:00
86 days, 4:19:00
8 days, 5:36:00
23 days, 8:47:00
116 days, 11:11:00
3 days, 7:07:00
9 days, 7:46:00
22 days, 20:10:00
16 days, 10:26:00
4 days, 14:07:00
6 days, 5:43:00
46 days, 0:33:00
32 days, 18:42:00
26 days, 0:15:00
20 days, 3:53:00
56 days, 9:07:00
28 days, 12:40:00
28 days, 21:16:00
153 days, 22:00:00
6 days, 18:44:00
7 days, 21:22:00
2 days, 12:26:00
8 days, 9:45:00
3 days, 11:49:00
7 days, 14:13:00
1 day, 20:03:00
3 days, 2:11:00
67 days, 2:12:00
3 days, 2:12:00
9 days, 13:43:00
10 days, 2:08:00
25 days, 18:41:00
136 days, 22:40:00
199 days, 16:31:00
5 days, 8:45:00
29 days, 5:22:00
36 days, 6:00:00
201 days, 12:16:00
5 days, 4:31:00
6 days, 1:19:00
48 days, 7:46:00
96 days, 15:39:00
3 days, 15:43:00
8 days, 6:10:00
26 days, 12:54:00
3 days, 13:19:00
10 days, 3:12:00
108 days, 3:42:00
80 days, 19:25:00
28 days, 23:18:00
12 days, 5:48:00
17 days, 9:29:00
26 days, 3:37:00
159 days, 4:03:00
22 days, 22:19:00
22 days, 2:34:00
24 days, 5:50:00
5 days, 7:55:00
25 days, 17:25:00
16 days, 2:36:00
9 days, 8:59:00
18 days, 13:57:00
10 days, 16:52:00
25 days, 0:54:00
468 days, 1:35:00
14 days, 7:27:00
26 days, 0:18:00
8 days, 5:06:00
34 days, 5:56:00
12 days, 5:52:00
1 day, 11:42:00
21 days, 12:27:00
1 day, 21:00:00
92 days, 6:00:00
30 days, 2:10:00
19 days, 20:11:00
19 days, 13:02:00
7 days, 4:39:00
8 days, 11:10:00
5 days, 23:09:00
5 days, 3:31:00
23 days, 21:49:00
18 days, 2:22:00
6 days, 18:08:00
145 days, 2:39:00
463 days, 19:31:00
17 days, 18:03:00
56 days, 10:13:00
63 days, 11:03:00
158 days, 10:09:00
32 days, 4:38:00
30 days, 11:04:00
31 days, 3:03:00
16 days, 13:59:00
30 days, 12:28:00
30 days, 3:51:00
30 days, 9:13:00
17 days, 18:18:00
5 days, 1:11:00
7 days, 11:29:00
20:44:00
8 days, 10:28:00
110 days, 15:09:00
100 days, 9:01:00
16 days, 11:03:00
416 days, 14:55:00
211 days, 11:18:00
19 days, 1:43:00
204 days, 17:17:00
137 days, 18:22:00
8 days, 18:21:00
6 days, 19:06:00
5 days, 0:25:00
1 day, 11:35:00
6 days, 20:59:00
77 days, 5:46:00
6 days, 10:51:00
57 days, 21:26:00
8 days, 1:25:00
16 days, 3:00:00
1 day, 7:18:00
25 days, 4:51:00
5 days, 12:16:00
108 days, 12:27:00
19:00:00
1 day, 15:33:00
20 days, 17:05:00
8 days, 0:48:00
2 days, 11:40:00
8 days, 21:08:00
189 days, 12:48:00
20 days, 22:43:00
9 days, 21:12:00
25 days, 1:34:00
4 days, 2:34:00
81 days, 7:35:00
4 days, 10:30:00
20:56:00
12 days, 8:30:00
9 days, 5:34:00
29 days, 1:17:00
4 days, 5:13:00
4 days, 18:22:00
4 days, 18:36:00
164 days, 5:14:00
4 days, 13:27:00
175 days, 1:16:00
14 days, 6:55:00
27 days, 22:58:00
19 days, 1:15:00
29 days, 5:38:00
9 days, 7:44:00
8 days, 8:14:00
578 days, 5:43:00
12 days, 14:37:00
90 days, 2:20:00
178 days, 4:51:00
178 days, 5:13:00
337 days, 6:54:00
12 days, 1:26:00
15 days, 21:21:00
608 days, 21:14:00
18 days, 9:34:00
1 day, 2:59:00
21 days, 8:21:00
28 days, 23:58:00
1 day, 3:53:00
22 days, 5:06:00
14 days, 5:41:00
98 days, 8:46:00
18:48:00
22 days, 14:00:00
344 days, 3:38:00
23 days, 15:27:00
232 days, 22:11:00
61 days, 11:37:00
66 days, 7:18:00
7 days, 18:05:00
42 days, 6:22:00
76 days, 7:48:00
37 days, 12:34:00
69 days, 5:57:00
50 days, 14:41:00
24 days, 21:37:00
1 day, 5:17:00
21 days, 21:32:00
78 days, 16:44:00
108 days, 12:27:00
24 days, 5:52:00
2 days, 12:49:00
5 days, 8:35:00
6 days, 18:58:00
446 days, 6:36:00
6 days, 12:53:00
36 days, 1:19:00
44 days, 3:37:00
181 days, 8:29:00
7 days, 14:50:00
30 days, 23:33:00
16 days, 15:26:00
34 days, 15:30:00
4 days, 13:18:00
76 days, 17:47:00
77 days, 1:31:00
1 day, 9:09:00
18 days, 1:43:00
40 days, 17:03:00
101 days, 12:19:00
23 days, 9:00:00
50 days, 14:20:00
417 days, 18:19:00
10:21:00
2 days, 8:28:00
46 days, 5:30:00
45 days, 15:33:00
6 days, 0:09:00
26 days, 5:09:00
18 days, 8:40:00
53 days, 18:40:00
4 days, 10:03:00
94 days, 3:35:00
6 days, 14:49:00
6 days, 15:33:00
11 days, 23:54:00
5 days, 20:27:00
1 day, 21:11:00
69 days, 7:06:00
1 day, 23:46:00
6 days, 21:43:00
29 days, 4:38:00
21 days, 8:44:00
7 days, 12:30:00
4 days, 13:30:00
10 days, 19:06:00
10 days, 5:58:00
15 days, 20:37:00
19 days, 0:52:00
4 days, 9:51:00
13 days, 15:53:00
16 days, 16:27:00
52 days, 14:40:00
140 days, 17:53:00
66 days, 22:27:00
57 days, 4:37:00
35 days, 23:40:00
1 day, 7:54:00
90 days, 4:05:00
19 days, 11:24:00
73 days, 10:51:00
69 days, 21:23:00
4 days, 11:13:00
5 days, 2:08:00
1 day, 12:01:00
1 day, 16:07:00
2 days, 9:09:00
224 days, 19:33:00
139 days, 3:10:00
168 days, 1:22:00
16 days, 3:54:00
43 days, 15:12:00
294 days, 11:30:00
9 days, 9:49:00
17 days, 11:49:00
8 days, 16:29:00
4 days, 3:40:00
5 days, 0:34:00
23 days, 16:17:00
3 days, 19:04:00
101 days, 0:30:00
28 days, 16:25:00
4 days, 16:50:00
6 days, 0:19:00
96 days, 17:49:00
5 days, 2:35:00
5 days, 9:00:00
14 days, 11:48:00
4 days, 15:18:00
10 days, 16:16:00
106 days, 12:00:00
7 days, 5:27:00
8 days, 18:54:00
453 days, 3:38:00
6 days, 16:00:00
54 days, 19:43:00
17:37:00
6 days, 2:39:00
1 day, 17:26:00
21 days, 8:32:00
15 days, 23:38:00
80 days, 10:12:00
8 days, 5:02:00
46 days, 11:23:00
13 days, 23:19:00
8 days, 5:38:00
47 days, 6:43:00
232 days, 7:38:00
76 days, 12:19:00
27 days, 14:23:00
148 days, 20:10:00
42 days, 0:36:00
12 days, 4:22:00
14 days, 9:05:00
16 days, 21:42:00
5 days, 2:05:00
3 days, 12:04:00
11 days, 6:25:00
1 day, 1:34:00
25 days, 19:18:00
101 days, 20:32:00
1 day, 11:13:00
15 days, 22:32:00
1 day, 2:50:00
355 days, 12:41:00
8 days, 11:16:00
474 days, 14:38:00
4 days, 12:49:00
26 days, 3:40:00
24 days, 0:40:00
44 days, 0:35:00
5 days, 14:52:00
18 days, 9:33:00
14:51:00
1 day, 13:17:00
2 days, 6:28:00
2 days, 17:18:00
9 days, 11:09:00
1 day, 1:45:00
141 days, 7:26:00
72 days, 9:45:00
23 days, 19:22:00
25 days, 12:29:00
7 days, 1:59:00
4 days, 0:34:00
109 days, 3:31:00
3 days, 14:53:00
6 days, 4:54:00
9 days, 21:45:00
396 days, 18:44:00
26 days, 20:54:00
187 days, 4:30:00
22 days, 7:27:00
9 days, 1:49:00
10 days, 20:51:00
215 days, 0:42:00
131 days, 7:16:00
111 days, 8:12:00
22 days, 4:59:00
27 days, 0:41:00
90 days, 4:47:00
3 days, 19:51:00
36 days, 12:56:00
5 days, 11:55:00
12 days, 19:40:00
49 days, 0:35:00
46 days, 1:06:00
12 days, 2:34:00
2 days, 4:25:00
5 days, 22:47:00
93 days, 20:01:00
26 days, 22:42:00
1 day, 4:18:00
2 days, 4:03:00
3 days, 12:59:00
450 days, 2:56:00
3 days, 5:24:00
11 days, 1:33:00
10 days, 2:26:00
13 days, 3:37:00
147 days, 18:09:00
1 day, 12:35:00
5 days, 13:01:00
6 days, 9:16:00
21:49:00
78 days, 3:01:00
25 days, 6:07:00
4 days, 19:53:00
8 days, 3:47:00
4 days, 2:02:00
16:36:00
18 days, 14:50:00
27 days, 18:50:00
30 days, 0:33:00
139 days, 18:02:00
354 days, 20:31:00
7 days, 4:05:00
9 days, 7:10:00
20 days, 1:37:00
183 days, 5:12:00
20 days, 12:28:00
20 days, 12:30:00
9 days, 16:15:00
151 days, 0:18:00
2 days, 6:37:00
9 days, 17:01:00
84 days, 1:41:00
10 days, 2:09:00
22 days, 2:48:00
109 days, 6:45:00
4 days, 3:17:00
5 days, 12:17:00
10 days, 20:11:00
551 days, 21:58:00
38 days, 16:09:00
151 days, 11:36:00
5 days, 15:14:00
105 days, 20:09:00
7 days, 3:54:00
82 days, 17:22:00
20 days, 22:12:00
17 days, 2:01:00
7 days, 2:42:00
33 days, 14:21:00
16 days, 3:12:00
108 days, 12:27:00
360 days, 9:18:00
1 day, 4:58:00
9 days, 8:28:00
11 days, 13:29:00
103 days, 18:35:00
17 days, 20:46:00
5 days, 4:42:00
3 days, 6:03:00
18 days, 9:06:00
103 days, 13:06:00
7 days, 13:36:00
8 days, 16:09:00
33 days, 22:01:00
461 days, 11:37:00
86 days, 12:51:00
55 days, 6:28:00
1 day, 8:15:00
125 days, 11:56:00
60 days, 8:32:00
17 days, 20:24:00
85 days, 14:01:00
5 days, 2:32:00
2 days, 21:17:00
235 days, 12:55:00
61 days, 13:50:00
16 days, 12:49:00
15 days, 2:49:00
2 days, 15:04:00
4 days, 16:33:00
15 days, 21:57:00
3 days, 4:21:00
10 days, 23:12:00
4 days, 2:53:00
4 days, 2:59:00
19 days, 20:56:00
18 days, 9:24:00
43 days, 5:37:00
5 days, 0:43:00
1 day, 9:11:00
16 days, 3:56:00
2 days, 7:22:00
8:20:00
58 days, 10:58:00
30 days, 0:00:00
26 days, 1:55:00
16 days, 7:59:00
170 days, 13:13:00
26 days, 1:54:00
16 days, 14:01:00
7 days, 10:47:00
362 days, 5:26:00
3 days, 0:10:00
5 days, 13:11:00
5 days, 22:53:00
1 day, 1:32:00
11 days, 6:12:00
1 day, 8:46:00
9 days, 1:30:00
149 days, 6:35:00
21 days, 22:05:00
2 days, 2:26:00
4 days, 6:05:00
119 days, 11:48:00
6 days, 8:59:00
7 days, 9:13:00
7 days, 21:52:00
11:55:00
11:57:00
290 days, 5:29:00
44 days, 1:57:00
85 days, 9:42:00
305 days, 20:23:00
13 days, 22:32:00
3 days, 1:41:00
221 days, 15:03:00
2 days, 8:41:00
103 days, 19:24:00
9 days, 12:49:00
15 days, 17:59:00
5 days, 15:36:00
42 days, 0:24:00
45 days, 4:15:00
6 days, 13:31:00
27 days, 16:47:00
15 days, 1:49:00
30 days, 17:56:00
6 days, 7:51:00
5 days, 13:45:00
305 days, 23:18:00
10 days, 12:42:00
4 days, 19:23:00
8 days, 2:53:00
10 days, 5:16:00
9 days, 12:56:00
15 days, 13:50:00
42 days, 14:30:00
8 days, 19:41:00
14 days, 18:02:00
3 days, 22:59:00
3 days, 15:54:00
16 days, 17:22:00
11 days, 21:31:00
9 days, 12:19:00
36 days, 20:21:00
5 days, 5:42:00
36 days, 18:36:00
25 days, 15:23:00
42 days, 0:46:00
448 days, 6:07:00
4 days, 9:09:00
3 days, 9:20:00
22 days, 1:27:00
41 days, 1:38:00
39 days, 6:13:00
95 days, 9:25:00
5 days, 17:03:00
16 days, 8:39:00
5 days, 4:33:00
232 days, 9:09:00
14 days, 18:47:00
22:33:00
21:33:00
6 days, 16:52:00
2 days, 6:28:00
11 days, 6:01:00
7 days, 7:50:00
34 days, 14:34:00
2 days, 22:37:00
3 days, 21:30:00
12 days, 5:47:00
28 days, 22:41:00
6 days, 10:46:00
3 days, 8:30:00
6 days, 2:52:00
3 days, 8:00:00
9 days, 5:37:00
15 days, 8:41:00
79 days, 2:57:00
59 days, 23:21:00
61 days, 0:52:00
6 days, 9:04:00
3 days, 21:36:00
4 days, 11:23:00
23:44:00
23:53:00
13 days, 14:30:00
446 days, 12:33:00
64 days, 2:16:00
15 days, 8:58:00
4 days, 1:28:00
132 days, 12:38:00
9 days, 13:48:00
8 days, 22:19:00
24 days, 22:28:00
20 days, 4:06:00
121 days, 8:08:00
3 days, 13:08:00
199 days, 20:35:00
14 days, 15:28:00
119 days, 8:53:00
1 day, 11:47:00
22 days, 10:13:00
4 days, 3:50:00
34 days, 11:16:00
14 days, 17:41:00
8 days, 6:59:00
15 days, 10:35:00
9 days, 11:54:00
17 days, 14:05:00
40 days, 15:26:00
30 days, 14:09:00
205 days, 4:34:00
6 days, 6:50:00
28 days, 12:47:00
43 days, 23:03:00
633 days, 10:33:00
9 days, 14:23:00
11 days, 16:34:00
109 days, 21:56:00
4 days, 21:47:00
3 days, 15:13:00
25 days, 3:18:00
5 days, 10:04:00
5 days, 21:52:00
34 days, 17:48:00
5 days, 16:23:00
5 days, 1:41:00
6 days, 10:42:00
193 days, 15:48:00
17 days, 20:19:00
5 days, 4:49:00
21 days, 9:56:00
40 days, 0:49:00
5 days, 2:22:00
44 days, 16:21:00
23 days, 3:59:00
2 days, 20:05:00
7 days, 8:55:00
53 days, 12:18:00
14 days, 19:20:00
19 days, 2:27:00
19 days, 6:13:00
171 days, 9:35:00
12 days, 10:19:00
34 days, 5:31:00
5 days, 6:33:00
6 days, 8:19:00
10 days, 13:14:00
784 days, 14:50:00
22 days, 13:39:00
47 days, 8:46:00
39 days, 13:35:00
44 days, 4:02:00
1 day, 11:11:00
25 days, 3:19:00
8 days, 4:56:00
104 days, 21:28:00
24 days, 22:02:00
5 days, 0:38:00
2 days, 23:14:00
7 days, 3:51:00
128 days, 10:32:00
124 days, 1:00:00
11 days, 15:51:00
7 days, 16:53:00
41 days, 8:49:00
13 days, 23:25:00
58 days, 16:12:00
5 days, 11:03:00
3 days, 19:12:00
9 days, 4:19:00
1 day, 4:41:00
1 day, 5:23:00
16 days, 5:39:00
2 days, 9:35:00
77 days, 17:16:00
14 days, 20:34:00
724 days, 2:47:00
5 days, 5:05:00
28 days, 2:10:00
12 days, 7:59:00
52 days, 15:30:00
34 days, 11:39:00
6 days, 7:42:00
23 days, 7:18:00
216 days, 8:57:00
65 days, 10:06:00
1 day, 11:28:00
93 days, 8:55:00
64 days, 9:02:00
1 day, 13:27:00
6 days, 23:54:00
286 days, 0:56:00
92 days, 2:41:00
608 days, 17:40:00
10 days, 23:07:00
1 day, 23:01:00
16 days, 4:42:00
5 days, 15:29:00
4 days, 22:01:00
13 days, 12:15:00
8 days, 23:32:00
11 days, 23:12:00
5 days, 6:43:00
18 days, 8:23:00
15 days, 2:06:00
2 days, 3:57:00
9 days, 17:05:00
14 days, 21:08:00
2 days, 22:28:00
228 days, 17:39:00
3 days, 21:38:00
1 day, 18:43:00
9 days, 11:03:00
10 days, 16:06:00
4 days, 12:36:00
1 day, 15:27:00
20 days, 16:27:00
18:04:00
13 days, 14:08:00
1 day, 15:25:00
1 day, 16:47:00
1 day, 5:16:00
4 days, 20:29:00
2 days, 11:15:00
14 days, 13:34:00
43 days, 10:29:00
20:41:00
8 days, 9:14:00
9 days, 5:31:00
17 days, 1:57:00
16 days, 20:01:00
476 days, 15:32:00
13 days, 22:28:00
10 days, 18:56:00
9 days, 6:32:00
74 days, 21:55:00
25 days, 8:30:00
28 days, 2:10:00
756 days, 7:12:00
15 days, 11:27:00
25 days, 7:22:00
28 days, 7:44:00
24 days, 7:26:00
25 days, 7:25:00
25 days, 6:13:00
17 days, 6:15:00
25 days, 7:30:00
18 days, 1:08:00
17 days, 9:27:00
732 days, 19:32:00
46 days, 2:21:00
62 days, 12:55:00
63 days, 2:16:00
7 days, 14:33:00
2 days, 16:04:00
32 days, 2:07:00
42 days, 12:00:00
542 days, 3:22:00
7 days, 12:21:00
27 days, 18:50:00
27 days, 7:47:00
5 days, 5:09:00
26 days, 9:55:00
1 day, 9:39:00
48 days, 20:04:00
7 days, 12:58:00
0:05:00
9 days, 17:41:00
476 days, 22:16:00
9 days, 2:35:00
4 days, 7:39:00
96 days, 0:20:00
296 days, 15:50:00
46 days, 19:41:00
9 days, 8:32:00
10 days, 8:55:00
51 days, 16:55:00
3 days, 4:12:00
2 days, 13:19:00
117 days, 1:15:00
17 days, 4:36:00
15 days, 5:12:00
14 days, 5:57:00
7 days, 7:21:00
3 days, 21:19:00
15 days, 17:48:00
17 days, 12:18:00
596 days, 3:20:00
29 days, 6:34:00
59 days, 4:47:00
78 days, 4:25:00
163 days, 18:38:00
2 days, 22:08:00
2:51:00
2 days, 20:50:00
4 days, 15:06:00
9 days, 14:11:00
20:31:00
153 days, 3:38:00
124 days, 11:57:00
112 days, 8:49:00
14 days, 4:02:00
111 days, 13:55:00
6 days, 16:13:00
3 days, 15:15:00
18 days, 15:19:00
466 days, 21:35:00
6 days, 7:32:00
46 days, 6:13:00
45 days, 7:07:00
45 days, 7:40:00
46 days, 8:03:00
377 days, 14:23:00
20 days, 23:26:00
20 days, 23:29:00
2 days, 4:23:00
2 days, 20:13:00
174 days, 15:10:00
34 days, 12:51:00
94 days, 9:22:00
28 days, 5:01:00
54 days, 1:02:00
24 days, 21:10:00
25 days, 12:53:00
14 days, 14:46:00
27 days, 6:23:00
12 days, 10:36:00
24 days, 22:54:00
75 days, 1:36:00
90 days, 10:01:00
98 days, 13:12:00
57 days, 8:09:00
349 days, 10:01:00
70 days, 6:19:00
197 days, 18:32:00
456 days, 15:51:00
211 days, 20:02:00
619 days, 2:25:00
81 days, 2:39:00
467 days, 10:40:00
203 days, 21:53:00
476 days, 5:56:00
205 days, 17:07:00
205 days, 5:00:00
470 days, 22:45:00
196 days, 20:20:00
124 days, 12:31:00
425 days, 8:44:00
126 days, 17:37:00
235 days, 20:39:00
626 days, 21:26:00
239 days, 22:16:00
146 days, 1:57:00
382 days, 16:55:00
638 days, 22:56:00
492 days, 5:12:00
422 days, 11:27:00
192 days, 11:58:00
457 days, 1:03:00
558 days, 3:15:00
483 days, 1:29:00
451 days, 2:07:00
143 days, 19:39:00
414 days, 18:10:00
866 days, 22:01:00
294 days, 21:28:00
1103 days, 17:12:00
1068 days, 17:17:00
623 days, 12:19:00
647 days, 18:29:00
770 days, 6:49:00
727 days, 1:15:00
498 days, 23:02:00
628 days, 12:55:00
382 days, 21:40:00
944 days, 5:00:00
560 days, 2:38:00
"""


# 将数据分割成单独的时间字符串
time_values = data.strip().split('\n')

total_seconds = 0

for value in time_values:
    if ',' in value:
        parts = value.split(', ')
        days = int(parts[0].split()[0])
        time_parts = parts[1].split(':')
    else:
        days = 0
        time_parts = value.split(':')

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    total_seconds += (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

average_seconds = total_seconds / len(time_values)

# 将平均秒数转换回天、小时、分钟和秒
avg_days = average_seconds // (24 * 60 * 60)
avg_hours = (average_seconds % (24 * 60 * 60)) // (60 * 60)
avg_minutes = (average_seconds % (60 * 60)) // 60
avg_seconds = average_seconds % 60

print(f"平均时间：{int(avg_days)} days, {int(avg_hours)}:{int(avg_minutes):02}:{int(avg_seconds):02}")