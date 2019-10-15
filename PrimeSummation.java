class PrimeSummation {

    static long Summation(){ // This method is setup in a weirdish way. My method of finding primes
        // requires this weird setup, but thats okay because this function does a lot

        long total = 2;
        for(long i = 1; i < 2000000; i+=2) {
            if(FindPrimes(i) && i != 1){ // This confirms the number is a prime
                total+=i;
                System.out.println(total);
            }
        }
        return total;
    }

    private static boolean FindPrimes(long i){
        for(long j = 2; j < i; j++){
            if(i % j == 0) {
                return false;
            }
        }
        return true;
    }

}
