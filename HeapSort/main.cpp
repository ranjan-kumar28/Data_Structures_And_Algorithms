#include <iostream>
using namespace std;
void buildHeap(int a[],int n)
{
    for(int i=1;i<n;i++)
    {
        int pi=i,j=i;
        while(pi>0){
            pi=(pi-1)/2;
            if(a[pi]<a[j]){swap(a[j],a[pi]);j=pi;}
            else break;
        }
    }
}

void HeapSort(int a[],int n){
    int j=n-1;
    while(j>0)
    {
        int i=0;
        swap(a[i],a[j]);
        while(i<j)
        {
            int lci=2*i+1;
            int rci=2*i+2;
            if(lci<j && rci<j) // when both left and right child are present
            {
                if(a[lci]>a[i] || a[rci]>a[i]){
                    if(a[lci]>a[rci]){swap(a[lci],a[i]);i=lci;}
                    else {swap(a[rci],a[i]);i=rci;}
                }
            }
            else if(lci<j)
            {
                if(a[lci]>a[i]){swap(a[lci],a[i]);i=lci;}
            }
            else if(rci<j)
            {
                if(a[lci]>a[i]){swap(a[rci],a[i]);i=rci;}
            }
            if(i!=lci && i!=rci)i=j;
        }j--;
    }
}
int main()
{
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    buildHeap(a,n);
    HeapSort(a,n);
    cout<<"Sorted Array :\t";
    for(int i=0;i<n;i++)cout<<a[i]<<" ";
    cout<<endl;
    return 0;
}
