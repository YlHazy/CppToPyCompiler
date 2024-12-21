#include <iostream>
using namespace std;

    int main() {
        int n;

        cout << "请输入数组的长度：";
        cin >> n;

        int arr[100];

        cout << "请输入 " << n << " 个整数：";
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        for (int i = 0; i < n - 1; ++i) {
            for (int j = 0; j < n - i - 1; ++j) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        cout << "排序后的数组是：";
        for (int i = 0; i < n; ++i) {
            cout << arr[i] << "nnn";
        }
        cout << endl;

        return 0;
    }
