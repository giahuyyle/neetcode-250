void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int removeElement(int* nums, int numsSize, int val) {
    int count = 0, i = 0, j = numsSize - 1;
    while (i <= j) {
        if (nums[i] == val) {
            if (nums[j] == val) {
                j--;
                count++;
            }
            else {
                swap(&nums[i], &nums[j]);
                i++;
                j--;
                count++;
            }
        }
        else {
            i++;
        }
    }
    return numsSize - count;
}