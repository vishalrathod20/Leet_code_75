class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> radient;
        queue<int> dire;

        int n = senate.size();

        for (int i = 0; i<n; i++){
            if(senate[i] == 'R'){
                radient.push(i);
            }
            else{
                dire.push(i);
            }
        }

        while(!radient.empty() && !dire.empty()){
              int rIndex = radient.front();
              int dIndex = dire.front();
              radient.pop();
              dire.pop();

              if(rIndex < dIndex){
                radient.push(rIndex+n);
              }
              else{
                dire.push(dIndex+n);
              }
        }
        return radient.empty() ? "Dire":"Radiant";
    }
};
