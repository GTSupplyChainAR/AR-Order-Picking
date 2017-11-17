package indoornavigation.com.glass;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;

public class MainActivityGlass extends Activity {

    int numberOfPicks = 10;

    String currentUser;

    Long lastStartTime;
    ArrayList<Long> pickTimes = new ArrayList<>(numberOfPicks);

    FirebaseDatabase database = FirebaseDatabase.getInstance();

    /* ----- UI ----- */
    View parentView;

    View aisleView;
    View[] letterViews;

    View rowView;
    // column, row
    View[][] blockViews;

    TextView locationText;
    TextView isbnText;
    TextView titleText;
    TextView authorText;

    TextView instructionText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);
       // parentView = findViewById(R.id.parent_view);
//
//        aisleView = findViewById(R.id.aisle_view);
//        letterViews = new View[] {
//                findViewById(R.id.block_a),
//                findViewById(R.id.block_b),
//                findViewById(R.id.block_c),
//                findViewById(R.id.block_d),
//                findViewById(R.id.block_e),
//                findViewById(R.id.block_f)
//        };
//
//        rowView = findViewById(R.id.row_view);
//        blockViews = new View[][] {
//                new View[] {
//                        findViewById(R.id.block_0_0),
//                        findViewById(R.id.block_0_1),
//                        findViewById(R.id.block_0_2),
//                        findViewById(R.id.block_0_3),
//                        findViewById(R.id.block_0_4),
//                        findViewById(R.id.block_0_5)
//                },
//                new View[] {
//                        findViewById(R.id.block_1_0),
//                        findViewById(R.id.block_1_1),
//                        findViewById(R.id.block_1_2),
//                        findViewById(R.id.block_1_3),
//                        findViewById(R.id.block_1_4),
//                        findViewById(R.id.block_1_5)
//                },
//                new View[] {
//                        findViewById(R.id.block_2_0),
//                        findViewById(R.id.block_2_1),
//                        findViewById(R.id.block_2_2),
//                        findViewById(R.id.block_2_3),
//                        findViewById(R.id.block_2_4),
//                        findViewById(R.id.block_2_5)
//                },
//                new View[] {
//                        findViewById(R.id.block_3_0),
//                        findViewById(R.id.block_3_1),
//                        findViewById(R.id.block_3_2),
//                        findViewById(R.id.block_3_3),
//                        findViewById(R.id.block_3_4),
//                        findViewById(R.id.block_3_5)
//                },
//                new View[] {
//                        findViewById(R.id.block_4_0),
//                        findViewById(R.id.block_4_1),
//                        findViewById(R.id.block_4_2),
//                        findViewById(R.id.block_4_3),
//                        findViewById(R.id.block_4_4),
//                        findViewById(R.id.block_4_5)
//                },
//                new View[] {
//                        findViewById(R.id.block_5_0),
//                        findViewById(R.id.block_5_1),
//                        findViewById(R.id.block_5_2),
//                        findViewById(R.id.block_5_3),
//                        findViewById(R.id.block_5_4),
//                        findViewById(R.id.block_5_5)
//                },
//        };
//
//        locationText = findViewById(R.id.location_text);
//        isbnText = findViewById(R.id.isbn_text);
//        titleText = findViewById(R.id.title_text);
//        authorText = findViewById(R.id.author_text);
//
//        instructionText = findViewById(R.id.instruction_text);
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
