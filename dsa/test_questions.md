# Spotnana - 13th October 2026

### Q1
There are n servers and two lists on length n. `request` and `max_req`. `max_req[i]` and `request[i]` indicate the maximum requests i-th server can handle and the current requests at the server, resepectively. If there are more requests than it can handle, we can divert the traffic to other servers. The latency in doing so is $|i - j|$. 

Find the minimum possible maximum latency. Return -1 if all requests couldn't be served. 

https://claude.ai/share/f227660d-9df0-43d2-bae3-698aaa7b9a42

### Q2
Given a list of integerts, find the count of all subarrays such that the bitwise OR of all the elements in the subarray is present in the subarray itself.

https://claude.ai/share/c7b838cc-d296-4564-bf33-2f3b6b7ec9d1

### Q3
Given, the count of airport nodes, list of from_nodes, list of to_nodes, list of costs, and a query containing, start airport, end airport, and maximum number of layovers allowed. find the minimum cost possible. 

https://claude.ai/share/1fd7fd60-15d2-4256-8c83-9a58c6165212


# Honda - 17th october 2026

### Q1
Given the list of coordinates and an integer k. Find the minimum area corresponding to a rectangle whose sides are parallel to the primary axes and strictly enclosing at least k points. 

https://claude.ai/share/8d6ae75c-046e-4e55-babe-a0050c52e166

### Q2
Insert and Shift identities

https://claude.ai/share/3b730389-6be1-4032-a493-2d23cb7cf9ce


# Flipkart Test - 28th october 2026
### Q1
Finding LCA given root val, position list and node values list.
The position list is as follows, [L, R, LL, LR, RL, RR, ...], and the corresponding values are given in the values list. Essentially make the tree and then find LCA.

### Q2
Maximum area rectangle.

### Q3
Permutation with first character a number.


# Commotion Test - 28th october 2026
### Q1
Cooling the Foundry Floor
There is an n*n tiled floor. Each tile has a temperature. The robot has to move from (0,0) to (n-1,n-1). Some tiles are safe for the robot to step on and some are not, depending on the hotness of their temperature. As time passes, the temperature of the tiles decrease. The robot can take a step a step to the its neighbor tiles (Up, Down, Left, Right) only if the current tile and the new tile are safe to walk on. Also, it can go to as many safe neighbors in 0 time. 
Find the shortest amount of time it takes for the robot to complete it's path.

### Q2
Smallest covering window
Given two strings, str1, and str2. Find the shortest substring in str1 which contains all the characters or more of str2. Both string may contain upper case and lower case english letters.

### Q3
Network Reliability Investigation
Given an edge list with weights as latency (positive). From 1 to n, find the following:
1. Minimum Latency
2. Number of minimum latency paths
3. Minimum number of links path
4. Maximum number of links path

### Q4
The Great Chai Stall Crawl