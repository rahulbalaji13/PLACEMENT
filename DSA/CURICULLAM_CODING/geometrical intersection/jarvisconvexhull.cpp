//
class Solution 
{
public:
    int check(pair<int , int> &p1, pair<int , int> &p2, pair<int , int> p3)
    {
         //X Coordinates
         int x1 = p1.first;
         int x2 = p2.first;
         int x3 = p3.first;
         
         //Y Coordinates
         int y1 = p1.second;
         int y2 = p2.second;
         int y3 = p3.second;
         
         //Jarvis algorithm formula to find which point is on which side(left or right)
         return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2);
    }

    vector<vector<int>> outerTrees(vector<vector<int>>& trees) 
    {
         vector<vector<int>> ans;
         sort(trees.begin() , trees.end());

         deque<pair<int , int>> lower, upper; //To perform dequeue operation simultaneously with both lower and upper

         for(auto &point : trees)
         {
             int l = lower.size();
             int u = upper.size();

             //For the lower points
             while(l >= 2 && check(lower[l-2] , lower[l-1] , {point[0],point[1]})<0)
             {
                 l--;
                 lower.pop_back();
             }
             
             //For the upper points
             while(u >= 2 && check(upper[u-2] , upper[u-1] , {point[0],point[1]})>0)
             {
                 u--;
                 upper.pop_back();
             }
                 upper.push_back({point[0],point[1]});
                 lower.push_back({point[0],point[1]});
         }
             set<pair<int , int>> set;
             
             for(auto &it:lower)
             {
                 set.insert(it);
             }
             
             for(auto &it:upper)
             {
                 set.insert(it);
             }
              
             for(auto &it:set)
             {
                ans.push_back({it.first , it.second});
             }
                 return ans;
    }
};
