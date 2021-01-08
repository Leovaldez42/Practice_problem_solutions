#include <bits/stdc++.h>
using namespace std;

void rightRotateByOne (int arr[], int n) {
    int temp = arr[n - 1], i;
    for (i = n - 1; i > 0; i--)
        arr[i] = arr[i - 1];
    arr[0] = temp;
    // A inbuilt function ;
	// right shift
	// rotate(v.begin(), v.begin()+v.size()-k, v.end());
	
	// left shift
	// rotate(v.begin(), v.begin()+k, v.end());
	
		
}

int main() {
	int t;
	cin >> t;
	while(t--) {
	    int n;  cin >> n;
	    int a[n];
	    for(int i=0; i<n; i++)
	        cin >> a[i];
	   rightRotateByOne(a, n);
	   for(int i=0; i<n; i++) {
	       cout << a[i] << " ";
	   }
	   cout << endl;
	}
	return 0;
}
