// Dynamic programming approach
class Solution 
{
    public List<List<Integer>> generate(int numRows) 
    {
       List<List<Integer>> res = new ArrayList<>();
       res.add(new ArrayList<>());
       res.get(0).add(1);

       for(int i = 1; i < numRows; i++)
       {
           // Create list to own current and previous element sum
           List<Integer> row = new ArrayList<>();
           List<Integer> prevRow = res.get(i - 1);

           // Fix the first row element as always 1
           row.add(1);
           
           for(int j = 1; j < i; j++)
           {
              row.add(prevRow.get(j - 1) + prevRow.get(j));
           }
           
           // Fix the last row element as always 1
           row.add(1);

           res.add(row);
       }
       return res;
    }
}

/**
1
1 1 
1 2 1
1 3 3 1
1 4 6 4 1

The traingle pascal tells 1 should be constant at starting and ending of any formation without any disturbance. In between each iteration, Take sum of first and second element and then add 1 as usual at start and end.

**/
