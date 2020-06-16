
```
//冒泡排序 Bubble Sort   时间复杂度: O(n*n)  空间复杂度: O(1)  ; 稳定的排序算法
void bubbleSort(int[] nums) {
    //定义一个布尔变量 hasChange，用来标记每轮遍历中是否发生了交换
    boolean hasChange = true; 

    //每轮遍历开始，将 hasChange 设置为 false
    for (int i = 0; i < nums.length - 1 && hasChange; i++) {
        hasChange = false;

        //进行两两比较，如果发现当前的数比下一个数还大，那么就交换这两个数，同时记录一下有交换发生
        for (int j = 0; j < nums.length - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {
                swap(nums, j, j + 1);
                hasChange = true;
            }
        }
     }
 }
 ```
 ```
 void swap(int[] nums, int i, int j )){
  if(nums==null || nums.length < i + 1 || nums.length < j + 1){ return ;}
  int temp = nums[i];
  nums[i] = nums[j];
  nums[j] = temp;
 }
```

```

//插入排序 时间复杂度: O(n*n)   时间复杂度: O(n*n)  空间复杂度: O(1)  ; 稳定的排序算法
void insertionSort(int[] nums) {
    // 将数组的第一个元素当作已经排好序的，从第二个元素，即 i 从 1 开始遍历数组
    for (int i = 1, j, current; i < nums.length; i++) {
        // 外围循环开始，把当前 i 指向的值用 current 保存
        current = nums[i];

        // 指针 j 内循环，和 current 值比较，若 j 所指向的值比 current 值大，则该数右移一位
        for (j = i - 1; j >= 0 && nums[j] > current; j--) {
            nums[j + 1] = nums[j];
            }
    
        // 内循环结束，j+1 所指向的位置就是 current 值插入的位置
        nums[j + 1] = current;
    }
}
```

```
//归并排序 Merge Sort  空间复杂度:O(n) 时间复杂度: O(nlogn)
void mergeSort(int[] A, int lo, int hi) {
  // 判断是否只剩下最后一个元素
  if (lo >= hi) return;
  
  // 从中间将数组分成两个部分
  int mid = lo + (hi - lo) / 2;
  
  // 分别递归地将左右两半排好序
  sort(A, lo, mid);
  sort(A, mid + 1, hi);

  // 将排好序的左右两半合并  
  merge(A, lo, mid, hi);
}

void merge(int[] nums, int lo, int mid, int hi) {
    // 复制一份原来的数组
    int[] copy = nums.clone();
  
    // 定义一个 k 指针表示从什么位置开始修改原来的数组，i 指针表示左半边的起始位置，j 表示右半边的起始位置
    int k = lo, i = lo, j = mid + 1;
  
    while (k <= hi) {
        if (i > mid) {
            nums[k++] = copy[j++];
        } else if (j > hi) {
          nums[k++] = copy[i++];
        } else if (copy[j] < copy[i]) {
          nums[k++] = copy[j++];
        } else {
          nums[k++] = copy[i++];
        }
    }
}
```
```
//快速排序 Quick Sort
void quickSort(int[] nums, int lo, int hi) {
    if (lo >= hi) return; // 判断是否只剩下一个元素，是，则直接返回
    
    // 利用 partition 函数找到一个随机的基准点
    int p = partition(nums, lo, hi);
    
    // 递归地对基准点左半边和右半边的数进行排序
    sort(nums, lo, p - 1);
    sort(nums, p + 1, hi);
}
 

int partition(int[] nums, int lo, int hi) {
    // 随机选择一个数作为基准值，nums[hi] 就是基准值
    swap(nums, randRange(lo, hi), hi);

    int i, j;

    // 从左到右用每个数和基准值比较，若比基准值小，则放到指针 i 所指向的位置。循环完毕后，i 指针之前的数都比基准值小
    for (i = lo, j = lo; j < hi; j++) {
        if (nums[j] <= nums[hi]) {
            swap(nums, i++, j);
        }
    }

    // 末尾的基准值放置到指针 i 的位置，i 指针之后的数都比基准值大
    swap(nums, i, j);

    // 返回指针 i，作为基准点的位置
    return i;
}
```

