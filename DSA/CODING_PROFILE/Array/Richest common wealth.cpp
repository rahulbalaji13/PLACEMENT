class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_wealth= 0; // let the answer initially be 0;
        for (int i=0; i<accounts.size(); i++){
            int customer=0; // now for each customer we start with wealth 0;
			// we in a for loop sum up all the accounts wealth
            for (int j=0; j<accounts[0].size();j++){
                customer+= accounts[i][j];
            }
            max_wealth= max(customer,max_wealth);  // now we compare it with the maximum wealth
        }
        return max_wealth; // return the maximum wealth out of all
    }
};
