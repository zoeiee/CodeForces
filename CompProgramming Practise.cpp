#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int a, x, y;
        cin >> a >> x >> y;

        if ((x < a && a < y) || (y < a && a < x))
            cout << "NO\n";
        else
            cout << "YES\n";
    }
    return 0;
}
