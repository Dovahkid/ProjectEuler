import java.util.ArrayList;

class ThreeAndFive {

    static int threeAndFive(){

        int total = 0;

        for(int i = 0; i < 1000; i++){

            if ((i % 3 == 0) || (i % 5 == 0)){
                total += i;
            }

        }

        return total;
    }

    static int customValues(ArrayList<Integer> values, int max){

        int total = 0;

        int i = 0;

        for(int j = 0; j < max; j++){

            for (; i < values.size() - 1; i++){

                if(j % values.get(i) != 0){
                    break;
                }
                else if( (i == values.size() - 1) && ( j % values.get(i) == 0)) {

                    total += j;

                }

            }
        }

        return total;
    }

}
