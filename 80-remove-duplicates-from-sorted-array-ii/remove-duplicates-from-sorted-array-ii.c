#define INF 40000
int removeDuplicates(int* nums, int numsSize) {
    int i=1;
    int freq=1;
    int current=nums[0];

    if(numsSize<3){
        return numsSize;
    }
    while(i<numsSize){
        if(current!=nums[i]){
            current=nums[i];
            i++;
            freq=1;
            continue;
        }

        if(current==nums[i]){
            freq++;
            }

        if(freq>2){
            nums[i]=INF;
        }

        i++;


    }

    i=0;
    int j=0;

    while(i<numsSize && nums[i]!=INF){
        i++;
    }

    

    if(i>=numsSize){
        return numsSize;

    }

    j=i;

    

    while(j<numsSize && nums[j]==INF){
        j++;
    }

    if(j>=numsSize){
        return i;
    }

    int temp=0;

    while(j<numsSize){
        if(nums[j]==INF){
            j++;
            continue;
        }
        temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
        i++;
        j++;
    }
    //return numsSize;
    return i;

}