#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

struct element {
    int grade;
    bool isPass;
};

class Comparator {
    public:
        bool operator()(element& x, element& y) {
            return x.grade < y.grade;
        }
};

int getAccurate(vector<element> &data, int thredhold) {
    int ret = 0;
    for (auto &ele : data)
    {
        if (ele.grade < thredhold && !ele.isPass)
            ret++;;
        if (ele.grade >= thredhold && ele.isPass)
            ret++;
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    int N;
    cin >> N;
    vector<element> data;
    unordered_map<int, int> leMap, gtEqMap; // 小于且isPass==False; 大于||等于且isPass==True
    
    for(int i=0; i < N; i++) {
        element temp;
        cin >> temp.grade >> temp.isPass;
        data.push_back(temp);
    }
    sort(data.begin(), data.end(), Comparator());

    int counter = 0;
    int l ,r;
    l = r = 0;
    int temp = 0; 
    for (; r < data.size(); r++){
        if (data[r].grade != data[l].grade) {
            int value = data[l].grade;
            leMap[value] = counter;
            l = r;
            counter += temp;
            temp = 0;
        }
        temp += (data[r].isPass == false);
    }
    leMap[data[r-1].grade] = counter;
    counter = 0;
    r = l = data.size() - 1;
    for (; l >= 0; l--) {
        if (data[r].grade != data[l].grade) {
            int value = data[r].grade;
            gtEqMap[value] = counter;
            r = l;
        }
        counter += data[l].isPass;
    }
    gtEqMap[(*data.begin()).grade] = counter;
    // int l = 0, r = N - 1;
    // int lValue = getAccurate(data, data[l].grade);
    // int rValue = getAccurate(data, data[r].grade);
    // while (r >= l) {
    //     int mid = (r + l) / 2;
    //     int midValue = getAccurate(data, data[mid].grade);
    //     if (midValue )
    // }
    int threshod = -1;
    int value = -1;
    for(auto &item: leMap) {
        int key = item.first;
        int currentValue = leMap[key] + gtEqMap[key];
        if ( currentValue> value) {
            threshod = key;
            value = currentValue;
        } else if (currentValue == value && key > threshod)
            threshod = key;
    }
    cout << threshod;
    return 0;
}