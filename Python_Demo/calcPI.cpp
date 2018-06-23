#include<stdio.h>
#include<time.h>
#include<math.h>
#include<stdlib.h>

int main()
{
    int times = 120000000;
    int hits = 0;
    int i;
    float x, y;
    float dist;
    //int a[101] = {0};
    srand((unsigned)time(NULL));
    for(i = 0; i < times; i++)
    {
        x = (1.0*rand()/(RAND_MAX-1));
        y = (1.0*rand()/(RAND_MAX-1));
        //printf("%d , %d  \n  ", x, y);
        //printf("%lf,%lf    ", x, y);
        //printf("%d  \n", x*x + y*y);
        dist = (x*x + y*y);
        //printf("%lf \n", dist);
        if(dist <= 1)
        {
            hits += 1;
        }
        //a[x] += 1;
        //a[y] += 1;
    }
    /*for(i=0; i<=100; i++) {
        printf("%d ",a[i]);
    }*/
    printf("%d\n",hits);
    printf("%lf\n", 4*(double)hits/(double)times);
    return 0;
}
