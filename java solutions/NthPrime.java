import java.util.ArrayList;

class NthPrime {

    static long FindingNthPrime(){ // This method is setup in a weirdish way. My method of finding primes
        // requires this weird setup, but thats okay because this function does a lot

        int count = 1;
        long currentPrime;
        for(long i = 1;; i+=2) {
            if(FindPrimes(i) && i != 1){ // This confirms the number is a prime
                count+=1;
                currentPrime = i;
                if(count == 10001){
                    return currentPrime;
                }
            }
        }
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
