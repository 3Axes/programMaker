package builtin;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.io.File;

public class Program {

    static final String version = "1.0.0b";
    static final String comment = "//Created with ProgramMaker " + version + "\n";

    static JFrame frame = new JFrame(String.format("ProgramMaker %s", version));

    public static void main(String[] args) {
        guiFunction(0);
    }

    public static void guiFunction(int MagicConstant) {
        switch(MagicConstant) {
            case 0:
                guiInitial();
                break;
            case 1:
                //guiMain();
                break;
        }
    }

    static void guiInitial() {
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        JPanel panel = new JPanel(new GridLayout(2,1));
        panel.setSize(new Dimension(600,600));

        JButton New = new JButton(new AbstractAction("New") {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {

            }
        });
        JButton Open = new JButton(new AbstractAction("Open") {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {

            }
        });

        panel.add(New);
        panel.add(Open);

        frame.add(panel);
        frame.pack();
        frame.setVisible(true);

    }
}
