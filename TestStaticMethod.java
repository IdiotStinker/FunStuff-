public class TestStaticMethod {
    
    int favNum;

    TestStaticMethod(int f){
        
        this.favNum = f;
        //System.out.println("Created Tester");
    }
    
    public int getFavNum(){
        return favNum;
    }
    
    public static void main(String args[]){
        
        TestStaticMethod fools = new TestStaticMethod(-15);
        
        System.out.println(Math.abs(fools.favNum));
        
    }
}