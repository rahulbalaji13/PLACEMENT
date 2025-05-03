class maxWorkerAssign 
{
  public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) 
    {
        int left = 0, right = Math.min(tasks.length, workers.length);
        
        Arrays.sort(tasks);
        Arrays.sort(workers);

        while (left < right) 
        {
            int mid = (left + right + 1) / 2; // Number of tasks we are trying to assign
            int usedPills = 0;
            
            /**TreeMap in Java is a class that implements the Map interface, storing key-value pairs in a sorted order based on the keys. 
            It uses a (red-black tree data structure), which ensures that the elements are always sorted. Keys can be sorted either by their natural ordering or by a custom Comparator provided at the time of TreeMap creation. 
            It does not allow null keys, but it can have null values. 
            TreeMap provides efficient retrieval, insertion, and deletion operations with a time complexity of O(log n), where n is the number of elements in the map. **/
            TreeMap<Integer, Integer> avail = new TreeMap<>();

            int n = workers.length;
            int start = workers.length - mid; // To consider only the string worker for assigning hard tasks 
            
            for (int i = start; i < n; i++)
            {                
               if(avail.containsKey(workers[i])) 
               {
                  avail.put(workers[i], avail.get(workers[i]) + 1);
               } 
               else 
               {
                  avail.put(workers[i], 1);
               }

            }
            
            boolean canAssign = true;

            int fromLast = mid - 1;
            
            for (int i = fromLast; i >= 0; i--) // Iterates the loop from last to first worker 
            {
                int t = tasks[i];
                int w = avail.lastKey(); // Assign last worker
                
                if (w >= t) // Check whether the worker strength is greater then task t
                {
                    decrement(avail, w); //If true, then assign the task to worker and decrement worker strength
                } 
                else 
                {
                    Integer key = avail.ceilingKey(t - strength);  // key + strength ≥ t 
                    
                    /** celingKey() method is used to find the least key in the map that is greater than or equal to the given key. 
                    This functionality is useful when you need to find the closest key that is at least a certain value, 
                    which is common in scenarios like range searching or finding the next available value in a sorted set. 
                    For example,if a TreeMap contains the keys {3, 5, 7, 9}, calling ceilingKey(6) would return 7, because 7 is the smallest key in the map that is greater than or equal to 6. 
                    If you call ceilingKey(7), it would return 7 as well, since 7 is present in the map. However, if you call ceilingKey(10), 
                    it would return null because there is no key in the map that is greater than or equal to 10.
                    **/
                    
                    if (key == null || ++usedPills > pills) //When no worker exsists or used pill is more then given pills then assign to FALSE
                    {
                        canAssign = false;
                        break;
                    }
                    decrement(avail, key); // Assign the task using this worker with pills and remove the key from avail
                }
            }

            if (canAssign)
                
                left = mid; //mid is the current number of tasks you're testing in binary search. can assign is true, so update left = mid to search higher in the next round. 
                //So update left = mid to search higher in the next round.
            else
                right = mid - 1; //We can't assign mid tasks. So reduce the search space: right = mid - 1.
        }

        return left;
    }

    private void decrement(TreeMap<Integer, Integer> m, int k) 
    {
        int c = m.get(k); //Get current count of workers with strength k
        
        if (c == 1) 
            
            m.remove(k); //If only one such worker exists (c == 1), ➤ remove the key completely from the map: m.remove(k)
        else 
            m.put(k, c - 1); //If more than one, ➤ decrement the count: m.put(k, c - 1)
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
