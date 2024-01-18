#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

std::pair<int, int> calculateMaxMin(vector<int>& arr, int i, int j) {
    if (i == j) {
        int max_val = arr[i];
        int min_val = arr[i];
        return make_pair(max_val, min_val);
    }
    else if (i == (j - 1)) {
        if (arr[i] > arr[j]) {
            int max_val = arr[i];
            int min_val = arr[j];
            return make_pair(max_val, min_val);
        }
        else {
            int max_val = arr[j];
            int min_val = arr[i];
            return make_pair(max_val, min_val);
        }
    }
    else {
        int mid = i + (j - i) / 2;
        std::pair<int, int> left = calculateMaxMin(arr, i, mid);
        std::pair<int, int> right = calculateMaxMin(arr, mid + 1, j);
        int max_l = left.first;
        int min_l = left.second;
        int max_r = right.first;
        int min_r = right.second;
        int max_val = max(max_l, max_r);
        int min_val = min(min_l, min_r);
        return make_pair(max_val, min_val);
    }
}

int main() {
    std::vector<int> arr = {50, 10, 20, 45, 12, 78, 20, 45, 25, 35, 655, 8, 1, 552, -9};
    int i = 0;
    int j = arr.size() - 1;
    pair<int, int> result = calculateMaxMin(arr, i, j);
    int max_val = result.first;
    int min_val = result.second;
    std::cout << "The max value is " << max_val << " and min value is " << min_val << std::endl;
    return 0;
}

