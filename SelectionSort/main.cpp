#include <iostream>
using namespace std;
void SelectionSort(int a[],int n)
{
    for(int i=0;i<n-1;i++){
        int minInd=i;
        for(int j=i;j<n;j++){
            if(a[j]<a[minInd])minInd=j;
            cout<<"minIndex = "<<minInd<<"\n";
        }
        if(minInd!=i)swap(a[i],a[minInd]);
        cout<<"after iteration\n";
        for(int i=0;i<n;i++)cout<<a[i]<<" ";
        cout<<endl;
    }
}

int main()
{
    int n;cin>>n;
    int a[n];for(int i=0;i<n;i++)cin>>a[i];
    SelectionSort(a,n);
    for(int i=0;i<n;i++)cout<<a[i]<<" ";
    cout<<endl;
    return 0;
}
