#include <iostream>
#include <string>
using namespace std;
int main()
{
  string s;
  cin >> s;
  bool ans = true;
  int len = s.length();
  for (int i = 0; i < len / 2; ++i)
  {
    if (s[i] != s[len - 1 - i]) ans = false;
  }
  if (ans)
  {
    cout << "True" << endl;
  } else {
    cout << "False" << endl;
  }
  return 0;
}