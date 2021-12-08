import java.util.ArrayList;
class PrimeFactors {

    static long FindingFactors(long numToCheck){ // This method is setup in a weirdish way. My method of finding primes
                                  // requires this weird setup, but thats okay because this function does a lot
        System.out.println("*** Finding Primes ***");

        ArrayList<Long> primes = new ArrayList<>();
        for(long i = 1; i < numToCheck; i+=2) {
            if(FindPrimes(i) && i != 1){ // This confirms the number is a prime
                if(numToCheck % i == 0) { // This checks if its a factor of the big number
                    primes.add(i);
                    System.out.println(primes);
                }
            }
        }
        return primes.get(primes.size() - 1);
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
