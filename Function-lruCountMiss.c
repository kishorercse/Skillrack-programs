/*
You can click on Run anytime to check the compilation/execution status of the program. You can use printf to debug your code. The submitted code should be logically/syntactically
correct and pass all test cases.
Do not write the main() function as it is not required.
Code Approach: 
For this question, you will need to implement the logic for the function. The least recently used (LRU) cache algorithm evicts the element from the cache that was least recently
used when the cache is full. After an element is requested from the cache, it should be added to the cache (if not there) and considered the most recently used element in the 
cache whether it is newly added or was already existing. Initially, the cache is empty. Implement the function lruCountMiss. The input to the function lruCountMiss shall consist 
of an integer MAX_CACHE_SIZE, an array pages and its length len. The function is supposed to return an integer for the number of cache misses using the LRU cache algorithm. 

Assume that the array pages always have pages numbered from 0 to 50. (A hit means the requested page is already existing in the cache and a miss means the requested page is not 
found in the cache). Your task is to implement the logic for the function to pass all test cases.

Example Input/Output 1:
Input:
3 16 
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 

Output: 
11
*/
int lruCountMiss(int MAX_CACHE_SIZE, int *pages, int len)
{
    int cache[MAX_CACHE_SIZE], missCount=0;
    memset(cache, -1, sizeof(int)*MAX_CACHE_SIZE);
    for(int i=0; i<len; i++)
    {
        int found=0, index=0;
        for(int j=0; j<MAX_CACHE_SIZE; j++)
        {
            if (cache[j]==pages[i])
            {
                found=1;
                index=j;
                break;
            }
        }
        if (found==0)
            missCount++;
        for(int j=index+1; j<MAX_CACHE_SIZE; j++)
        {
            cache[j-1]=cache[j];
        }
        cache[MAX_CACHE_SIZE-1]=pages[i];
    }
    return missCount;
}
