#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end());
    // n = len(citations)
    int n = citations.size();
    
    // h = 0 ~ n 
    int h = n;
    
    while(1) { // 0 1 3 5 6 , h = 5
        if(h <= citations[n - h])
            return h;
        else
            h--;
    }
    
    return h;
}


