class Solution {
    public int numTilings(int n) {
        
        int mod=1_000_000_007;

        long[] v=new long[Math.max(4, n+1)];

        v[1]=1; v[2]=2; v[3]=5;

        for(int i=4;i<=n;i++){

            v[i]=(2*v[i-1]+v[i-3])%mod;
        }

        return (int)v[n];
    }
}
