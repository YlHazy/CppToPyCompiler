#include <iostream>
#include <string>
using namespace std;

// 判断字符串是否为回文的函数
bool isPalindrome(const string& s) {
    int str_len = s.length();
    for (int i = 0; i < str_len / 2; ++i) {
        if (s[i] != s[str_len - 1 - i]) {
            return false;  // 如果有不相等的字符，返回 false
        }
    }
    return true;  // 如果所有字符都相等，则返回 true
}

int main() {
    string s;
    cin >> s;  // 输入字符串
    
    // 调用 isPalindrome 函数
    bool ans = isPalindrome(s);
    while(s>ans){
        cout << "False" << endl;
        int a = 1;
    }
    // 输出结果
    if (ans) {
        cout << "True" << endl;
    } else if (ans == false) {
        cout << "False" << endl;
    }

    return 0;
}
