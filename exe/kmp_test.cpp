#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> kmp_search(const string &s, const string &t) {
    vector<int> result;
    int m = t.size(), n = s.size();
    for (int i = 0; i <= n - m; i++) {
        if (s.substr(i, m) == t) result.push_back(i);
    }
    return result;
}

int main() {
    string s, t;
    cin >> s >> t;
    vector<int> matches = kmp_search(s, t);
    if (matches.empty()) {
        cout << "False" << endl;
    } else {
        for (int pos : matches) cout << pos << ' ';
        cout << endl;
    }
    return 0;
}
