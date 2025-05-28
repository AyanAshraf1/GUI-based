package com.example.percentagecalculator;

import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import android.graphics.Color;
import android.util.TypedValue;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    // UI containers
    private LinearLayout rootLayout;
    private ScrollView scrollView;

    // Step 1: Subject names
    private LinearLayout subjectInputLayout;
    private EditText[] subjectEdits = new EditText[8];
    private Button continueButton;

    // Step 2: Marks input
    private LinearLayout marksInputLayout;
    private ArrayList<TextView> subjectLabels;
    private ArrayList<EditText> obtainedMarksEdits;
    private ArrayList<EditText> totalMarksEdits;
    private Button submitButton;
    private TextView resultTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Root scrollable layout
        scrollView = new ScrollView(this);
        rootLayout = new LinearLayout(this);
        rootLayout.setOrientation(LinearLayout.VERTICAL);
        rootLayout.setPadding(dpToPx(16), dpToPx(16), dpToPx(16), dpToPx(16));
        rootLayout.setBackgroundColor(Color.parseColor("#00ff00")); // bright green background

        scrollView.addView(rootLayout);
        setContentView(scrollView);

        setupStep1View();
    }

    private void setupStep1View() {
        subjectInputLayout = new LinearLayout(this);
        subjectInputLayout.setOrientation(LinearLayout.VERTICAL);
        rootLayout.addView(subjectInputLayout);

        // Instructions Title
        TextView instructionsTitle = new TextView(this);
        instructionsTitle.setText("Instructions");
        instructionsTitle.setTextSize(TypedValue.COMPLEX_UNIT_SP, 30);
        instructionsTitle.setTextColor(Color.BLACK);
        instructionsTitle.setGravity(Gravity.CENTER_HORIZONTAL);
        subjectInputLayout.addView(instructionsTitle);

        // Instructions detail
        TextView instructionsDetail = new TextView(this);
        instructionsDetail.setText("Enter the names of the subjects you need only, no need to fill the rest.");
        instructionsDetail.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20);
        instructionsDetail.setTextColor(Color.BLACK);
        instructionsDetail.setGravity(Gravity.CENTER_HORIZONTAL);
        instructionsDetail.setPadding(0, dpToPx(8), 0, dpToPx(24));
        subjectInputLayout.addView(instructionsDetail);

        // Subject inputs
        for (int i = 0; i < subjectEdits.length; i++) {
            LinearLayout hLayout = new LinearLayout(this);
            hLayout.setOrientation(LinearLayout.HORIZONTAL);
            hLayout.setPadding(0, dpToPx(8), 0, dpToPx(8));
            hLayout.setGravity(Gravity.CENTER_VERTICAL);

            TextView label = new TextView(this);
            label.setText("Subject number " + (i + 1) + ": ");
            label.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20);
            label.setTextColor(Color.BLACK);
            label.setLayoutParams(new LinearLayout.LayoutParams(dpToPx(180), LinearLayout.LayoutParams.WRAP_CONTENT));
            hLayout.addView(label);

            EditText subjectEdit = new EditText(this);
            subjectEdit.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20);
            subjectEdit.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
            subjectEdit.setSingleLine(true);
            hLayout.addView(subjectEdit);

            subjectInputLayout.addView(hLayout);
            subjectEdits[i] = subjectEdit;
        }

        continueButton = new Button(this);
        continueButton.setText("Continue");
        continueButton.setTextSize(TypedValue.COMPLEX_UNIT_SP, 24);
        continueButton.setTextColor(Color.RED);
        continueButton.setBackgroundColor(Color.BLUE);
        LinearLayout.LayoutParams btnParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT);
        btnParams.setMargins(0, dpToPx(24), 0, 0);
        continueButton.setLayoutParams(btnParams);
        subjectInputLayout.addView(continueButton);

        continueButton.setOnClickListener(v -> {
            // Collect entered subjects; filter out empty
            ArrayList<String> subjects = new ArrayList<>();
            for (EditText et : subjectEdits) {
                String text = et.getText().toString().trim();
                if (!text.isEmpty()) {
                    subjects.add(text);
                }
            }
            if (subjects.size() == 0) {
                Toast.makeText(MainActivity.this, "Please enter at least one subject name.", Toast.LENGTH_SHORT).show();
                return;
            }

            showMarksInput(subjects);
        });
    }

    private void showMarksInput(ArrayList<String> subjects) {
        // Hide step 1 views
        subjectInputLayout.setVisibility(View.GONE);

        // Setup step 2 views if not already present
        if (marksInputLayout == null) {
            marksInputLayout = new LinearLayout(this);
            marksInputLayout.setOrientation(LinearLayout.VERTICAL);
            rootLayout.addView(marksInputLayout);

            // Header row
            LinearLayout headerLayout = new LinearLayout(this);
            headerLayout.setOrientation(LinearLayout.HORIZONTAL);
            headerLayout.setPadding(0, 0, 0, dpToPx(12));

            TextView subjectHeader = createHeaderTextView("Subject", 0, 1);
            TextView obtainedHeader = createHeaderTextView("Obtained Marks", 1, 1);
            TextView totalHeader = createHeaderTextView("Total Marks", 2, 1);

            headerLayout.addView(subjectHeader);
            headerLayout.addView(obtainedHeader);
            headerLayout.addView(totalHeader);

            marksInputLayout.addView(headerLayout);

            subjectLabels = new ArrayList<>();
            obtainedMarksEdits = new ArrayList<>();
            totalMarksEdits = new ArrayList<>();

            // Subjects row to be added dynamically below

            submitButton = new Button(this);
            submitButton.setText("Submit");
            submitButton.setTextSize(TypedValue.COMPLEX_UNIT_SP, 24);
            submitButton.setTextColor(Color.RED);
            submitButton.setBackgroundColor(Color.BLUE);

            LinearLayout.LayoutParams submitBtnParams = new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT);
            submitBtnParams.setMargins(0, dpToPx(24), 0, 0);
            submitButton.setLayoutParams(submitBtnParams);
            marksInputLayout.addView(submitButton);

            resultTextView = new TextView(this);
            resultTextView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 28);
            resultTextView.setTextColor(Color.BLACK);
            resultTextView.setPadding(0, dpToPx(24),0,0);
            marksInputLayout.addView(resultTextView);

            submitButton.setOnClickListener(v -> calculatePercentage());
        }

        // Clear previous inputs (if any)
        int childCount = marksInputLayout.getChildCount();
        // Remove previous subjects rows: index 1 to childCount-3 (header=0, submit, result)
        // Remove all views added before submit button index
        while (childCount > 4) { 
            marksInputLayout.removeViewAt(1);
            childCount = marksInputLayout.getChildCount();
        }

        subjectLabels.clear();
        obtainedMarksEdits.clear();
        totalMarksEdits.clear();

        for (String subject : subjects) {
            LinearLayout rowLayout = new LinearLayout(this);
            rowLayout.setOrientation(LinearLayout.HORIZONTAL);
            rowLayout.setPadding(0, dpToPx(8), 0, dpToPx(8));
            rowLayout.setGravity(Gravity.CENTER_VERTICAL);

            TextView subjectTextView = new TextView(this);
            subjectTextView.setText(subject);
            subjectTextView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20);
            subjectTextView.setTextColor(Color.BLACK);
            subjectTextView.setLayoutParams(new LinearLayout.LayoutParams(dpToPx(180), LinearLayout.LayoutParams.WRAP_CONTENT));
            rowLayout.addView(subjectTextView);
            subjectLabels.add(subjectTextView);

            EditText obtainedEdit = new EditText(this);
            obtainedEdit.setHint("Obtained");
            obtainedEdit.setInputType(InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
            obtainedEdit.setTextSize(TypedValue.COMPLEX_UNIT_SP, 18);
            obtainedEdit.setLayoutParams(new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1));
            rowLayout.addView(obtainedEdit);
            obtainedMarksEdits.add(obtainedEdit);

            EditText totalEdit = new EditText(this);
            totalEdit.setHint("Total");
            totalEdit.setInputType(InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
            totalEdit.setTextSize(TypedValue.COMPLEX_UNIT_SP, 18);
            totalEdit.setLayoutParams(new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1));
            rowLayout.addView(totalEdit);
            totalMarksEdits.add(totalEdit);

            marksInputLayout.addView(rowLayout, marksInputLayout.getChildCount() - 2); // before submit and result
        }

        marksInputLayout.setVisibility(View.VISIBLE);
    }

    private TextView createHeaderTextView(String text, int weightIndex, int weight) {
        TextView tv = new TextView(this);
        tv.setText(text);
        tv.setTextSize(TypedValue.COMPLEX_UNIT_SP, 22);
        tv.setTextColor(Color.BLACK);
        tv.setTypeface(null, android.graphics.Typeface.BOLD);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                0,
                LinearLayout.LayoutParams.WRAP_CONTENT,
                weight);
        if(weightIndex == 0) {
            // Subject column is wider
            lp = new LinearLayout.LayoutParams(dpToPx(180), LinearLayout.LayoutParams.WRAP_CONTENT);
        }
        tv.setLayoutParams(lp);
        return tv;
    }

    private void calculatePercentage() {
        double totalObtained = 0;
        double totalMax = 0;

        for (int i = 0; i < obtainedMarksEdits.size(); i++) {
            String obtainedStr = obtainedMarksEdits.get(i).getText().toString().trim();
            String totalStr = totalMarksEdits.get(i).getText().toString().trim();

            if (obtainedStr.isEmpty() || totalStr.isEmpty()) {
                // skip empty inputs
                continue;
            }

            double obtained;
            double total;
            try {
                obtained = Double.parseDouble(obtainedStr);
                total = Double.parseDouble(totalStr);
            } catch (NumberFormatException e) {
                resultTextView.setText("Error: Please enter valid numeric values.");
                return;
            }

            if (obtained > total) {
                resultTextView.setText("Error: Obtained marks cannot exceed total marks.");
                return;
            }

            totalObtained += obtained;
            totalMax += total;
        }

        if (totalMax == 0) {
            resultTextView.setText("Error: Total marks must be greater than zero.");
            return;
        }

        double percent = (totalObtained / totalMax) * 100;
        resultTextView.setText(String.format("Total Percentage: %.2f%%", percent));
    }

    private int dpToPx(int dp) {
        float density = this.getResources().getDisplayMetrics().density;
        return Math.round((float) dp * density);
    }
}

