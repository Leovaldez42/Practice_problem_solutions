#include<bits/stdc++.h>
using namespace std;

int main () {
    int n, k;
    cin >> n >> k;
    
    int a[n], i;
    for(i=0; i<n; i++)
        cin >> a[i];
        
    sort(a, a+n);
    cout << a[k-1] << endl; // This is for min
    cout << a[n-k] << endl; // This is for max 
}