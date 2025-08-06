/**
Approach 2: Segment Tree + Binary Search
Intuition
This is a template problem for a segment tree, where we can use a segment tree to maintain the maximum value of the baskets array over intervals, and then use binary search to find the first basket that meets the condition. The specific method is as follows:
First, establish a tree where the content maintained at initialization is the maximum value of each interval.
Then, enumerate the fruits in fruits, and use the segment tree to find the maximum value in the interval during the binary search process 
to locate the first basket that meets the condition. If such a basket is found, use the segment tree to perform a single-point update on that basket, setting its value to 0. Otherwise, increment the counter count.
The process of binary search is as follows: If the maximum value in the left interval is greater than the current number of fruits, continue the binary search in the left interval. 
If the maximum value in the left interval is less than the current number of fruits and the maximum value in the right interval is greater than or equal to the current number of fruits, 
continue the binary search in the right interval. Otherwise, there is no interval that meets the condition in the current range.

Complexity Analysis
Let n be the length of the array baskets.

Time complexity: O(nlogn).

Constructing the segment tree takes O(n) time. Enumerating the fruits in fruits requires O(n) time, and each binary search, segment tree query, and update operation takes O(logn) time.

Space complexity: O(n).

It requires O(n) space to store the segment tree.
**/

class Solution {

    private int[] segTree = new int[400007];
    private int[] baskets;

    private void build(int p, int l, int r) {
        if (l == r) {
            segTree[p] = baskets[l];
            return;
        }
        int mid = (l + r) >> 1;
        build(p << 1, l, mid);
        build((p << 1) | 1, mid + 1, r);
        segTree[p] = Math.max(segTree[p << 1], segTree[(p << 1) | 1]);
    }

    private int query(int p, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) {
            return Integer.MIN_VALUE;
        }
        if (ql <= l && r <= qr) {
            return segTree[p];
        }
        int mid = (l + r) >> 1;
        return Math.max(
            query(p << 1, l, mid, ql, qr),
            query((p << 1) | 1, mid + 1, r, ql, qr)
        );
    }

    private void update(int p, int l, int r, int pos, int val) {
        if (l == r) {
            segTree[p] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) {
            update(p << 1, l, mid, pos, val);
        } else {
            update((p << 1) | 1, mid + 1, r, pos, val);
        }
        segTree[p] = Math.max(segTree[p << 1], segTree[(p << 1) | 1]);
    }

    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        this.baskets = baskets;
        int m = baskets.length;
        int count = 0;
        if (m == 0) {
            return fruits.length;
        }
        Arrays.fill(segTree, Integer.MIN_VALUE);
        build(1, 0, m - 1);
        for (int i = 0; i < fruits.length; i++) {
            int l = 0;
            int r = m - 1;
            int res = -1;
            while (l <= r) {
                int mid = (l + r) >> 1;
                if (query(1, 0, m - 1, 0, mid) >= fruits[i]) {
                    res = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            if (res != -1 && baskets[res] >= fruits[i]) {
                update(1, 0, m - 1, res, Integer.MIN_VALUE);
            } else {
                count++;
            }
        }
        return count;
    }
}
