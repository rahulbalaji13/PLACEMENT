#include <bits/stdc++.h>
using namespace std;

int main() {
    // ====== VECTOR ======
    cout << "=== VECTOR ===" << endl;
    vector<int> v = {10, 20, 30};
    v.push_back(40);
    v.pop_back();

    // Iterators
    cout << "Using iterators: ";
    for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) cout << *it << " ";
    cout << endl;

    cout << "Using auto & reverse iterators: ";
    for (auto it = v.rbegin(); it != v.rend(); ++it) cout << *it << " ";
    cout << endl;

    cout << "Front: " << v.front() << " Back: " << v.back() << " Size: " << v.size() << endl;


    // ====== LIST ======
    cout << "\n=== LIST ===" << endl;
    list<int> l = {1, 2, 3};
    l.push_front(0);
    l.push_back(4);
    l.pop_front();
    for (auto it = l.begin(); it != l.end(); ++it) cout << *it << " ";
    cout << endl;


    // ====== DEQUE ======
    cout << "\n=== DEQUE ===" << endl;
    deque<int> dq = {5, 6, 7};
    dq.push_front(4);
    dq.push_back(8);
    dq.pop_front();
    dq.pop_back();
    for (auto x : dq) cout << x << " "; cout << endl;


    // ====== STACK ======
    cout << "\n=== STACK ===" << endl;
    stack<int> st;
    st.push(1); st.push(2); st.push(3);
    while (!st.empty()) { cout << st.top() << " "; st.pop(); }
    cout << endl;


    // ====== QUEUE ======
    cout << "\n=== QUEUE ===" << endl;
    queue<int> q;
    q.push(10); q.push(20); q.push(30);
    while (!q.empty()) { cout << q.front() << " "; q.pop(); }
    cout << endl;


    // ====== PRIORITY QUEUE ======
    cout << "\n=== PRIORITY QUEUE (Max-Heap) ===" << endl;
    priority_queue<int> pq;
    pq.push(5); pq.push(10); pq.push(1);
    while (!pq.empty()) { cout << pq.top() << " "; pq.pop(); }
    cout << endl;

    cout << "\n=== PRIORITY QUEUE (Min-Heap) ===" << endl;
    priority_queue<int, vector<int>, greater<int>> pqmin;
    pqmin.push(5); pqmin.push(10); pqmin.push(1);
    while (!pqmin.empty()) { cout << pqmin.top() << " "; pqmin.pop(); }
    cout << endl;


    // ====== SET ======
    cout << "\n=== SET ===" << endl;
    set<int> s = {3, 1, 2, 2};
    s.insert(4);
    for (auto it = s.begin(); it != s.end(); ++it) cout << *it << " ";
    cout << endl;
    cout << "Find 2: " << (s.find(2) != s.end() ? "Found" : "Not Found") << endl;


    // ====== MULTISET ======
    cout << "\n=== MULTISET ===" << endl;
    multiset<int> ms = {1, 1, 2};
    ms.insert(2);
    for (auto x : ms) cout << x << " "; cout << endl;


    // ====== UNORDERED SET ======
    cout << "\n=== UNORDERED SET ===" << endl;
    unordered_set<int> us = {10, 20, 10, 30};
    for (auto x : us) cout << x << " "; cout << endl;


    // ====== MAP ======
    cout << "\n=== MAP ===" << endl;
    map<int, string> mp;
    mp[1] = "One"; mp[2] = "Two"; mp[3] = "Three";
    for (auto it = mp.begin(); it != mp.end(); ++it)
        cout << it->first << " => " << it->second << endl;


    // ====== MULTIMAP ======
    cout << "\n=== MULTIMAP ===" << endl;
    multimap<int, string> mmp;
    mmp.insert({1, "Apple"}); mmp.insert({1, "Mango"});
    for (auto &p : mmp) cout << p.first << " => " << p.second << endl;


    // ====== UNORDERED MAP ======
    cout << "\n=== UNORDERED MAP ===" << endl;
    unordered_map<string, int> ump;
    ump["a"] = 100; ump["b"] = 200;
    for (auto &p : ump) cout << p.first << " => " << p.second << endl;


    // ====== ALGORITHMS ======
    cout << "\n=== ALGORITHMS ===" << endl;
    vector<int> arr = {5, 1, 4, 2, 3};
    sort(arr.begin(), arr.end());
    cout << "Sorted: "; for (int x : arr) cout << x << " "; cout << endl;

    reverse(arr.begin(), arr.end());
    cout << "Reversed: "; for (int x : arr) cout << x << " "; cout << endl;

    cout << "Count of 2: " << count(arr.begin(), arr.end(), 2) << endl;
    cout << "Binary search 3: " << binary_search(arr.begin(), arr.end(), 3) << endl;

    cout << "Lower bound of 3: " << *lower_bound(arr.begin(), arr.end(), 3) << endl;
    cout << "Upper bound of 3: " << *upper_bound(arr.begin(), arr.end(), 3) << endl;

    int sum = accumulate(arr.begin(), arr.end(), 0);
    cout << "Accumulate sum: " << sum << endl;


    // ====== UTILITIES ======
    cout << "\n=== UTILITIES ===" << endl;
    pair<int, string> p = {1, "One"};
    cout << "Pair: " << p.first << " " << p.second << endl;

    tuple<int, string, double> t = {2, "Two", 2.5};
    cout << "Tuple: " << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
    
    int second_len = (int)p.second.size();
    swap(p.first,second_len); // just for demo
    cout << "Swapped Pair first: " << p.first << " second: " << p.second << endl;

    return 0;
}




