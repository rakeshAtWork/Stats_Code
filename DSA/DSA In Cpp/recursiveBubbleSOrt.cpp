#include<bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[],int n){
    if(n==1) return;

    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1]){
            int tmp = arr[i+1];
            arr[i+1]=arr[i];
            arr[i]=tmp;
        }

    }

    bubbleSort(arr,n-1);

}


int main(){
    int arr[]={13,46,24,52,20,9};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout<<"Before Using Bubble Sort: "<<endl;

    for(int i=0;i<n;i++){
        cout<< arr[i]<<" ";
    }
    cout<<endl;

    bubbleSort(arr,n);
    cout<<"After using bubble sort : "<<"\n";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}   