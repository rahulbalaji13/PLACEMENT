class maxWorkerAssign {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        int left = 0, right = Math.min(tasks.length, workers.length);
        Arrays.sort(tasks);
        Arrays.sort(workers);

        while (left < right) {
            int mid = (left + right + 1) / 2;
            int usedPills = 0;
            TreeMap<Integer, Integer> avail = new TreeMap<>();
            for (int i = workers.length - mid; i < workers.length; ++i)
                avail.put(workers[i], avail.getOrDefault(workers[i], 0) + 1);

            boolean canAssign = true;
            for (int i = mid - 1; i >= 0; --i) {
                int t = tasks[i];
                int w = avail.lastKey();
                if (w >= t) {
                    decrement(avail, w);
                } else {
                    Integer key = avail.ceilingKey(t - strength);
                    if (key == null || ++usedPills > pills) {
                        canAssign = false;
                        break;
                    }
                    decrement(avail, key);
                }
            }

            if (canAssign)
                left = mid;
            else
                right = mid - 1;
        }

        return left;
    }

    private void decrement(TreeMap<Integer, Integer> m, int k) {
        int c = m.get(k);
        if (c == 1) m.remove(k);
        else m.put(k, c - 1);
    }
}
        
        /**int n = tasks.length;
        int m = workers.length;

        //Strength of worker 
        worker[0] 

        //Task assign constraint
        if(workers[j] >= tasks[i])
        {

        }   

        //number of pills is equal to number of strngth points increase
        //atmost 1 pills
        if(pills <= 1)
        
        //0-indexed: task and worker
        //Integer: pills, strength

        //Return the MAXIMUM number of tasks completed
        int completed = Math.max(0,task[j]); 
        return completed;
        
        SOLUTION: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/solutions/6703695/binary-search-greedy-with-images-example-walkthrough-c-python-java
        
        **/
