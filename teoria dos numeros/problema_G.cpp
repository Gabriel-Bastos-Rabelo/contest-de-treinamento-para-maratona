#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is prime
bool ehPrimo(int n) {
    if (n == 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// Function to check if it's possible to express a number as the sum of two prime numbers
bool ehPossivel(int n) {
    int l = 2;
    int r = n;
    while (l < r) {
        bool ehPrimoL = ehPrimo(l);
        bool ehPrimoR = ehPrimo(r);
        if (ehPrimoL && ehPrimoR) {
            int soma = l + r;
            if (soma == n) {
                return true;
            } else if (soma > n) {
                r--;
            } else {
                l++;
            }
        } else if (ehPrimoL) {
            r--;
        } else if (ehPrimoR) {
            l++;
        } else {
            l++;
            r--;
        }
    }
    return false;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        if (v <= 3) {
            cout << 0 << endl;
        } else if (v % 2 == 0) {
            cout << 1 << endl;
        } else {
            cout << ehPossivel(v) << endl;
        }
    }

    return 0;
}
