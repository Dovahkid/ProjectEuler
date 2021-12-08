import java.util.ArrayList;


class EvenFibonacci {

    static long fibonacci(){

        final double dblPhi = (1 + Math.sqrt(5)) / 2;
        long total = 0;

        for(int i = 0; i <= 33; i++){

            // Generating fibonacci sequence
            double dblNthTerm = (Math.pow(dblPhi, i)) / Math.sqrt(5);
            double tempNum = dblNthTerm - Math.floor(dblNthTerm);

            long intNthTerm = tempNum >= .5 ? (long) Math.ceil(dblNthTerm) : (long) Math.floor(dblNthTerm);

            // Now looking for all even numbers and adding them
            if (intNthTerm % 2 == 0){
                total += intNthTerm;
            }

        }

        return total;
    }

}
