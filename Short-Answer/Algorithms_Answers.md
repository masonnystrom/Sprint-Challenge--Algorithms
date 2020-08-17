#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(1) because the while loop will iterate n times regardless of the size of n


b) The while loop will run log(n) times and the for loop runs at O(n) meaning the combined algorithm will have a runtime of O(n log n) because as the size of the input increases the runtime will grow at a slightly faster rate. 


c) The runtime of this function will be O(n) because BunnyEars is recurrisvely called n times before it reaches the base case. 

## Exercise II

Assuming there are n floors in a range(1,n) and our target is f, then we could utilize a binary search using a midpoint. If the egg breaks we can eliminate all the floors below. If egg doesn't break eliminate all floows above.

Repeat recursively on subsections/the new range of floors
Stop when you reach a floor where the egg doesn't break from dropping
This would have a runtime complexity of O(log n) since we'd be using a binary search algorithm. 

