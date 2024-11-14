#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, num;
    vector<int> numbers;
    while (cin >> num) {
        numbers.push_back(num);
        if (cin.get() == '\n') break;
    }
    sort(numbers.begin(), numbers.end());
    for (int i : numbers) cout << i << ' ';
    cout << endl;
    return 0;
}
