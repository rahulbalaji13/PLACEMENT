/**
Okay, imagine you and your friend have two baskets of fruit. 
🍎 🍌 🍇 The goal is to make sure you both have the exact same amount of each type of fruit. But, 
you can only swap fruits between the baskets. Each swap costs you something (kinda like a trading card game). 
The mission? Figure out the cheapest way to balance the fruit baskets! If it's impossible to balance them (like, you have an odd number of a particular fruit total), 
then you're out of luck and have to return -1.
**/

class Solution {

    public long minCost(int[] basket1, int[] basket2) {
        TreeMap<Integer, Integer> freq = new TreeMap<>();
        int m = Integer.MAX_VALUE;
        for (int b1 : basket1) {
            freq.put(b1, freq.getOrDefault(b1, 0) + 1);
            m = Math.min(m, b1);
        }
        for (int b2 : basket2) {
            freq.put(b2, freq.getOrDefault(b2, 0) - 1);
            m = Math.min(m, b2);
        }

        List<Integer> merge = new ArrayList<>();
        for (var entry : freq.entrySet()) {
            int count = entry.getValue();
            if (count % 2 != 0) return -1;
            for (int i = 0; i < Math.abs(count) / 2; i++) {
                merge.add(entry.getKey());
            }
        }

        Collections.sort(merge);
        long res = 0;
        for (int i = 0; i < merge.size() / 2; i++) {
            res += Math.min(2 * m, merge.get(i));
        }
        return res;
    }
}
