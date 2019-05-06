// Problem 50: implement pow(x,n) (done recursively as part of lesson)
// Note that there are many cases which may or may not break this....
// But at least for now this is 4ms runtime which beats 100% of C submissions
double helper(double x, int n){
    if (n == 0) return 1;
    double x2 = helper(x, n/2);
    
    if (n % 2 == 0) return x2 * x2;
    
    return x2 * x2 * x;
}

double myPow(double x, int n){
    if (n < 0) {
        if (n == INT_MIN) {
            if (x < 0) {
                return 1 / helper(-x, INT_MAX);
            }
            return 1 / helper(x, INT_MAX);
        }
        return 1 / helper(x,-n);
    }
    return helper(x,n);
}