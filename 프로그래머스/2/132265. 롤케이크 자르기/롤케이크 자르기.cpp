#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> topping) { // set로 바꿔서 size 보기
    vector<int> left(10001, 0);
    vector<int> right(10001, 0);
    
    int leftKinds = 0;
    int rightKinds = 0;
    int answer = 0;
    
    for (int t : topping) {
        if (right[t] == 0)
            rightKinds++;

        right[t]++;
    }
    
    for (int i = 0; i + 1 < topping.size(); i++) {
        int t = topping[i];

        if (left[t] == 0)
            leftKinds++;

        left[t]++;

        right[t]--;

        if (right[t] == 0)
            rightKinds--;

        if (leftKinds == rightKinds)
            answer++;
    }

    return answer;
}