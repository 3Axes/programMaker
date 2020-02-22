package gui;

import javax.swing.*;
import backend.Program;
import java.awt.*;
import java.awt.event.ActionEvent;

import java.awt.*;

public class gui {

    static JFrame frame = new JFrame(String.format("ProgramMaker %s", Program.version));

    public static void update(int Function) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                GUI(Function);
            }
        });
    }

    public static void GUI(int Function) {
        switch (Function) {
            case 0:
                firstStartGUI();
                break;
            case 1:
                //mainLoopGUI();
                break;
        }
    }

    static void firstStartGUI() {
            frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

            JPanel panel = new JPanel();
            panel.setLayout(new BoxLayout(panel, BoxLayout.PAGE_AXIS));

            panel.add(new JButton(new AbstractAction("New") {
                @Override
                public void actionPerformed(ActionEvent actionEvent) {
                    System.out.println("New pressed");
                }
            }));
            panel.add(new JButton(new AbstractAction("Open") {
                @Override
                public void actionPerformed(ActionEvent actionEvent) {
                    System.out.println("Open pressed");
                }
            }));

            frame.add(panel);
            frame.setVisible(true);
            frame.validate();
    }
}
