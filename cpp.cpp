#include <iostream>
using namespace std;
int main()
{
    int a[3][3] = {1,2,3,4,5,6,7,8,9};
    int row[3];
    int column[3];
    for (int i=0;i<3;i++)
    {
        int sum = 0;
        for (int j=0;j<3;j++)
        {
            sum = sum + a[i][j];
        }
        row[i] = sum;
        cout<<endl;
    }
    for (int i = 0; i < 3; i++)
    {
        cout<< row[i]<<endl;
    }    
}