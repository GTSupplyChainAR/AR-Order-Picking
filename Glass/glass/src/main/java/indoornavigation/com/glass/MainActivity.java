package indoornavigation.com.glass;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    int numberOfPicks = 10;

    String currentUser;

    Long lastStartTime;
    ArrayList<Long> pickTimes = new ArrayList<>(numberOfPicks);

    FirebaseDatabase database = FirebaseDatabase.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // todo set up blank initial view

        setContentView(R.layout.activity_main);
    }

    // todo this needs to be called by user input
    private void startPicking() {

        // todo debug this
        currentUser = database.getReference("ar-order-picking").push().getKey();

        generateNextPick();
    }

    // todo this needs to be called when a user has picked
    private void completePick() {
        pickTimes.add(System.currentTimeMillis() - lastStartTime);

        generateNextPick();
    }

    private void generateNextPick() {
        // todo display next pick on ui

        if (pickTimes.size() < numberOfPicks) {
            lastStartTime = System.currentTimeMillis();
        } else {
            finishPicking();
        }
    }

    private void finishPicking() {
        // todo: debug this
        database.getReference("ar-order-picking").child(currentUser).setValue(pickTimes);
    }
}
