class Twitter {
public:
    map<int,set<int>> mp;
    int time=0;
    priority_queue<vector<int>> pq;
    Twitter() {
        time=0;
        mp.clear();
        pq= priority_queue<vector<int>>();
    }
    
    void postTweet(int userId, int tweetId) {
        pq.push({time++,tweetId,userId});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> ans;
        priority_queue<vector<int>> npq=pq;
        int n=9;
        while(!npq.empty() && n >= 0)
        {
            auto it=npq.top();
            npq.pop();
            int user=it[2];
            int tweet=it[1];
            if(user==userId || mp[userId].find(user)!=mp[userId].end())
            {
                ans.push_back(tweet);
                n--;
            }
        }
        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        mp[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        mp[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