/**
| **Container**       | **Common Operations**                                                                         | **Iterators**                                    | **Time Complexity**                                                 |
| ------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| **vector**          | `push_back()`, `pop_back()`, `front()`, `back()`, `at()`, `size()`, `capacity()`, `clear()`   | `begin()`, `end()`, `rbegin()`, `rend()`, `auto` | Access: O(1), Insert at end: Amortized O(1), Insert in middle: O(n) |
| **list**            | `push_front()`, `push_back()`, `pop_front()`, `pop_back()`, `insert()`, `erase()`, `remove()` | `begin()`, `end()`, `rbegin()`, `rend()`         | Access: O(n), Insert/Delete anywhere: O(1)                          |
| **deque**           | `push_front()`, `push_back()`, `pop_front()`, `pop_back()`, `at()`, `size()`                  | `begin()`, `end()`, `rbegin()`, `rend()`         | Access: O(1), Insert/Delete both ends: O(1)                         |
| **stack**           | `push()`, `pop()`, `top()`, `size()`, `empty()`                                               | No iterators                                     | Push/Pop/Top: O(1)                                                  |
| **queue**           | `push()`, `pop()`, `front()`, `back()`, `size()`                                              | No iterators                                     | Enqueue/Dequeue: O(1)                                               |
| **priority\_queue** | `push()`, `pop()`, `top()`                                                                    | No iterators                                     | Push: O(log n), Pop: O(log n), Top: O(1)                            |
| **set**             | `insert()`, `erase()`, `find()`, `count()`, `lower_bound()`, `upper_bound()`                  | `begin()`, `end()`                               | Insert/Find: O(log n)                                               |
| **multiset**        | Same as `set`, allows duplicates                                                              | Same as `set`                                    | Insert/Find: O(log n)                                               |
| **unordered\_set**  | `insert()`, `erase()`, `find()`, `count()`                                                    | `begin()`, `end()`                               | Average O(1), Worst O(n)                                            |
| **map**             | `insert()`, `erase()`, `find()`, `count()`, `operator[]`                                      | `begin()`, `end()`                               | Insert/Find: O(log n)                                               |
| **multimap**        | Same as `map`, allows duplicate keys                                                          | Same as `map`                                    | Insert/Find: O(log n)                                               |
| **unordered\_map**  | `insert()`, `erase()`, `find()`, `count()`, `operator[]`                                      | `begin()`, `end()`                               | Average O(1), Worst O(n)                                            |


| **Algorithm**                          | **Usage**                | **Complexity** |
| -------------------------------------- | ------------------------ | -------------- |
| `sort(v.begin(), v.end())`             | Sorts in ascending order | O(n log n)     |
| `reverse(v.begin(), v.end())`          | Reverses container       | O(n)           |
| `binary_search(v.begin(), v.end(), x)` | Checks if element exists | O(log n)       |
| `lower_bound(v.begin(), v.end(), x)`   | First index ≥ x          | O(log n)       |
| `upper_bound(v.begin(), v.end(), x)`   | First index > x          | O(log n)       |
| `count(v.begin(), v.end(), x)`         | Counts occurrences       | O(n)           |
| `find(v.begin(), v.end(), x)`          | Finds first occurrence   | O(n)           |
| `accumulate(v.begin(), v.end(), 0)`    | Sum of elements          | O(n)           |
| `max_element(v.begin(), v.end())`      | Largest element          | O(n)           |
| `min_element(v.begin(), v.end())`      | Smallest element         | O(n)           |

| **Utility**                                     | **Usage Example**      |
| ----------------------------------------------- | ---------------------- |
| `pair<int, string> p = {1, "one"};`             | Stores two values      |
| `make_pair(1, "one");`                          | Creates pair           |
| `tuple<int, string, double> t = {1, "x", 2.5};` | Stores multiple values |
| `get<0>(t)`                                     | Access tuple element   |
| `swap(a, b)`                                    | Swaps values           |

**/
